# Packaging Preflight | Making every finding traceable to evidence

> Public reproduction · brand and packaging content are synthetic

[中文](packaging-preflight.zh-CN.md) · [Code](../experiments/packaging-preflight/run.py) · [Fixtures](../experiments/packaging-preflight/fixtures.json) · [Raw results](../experiments/packaging-preflight/results.json)

## Packaging risk appears at the last mile

Food packaging passes through product, design, regulatory, supplier, and approval teams. Formula sheets, nutrition data, artwork, comments, and final print files move between tools. The closer a mistake gets to production, the more expensive a one-word change becomes.

Reviewers inspect both missing fields and contradictions across the package: front and back names, net weight, serving math, ingredients, and allergen notices. Rules may already exist; the difficulty is that text appears in complex layouts and the same fact appears in several places.

This is easy to turn into a visually impressive but weak AI demo: upload an image and receive a list of “possible risks.” Without the source region, extracted text, calculation, and rule, the reviewer still has to restart the inspection.

I defined the product as preflight, not approval. It finds explainable issues and presents evidence. Regulatory interpretation, marketing claims, and final release remain human decisions.

## I separated perception from rules

The full workflow contains two different problems: reading text from artwork and applying rules to extracted fields. Combining them too early makes a miss impossible to diagnose.

The public reproduction therefore begins with structured fields. It creates 12 fictional oat-product packages containing front/back names, net weight, serving size, serving count, ingredients, and allergen text. It injects seven issues: two name mismatches, three serving-math errors, and two missing allergen notices.

Every issue has an expected label, and three deterministic rules process the fixtures. This validates the rule layer before OCR noise is introduced.

## A perfect first score has a narrow meaning

The checker found **all 7 injected issues with zero false positives and zero false negatives**.

That result proves only that three rules work on clean fields I designed. It does not prove the system can read packaging artwork, cover real layouts, or determine compliance.

This limitation is part of the result. FDE prototypes often look excellent on clean data, then meet blur, reflections, stylized fonts, table shifts, and uncontrolled versions in the real workflow.

## The next phase must separate error sources

With images, every field needs a source region, OCR text, normalized value, and confidence. Low-confidence fields should be confirmed before generating a rule finding. A serving mismatch should show its arithmetic: “25 g × 3 = 75 g; declared net weight is 100 g.”

Evaluation also needs layers. OCR metrics measure field extraction; rule metrics measure issue recall and false positives; workflow metrics record which suggestions reviewers accept, reject, or edit. A single accuracy score cannot reveal which layer needs repair.

Regulatory and marketing checks should retrieve relevant material and flag uncertainty, not produce a legal conclusion. Rules require version dates, markets, and product scopes.

## Reviewers need an evidence workspace

The useful interface centers on the package, not a chat transcript. The left side shows the artwork and highlighted region; the right side shows extracted text, triggering rule, calculation, severity, and suggested owner. Reviewers can accept, reject, or amend the finding with a reason.

When no rule fires, the product may say “no issue found by the current checks.” It must not say “this package is compliant.” When artwork changes, the system should recheck changed regions and ensure critical fields were not altered accidentally.

## What the project leaves behind

The repository preserves 12 fixtures, seven injected issues, three rules, and every case result. It demonstrates a reproducible minimum rule loop while exposing the perception and regulatory work that remains.

The project produced four FDE principles:

1. Evaluate OCR, rule execution, and human review separately.
2. Trace every finding to a region, field, and calculation.
3. Perfect synthetic-data performance is not real-image performance.
4. AI performs preflight and evidence assembly; people own interpretation and release.

The next milestone adds realistic artwork, blur, glare, small text, and displaced tables, followed by OCR and a review workspace. Only then does the evaluation begin to resemble production conditions.
