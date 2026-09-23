# Capabilities

## Inherited Working Capabilities

This kit is designed to transfer these concrete capabilities to another Codex setup.

### 1. Skill-First Execution

- treat skills as mandatory when relevant
- do not skip process skills just because the task looks simple
- use explicit skill invocation before substantive work

### 2. Lightweight LOOP

- restore context
- frame outcome and file scope
- plan before risky work
- implement narrowly
- verify with fresh evidence
- audit against the plan
- update state and logs

### 3. Resume-Safe Project Context

- project carries context in files
- future sessions should not depend on one agent's memory
- state, plan, and audit become re-entry points

### 4. 夯实地基

- requirement points define goal, status, scope, verification, and open questions
- reusable knowledge sits behind `KB-*` entries
- requirements link to knowledge instead of embedding all conclusions inline
- this is the foundation layer that later can support graphs, structured maps, and even richer model representations

### 5. Experiment-Then-Promote Knowledge

- not every observation becomes canonical knowledge
- experiments record hypotheses and evidence first
- only stable conclusions get promoted into `KB-*`

### 6. Narrow-Change Discipline

- keep edits close to the actual request
- avoid unrelated cleanup
- preserve historical dirty state unless explicitly asked

### 7. Guardrail-Oriented Completion

- do not claim completion from stale results
- attach verification to the actual changed path
- use audit records for meaningful milestones

### 8. Execution Continuity

- record requirement changes before silently changing scope
- create a task and plan baseline before multi-step implementation
- capture Git-backed checkpoints at context boundaries
- reconcile every planned step against the actual result
- generate a handoff that tells the next session what to read first
- keep machine-observable lifecycle events in `.diji/events.jsonl`

## Capability Boundary

This kit does not itself provide:

- secrets
- project runtimes
- deployment credentials
- browser cookies
- third-party account state
