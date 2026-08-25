# EXP-SUNO-001: Cantonese handling drift recovery

## Problem Pattern

- Cantonese generation drifted when too many voice and range constraints were stacked together.

## Root Cause

- conflicting constraints overloaded the prompt and reduced singing stability.

## Successful Fix

- reduce constraint density and keep the Cantonese layer separate from low-voice shaping

## Invalid Fixes

- stacking more voice constraints without reducing prompt load
- treating all failures as a prompt-language problem

## Applicability

- multilingual singing prompts with strong language constraints

## Non-Applicability

- purely instrumental tasks
- unrelated product workflows

## Derived Method

- isolate one variable at a time when testing language-specific vocal stability

## Linked Requirements

- `REQ-SUNO-001`

## Linked KB

- `KB-SUNO-001`

