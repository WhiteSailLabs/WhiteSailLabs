# Reconcile Agent

## Field problem

Store staff repeatedly compare POS exports, mall settlement sheets, and scanned receipts. Most rows are routine, while a small number of mismatches consume attention and can hide recoverable revenue.

## Personal implementation

Create a reproducible demo with generated POS transactions, settlement spreadsheets, receipt images, and deliberately injected discrepancies. The goal is not a chatbot—it is a controlled first-pass reconciliation workflow.

## Workflow

1. Define the matching hierarchy, tolerance policy, and exception ownership.
2. Parse structured files deterministically and use OCR only where documents require it.
3. Auto-match high-confidence records and explain the matching rule used.
4. Route discrepancies into a human review queue with source evidence.
5. Export an auditable reconciliation report and corrected decision log.

## Human / agent boundary

- Code handles arithmetic, identifiers, dates, tolerances, and deterministic matching.
- Models assist with OCR normalization and ambiguous document interpretation.
- Humans approve unresolved differences and any accounting adjustment.

## Evidence

- Auto-match coverage
- False-match rate, with a target of zero on the test set
- Precision/recall for injected discrepancies
- Human review time per cycle
- Value of previously ignored variance surfaced

## Deliverables

- Synthetic dataset generator
- Reconciliation engine
- Exception-review interface
- Audit report with row-level provenance
- Scale-up and failure-recovery notes

## Source pattern

Adapted from the retail reconciliation pattern in Case 10 of [Datawhale FDE案例100](https://assets.datawhale.cn/Datawhale%20FDE%E6%A1%88%E4%BE%8B100.pdf).
