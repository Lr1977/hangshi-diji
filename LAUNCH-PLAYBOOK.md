# Launch Playbook

## Goal

Turn this repository from a passive public repo into a project that the right developers can discover, understand, and star.

## 1. GitHub Setup Checklist

Complete these items before pushing traffic to the repository:

1. set repository topics
2. upload a social preview image
3. pin the repository on your GitHub profile
4. keep `README.md` first screen clear and bilingual
5. add at least one diagram and one case summary
6. make sure `LICENSE`, `CONTRIBUTING.md`, and `CHANGELOG.md` stay current

### Suggested Topics

- `ai-agent`
- `agent-workflow`
- `requirements-management`
- `knowledge-base`
- `developer-workflow`
- `prompt-engineering`
- `openai`
- `codex`

## 2. Social Preview Brief

Use a dark background and keep the message direct.

### Main Title

Hangshi Diji

### Subtitle

Keep AI projects aligned across requirements, knowledge, implementation, and verification.

### Chinese Variant

让 AI 长任务不再越做越偏

## 3. Positioning

### One-line Positioning

Hangshi Diji is a reusable operating layer for long-running AI development work.

### Chinese One-line Positioning

夯实地基是一套面向 AI 长任务开发的可复用工作底座。

### Pain Statement

Most AI development workflows fail slowly: requirements drift, knowledge stays trapped in chat history, verification is weak, and later agents repeat old mistakes.

## 4. Publishing Sequence

Recommended order:

1. finish GitHub repo presentation
2. publish a long-form Zhihu article
3. adapt it into a Juejin engineering article
4. compress it into short posts for V2EX, WeChat groups, QQ groups, and friend circles
5. collect feedback and update FAQ / examples

Execution details and platform-specific drafts live in `PROMOTION-EXECUTION-PLAN.md`, `PROMOTION-JUEJIN-DRAFT.md`, `PROMOTION-V2EX-DRAFT.md`, and `PROMOTION-SHORT-COPY.md`.

## 5. Zhihu Draft

### Suggested Title A

AI 长任务为什么总是越做越偏？我把需求、知识库、验证绑成了一套工作底座

### Suggested Title B

做 AI 项目最怕的不是不会写，而是需求漂移：这是我解决它的方法

### Suggested Structure

1. 先写你踩过的坑：长任务、断上下文、需求和代码逐渐脱节
2. 再写为什么单靠聊天记录不够
3. 介绍夯实地基的四层结构和 loop
4. 举一个真实案例，说明“绑定知识后，试错次数如何下降”
5. 最后给 GitHub 仓库链接和使用方式

### Ready-to-Post Opening Paragraph

过去一段时间，我在用 AI 持续推进一些周期很长的项目。最明显的感受不是 AI 不会做，而是项目越做越容易偏：需求文档和代码逐渐脱节，前面试过的东西后面又重复试，换一个 agent 接手之后，很多结论又退回到“重新摸索”。后来我把这些问题拆开，做成了一套更像工程底座的结构：需求点、知识条目、计划、验证、审计都不再分散，而是绑定在一起。这套方法，我把它叫做“夯实地基”。

## 6. Juejin Draft

### Suggested Title

我把 AI 长任务的需求、知识库和验证流程做成了一套可复用底座

### Recommended Angle

Focus on engineering structure, not inspiration.

### Suggested Outline

1. 问题定义：AI 长任务里的需求漂移和重复试错
2. 方案结构：Core / Project / Learnings / Deprecated
3. 工作流：plan -> implement -> verify -> audit
4. 如何把 `KB-*` 绑定到需求点
5. 迁移到新项目的步骤
6. 已知边界：它不是运行环境克隆，也不替代业务判断

## 7. Short Community Post

### Version A

做 AI 长任务时，我反复遇到三个问题：需求会漂、经验会丢、验证会散。后来我把需求、知识库、计划、验证、审计拆成固定结构，做成了一套可复用底座。现在把它整理成开源仓库了，有需要的人可以直接拿去套到自己的项目里。 

### Version B

如果你也在做长期 AI 项目，可能会遇到需求文档和代码慢慢脱节、换 agent 后要重复摸索的问题。我把这件事结构化了一下，做成了一个叫“夯实地基”的工作底座，核心是 requirement-to-knowledge binding 加上固定 loop，仓库刚开源。

## 8. What To Show In Public Posts

Always include:

- one pain point
- one structure diagram
- one case summary
- one repository link

Avoid posting only a naked GitHub URL.

## 9. First Week Maintenance Plan

Day 1:

- publish GitHub repo polish
- post Zhihu article

Day 2 to Day 3:

- answer comments
- note repeated questions into FAQ candidates

Day 4:

- post Juejin version

Day 5 to Day 7:

- circulate the short community version
- collect terminology confusion points
- update `README.md` and examples based on feedback

## 10. Metrics To Watch

Use simple metrics first:

- GitHub stars
- repository traffic
- issue / discussion quality
- article saves and comments
- how many people can actually adopt the starter without extra explanation

## 11. Promotion Log

Use this section to record public launches and later review what actually worked.

### 2026-08-27 Zhihu Article

- Platform: Zhihu
- Title: AI 长任务为什么总是越做越偏？我把需求、知识库、验证绑成了一套工作底座
- Article URL: https://zhuanlan.zhihu.com/p/2076243464157664696
- Status: published
- Purpose: first long-form public explanation of Hangshi Diji / 夯实地基
- Follow-up: watch reads, likes, saves, comments, and GitHub traffic changes for 7 days

## 12. Follow-up Rhythm

After each public post:

1. record the publication URL and date
2. check metrics after 24 hours, 72 hours, and 7 days
3. collect repeated questions into FAQ candidates
4. promote stable feedback into `KB-*` or docs only after it repeats
5. adjust the next platform draft instead of reposting the same copy unchanged
