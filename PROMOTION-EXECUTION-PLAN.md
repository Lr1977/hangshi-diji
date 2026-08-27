# Promotion Execution Plan

## Goal

Run the first public promotion cycle for Hangshi Diji / 夯实地基 and turn external feedback into project improvements.

## Operating Rule

Do not publish the same text everywhere. Each platform gets a version that matches its audience.

## Current Published Asset

- Platform: Zhihu
- Title: AI 长任务为什么总是越做越偏？我把需求、知识库、验证绑成了一套工作底座
- URL: https://zhuanlan.zhihu.com/p/2076243464157664696
- Status: published
- Next checks: 24 hours, 72 hours, 7 days

## Execution Order

### Step 1: GitHub Readiness

Owner: Codex executes, user confirms login when needed.

Actions:

1. check repository first screen and topics
2. confirm repository URL is visible in every public post
3. prepare a short social preview brief
4. check whether README has a simple adoption path

Trigger to proceed: repository link is usable and public-facing text is coherent.

Current check on 2026-08-27:

- Remote URL: `https://github.com/Lr1977/hangshi-diji.git`
- Public repository: yes
- Default branch: `main`
- Latest pushed commit: `3d113c52890748b3141aa96950ced5425a49a74c`
- README online: updated and readable
- Description: missing in GitHub repository settings
- Homepage: missing in GitHub repository settings
- Topics: missing in GitHub repository settings
- Social preview: not confirmed

Recommended GitHub repository settings:

- Description: `Reusable operating layer for long-running AI development: requirements, knowledge, verification, and audit.`
- Website: `https://zhuanlan.zhihu.com/p/2076243464157664696`
- Topics: `ai-agent`, `agent-workflow`, `requirements-management`, `knowledge-base`, `developer-workflow`, `prompt-engineering`, `openai`, `codex`

Manual action needed if Codex cannot access GitHub settings UI: open `https://github.com/Lr1977/hangshi-diji`, click the About gear, then fill the description, website, and topics above.

### Step 2: Juejin

Owner: Codex writes and fills, user logs in or confirms publish.

Purpose: reach Chinese engineering readers.

Content angle: engineering workflow, not personal essay.

Use draft: `PROMOTION-JUEJIN-DRAFT.md`

Trigger to proceed: user is logged into Juejin and confirms publish.

### Step 3: V2EX

Owner: Codex writes and fills, user confirms account state and publish.

Purpose: get direct developer feedback.

Content angle: concise, ask for critique, avoid sales tone.

Use draft: `PROMOTION-V2EX-DRAFT.md`

Trigger to proceed: Juejin is posted or intentionally skipped.

### Step 4: WeChat / QQ / Friend Circle

Owner: Codex prepares copy, user sends to private groups.

Purpose: warm-start feedback from known people.

Content angle: one pain point, one link, one request for feedback.

Use draft: `PROMOTION-SHORT-COPY.md`

Trigger to proceed: public article and repo link are ready.

### Step 5: Gitee / OSCHINA / CSDN

Owner: Codex prepares or fills, user confirms accounts.

Purpose: improve domestic access and search discovery.

Content angle: tutorial or project introduction.

Trigger to proceed: first week feedback shows repeated interest or access friction.

## Permission / Login Checklist

The user should log in through the browser when needed. Do not paste passwords into chat.

- GitHub: required for topics, social preview, traffic checks
- Juejin: required for article publishing
- V2EX: required for topic publishing
- Gitee: optional, required for mirror setup
- OSCHINA: optional
- CSDN: optional

## Metrics Collection

Collect these after each post:

- article URL
- publish time
- reads / views
- likes
- saves / bookmarks
- comments
- GitHub stars before and after
- repeated questions
- friction points

## Feedback Handling

Classify feedback into four buckets:

1. FAQ candidate: repeated confusion, answer in docs
2. KB candidate: stable reusable project rule
3. README improvement: first-screen clarity issue
4. Ignore for now: one-off preference or unsupported use case

## First Week Schedule

Day 1:

- record Zhihu launch
- prepare Juejin and V2EX drafts

Day 2:

- check Zhihu 24-hour data
- publish or prepare Juejin

Day 3:

- answer public comments
- record repeated questions

Day 4:

- post V2EX short version
- compare feedback tone against Zhihu and Juejin

Day 5 to Day 7:

- circulate short copy in private groups
- update FAQ / README candidates
- decide whether Gitee mirror is necessary
