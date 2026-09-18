# Packaging Preflight

> Status: test plan complete; no working version yet

[简体中文](packaging-preflight.zh-CN.md)

I plan to design 12 fictional food packages and deliberately put mistakes in them.

Some will omit fields. Some nutrition tables will contain calculation errors. Some will disagree between the front and back. A few claims will have no automatic answer and should be reviewed by a person.

The question is not whether a model can “look at packaging.” It is whether the system can show where a problem is, why it is a problem, and when it should stop.

## Why one model call is not enough

A package mixes normal text, decorative lettering, nutrition tables, marks, product images, and layout. A model looking at the full image may miss small text or read a number correctly but calculate it incorrectly.

I will split the artwork into regions. OCR will read text and tables. Normal code will recalculate nutrition values. Fixed rules will check missing fields and contradictions. A model can help with irregular text and explanations. People will handle claims, visual judgment, and rule applicability.

## Evidence for every finding

Each result should include the exact image region, extracted value, calculation or rule, confidence, and suggested reviewer.

For a nutrition mismatch, the page should show the original numbers and the recalculation instead of asking a model to guess in prose.

## Evaluation

The 12 packages will contain clean examples, clear mistakes, and boundary cases. I will report detection by error type, serious misses, extraction errors by region, evidence coverage, and which suggestions people accept or reject.

This project provides review suggestions, not legal conclusions. “No issue found” will never be presented as compliance approval.

## Progress

- [x] Define package regions
- [x] Define the first error types
- [x] Define evidence required for a finding
- [ ] Create 12 fictional packages
- [ ] Label every injected issue
- [ ] Build text and table extraction
- [ ] Build rule checks
- [ ] Build the review page
- [ ] Publish false-negative and false-positive results

If the first version can only check nutrition tables and front/back consistency reliably, that is enough. Doing two checks well is more useful than claiming to review an entire package.
