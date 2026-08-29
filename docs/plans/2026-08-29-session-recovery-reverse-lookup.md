# Session Recovery Reverse Lookup Implementation Plan

> **For Codex:** REQUIRED SUB-SKILL: Use $subagent-driven-development to implement this plan task-by-task.

**Goal:** Make the project's docs support reverse lookup from a later session back to the active project and last completed work.

**Architecture:** Treat `STATE.md` as the live pointer, `docs/handoff/LATEST.md` as the last transition record, and `docs/requirements/`, `docs/kb/`, `docs/verification/`, and `docs/audits/` as the durable trail.

**Tech Stack:** Markdown only.

---

### Task 1: Write the recovery contract

**Files:**
- Create: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\docs\requirements\REQ-SESSION-RECOVERY-001.md`
- Create: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\docs\kb\KB-SESSION-RECOVERY-001.md`

**Step 1: Write the requirement**

Capture the goal, bindings, and verification targets for session recovery.

**Step 2: Write the knowledge entry**

Capture the file-driven read order and the role of `STATE.md` versus `docs/handoff/LATEST.md`.

**Step 3: Review the scope**

Keep the contract narrow: no secrets, no runtime state, no chat-memory dependency.

### Task 2: Update the project entry points

**Files:**
- Modify: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\README.md`
- Modify: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\MANUAL.md`
- Modify: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\ADOPTION-STEPS.md`
- Modify: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\protocol-starter\AGENTS.md`
- Modify: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\protocol-starter\LOOP.md`
- Modify: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\protocol-starter\STATE.md`
- Modify: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\starter\AGENTS.md`
- Modify: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\starter\LOOP.md`
- Modify: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\starter\STATE.md`
- Modify: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\protocol-starter\docs\FOUNDATION-MAP.md`

**Step 1: Add the read order**

Make `docs/handoff/LATEST.md` part of the session entry sequence.

**Step 2: Add the project state fields**

Make `STATE.md` carry project identity, last session summary, and next-session read hints.

**Step 3: Add the classification note**

Record that session recovery and handoff files are project-local knowledge, not core universal doctrine.

### Task 3: Add the live handoff example and verify the chain

**Files:**
- Create: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\docs\handoff\LATEST.md`
- Create: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\docs\verification\2026-08-29-session-recovery-reverse-lookup.md`
- Create: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\docs\audits\2026-08-29-session-recovery-reverse-lookup.md`
- Create: `C:\Users\ASUS\Desktop\LQ\codex-universal-inheritance-kit\docs\experience\EXP-SESSION-RECOVERY-001.md`

**Step 1: Write the handoff**

Summarize what changed, what was verified, and what the next session should read first.

**Step 2: Verify the links**

Run `rg` over the repo to confirm the new read order and recovery docs are discoverable.

**Step 3: Record the audit**

Capture the remaining risk: downstream projects still need to copy the template into their own root.

**Step 4: Commit**

```bash
git add README.md MANUAL.md ADOPTION-STEPS.md protocol-starter starter docs
git commit -m "docs: land session recovery contract"
```
