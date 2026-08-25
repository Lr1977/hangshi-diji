# KB-SAMPLE-002: Japanese lyric preprocessing rule

## Type

- implementation constraint
- experiment conclusion

## Statement

- Japanese generation is more stable when romanization noise is removed from the lyric body and the style prompt stays Japanese-first.

## Why This Matters

- Mixed-script noise can degrade pronunciation and section handling.

## Applies To

- `REQ-SAMPLE-002`

## Does Not Automatically Apply To

- Cantonese generation
- English generation

## Evidence

- Japanese repeatability tests in the multilingual song project

