<p align="center">
  <img src="assets/editorial-fde-banner-3x1.png" alt="从模糊问题走向精准、可部署的结果" width="100%" />
</p>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong>
</p>

<h1 align="center">LiFan Chen · Agent 工程师 / FDE</h1>

<p align="center">
  <strong>我把模糊的业务流程转化为可度量、可部署的 Agent 系统。</strong><br/>
  从现场发现、快速原型，到评估、集成与能力转移。
</p>

<p align="center">
  中国上海 · 上海科技大学
</p>

## 我的工作方式

`观察真实流程` → `定义最小价值问题` → `构建端到端闭环` → `评估真实失败模式` → `接入现有工作流` → `完成能力转移`

- 从用户每天真正做的工作出发，而不是从模型或框架出发。
- 把调研中发现的问题转化为测试样例与验收标准。
- 自动化确定性步骤；判断、升级和最终责任仍由人承担。
- 当数据敏感或环境受限时，优先采用本地优先部署。
- 最终留下可观测的系统，以及能够继续解决下一类问题的团队。

## FDE Build Lab

这些项目是我对真实部署模式的个人公开实现，并非虚构客户经历。每个项目都必须包含基线、评估集、人工接管机制、部署记录以及诚实的失败日志。

| 项目 | 现场问题 | Agent 系统 | 证据目标 | 状态 |
| --- | --- | --- | --- | --- |
| [Knowledge Relay](case-studies/knowledge-relay.zh-CN.md) | 关键经验留在资深人员头脑和零散手册中。 | 知识采集、带引用检索、引导学习、进度跟踪与升级处理。 | 检索召回率、有依据回答率、任务完成率、减少专家打断次数。 | 调研设计完成 |
| [Local Asset Navigator](case-studies/local-asset-navigator.zh-CN.md) | 文件和图片虽然存在，但缺乏关系与业务语境。 | 带权限、来源追踪、搜索和可复用工作流的本地多模态索引。 | Top-k 检索率、搜索耗时、隐私边界、任务复用成功率。 | 基于 [llm-obsidian-agent](https://github.com/WhiteSailLabs/llm-obsidian-agent) 构建中 |
| [Reconcile Agent](case-studies/reconcile-agent.zh-CN.md) | 工作人员反复核对 POS 导出、结算表和扫描票据。 | 确定性匹配、OCR/视觉提取与人工异常审核队列。 | 自动匹配覆盖率、误匹配率、审核耗时、异常识别率。 | 原型规格完成 |
| [Packaging Preflight](case-studies/packaging-preflight.zh-CN.md) | 包装错误发现太晚，造成排队和返工。 | OCR/VLM 提取、确定性规则检查、带依据的问题报告和人工批准。 | 规则覆盖率、漏检率、可追溯性、审核时间缩短比例。 | 技术设计完成 |

## 代表项目

- **[resume-job-agent](https://github.com/WhiteSailLabs/resume-job-agent)** — 面向中国求职场景的本地优先 FDE 工作流，覆盖职位发现、JD 审核和基于证据的简历定制。
- **[llm-obsidian-agent](https://github.com/WhiteSailLabs/llm-obsidian-agent)** — 将高价值对话转化为结构化、用户自主拥有知识的本地 LLM 工作空间。
- **[daily-tech-research](https://github.com/WhiteSailLabs/daily-tech-research)** — 面向前沿技术与应用型 AI 系统的可重复研究流程。
- **[shengbei-wish](https://github.com/WhiteSailLabs/shengbei-wish)** — 基于 React、Three.js 和手势输入的浏览器原生交互实验。
- **[awesome-ai-agent-interview](https://github.com/WhiteSailLabs/awesome-ai-agent-interview)** — 用于理解 Agent 系统与准备工程面试的知识和资源。

## 工程标准

每个 FDE 项目都必须回答五个问题：

1. **价值** — 哪个昂贵、缓慢、高风险或过去被放弃的任务因此变得可行？
2. **边界** — 哪些步骤自动化，哪些由人完成，系统何时升级处理？
3. **证据** — 哪些真实样例构成评估集，什么结果才算成功？
4. **适配** — 系统如何进入现有流程，而不成为新的负担？
5. **转移** — 最终有哪些知识、工具和运营能力留在用户手中？

## 技术栈

`Python` · `TypeScript` · `React` · `PyTorch` · `RAG` · `工具调用` · `多模态 AI` · `评估` · `本地优先部署`

## 当前方向

我正在围绕 **Agent × Forward Deployed Engineering** 构建公开作品集：从真实工作流出发，用小型系统尽快证明可度量价值，并只在首个有效闭环成立后继续扩展。

Build Lab 中的每个项目都由我独立定义范围、实现、评估和记录。当缺少真实企业与私有数据时，我会使用合成数据建立可复现实验，并明确当前阶段与验证结果。

<p align="center">
  <sub>从模糊问题到可运行系统，再从可运行系统到可持续能力。</sub>
</p>
