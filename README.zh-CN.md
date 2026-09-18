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

`看清实际工作` → `选一个值得解决的问题` → `做出可用版本` → `测试容易出错的地方` → `放回日常流程`

- 从用户每天真正做的工作出发，而不是从模型或框架出发。
- 把发现的问题写成具体测试。
- 重复工作交给程序，需要判断的事情留给人。
- 资料敏感时，优先在本机运行。
- 做完以后，别人应该知道怎么使用、检查和继续修改。

## FDE Build Lab

这些是我正在公开开发的个人原型。每个项目都有可运行代码、测试数据和第一次运行结果。它们不是客户案例，也还没有进入生产环境。

| 项目 | 第一次做出的东西 | 实测结果 | 状态 |
| --- | --- | --- | --- |
| [Knowledge Relay](case-studies/knowledge-relay.zh-CN.md) | 设备知识查找与安全拒答 | 封闭测试从 15/40 提升到 40/40 | 公开复现版已运行 |
| [Local Asset Navigator](case-studies/local-asset-navigator.zh-CN.md) | 本地资料检索与目录权限控制 | 调整索引边界后从 6/20 提升到 8/20 | 公开复现版迭代中 |
| [Reconcile Agent](case-studies/reconcile-agent.zh-CN.md) | POS、结算记录的自动匹配与人工复核 | 569/600 判断正确；错误自动通过 0 | 公开复现版已运行 |
| [Packaging Preflight](case-studies/packaging-preflight.zh-CN.md) | 包装文案的规则检查与证据输出 | 结构化测试找到 7/7 个预埋问题 | 公开复现版已运行 |

## 代表项目

- **[resume-job-agent](https://github.com/WhiteSailLabs/resume-job-agent)** — 面向中国求职场景的本地优先 FDE 工作流，覆盖职位发现、JD 审核和基于证据的简历定制。
- **[llm-obsidian-agent](https://github.com/WhiteSailLabs/llm-obsidian-agent)** — 将高价值对话转化为结构化、用户自主拥有知识的本地 LLM 工作空间。
- **[daily-tech-research](https://github.com/WhiteSailLabs/daily-tech-research)** — 面向前沿技术与应用型 AI 系统的可重复研究流程。
- **[shengbei-wish](https://github.com/WhiteSailLabs/shengbei-wish)** — 基于 React、Three.js 和手势输入的浏览器原生交互实验。
- **[awesome-ai-agent-interview](https://github.com/WhiteSailLabs/awesome-ai-agent-interview)** — 用于理解 Agent 系统与准备工程面试的知识和资源。

## 工程标准

每个项目都要回答五个问题：

1. 它解决了什么具体问题？
2. 哪些事情程序做，哪些事情人来决定？
3. 用什么数据测试，怎样才算做对？
4. 用户是否需要为它增加很多额外工作？
5. 项目结束后，别人能不能继续维护？

## 技术栈

`Python` · `TypeScript` · `React` · `PyTorch` · `RAG` · `工具调用` · `多模态 AI` · `评估` · `本地优先部署`

## 当前方向

我正在围绕 **Agent × Forward Deployed Engineering** 做一组公开项目。每个项目先解决一个具体问题，跑通并测出结果后，再决定是否继续扩展。

Build Lab 中的每个项目都由我独立定义范围、实现、评估和记录。当缺少真实企业与私有数据时，我会使用合成数据建立可复现实验，并明确当前阶段与验证结果。

<p align="center">
  <sub>从模糊问题到可运行系统，再从可运行系统到可持续能力。</sub>
</p>
