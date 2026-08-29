# Project Protocol Rules

## Purpose

This project uses the `夯实地基 / Hangshi Diji` protocol mode.

This is not a suggestion-only workflow. It is a delivery gate.

Any Codex or other AI agent entering this project must follow the protocol below before claiming implementation progress or completion.

## Rule Order

Enter this project in the following order:

1. read global rules if the machine has them
2. read operator identity rules if the machine has them
3. read this file
4. read `LOOP.md`
5. read `STATE.md`
6. read `docs/handoff/LATEST.md`
7. read the relevant requirement doc
8. read linked `KB-*` entries
9. read the latest plan, verification, and audit docs for the active requirement

Do not continue from chat memory alone when these files exist.

## Protocol Gate

For any non-trivial task, the agent must not skip the following sequence:

1. Restore
2. Frame
3. Plan
4. Implement
5. Verify
6. Audit
7. Update Docs
8. Hand Off

If one of these steps is skipped, the agent must explicitly say the protocol is incomplete and may not claim the work is done.

## Mandatory Work Products

For any multi-step task or any task involving code, UI, behavior, runtime, API, auth, or data flow, the agent must create or update all of the following:

1. a plan doc in `docs/plans/`
2. a verification doc in `docs/verification/`
3. an audit doc in `docs/audits/`

If requirement drift risk exists, the agent must also confirm or update:

4. the relevant requirement doc in `docs/requirements/`
5. any linked KB docs in `docs/kb/`
6. linked experience notes in `docs/experience/` when prior failed attempts or migration lessons matter

Without these artifacts, the work is not protocol-complete.

## Completion Claim Rules

The agent may only say a task is complete when all of the following are true:

1. code or docs were actually changed when change was required
2. verification was actually run, not assumed
3. verification output was recorded in `docs/verification/`
4. the result was compared against the requirement and plan, not against intent
5. residual risks and unverified areas were recorded in `docs/audits/`
6. the final report includes concrete evidence, not only a summary claim

Endpoint ping, server restart, or page load alone does not count as regression verification unless the requirement was only about service availability.

## Requirement-to-Knowledge Binding Rule

If the project has requirement / implementation / knowledge drift risk, the agent must bind work to requirement points instead of operating from free-form memory.

Each active requirement should declare:

- goal
- current status
- linked KB entries
- linked evidence
- linked experience notes
- verification targets
- open questions

If these bindings do not exist yet, the agent must create or repair them before broad implementation.

## Gate Failure Rule

If the user asks why the protocol was not followed, the agent must answer directly:

- which protocol step was skipped
- what artifact is missing
- what was actually done
- what still needs to be done to become compliant

Do not hide behind generalities.

## Required Local Operating Docs

- `LOOP.md`
- `STATE.md`
- `docs/requirements/`
- `docs/kb/`
- `docs/plans/`
- `docs/verification/`
- `docs/audits/`
- `docs/experience/`
- `docs/handoff/`

The latest handoff file is part of the required recovery path, not an optional summary.

## Working Rule

Do not present work as complete unless the protocol artifacts make the work discoverable by a future session with no chat history.
