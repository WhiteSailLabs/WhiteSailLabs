# Reconcile Agent | Turning discrepancies into evidence people can review

> Public reproduction · private transactions are replaced by 600 deterministic synthetic rows

[中文](reconcile-agent.zh-CN.md)

## Reconciliation is slow because exceptions are fragmented

Retail reconciliation combines POS exports, settlement records, and receipts. They come from different systems, use different fields, and may disagree about dates. Refunds cross days, order IDs gain prefixes, and one receipt may cover several transactions.

The spreadsheet workflow is reasonable: match IDs, compare dates and amounts, then move unresolved rows into an exception sheet. The expensive part is the small set of exceptions. Reviewers switch between files and still need to explain why two rows belong together.

The dangerous failure is not sending too many records to review. It is automatically approving unrelated transactions. I therefore defined the safety target first: only strong evidence can produce an automatic match; everything else must retain its source and reason.

## I kept the model away from arithmetic

The first division of labor is explicit. Deterministic code handles amounts, dates, identifiers, and matching. A model may later extract receipt text. People own ambiguous matches, exception approval, and final responsibility.

Using a fixed random seed, the public reproduction creates 600 POS rows and corresponding settlement data. It injects 15 missing records, 11 duplicates, 16 amount changes, and 20 modified order IDs. Because the generator creates each anomaly, the expected state is known and every run is repeatable.

## Run one: conservative rules protect the floor

The rule order starts with the strongest evidence. An order ID must be unique and the amount identical before a row passes automatically. Duplicate IDs or changed amounts go to review; no same-ID record becomes missing.

The system made **569 correct decisions out of 600: 94.8%**. It auto-matched 538 rows, sent 27 to review, marked 35 missing, and produced **zero wrong automatic matches**.

That meets the first safety objective without solving the full problem. The 20 modified IDs are usually labeled missing instead of appearing as related candidates. The engine avoids a false match but does not yet help the reviewer locate the likely peer.

## Failure evidence defines the next layer

The next matcher cannot simply loosen its conditions. Date and amount alone can merge two legitimate transactions with the same value. Instead it should generate candidates: normalize ID formats, combine a date window, amount, store, and receipt fields, then show a candidate score to a reviewer.

Candidate ranking and automatic matching must remain separate metrics. A top candidate does not grant the system authority to approve it. Only a reviewer can confirm the relationship.

## The product is a review workspace, not a chat window

The reviewer needs three evidence columns: original POS row, settlement row, and receipt or missing-data state. Changed fields are highlighted, and the triggering rule is explicit: “same ID, amount differs by 1.00” or “ID prefix differs; date and amount agree.”

Each exception has a small set of actions: confirm match, confirm discrepancy, or wait for evidence. Every decision preserves the operator, timestamp, source files, and rationale. Rule changes must be replayable against historical data to detect newly introduced false matches.

Success is measured by wrong auto-matches, manual review volume, anomaly recall, and batch processing time, not just automation rate.

## What the project leaves behind

The repository includes the generator, anomaly injection, matching rules, and complete result. Anyone can recreate the 600-row run and trace every metric.

The work produced four FDE principles:

1. Define the unacceptable error before optimizing automation.
2. Keep deterministic calculations in code; use models for unstructured inputs.
3. Ambiguous matching should propose candidates, not bypass approval.
4. Review interfaces must show source evidence and rules, not just explanations.

The public version has no receipt OCR, split orders, cross-store data, production UI, or labor-saving claim. The next milestone adds candidate matching and a review screen, then measures candidate errors and reviewer workload separately.
