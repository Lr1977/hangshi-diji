# Project: Suno Multilanguage Generation Sample

## Goal

Stabilize multilingual song generation with project-isolated requirement and knowledge bindings.

## Current Status

- partially complete

## Why It Exists

This sample shows how a real project should avoid knowledge drift by binding each requirement point to explicit KB entries and verification evidence.

## Active Requirements

- `REQ-SAMPLE-001` Cantonese lyric handling
- `REQ-SAMPLE-002` Japanese lyric handling

## KB Bindings

- `KB-SAMPLE-001` Cantonese prompt-language rule
- `KB-SAMPLE-002` Japanese lyric preprocessing rule

## Verification Targets

- generation completes
- output language stays stable
- download and playback work

## Open Questions

- whether every language should get a dedicated isolation rule or only problematic languages
- whether future quality tuning should be promoted into core or remain project-local

