# REQ-EXECUTION-CONTINUITY-001: Execution Continuity

## Goal

Preserve the relationship between requirements, approved plans, actual changes,
verification evidence, and the next-session handoff even when a chat session is
compressed or replaced.

## Current Status

- complete and stable

## Why It Exists

The foundation must preserve facts, not only intentions. A plan can become
stale while work is running, and a new requirement can silently change the
scope of an existing one. This requirement adds explicit change analysis,
task baselines, checkpoints, and plan-to-result reconciliation.

## Knowledge Bindings

- `KB-EXECUTION-CONTINUITY-001`
- `KB-SESSION-RECOVERY-001`

## Implementation Notes

- Every non-trivial task has a stable task id and a plan baseline.
- Every new requirement records its relationship to existing requirements.
- Checkpoints capture the current task, Git evidence, risks, and next action.
- Reconciliation records planned steps versus actual results and deviations.
- The `diji` CLI may automate evidence collection but does not invent semantic
  completion claims.

## Verification Targets

- a new project can be initialized with the required directories and state
  files
- a task and change record can be created without third-party dependencies
- a checkpoint includes current Git status and diff evidence
- a reconciliation report makes deviations explicit
- a handoff can be regenerated from the latest checkpoint

## Open Questions

- whether a future Codex runtime exposes a reliable pre-compaction hook
- whether event records should remain JSONL or move to a small local database
