# Foundation-Project Bootstrap

## Purpose

Use this file as the entry point for one concrete project under the Hangshi Diji structure.

## What Belongs Here

- project name
- project goal
- current status
- project-specific requirement index
- project-specific KB index
- project-specific verification targets
- project-specific open questions

## What Must Stay Out

- generic cross-project protocol rules
- reusable core workflow guidance
- unrelated project notes
- deprecated material

## Recommended Structure

```text
project-name/
  PROJECT.md
  STATE.md
  requirements/
  kb/
  plans/
  verification/
  audits/
  experience/
  handoff/
```

## Required Fields

Each project bootstrap should answer:

1. what this project is
2. what problem it solves
3. which requirement points are active
4. which KB entries are authoritative
5. what must be verified before claiming progress

## Migration Rule

When an existing project is brought into the system:

1. create a project bootstrap file
2. list all active requirements
3. bind each requirement to KB entries
4. separate experiments from core knowledge
5. flag deprecated content explicitly

## Minimal Example

```md
# Project: Example

## Goal
Stabilize multilingual song generation.

## Active Requirements
- REQ-001 Cantonese lyric handling
- REQ-002 Japanese lyric handling

## KB Bindings
- KB-CANTO-001 Cantonese prompt-language rule
- KB-MULTI-004 language strategy baseline

## Verification
- generation completes
- output language stays stable
- download and playback work
```

