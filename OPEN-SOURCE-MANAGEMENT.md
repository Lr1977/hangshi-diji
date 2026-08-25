# Open Source Management

## Goal

Publish the kit as a reusable method package without exposing private project state.

## Public Scope

- `README.md`
- `MANUAL.md`
- `CAPABILITIES.md`
- `ADOPTION-STEPS.md`
- `PROTOCOL-UPGRADE.md`
- `protocol-starter/`
- sample project docs

## Private Scope

- real project runtime state
- secrets and login state
- private attachments
- private codebases and customer data

## Release Model

### v0.1

- publish the structure
- keep samples small
- keep the method readable

### v0.2+

- improve templates
- add more sample projects
- refine maintenance docs

### v1.0

- only after the layer model is stable across repeated use

## Maintenance Rules

1. keep `Core` stable
2. keep project examples isolated
3. move new observations into `Learnings` first
4. promote to `Core` only after repeated verification
5. archive old guidance in `Deprecated`

## Upgrade Rules

- backward-compatible doc changes can ship in small releases
- structural changes need a migration note
- sample additions should not rewrite the core protocol

