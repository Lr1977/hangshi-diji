# Foundation Read/Write Flow

## Read Flow

```mermaid
flowchart TD
  A[Start] --> B[Read Foundation-Core]
  B --> C[Read current Foundation-Project]
  C --> D{Requirement point has KB bindings?}
  D -- Yes --> E[Read linked Foundation-Learnings]
  D -- No --> F[Proceed with project scope only]
  E --> F
  F --> G{Need historical trace?}
  G -- Yes --> H[Read Foundation-Deprecated]
  G -- No --> I[Implement / verify / audit]
  H --> I
```

## Write Flow

```mermaid
flowchart TD
  A[New information] --> B{Is it cross-project stable?}
  B -- Yes --> C[Write to Foundation-Core]
  B -- No --> D{Is it project-bound?}
  D -- Yes --> E[Write to Foundation-Project]
  D -- No --> F{Is it evidence from experiment or pitfall?}
  F -- Yes --> G[Write to Foundation-Learnings]
  F -- No --> H[Write to Foundation-Deprecated or keep out]
  C --> I[Add status and verification note]
  E --> I
  G --> I
  H --> I
```

## Rules

### Read before acting

Always read from top to bottom:

1. Core
2. Project
3. Learnings
4. Deprecated only if needed

### Write with classification

Before writing any new item, decide:

- stable rule
- project rule
- learning
- deprecated

### Never mix layers

Do not place project-local findings directly into Core unless they have been verified as stable across projects.

### Keep verification attached

Every promoted item should carry:

- scope
- status
- verification target
- deprecation path if superseded

