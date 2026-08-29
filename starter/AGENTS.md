# Project Rules

## Rule Order

Enter this project in the following order:

1. read global rules
2. read operator identity rules if any
3. read this file
4. read `LOOP.md`
5. read `STATE.md`
6. read `docs/handoff/LATEST.md`

## Core Safety Rules

1. do not expose secrets
2. do not delete or clean historical dirty state unless explicitly requested
3. frame target outcome, file scope, and verification before risky edits
4. keep changes narrow
5. do not claim completion without fresh verification

## Required Local Operating Docs

- `LOOP.md`
- `STATE.md`
- `docs/plans/`
- `docs/guardrails/`
- `docs/handoff/`

If the project has requirement / knowledge drift risk, also use:

- `docs/requirements/`
- `docs/kb/`

When a later session resumes work, `docs/handoff/LATEST.md` is part of the required recovery path.

## Working Rule

Do not continue work from chat memory alone when local project docs exist.
