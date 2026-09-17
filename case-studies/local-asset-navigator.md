# Local Asset Navigator

## Field problem

A small business may have years of documents, product images, templates, and delivery files, but no reliable way to ask which files belong to a customer, product, or past decision. The files exist; the relationships do not.

## Personal implementation

Extend [llm-obsidian-agent](https://github.com/WhiteSailLabs/llm-obsidian-agent) into a local-first multimodal workspace. Use a synthetic customer/product directory plus the user's own opt-in notes so the demo can be reproduced without exposing private company data.

## Workflow

1. Inventory file types, folder conventions, permissions, and recurring search tasks.
2. Extract text, image descriptions, metadata, and explicit entity relationships locally.
3. Build a provenance-aware index across customers, products, projects, and versions.
4. Support natural-language retrieval and reusable tasks such as “find the latest approved template and its related delivery files.”
5. Record corrections as durable metadata rather than ephemeral chat feedback.

## Human / agent boundary

- The agent proposes relationships and retrieval results with provenance.
- The user confirms sensitive links, permissions, and canonical versions.
- Data stays local by default; external model use must be explicit and scoped.

## Evidence

- Top-5 retrieval success on a task-based evaluation set
- Median time to locate a complete asset bundle
- Provenance coverage and stale-version errors
- Permission-boundary tests
- Number of corrected relationships reused successfully

## Deliverables

- Local multimodal indexer
- Search and relationship browser
- Permission and provenance model
- Evaluation tasks with expected asset bundles
- Migration and backup runbook

## Source pattern

Adapted from the local file-asset and capability-transfer pattern in Case 11 of [Datawhale FDE案例100](https://assets.datawhale.cn/Datawhale%20FDE%E6%A1%88%E4%BE%8B100.pdf).
