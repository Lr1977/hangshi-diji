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

## Release / Maintenance Resource Checklist

### Required

- GitHub repository access
- Gitee repository access if mirroring is planned
- a maintained README with project purpose and quick start
- at least one runnable demo or sample workflow
- screenshots or short screen recordings
- changelog entries for each meaningful release
- stable issue / feedback channel

### Recommended

- a public discussion post or article for the first release
- FAQ / troubleshooting notes
- sample templates for requirements, KB, plans, verification, and audit
- version tags for stable milestones
- a backup copy of private-only assets and runtime state

### Maintenance Rhythm

1. update docs when behavior changes
2. promote only stable conclusions into `KB-*`
3. move failed or outdated guidance into `Deprecated`
4. attach verification evidence before marking a release complete
5. review public/private scope before every publish

### Minimum Launch Package

- project name and one-line positioning
- problem statement
- installation or adoption steps
- one demo flow
- known limitations
- maintenance owner or contact method
