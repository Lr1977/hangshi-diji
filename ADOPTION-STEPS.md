# Adoption Steps

## 1. Install or copy the base Codex environment

If you already have a portable Codex layer, reuse it.

This kit is meant to sit on top of that base.

## 2. Copy the `starter/` folder into the target project or workspace

Use it as a template, not as immutable content.

## 3. Fill in project facts

At minimum, update:

- `starter/AGENTS.md`
- `starter/LOOP.md`
- `starter/STATE.md`

## 4. If the project is knowledge-heavy, also adopt:

- `starter/docs/requirements/`
- `starter/docs/kb/`
- `starter/docs/kb/INDEX.md`
- `starter/docs/kb/experiment-template.md`
- `starter/docs/handoff/LATEST.md`

## 5. Tell the new Codex to start sessions by reading:

1. global rules
2. project `AGENTS.md`
3. project `LOOP.md`
4. project `STATE.md`
5. project `docs/handoff/LATEST.md`

Then, if requirement docs exist:

6. target requirement doc
7. linked `KB-*` entries

## 6. Do not skip the split between requirement and knowledge

Rules:

- requirement docs carry intent
- KB docs carry reusable conclusions
- experiments carry provisional evidence

## 7. Do not migrate secrets

Re-enter:

- API keys
- login state
- local env vars

manually on the target machine.

## 8. Adopt execution continuity for long-running work

Copy or create these directories in the target project:

- `docs/changes/`
- `docs/plans/`
- `docs/tasks/`
- `docs/checkpoints/`
- `docs/reconciliation/`
- `docs/events/`
- `.diji/` (generated state and event log)

Then initialize the optional CLI from this repository:

```text
python tools/diji.py --root <target-project> init
```

Use `change` before a new requirement changes scope, `start` before a
multi-step task, `checkpoint` at meaningful boundaries, `reconcile` after
verification, and `handoff` before leaving the session.
