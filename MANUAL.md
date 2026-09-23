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
4. `docs/handoff/LATEST.md`
5. `docs/plans/`
6. `docs/guardrail_report_*.md`

### Layer 3: Requirement Continuation Layer

For any project with drift risk, add:

1. `docs/requirements/`
2. `docs/kb/`
3. stable `KB-*` ids
4. experiment records before promoting new conclusions

This layer is now referred to as:

- `夯实地基`

### Layer 4: Execution Continuity Layer

For long-running work, add the explicit chain:

1. requirement change analysis
2. task and plan baseline
3. execution checkpoint
4. verification evidence
5. plan-versus-actual reconciliation
6. handoff update

The `diji` CLI can generate the records and collect Git evidence. It cannot
replace semantic review or verification.

## Session Entry Order

Every serious session should read, in order:

1. global rules
2. identity/operator rules
3. project `AGENTS.md`
4. project `LOOP.md`
5. project `STATE.md`
6. project `docs/handoff/LATEST.md`
7. relevant requirement docs
8. linked `KB-*` entries

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

## Session Recovery Rule

If a later session needs to re-enter a project, the project must be recoverable from files alone:

1. `STATE.md` identifies the project and active work
2. `docs/handoff/LATEST.md` captures the last transition
3. requirement docs and `KB-*` entries carry the durable trail

If any of those are missing, the project is not fully inheritable yet.

## Change And Reconciliation Rule

When a new request arrives, do not silently edit an old plan. Create a change
record that states whether the request appends, revises, replaces, conflicts
with, or is unrelated to the existing requirement. At task completion, compare
every planned step with the actual result and record deviations explicitly.
