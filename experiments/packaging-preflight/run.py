"""Check structured package-copy fixtures with explicit, inspectable rules."""
from pathlib import Path
import json

ROOT = Path(__file__).parent
fixtures = []
expected = {}
for i in range(12):
    item = {
        "id": f"P{i+1:02d}", "front_name": f"燕麦脆片 {i+1}", "back_name": f"燕麦脆片 {i+1}",
        "net_g": 100, "serving_g": 25, "servings": 4, "energy_per_serving_kj": 420,
        "ingredients": "燕麦, 坚果, 蜂蜜", "allergen": "含坚果",
    }
    issues = []
    if i in {1, 7}:
        item["back_name"] = "燕麦谷物棒"
        issues.append("name_mismatch")
    if i in {2, 8, 11}:
        item["servings"] = 3
        issues.append("serving_math")
    if i in {4, 9}:
        item["allergen"] = ""
        issues.append("missing_allergen")
    fixtures.append(item)
    expected[item["id"]] = issues

def check(item):
    found = []
    if item["front_name"] != item["back_name"]:
        found.append("name_mismatch")
    if item["serving_g"] * item["servings"] != item["net_g"]:
        found.append("serving_math")
    if "坚果" in item["ingredients"] and not item["allergen"]:
        found.append("missing_allergen")
    return found

found = {item["id"]: check(item) for item in fixtures}
tp = sum(len(set(found[k]) & set(expected[k])) for k in expected)
fp = sum(len(set(found[k]) - set(expected[k])) for k in expected)
fn = sum(len(set(expected[k]) - set(found[k])) for k in expected)
report = {
    "experiment": "packaging-preflight",
    "dataset": {"structured_packages": len(fixtures), "injected_issues": sum(map(len, expected.values()))},
    "metrics": {"true_positives": tp, "false_positives": fp, "false_negatives": fn},
    "cases": [{"id": x["id"], "expected": expected[x["id"]], "found": found[x["id"]]} for x in fixtures],
    "limitations": "Structured text fixtures only; no OCR, images, legal judgment, or production use.",
}
(ROOT / "fixtures.json").write_text(json.dumps(fixtures, ensure_ascii=False, indent=2) + "\n")
(ROOT / "results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report["metrics"], ensure_ascii=False))
