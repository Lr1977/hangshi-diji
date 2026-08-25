# Portable Integration

## If You Already Have A Portable Codex Package

This kit is designed to layer cleanly onto an existing portable Codex package such as:

- `codex-portable-migration`

## Recommended Merge Strategy

Use the existing portable package for:

- `.codex` base assets
- plugins
- localized launcher layer
- isolation launchers
- setup and verify scripts

Use this kit for:

- the general operating model
- the requirement-to-knowledge binding method
- the new project starter templates

## Practical Integration

Copy these into the portable package as a new reference area or starter bundle:

- `README.md`
- `MANUAL.md`
- `CAPABILITIES.md`
- `ADOPTION-STEPS.md`
- `SKILLSET-RECOMMENDED.md`
- `starter/`

## Boundary

Do not overwrite working machine-specific files unless you intend to replace them.

This kit is meant to complement the portable package, not destroy it.
