# AUDIT-SAMPLE-001: Cantonese lyric handling sample audit

## Linked Plan

- `PLAN-SAMPLE-001`

## Linked Verification

- `VERIFICATION-SAMPLE-001`

## Requirement Comparison

- requirement: Cantonese output should remain stable
- expected: no Mandarin drift in the verified sample
- actual: verified sample stayed Cantonese
- status: pass

## What Changed

- the sample project used a Cantonese-specific prompt pack and lyric preprocessing rule

## What Is Confirmed

- the sample path is valid for the sample project

## Residual Risks

- the result is still sample-scoped, not yet cross-project proof

## Human Test Still Needed

- another run on a different lyric set

## Completion Decision

- partial

## Reason

- one sample is enough for a project sample, not enough to promote to Core
