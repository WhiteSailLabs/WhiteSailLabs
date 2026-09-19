# Local Asset Navigator | Searching my own public repository first

> Public reproduction · a public repository replaces private project directories

[中文](local-asset-navigator.zh-CN.md) · [Code](../experiments/local-asset-navigator/run.py) · [Raw results](../experiments/local-asset-navigator/results.json)

I often remember writing something but not its filename or folder. The first version deliberately indexes only this public profile repository. It does not scan my home directory, which keeps the privacy boundary clear and the test reproducible.

The script reads paths and text, then ranks files by literal query frequency with extra weight for path matches. The 20 tasks cover both profile languages and all four case studies. There is no vector database, model, or pre-built tagging system.

The unscoped baseline returned the correct top result for only **6 of 20 tasks**. Evaluation code and summary pages polluted the index. After excluding tool/output directories and increasing title weight, the final reproducible run reached **9/20**.

The next version needs to separate user documents from tool code and weight titles, links, and file types differently. Images, PDFs, version conflicts, latency, and private directories are not tested yet.
