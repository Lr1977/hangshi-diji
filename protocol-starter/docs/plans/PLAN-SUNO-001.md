# PLAN-SUNO-001: Cantonese lyric handling

## Goal

- Stabilize Cantonese lyric handling for the Suno project.

## Scope

- Cantonese prompt pack
- Cantonese lyric preprocessing
- output stability check

## Out Of Scope

- Japanese handling
- cross-project reuse claims

## Requirement Bindings

- `REQ-SUNO-001`

## Knowledge Bindings

- `KB-SUNO-001`

## Experience Bindings

- `EXP-SUNO-001`

## Assumptions

- Cantonese-specific preprocessing improves stability in this project.

## Implementation Steps

1. apply Cantonese lyric preprocessing
2. use Cantonese-specific prompt pack
3. verify output language and playback

## Verification Matrix

1. command / action: manual browser submission
   expected: generation completes
2. command / action: playback and download check
   expected: output remains Cantonese and usable

## Audit Target

- the run remains Cantonese and supports playback/download

