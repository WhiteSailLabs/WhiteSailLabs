# Knowledge Relay

## Field problem

Experienced operators hold critical tacit knowledge, while manuals capture only the standard path. Newcomers repeatedly interrupt experts, training progress is hard to observe, and rare exceptions are learned too late.

## Personal implementation

Build a public demonstration using open technical manuals, annotated troubleshooting notes, and a synthetic set of expert exceptions. The system will not pretend to reproduce a real factory; it will demonstrate the delivery method on a transparent dataset.

## Workflow

1. Map the tasks, recurring questions, failure points, and escalation moments.
2. Convert the discovery set into an evaluation set before building retrieval.
3. Parse manuals and expert notes into cited, versioned knowledge units.
4. Answer routine questions with evidence and route uncertain cases to a human.
5. Turn recurring questions into guided lessons and track completion.

## Human / agent boundary

- The agent retrieves, explains, quizzes, and records uncertainty.
- A human owns safety-critical judgment, exception approval, and knowledge updates.
- Unsupported answers must abstain rather than improvise.

## Evidence

- Document parsing coverage
- Recall@k on the discovery question set
- Citation correctness and grounded-answer rate
- Abstention quality on unsupported questions
- Time-to-answer and expert interruptions avoided

## Deliverables

- Local web application
- Versioned knowledge map
- Evaluation dataset and test runner
- Training/progress view
- Failure log and deployment runbook

## Source pattern

Adapted from the knowledge-transfer and AI-assisted training pattern in Case 1 of [Datawhale FDE案例100](https://assets.datawhale.cn/Datawhale%20FDE%E6%A1%88%E4%BE%8B100.pdf).
