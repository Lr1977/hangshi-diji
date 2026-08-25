# REQ-SAMPLE-002: Japanese lyric handling

## Goal

- Keep Japanese lyrics in Japanese after generation.

## Current Status

- complete and stable

## Why It Exists

- Prevent mixed-script output and keep Japanese pronunciation stable.

## Knowledge Bindings

- `KB-SAMPLE-002`

## Evidence Bindings

- `VERIFICATION-SAMPLE-002`
- `AUDIT-SAMPLE-002`

## Experience Bindings

- `EXP-SAMPLE-002`

## Implementation Notes

- Remove romanization noise from the lyric body before submission.
- Keep style prompt Japanese-first.

## Verification Targets

- generation completes
- output remains Japanese
- no English drift in the chorus

## Open Questions

- whether Japanese should always use a dedicated preprocessing path or only in high-risk prompts

