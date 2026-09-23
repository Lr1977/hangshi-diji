# Protocol Upgrade For Hangshi Diji

## Summary

The original lightweight inheritance kit improves continuity, but it does not fully prevent workflow bypass.

This upgrade adds a stronger execution gate so that:

- skills are not only available, but operationally reinforced
- plans are not optional for multi-step work
- verification is recorded, not implied
- audits compare result against requirements, not intention
- requirement changes are analyzed before implementation
- task plans can be reconciled against actual workspace evidence
- session checkpoints and handoffs can be regenerated from the project state

## New Layer

This upgrade effectively adds a new layer before the existing foundation stack:

- Layer 0: execution gate

Then the existing stack continues:

1. requirement binding
2. knowledge binding
3. evidence matrix
4. experience / migration layer
5. reasoning / foundation view

## Output Package

Use `protocol-starter/` when strict process continuity matters more than minimal setup.

The P1/P2 execution continuity package adds:

- `docs/changes/` for requirement impact analysis
- `docs/tasks/` for task baselines
- `docs/checkpoints/` for Git-backed recovery points
- `docs/reconciliation/` for plan-versus-actual comparison
- `.diji/events.jsonl` for machine-observable lifecycle events
- `tools/diji.py` for dependency-free automation
