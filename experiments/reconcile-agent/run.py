"""Generate deterministic transaction data and evaluate conservative matching rules."""
from pathlib import Path
import json
import random

ROOT = Path(__file__).parent
rng = random.Random(20260919)
pos = []
settlement = []
truth = {}
anomalies = {"missing": 0, "duplicate": 0, "amount_changed": 0, "id_changed": 0}

for i in range(600):
    order = f"O{i:05d}"
    amount = rng.randint(800, 38000)
    row = {"order_id": order, "day": 1 + i % 30, "amount_cents": amount}
    pos.append(row)
    if i % 41 == 0:
        anomalies["missing"] += 1
        truth[order] = "missing"
        continue
    peer = dict(row)
    if i % 37 == 0:
        peer["amount_cents"] += 100
        anomalies["amount_changed"] += 1
        truth[order] = "review"
    elif i % 29 == 0:
        peer["order_id"] = "X-" + order
        anomalies["id_changed"] += 1
        truth[order] = "review"
    else:
        truth[order] = "matched"
    settlement.append(peer)
    if i % 53 == 0:
        settlement.append(dict(peer))
        anomalies["duplicate"] += 1

by_id = {}
for row in settlement:
    by_id.setdefault(row["order_id"], []).append(row)

decisions = {}
for row in pos:
    candidates = by_id.get(row["order_id"], [])
    if len(candidates) == 1 and candidates[0]["amount_cents"] == row["amount_cents"]:
        decisions[row["order_id"]] = "matched"
    else:
        decisions[row["order_id"]] = "review" if candidates else "missing"

wrong_auto_matches = sum(v == "matched" and truth[k] != "matched" for k, v in decisions.items())
correct = sum(v == truth[k] for k, v in decisions.items())
report = {
    "experiment": "reconcile-agent",
    "dataset": {"pos_rows": len(pos), "settlement_rows": len(settlement), "injected": anomalies},
    "metrics": {
        "correct_decisions": correct,
        "decision_accuracy": round(correct / len(pos), 3),
        "automatic_matches": sum(v == "matched" for v in decisions.values()),
        "sent_to_review": sum(v == "review" for v in decisions.values()),
        "missing": sum(v == "missing" for v in decisions.values()),
        "wrong_automatic_matches": wrong_auto_matches,
    },
    "limitations": "Synthetic rows only; no OCR, split-order matching, UI, or production use.",
}
(ROOT / "results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report["metrics"], ensure_ascii=False))

