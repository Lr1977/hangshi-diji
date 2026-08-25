# EXP-SAMPLE-002: Japanese handling drift recovery

## Problem Pattern

- Japanese generation drifted when romanization noise stayed in the lyric body.

## Root Cause

- mixed-script input reduced pronunciation stability.

## Successful Fix

- remove romanization noise and keep the style prompt Japanese-first

## Invalid Fixes

- adding more unrelated voice constraints
- treating Japanese drift the same as Cantonese drift

## Applicability

- Japanese song generation with mixed-script risk

## Non-Applicability

- Cantonese generation
- pure instrumental tasks

## Derived Method

- clean the lyric body before submission and keep prompt language consistent

## Linked Requirements

- `REQ-SAMPLE-002`

## Linked KB

- `KB-SAMPLE-002`

