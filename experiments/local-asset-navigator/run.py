"""Index this public profile repository and test filename/content search."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent / "results.json"

files = [
    p for p in ROOT.rglob("*")
    if p.is_file() and ".git" not in p.parts and "experiments" not in p.parts and p != OUT
]
docs = {}
for path in files:
    rel = str(path.relative_to(ROOT))
    if path.suffix.lower() in {".md", ".py", ".json", ".txt"}:
        try:
            docs[rel] = path.read_text(errors="ignore").lower()
        except OSError:
            pass

tasks = [
    ("中文主页", "README.zh-CN.md"), ("english profile", "README.md"),
    ("设备知识助手", "case-studies/knowledge-relay.zh-CN.md"),
    ("manual retriever", "case-studies/knowledge-relay.md"),
    ("本地资料搜索", "case-studies/local-asset-navigator.zh-CN.md"),
    ("local files", "case-studies/local-asset-navigator.md"),
    ("自动对账", "case-studies/reconcile-agent.zh-CN.md"),
    ("reconciliation", "case-studies/reconcile-agent.md"),
    ("包装检查", "case-studies/packaging-preflight.zh-CN.md"),
    ("packaging", "case-studies/packaging-preflight.md"),
]
tasks = tasks + [(q + " 项目", expected) for q, expected in tasks]

def search(query):
    terms = re.findall(r"[a-z0-9-]+|[\u4e00-\u9fff]{2,}", query.lower())
    scored = []
    for rel, text in docs.items():
        title = text.splitlines()[0] if text else ""
        score = sum(
            (8 if term in title else 0) + (4 if term in rel.lower() else 0) + text.count(term)
            for term in terms
        )
        scored.append((score, rel))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return scored[0][1] if scored and scored[0][0] else None

rows = [{"query": q, "expected": e, "actual": search(q)} for q, e in tasks]
for row in rows:
    row["correct"] = row["expected"] == row["actual"]
correct = sum(r["correct"] for r in rows)
report = {
    "experiment": "local-asset-navigator",
    "dataset": {"files_seen": len(files), "text_files_indexed": len(docs), "tasks": len(rows)},
    "metrics": {"top_1_correct": correct, "top_1_accuracy": round(correct / len(rows), 3)},
    "failures": [r for r in rows if not r["correct"]],
    "privacy": "Only this public repository was indexed; no home-directory scan.",
}
OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report["metrics"], ensure_ascii=False))
