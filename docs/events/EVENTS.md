# Execution Events

`diji` records machine-observable lifecycle events in `.diji/events.jsonl`.

The event log is evidence of actions and state observations. It is not a
replacement for requirement documents, verification records, or human review.

Supported event types include:

- `PROJECT_INITIALIZED`
- `CHANGE_RECORDED`
- `TASK_STARTED`
- `CHECKPOINT_CREATED`
- `RECONCILIATION_CREATED`
- `HANDOFF_CREATED`

Do not put secrets, tokens, cookies, or private customer data into event
metadata.
