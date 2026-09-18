"""Evaluate a small source-citing manual retriever without external services."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).parent
SECTIONS = {
    "S1": "开机前检查：确认急停按钮已复位，防护门关闭，气压在 0.5 到 0.7 MPa。",
    "S2": "E12 气压不足：停止启动。检查进气阀、软管泄漏和压力表。恢复到 0.5 MPa 以上再复位。",
    "S3": "E21 防护门未闭合：清理门轨异物，确认门锁指示灯亮。不得短接门锁传感器。",
    "S4": "主轴异响：立即停机并记录转速、材料和出现时间。异响原因不能仅凭声音判断，应由维修人员检查。",
    "S5": "日常保养：每班清理导轨碎屑；每周检查润滑油液位；每月检查气路接头。",
    "S6": "复位流程：排除报警原因，关闭防护门，长按复位键两秒。报警仍在时不要重复启动。",
}
STOP = {"的", "了", "和", "在", "是", "要", "怎么", "什么", "一下", "机器", "设备"}

def tokens(text):
    return {x for x in re.findall(r"[A-Za-z]+\d*|[\u4e00-\u9fff]{2,}", text.lower()) if x not in STOP}

def retrieve(question):
    q = tokens(question)
    ranked = []
    for sid, text in SECTIONS.items():
        score = len(q & tokens(text))
        for code in ("e12", "e21"):
            if code in question.lower() and code in text.lower():
                score += 4
        ranked.append((score, sid))
    ranked.sort(reverse=True)
    return ranked[0][1] if ranked[0][0] else None

base = [
    ("开机前气压应该多少", "S1"), ("E12 报警先查哪里", "S2"),
    ("防护门关了还是 E21", "S3"), ("主轴有怪声还能继续吗", "S4"),
    ("导轨多久清理一次", "S5"), ("报警排除后怎样复位", "S6"),
    ("进气压力只有 0.4 MPa", "S2"), ("门轨有碎屑怎么办", "S3"),
]
cases = []
for i in range(5):
    for question, expected in base:
        suffix = ["", "请告诉我", "现在要处理", "操作步骤是什么", "新人应该怎么办"][i]
        cases.append({"id": len(cases) + 1, "question": question + suffix, "expected": expected})

predictions = []
for case in cases:
    actual = retrieve(case["question"])
    predictions.append({**case, "actual": actual, "correct": actual == case["expected"]})

correct = sum(x["correct"] for x in predictions)
report = {
    "experiment": "knowledge-relay",
    "dataset": {"manual_sections": len(SECTIONS), "questions": len(cases)},
    "metrics": {"top_1_correct": correct, "top_1_accuracy": round(correct / len(cases), 3)},
    "failures": [x for x in predictions if not x["correct"]],
    "note": "Hand-written fictional manual; retrieval only, no answer generation or factory deployment.",
}
(ROOT / "results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report["metrics"], ensure_ascii=False))
