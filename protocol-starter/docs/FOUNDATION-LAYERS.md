# Foundation Layers

## Goal

Keep Hangshi Diji clean across multiple projects by separating stable protocol rules from project-bound knowledge and historical noise.

## Layers

### 1. Foundation-Core

Path:

- `docs/foundation-core/`

Meaning:

- globally reusable protocol rules

### 2. Foundation-Project

Path:

- `docs/foundation-project/`

Meaning:

- current project's isolated requirements and bound knowledge

### 3. Foundation-Learnings

Path:

- `docs/foundation-learnings/`

Meaning:

- experiments, pitfalls, and evidence-backed observations

### 4. Foundation-Deprecated

Path:

- `docs/foundation-deprecated/`

Meaning:

- historical but inactive material

## Standard Read Order

1. `docs/foundation-core/`
2. current project's `docs/foundation-project/`
3. linked `docs/foundation-learnings/`
4. `docs/foundation-deprecated/` only if historical tracing is needed

## Promotion Rules

### Promote into Core only if

- it is stable across projects
- it is not tied to one repo or one upstream quirk
- it changes how future agents should operate in general

### Keep in Project if

- it depends on the current repo
- it depends on the current product shape
- it is a local capability or requirement rule

### Keep in Learnings if

- it is evidence-bearing but not yet universal
- it is still contextual
- it is a pitfall or experiment outcome

### Move to Deprecated if

- it has been replaced
- it is no longer recommended
- it survives only for traceability

## Minimal Naming Guidance

- core rule docs: `CORE-*`
- project-bound docs: keep project-native naming
- learning docs: `LEARN-*` or dated experience docs
- deprecated docs: preserve original names and add deprecation note

