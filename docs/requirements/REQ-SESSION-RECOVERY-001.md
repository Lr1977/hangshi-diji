# REQ-SESSION-RECOVERY-001: Session Recovery Reverse Lookup

## Goal

Make a future Codex session able to recover the project, current work, and next action from files even when chat history is missing.

## Current Status

complete and stable

## Why It Exists

Chat history is not a durable project store. A later session needs a fixed file path back into the project so it can answer:

- which project this is
- what the last session did
- what remains open
- what to read next

## Knowledge Bindings

- `KB-SESSION-RECOVERY-001`

## Implementation Notes

- `STATE.md` must carry project identity, active requirement ids, last session summary, and the next-session read order
- `docs/handoff/LATEST.md` must record the latest transition in one place
- `AGENTS.md` and `LOOP.md` must require reading the handoff file before continuing
- requirement docs must not depend on chat memory alone

## Verification Targets

- a new session can identify the project from `STATE.md`
- a new session can find the latest transition from `docs/handoff/LATEST.md`
- the read order is explicit in the main docs and starter templates

## Open Questions

- whether downstream projects should keep a single `LATEST.md` or one handoff file per active requirement
