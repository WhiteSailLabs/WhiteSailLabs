<p align="center">
  <img src="assets/editorial-fde-banner-3x1.png" alt="From ambiguity to a precise deployed outcome" width="100%" />
</p>

<p align="center">
  <strong>English</strong> · <a href="README.zh-CN.md">简体中文</a>
</p>

<h1 align="center">LiFan Chen · Agent Engineer / FDE</h1>

<p align="center">
  <strong>I turn ambiguous workflows into measurable, deployable agent systems.</strong><br/>
  From field discovery and rapid prototyping to evaluation, integration, and capability transfer.
</p>

<p align="center">
  Shanghai, China · ShanghaiTech University
</p>

## How I work

`Observe the workflow` → `Define the smallest valuable problem` → `Build an end-to-end slice` → `Evaluate real failure modes` → `Deploy into the existing process` → `Transfer capability`

- Start from the user's daily work, not from a model or framework.
- Turn discovery findings into test cases and acceptance criteria.
- Automate deterministic steps; keep judgment, escalation, and accountability with people.
- Prefer local-first deployment when data sensitivity or environment constraints matter.
- Leave behind an observable system and a team that can solve the next problem.

## FDE Build Lab

These are personal prototypes I am building in public. Each one now includes runnable code, test data, and a first-run result. They are not customer deployments.

| Project | First working scope | Measured result | Status |
| --- | --- | --- | --- |
| [Knowledge Relay](case-studies/knowledge-relay.md) | Six manual sections and 40 retrieval questions | 15/40 top-1 hits (37.5%) | First run complete; many failures |
| [Local Asset Navigator](case-studies/local-asset-navigator.md) | Local search limited to this public repository | 6/20 top-1 hits (30%) | First run complete; index pollution is visible |
| [Reconcile Agent](case-studies/reconcile-agent.md) | 600 generated POS rows and conservative matching rules | 569/600 correct decisions; zero wrong auto-matches | First run complete |
| [Packaging Preflight](case-studies/packaging-preflight.md) | 12 structured package-copy fixtures and three rules | 7/7 injected issues found; zero false positives | Rules prototype complete |

## Selected work

- **[resume-job-agent](https://github.com/WhiteSailLabs/resume-job-agent)** — local-first FDE workflow for China job discovery, JD review, and evidence-grounded resume tailoring.
- **[llm-obsidian-agent](https://github.com/WhiteSailLabs/llm-obsidian-agent)** — local LLM workspace that converts useful conversations into structured, user-owned knowledge.
- **[daily-tech-research](https://github.com/WhiteSailLabs/daily-tech-research)** — repeatable research workflow for emerging technologies and applied AI systems.
- **[shengbei-wish](https://github.com/WhiteSailLabs/shengbei-wish)** — browser-native interaction experiment built with React, Three.js, and gesture input.
- **[awesome-ai-agent-interview](https://github.com/WhiteSailLabs/awesome-ai-agent-interview)** — notes and resources for reasoning about agent systems and engineering interviews.

## Engineering bar

Every FDE build should answer five questions:

1. **Value** — What costly, slow, risky, or previously abandoned task becomes possible?
2. **Boundary** — What is automated, what remains human, and when does the system escalate?
3. **Evidence** — Which real examples form the evaluation set, and what counts as success?
4. **Fit** — How does the system enter the existing workflow without creating another burden?
5. **Transfer** — What knowledge, tooling, and operating ability remain with the user?

## Toolkit

`Python` · `TypeScript` · `React` · `PyTorch` · `RAG` · `Tool Use` · `Multimodal AI` · `Evaluation` · `Local-first Deployment`

## Current focus

I am building a public portfolio around **Agent × Forward Deployed Engineering**: small systems that begin with a real workflow, expose measurable value quickly, and grow only after the first useful loop works.

Every Build Lab project is scoped, implemented, evaluated, and documented as my own public engineering work. Synthetic data is used where a real organization or private dataset is not available.

<p align="center">
  <sub>From ambiguity to a working system—and from a working system to lasting capability.</sub>
</p>
