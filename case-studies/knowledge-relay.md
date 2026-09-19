# Knowledge Relay | Turning troubleshooting knowledge into traceable answers

> Public reproduction · private material is replaced by a synthetic manual and 40 test questions

[中文](knowledge-relay.zh-CN.md) · [Code](../experiments/knowledge-relay/run.py) · [Raw results](../experiments/knowledge-relay/results.json)

## The field problem was not “we need a chatbot”

The project began with a common manufacturing constraint: equipment and product variants keep growing, while frontline troubleshooting still depends on a small number of experienced operators.

New operators usually check the manual, describe the symptom in a group chat, and then interrupt a senior technician. Manuals contain controls, parameters, and standard procedures. They rarely contain judgments such as “stop immediately when this sound appears” or the follow-up questions an expert asks before suggesting an action.

The existing apprenticeship model was valuable because it carried context and judgment. It was also difficult to scale: experts repeated the same explanations, learners could not see their knowledge gaps, and managers could not see where the training process repeatedly stalled.

I reduced the work to three testable questions:

1. Can an everyday-language question retrieve the right manual section?
2. Can every answer point to evidence rather than merely sound plausible?
3. Can the system stop and escalate when evidence is missing or safety is involved?

The system performs first-line retrieval and routing only. It does not control equipment or replace maintenance judgment.

## I followed the workflow before choosing the technology

Instead of immediately loading documents into a vector database, I broke down the existing path: how a learner describes a fault, what they check first, what an expert asks next, and which situations require shutdown.

The knowledge fell into three layers:

- **Standard knowledge:** startup checks, maintenance intervals, and reset procedures.
- **Field language:** phrases such as “strange noise” or “not enough air” that must map to manual terminology.
- **Safety boundaries:** guard, spindle, and unexplained-fault cases that must stop and escalate.

The public reproduction contains six synthetic manual sections and 40 questions. I wrote eight base tasks and expressed each in five ways, so discovery findings became the evaluation set rather than remaining in a requirements document.

## Run one: working software, weak field understanding

The baseline used standard-library Python only. It ranked sections by literal token overlap and added weight for explicit alarm codes such as E12 and E21.

It retrieved the correct top section for **15 of 40 questions: 37.5%**.

Alarm-code questions worked because the user and manual shared the same term. Everyday language failed: “strange noise” did not match “abnormal spindle noise,” and “how often should I clean it?” did not match “clean every shift.”

The failure changed the order of work. Adding answer generation at this point would only make wrong evidence sound more convincing.

## Run two: fix the knowledge expression first

I added a small, inspectable field-language map and Chinese bigram tokenization while preserving alarm-code weighting. The second run reached **40 of 40 on the same closed set**.

That is not a production-accuracy claim. The fixes were informed by the first-run failures and may be overfit. The next gate must use blind questions written by people who did not build the retriever, plus cases with no answer, missing machine context, or multiple plausible causes.

Keeping both runs visible matters. The progress did not come from swapping in a larger model. Failure evidence changed the way operational language was represented.

## The product is a workflow, not an answer box

A deployable interaction should collect the machine, material, process, and timing; retrieve evidence; show the source and conditions; and route low-confidence or high-risk cases to a human. A technician's resolution may suggest new terminology, but it must be reviewed before entering the trusted knowledge base.

For learners, the system reduces the time spent figuring out where to look. For experts, it filters repetitive questions while preserving judgment. For managers, failed searches expose gaps in training material.

## What the project leaves behind

The public repository preserves the manual, question-generation method, retrieval code, results, and failure cases. It can be rerun instead of being trusted as a screenshot.

The work produced four reusable FDE lessons:

1. When a user asks to “capture experience,” first observe when and how that experience is used.
2. Turn discovery questions directly into the evaluation set.
3. Do not use generation quality to hide retrieval errors.
4. Put AI inside the existing training and escalation process, while people retain safety, judgment, and knowledge approval.

The public reproduction has no connected machine, production deployment, or user-efficiency claim. The next milestone is a blind evaluation, refusal testing, and a complete human-escalation loop.
