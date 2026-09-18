# Knowledge Relay | Turning troubleshooting knowledge into traceable answers

> Public reproduction · private material replaced by a synthetic manual and 40 test questions

[中文](knowledge-relay.zh-CN.md) · [Code](../experiments/knowledge-relay/run.py) · [Raw results](../experiments/knowledge-relay/results.json)

## Why I built it

Manuals are organized for reading, not for anxious questions. A user says “the door is closed but the alarm remains,” while the manual says “E21 guard-door interlock.” The first problem is not generating a polished answer. It is finding the right evidence.

I reduced the first version to one test: can a natural-language question retrieve the correct section?

## What I implemented

I wrote six fictional manual sections and 40 questions: eight base questions, each expressed five ways. A standard-library Python script ranks sections by token overlap and gives explicit alarm codes extra weight. It uses no model or external service.

## What actually happened

The first run retrieved the right section for **15 of 40 questions: 37.5%**. Explicit codes worked; everyday language did not. I added a small field-language map and Chinese bigram tokenization. The second run reached **40/40 on the same closed set**.

That 100% is not a production claim: the fixes were informed by the same failures and may be overfit. The next gate is a blind set written by people who did not build the retriever, plus missing-information and no-answer cases.

There is no real machine, factory data, user study, or training-time claim in this prototype.
