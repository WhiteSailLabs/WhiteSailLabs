# Reconcile Agent | Finding what should not pass automatically

> Personal prototype · first reproducible run completed on 2026-09-19

[中文](reconcile-agent.zh-CN.md) · [Code](../experiments/reconcile-agent/run.py) · [Raw results](../experiments/reconcile-agent/results.json)

The dangerous failure in reconciliation is not sending too many records to review. It is automatically approving unrelated records. So the first version is a conservative rule engine, not a chatbot.

Using a fixed random seed, the script generates 600 POS transactions and settlement rows with 15 missing records, 11 duplicates, 16 amount changes, and 20 changed order IDs. A row passes only when its ID is unique and its amount is identical.

The first run made the correct final decision for **569 of 600 rows (94.8%)**. It auto-matched 538, sent 27 to review, marked 35 missing, and made **zero wrong automatic matches**.

The score is not a production claim. Changed IDs are classified as missing rather than related candidates, and overlapping anomalies change the final label. The next version will propose explainable candidates without auto-approving them.

The data is synthetic. There is no receipt OCR, split-order handling, store deployment, UI, or labor-saving claim.
