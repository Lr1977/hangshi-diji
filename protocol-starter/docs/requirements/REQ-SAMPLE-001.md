# REQ-SAMPLE-001: Cantonese lyric handling

## Goal

- Keep Cantonese lyrics in Cantonese after generation.

## Current Status

- complete and stable

## Why It Exists

- Prevent mixed Mandarin-Cantonese output and preserve Cantonese pronunciation behavior.

## Knowledge Bindings

- `KB-SAMPLE-001`

## Evidence Bindings

- `VERIFICATION-SAMPLE-001`
- `AUDIT-SAMPLE-001`

## Experience Bindings

- `EXP-SAMPLE-001`

## Implementation Notes

- Use Cantonese-specific preprocessing before submission.
- Keep the style prompt and lyric body separated.

## Verification Targets

- generation completes
- output remains Cantonese
- no Mandarin drift in the chorus

## Open Questions

- whether the current lock should be strict or soft for all Cantonese variants

