# Project LOOP Protocol

## Purpose

This project uses the `夯实地基 / Hangshi Diji` protocol loop.

This loop exists to prevent:

- requirement drift
- knowledge drift
- shallow verification
- undocumented implementation
- false completion claims

## The 8-Step Protocol

### 1. Restore

Read:

1. `AGENTS.md`
2. `LOOP.md`
3. `STATE.md`
4. `docs/handoff/LATEST.md`
5. active requirement docs
6. linked `KB-*` entries
7. latest related plan, verification, and audit docs

Restore must answer:

- what is the target requirement
- what is already known
- what has already been verified
- what remains uncertain

### 2. Frame

Before editing, state:

- target outcome
- intended file scope
- linked requirement ids
- linked KB ids
- verification to run afterward

For multi-step work, this framing must appear in the plan doc and in the live task tracking.

### 3. Plan

Before substantial work, create a dated plan doc in `docs/plans/`.

The plan must include:

- scope
- assumptions
- requirement bindings
- implementation steps
- verification matrix
- audit target
- out-of-scope items

No plan means no protocol-compliant implementation.

### 4. Implement

Make narrow changes aligned to the requirement and plan.

Do not expand scope silently.

If the implementation reveals a requirement mismatch, update the requirement or record the mismatch before continuing.

### 5. Verify

Run real verification appropriate to the change.

Examples:

- syntax and parse checks
- build
- tests
- browser interaction
- API behavior
- auth behavior
- error-path recovery

Record what was run, what passed, what failed, and what was not run in `docs/verification/`.

### 6. Audit

Compare result against:

1. requirement
2. KB / design
3. implementation plan
4. verification evidence

Record:

- what changed
- what is confirmed
- where drift remains
- what still needs human testing
- whether the task is truly complete or only partially closed

### 7. Update Docs

Update any local state that changed:

- `STATE.md`
- requirement docs
- KB docs
- experience notes
- `docs/handoff/LATEST.md`

### 8. Hand Off

Final report must include:

- concrete changes
- verification evidence
- residual risk
- exact next steps

Do not hand off with vague confidence language.

## Protocol Triggers

This loop is mandatory:

- at the start of a new session
- before any multi-step implementation
- before UI or behavior changes
- before auth or API flow changes
- before claiming a fix
- before asking the user to test a changed path

## Failure Examples

The following do not count as protocol compliance:

- reading docs without creating a plan
- restarting a service and calling it implementation
- pinging endpoints and calling it regression testing
- saying "verified" without recording evidence
- claiming completion before updating audit artifacts
