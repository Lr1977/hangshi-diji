# KB-SUNO-001: Cantonese prompt-language rule

## Type

- design rule
- experiment conclusion

## Statement

- Suno Cantonese output is more stable when the prompt uses a Cantonese-specific style pack, short section labels, and explicit anti-Mandarin constraints.

## Why This Matters

- Without this rule, the model can drift into Mandarin phrasing or lose phonetic control.

## Applies To

- `REQ-SUNO-001`

## Does Not Automatically Apply To

- Japanese generation
- English generation
- unrelated projects

## Evidence

- repeated Cantonese test runs in the Suno project

