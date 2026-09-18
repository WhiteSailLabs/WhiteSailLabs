# Knowledge Relay | The first retriever scored 37.5%

> Personal prototype · first reproducible run completed on 2026-09-19

[中文](knowledge-relay.zh-CN.md) · [Code](../experiments/knowledge-relay/run.py) · [Raw results](../experiments/knowledge-relay/results.json)

## Why I built it

Manuals are organized for reading, not for anxious questions. A user says “the door is closed but the alarm remains,” while the manual says “E21 guard-door interlock.” The first problem is not generating a polished answer. It is finding the right evidence.

I reduced the first version to one test: can a natural-language question retrieve the correct section?

## What I implemented

I wrote six fictional manual sections and 40 questions: eight base questions, each expressed five ways. A standard-library Python script ranks sections by token overlap and gives explicit alarm codes extra weight. It uses no model or external service.

## What actually happened

The first run retrieved the right section for **15 of 40 questions: 37.5%**. Explicit codes such as E12 worked. Everyday wording did not: “strange noise” and “abnormal spindle noise” were invisible to a literal tokenizer.

That failure changed the order of work. At 37.5% retrieval accuracy, adding answer generation would only make wrong evidence sound convincing. I will add phrase splitting, synonyms, and a refusal threshold before generating answers.

There is no real machine, factory data, user study, or training-time claim in this prototype.
