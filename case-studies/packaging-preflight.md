# Packaging Preflight

## Field problem

Packaging reviews mix deterministic checks, changing channel requirements, regulatory interpretation, and subjective product judgment. When basic errors are found late, design, procurement, and launch schedules all absorb the rework.

## Personal implementation

Build a demonstrator using synthetic food-package artwork and publicly documented labeling rules. This is an engineering portfolio project, not legal advice or a production compliance guarantee.

## Workflow

1. Decompose the artwork into text, nutrition table, marks, claims, and layout regions.
2. Use OCR/VLM extraction with confidence and source-region coordinates.
3. Implement deterministic calculations and explicit rules in code.
4. Retrieve the rule source for every finding and explain the evidence.
5. Route ambiguous claims and visual judgment to a human reviewer.
6. Store accepted/rejected findings as future test cases.

## Human / agent boundary

- Code owns reproducible calculations and deterministic checks.
- Models extract, normalize, and explain; they do not invent regulations.
- A qualified human owns legal interpretation and final approval.

## Evidence

- OCR field accuracy by region type
- Deterministic-rule coverage
- False-negative rate on seeded violations
- Citation/provenance completeness
- Human review time and correction turnaround

## Deliverables

- Annotated sample package dataset
- Multimodal preflight pipeline
- Rule engine with tests
- Review interface with evidence and confidence
- Audit trail, limitation statement, and failure catalog

## Source pattern

Adapted from the packaging-review and product-lifecycle pattern in Case 19 of [Datawhale FDE案例100](https://assets.datawhale.cn/Datawhale%20FDE%E6%A1%88%E4%BE%8B100.pdf).
