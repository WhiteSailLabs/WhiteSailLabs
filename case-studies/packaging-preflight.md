# Packaging Preflight | Starting with three explainable checks

> Personal prototype · structured-rules run completed on 2026-09-19

[中文](packaging-preflight.zh-CN.md) · [Code](../experiments/packaging-preflight/run.py) · [Fixtures](../experiments/packaging-preflight/fixtures.json) · [Raw results](../experiments/packaging-preflight/results.json)

A packaging demo can look convincing while hiding the original text, calculations, and rules. I therefore removed OCR from the first version and tested the rules on already-structured copy.

The script creates 12 fictional oat-product records containing front/back names, net weight, serving size, serving count, ingredients, and allergen text. It injects seven issues: two name conflicts, three serving-math errors, and two missing allergen notices. Three explicit rules check those fields.

The run found **all 7 injected issues with zero false positives and zero false negatives**. That perfect result has a narrow meaning: I designed both the clean fields and the rules. It does not show that the system can read a package image or judge legal compliance.

The next meaningful test is to add images and OCR while preserving the source region, extracted text, calculation, and confidence for every finding. Marketing claims, regulatory interpretation, and final approval remain human decisions.
