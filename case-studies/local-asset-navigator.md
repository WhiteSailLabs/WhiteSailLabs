# Local Asset Navigator | Searching my own public repository first

> Personal prototype · first reproducible run completed on 2026-09-19

[中文](local-asset-navigator.zh-CN.md) · [Code](../experiments/local-asset-navigator/run.py) · [Raw results](../experiments/local-asset-navigator/results.json)

I often remember writing something but not its filename or folder. The first version deliberately indexes only this public profile repository. It does not scan my home directory, which keeps the privacy boundary clear and the test reproducible.

The script reads paths and text, then ranks files by literal query frequency with extra weight for path matches. The 20 tasks cover both profile languages and all four case studies. There is no vector database, model, or pre-built tagging system.

In the final repository state it saw 25 files, indexed 20 text files, and returned the correct top result for only **6 of 20 tasks: 30%**. Before the experiment files were added, the same baseline scored 55%; the drop itself exposed index pollution. The evaluation script ranked first for queries it contained, while summary links in the profile README often outranked the underlying case pages.

The next version needs to separate user documents from tool code and weight titles, links, and file types differently. Images, PDFs, version conflicts, latency, and private directories are not tested yet.
