# Reconcile Agent

> Status: data and matching rules designed; interface not built

[简体中文](reconcile-agent.zh-CN.md)

I want to test a simple question: which parts of reconciliation belong in normal code, and which parts actually need a model?

The project starts with generated data, not a claimed retail client or invented savings.

## A dataset designed to fail

I will generate three months of transactions for eight fictional stores. Each cycle contains POS exports, mall settlement sheets, and receipt images.

The generator will add refunds, duplicates, split payments, date rollovers, rounding differences, changed order formats, missing receipts, and OCR errors. Because every problem is injected by code, I know the expected result.

## First version

The matcher will start with unique transaction IDs, then use order numbers, dates, and amounts, and finally apply controlled tolerances. Records without enough evidence go to a review list.

Normal code handles money and matching rules. A model is limited to receipt images and inconsistent text formats.

If the system cannot explain why two records match, it cannot approve them automatically.

## What the reviewer sees

The review page places the POS record, settlement row, and receipt next to each other. It highlights changed fields and explains why the record was held back. The reviewer can confirm a match, confirm a difference, or wait for more evidence.

Every decision keeps the source files and reason.

## Results I will publish

I will report automatic match coverage, false matches, recall by error type, OCR errors by field, remaining review work, and processing time. False matches are the main guardrail. The first version should send extra cases to a person rather than combine unrelated records.

## Progress

- [x] Define error types
- [x] Design the matching order
- [x] Design review states
- [ ] Build the data generator
- [ ] Build the matching engine
- [ ] Add receipt extraction
- [ ] Build the review page
- [ ] Publish test results

The project should answer one concrete question: if the model never performs accounting calculations and only handles images and messy text, is it already useful?
