# KB-EXECUTION-CONTINUITY-001: Execution Continuity Contract

## Summary

The durable unit is not the whole chat. It is the traceable chain:

```text
requirement -> change analysis -> task plan -> execution evidence ->
verification -> reconciliation -> handoff
```

## Rules

1. Do not overwrite an approved plan to hide an execution change.
2. Record new requirements as additions, revisions, replacements, conflicts,
   or unrelated requests.
3. Treat Git evidence as facts about the workspace, not as proof that a
   requirement was semantically satisfied.
4. A checkpoint may be generated automatically; completion still requires
   verification and reconciliation.
5. A deviation must state its cause, impact, evidence, and next action.
6. Keep the latest handoff short enough for a new session to read first.

## Automation Boundary

The CLI can collect timestamps, Git status, changed files, diff statistics,
task ids, and document links. It cannot infer the user's intent or certify
that a behavior is correct without a verification record.

## Non-Goal

This contract does not capture hidden model reasoning, secrets, browser state,
or the runtime's internal context-compression operation.
