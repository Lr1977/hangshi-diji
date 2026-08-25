# REQ-SUNO-001: Cantonese lyric handling

## Goal

- Keep Cantonese lyrics in Cantonese after generation.

## Current Status

- complete and stable

## Why It Exists

- Prevent Mandarin drift and preserve Cantonese pronunciation behavior in Suno generation.

## Knowledge Bindings

- `KB-SUNO-001`

## Evidence Bindings

- `VERIFICATION-SUNO-001`
- `AUDIT-SUNO-001`

## Experience Bindings

- `EXP-SUNO-001`

## Implementation Notes

- Use Cantonese-specific preprocessing before submission.
- Keep style prompt and lyric body separated.

## Verification Targets

- generation completes
- output remains Cantonese
- no Mandarin drift in the chorus

## Open Questions

- whether future Cantonese tuning should use strict or soft lock modes

