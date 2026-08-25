# PLAN-SAMPLE-002: Japanese lyric handling sample plan

## Goal

- Stabilize Japanese lyric handling for the sample project.

## Scope

- Japanese-first style prompt
- lyric-body cleanup
- output stability check

## Out Of Scope

- Cantonese handling
- cross-project reuse claims

## Requirement Bindings

- `REQ-SAMPLE-002`

## Knowledge Bindings

- `KB-SAMPLE-002`

## Experience Bindings

- `EXP-SAMPLE-002`

## Assumptions

- removing romanization noise improves Japanese stability in this sample project.

## Implementation Steps

1. remove romanization noise from lyric body
2. keep style prompt Japanese-first
3. verify output language and playback

## Verification Matrix

1. command / action: manual browser submission
   expected: generation completes
2. command / action: playback and download check
   expected: output remains Japanese and usable

## Audit Target

- the sample run remains Japanese and supports playback/download

