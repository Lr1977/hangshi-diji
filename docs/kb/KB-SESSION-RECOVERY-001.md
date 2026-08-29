# KB-SESSION-RECOVERY-001: Session Recovery Contract

## Summary

Session recovery must be file-driven, not chat-driven.

## Rules

1. Read `AGENTS.md`, then `LOOP.md`, then `STATE.md`.
2. Read `docs/handoff/LATEST.md` before resuming any active work.
3. Read the relevant requirement doc, then linked `KB-*` entries.
4. Read the latest plan, verification, and audit docs before editing.
5. If any of those files are missing, declare recovery incomplete and repair the docs first.

## Project State Contract

`STATE.md` should answer:

- what project this is
- what requirement is active
- what the last verified change was
- what the next session should read first

## Handoff Contract

`docs/handoff/LATEST.md` should answer:

- what was done
- what was verified
- what remains open
- what the next action is

## Non-Goal

This contract does not restore secrets, cookies, tokens, or runtime-only machine state.
