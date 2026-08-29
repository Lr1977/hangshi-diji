# Audit: Session Recovery Reverse Lookup

## What Changed

- added file-driven recovery guidance for later Codex sessions
- added the canonical handoff file and the read order around it
- added a concrete example of how the recovery chain should look

## What Is Confirmed

- future sessions have an explicit path from `STATE.md` to `docs/handoff/LATEST.md`
- the kit now documents that chat history is not the source of truth

## Residual Risk

- this only helps after downstream projects copy the templates into their own root
- projects that do not maintain `STATE.md` and `docs/handoff/LATEST.md` will still be hard to recover

## Completion State

- the documentation change is complete for this repository
