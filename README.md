# Hangshi Diji / 夯实地基

Bind requirements, knowledge, implementation, verification, and audit into one reusable operating layer for long-running AI development work.

把需求、知识、实现、验证、审计绑定成一套可复用工作层，专门解决 AI 长任务里的漂移、遗忘和反复试错。

## Why This Exists

Long AI-assisted projects usually break in predictable ways:

- the requirement doc says one thing, the code ends up doing another
- good conclusions stay in chat history instead of becoming reusable knowledge
- later agents repeat old experiments because the last round was not structured
- verification is scattered, so completion claims are weak

AI 长任务最常见的问题不是不会做，而是越做越偏：

- 需求文档和实际代码慢慢脱节
- 有价值的结论留在对话里，没有沉淀成知识
- 后续 agent 不知道前面试过什么，又重复踩坑
- 验证和审计分散，导致“完成”缺乏依据

Hangshi Diji is a practical answer to those problems.

## What You Get

This repository gives you a portable method kit, not a machine clone.

- a repeatable loop: `plan -> implement -> verify -> audit -> report`
- a structure for carrying project state in files instead of chat memory alone
- requirement-to-knowledge binding through stable `KB-*` references
- a four-layer foundation model to keep core rules, project state, learnings, and retired guidance separated
- starter templates you can copy into a real project immediately

这不是环境克隆包，而是一套可迁移的工作方法：

- 固定 loop：`方案 -> 实施 -> 验证 -> 审计 -> 汇报`
- 用文件承载项目上下文，而不是只靠聊天记忆
- 用 `KB-*` 把需求点和知识条目绑定起来
- 用四层地基模型隔离核心规则、项目状态、经验沉淀和废弃内容
- 提供可直接落地的 starter 模板

## Foundation Model

The method is organized around four layers:

1. `Foundation-Core`: stable rules, reusable protocol, durable operating guidance
2. `Foundation-Project`: live project state, active requirements, current plans, verification targets
3. `Foundation-Learnings`: experiments, evidence, promotion candidates, reusable findings
4. `Foundation-Deprecated`: retired guidance kept for traceability, not active use

对应中文理解：

1. `Foundation-Core`：稳定规则和长期复用的方法
2. `Foundation-Project`：当前项目的需求、计划、状态、验证对象
3. `Foundation-Learnings`：实验记录、证据、待升级经验
4. `Foundation-Deprecated`：已废弃但保留追溯价值的内容

## Quick Start

1. Copy `protocol-starter/` into a new or existing project.
2. Read `MANUAL.md` and `ADOPTION-STEPS.md`.
3. Start from one requirement doc and bind it to one or more `KB-*` entries.
4. Run work through the loop: plan, implement, verify, audit, then update state.
5. Promote only stable conclusions from experiments into reusable knowledge.

快速开始：

1. 把 `protocol-starter/` 复制到你的项目里
2. 先读 `MANUAL.md` 和 `ADOPTION-STEPS.md`
3. 从一个需求点开始，绑定到一个或多个 `KB-*`
4. 严格按 loop 推进：方案、实施、验证、审计、更新状态
5. 只有稳定结论才能从实验升级为知识条目

## Package Structure

- `MANUAL.md`: operating explanation
- `CAPABILITIES.md`: what this kit transfers
- `ADOPTION-STEPS.md`: how to install it into another setup
- `OPEN-SOURCE-MANAGEMENT.md`: public/private boundary and maintenance rules
- `protocol-starter/`: reusable starter structure
- `starter/`: smaller starter assets and templates

## What This Repository Does Not Include

This kit intentionally does not ship:

- login state
- secret tokens
- `.env` files
- browser cookies
- private customer data
- local attachments and raw runtime state

也就是说，它解决的是“工作结构继承”，不是“隐私和运行状态复制”。

## Release / Maintenance Snapshot

- keep `README.md` and `OPEN-SOURCE-MANAGEMENT.md` aligned
- publish only stable `KB-*` conclusions
- move failed or outdated guidance into `Deprecated`
- attach verification before calling a release complete
- keep public docs separate from private runtime state

## Recommended GitHub Topics

Add these topics in the GitHub repository UI for discoverability:

- `ai-agent`
- `agent-workflow`
- `requirements-management`
- `knowledge-base`
- `developer-workflow`
- `prompt-engineering`
- `openai`
- `codex`

## Launch Assets

If you want this repository to attract the right users, prepare these assets:

- a clear social preview image
- one structure diagram
- one loop diagram
- one real case summary
- one launch post for GitHub / Zhihu / Juejin / community groups

Execution details and ready-to-post copy live in [LAUNCH-PLAYBOOK.md](C:/Users/ASUS/Desktop/LQ/codex-universal-inheritance-kit/LAUNCH-PLAYBOOK.md).
