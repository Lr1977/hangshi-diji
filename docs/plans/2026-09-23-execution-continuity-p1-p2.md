# Execution Continuity P1/P2 Plan

## Goal

Upgrade Hangshi Diji from a documentation-only recovery method into a small,
dependency-free protocol and CLI that preserves requirement changes, task
baselines, execution evidence, checkpoints, and handoffs.

## Scope

- P1 protocol templates for changes, tasks, checkpoints, events, and
  reconciliation
- P2 `diji` CLI for project initialization, change records, task records,
  checkpoints, reconciliation drafts, status, and handoff generation
- tests using temporary Git repositories

## Out Of Scope

- intercepting the model runtime's private context compression
- automatic capture of hidden reasoning
- remote synchronization or a database service
- automatic semantic approval of a task

## Requirement Bindings

- `REQ-EXECUTION-CONTINUITY-001`
- `REQ-SESSION-RECOVERY-001`

## Implementation Steps

1. Add P1 protocol documents and starter templates.
2. Implement `tools/diji.py` with standard-library-only commands.
3. Add CLI tests and run a temporary-project acceptance flow.
4. Update adoption and release documentation.

## Verification Matrix

1. `python tools/diji.py --help`
   expected: command help renders successfully.
2. `python -m unittest discover -s tests -v`
   expected: CLI unit tests pass.
3. temporary project: `init -> change -> start -> checkpoint -> reconcile -> handoff`
   expected: all artifacts exist and Git evidence is present.
4. `git diff --check`
   expected: no whitespace errors in changed files.

## Audit Target

The result is complete only when a new project can recover its current task,
workspace evidence, deviations, and next action without the original chat.

## Actual Result

- P1 templates added in the repository root and `protocol-starter/`.
- P2 `tools/diji.py` implemented with standard-library-only commands.
- CLI defects found during acceptance were fixed: missing `docs/plans/` creation
  and Windows path handling in the managed `STATE.md` block replacement.
- All CLI commands now require a Git repository, preventing invalid Git evidence
  from being written to recovery artifacts.
- `.gitignore` now excludes Python caches and generated `.diji/` state.
- README launch-playbook link now resolves relative to the repository.
- Unit tests: `python -m unittest discover -s tests -v` passed, 6 tests.
- Failure-path coverage includes non-Git directories, corrupt config, invalid
  step status, Unicode/space paths, and preservation of user-owned state text.
- Acceptance flow in a fresh Git repository passed:
  `init -> change -> start -> checkpoint -> reconcile -> handoff -> status`.
- Formatting check: `git diff --check` passed.
- Verification record: `docs/verification/VERIFICATION-EXECUTION-CONTINUITY-001.md`.
