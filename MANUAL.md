# Manual

## Goal

This manual explains how to make another Codex instance inherit the current working model in a way that is durable and general.

## Inheritance Layers

### Layer 1: Global Behavior

The inherited Codex should always have:

1. skill-first discipline
2. explicit file-scope framing before edits
3. verification before completion claims
4. no secret exposure
5. no destructive cleanup without explicit approval

### Layer 2: Project Operating Layer

Each project should expose:

1. `AGENTS.md`
2. `LOOP.md`
3. `STATE.md`
4. `docs/plans/`
5. `docs/guardrail_report_*.md`

### Layer 3: Requirement Continuation Layer

For any project with drift risk, add:

1. `docs/requirements/`
2. `docs/kb/`
3. stable `KB-*` ids
4. experiment records before promoting new conclusions

This layer is now referred to as:

- `夯实地基`

## Session Entry Order

Every serious session should read, in order:

1. global rules
2. identity/operator rules
3. project `AGENTS.md`
4. project `LOOP.md`
5. project `STATE.md`
6. relevant requirement docs
7. linked `KB-*` entries

## Why This Matters

Without this order, different AI sessions drift toward:

- chat-memory-only continuation
- blind rediscovery
- requirement / implementation mismatch
- repeated testing of the same already-known facts

## Minimum Viable Adoption

If a project is still early or unstable, only adopt:

1. `AGENTS.md`
2. `LOOP.md`
3. `STATE.md`
4. one plan file
5. one audit record

If the project becomes knowledge-heavy, then add requirement and KB layers.
