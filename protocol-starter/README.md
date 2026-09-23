# Protocol Starter

This starter is the hardened version of the Codex working kit.

Use it when you do not want the agent to merely "know the workflow", but to operate under a document-driven protocol with explicit delivery gates.

## What This Adds

Compared with the lightweight starter, this version adds:

1. a gate-oriented `AGENTS.md`
2. a protocol `LOOP.md`
3. mandatory plan / verification / audit artifacts
4. requirement-to-knowledge binding templates
5. an experience layer for non-mechanical pitfall reuse
6. execution continuity templates for requirement changes, tasks, checkpoints, events, and reconciliation

## Why It Exists

This starter addresses the common failure mode where:

- the AI reads docs
- understands the intended design
- skips implementation planning
- performs shallow checks
- claims progress without evidence

## Execution Continuity

For long-running work, use the execution chain:

```text
requirement -> change analysis -> task plan -> checkpoint -> verification -> reconciliation -> handoff
```

The starter includes the document templates for this chain. The optional
dependency-free CLI lives at the repository root in `tools/diji.py`; copy it
with the starter or invoke it from the source repository when adopting the
protocol. It records observable Git evidence but does not replace semantic
verification or reviewer judgment.

## Foundation Hygiene

This starter also assumes a four-layer Hangshi Diji structure:

1. `docs/foundation-core/`
2. `docs/foundation-project/`
3. `docs/foundation-learnings/`
4. `docs/foundation-deprecated/`

Read [FOUNDATION-LAYERS.md](./docs/FOUNDATION-LAYERS.md) before promoting cross-project guidance.

## Adoption Rule

Copy this starter into a project root when the project has:

- multiple sessions
- multiple agents
- requirement drift risk
- upstream quirks
- non-trivial verification needs
