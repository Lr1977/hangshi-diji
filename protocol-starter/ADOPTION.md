# Protocol Starter Adoption

## Recommended Use

Use this starter when:

- the project spans many sessions
- multiple AI agents may continue the same work
- requirements, implementation, and learned knowledge can drift apart
- shallow "verification" has already caused trust damage

## How To Adopt

1. Copy the contents of `protocol-starter/` into the project root.
2. Merge project-specific safety and verification rules into `AGENTS.md`.
3. Update `STATE.md` with current live state and active requirement ids.
4. Create or normalize requirement docs under `docs/requirements/`.
5. Bind active requirements to `KB-*` and `EXP-*` entries.
6. Require new work to start with a `docs/plans/` plan doc.
7. Require every substantive change to end with `docs/verification/` and `docs/audits/`.

## Minimal Migration Strategy

If the project already has `AGENTS.md`, `LOOP.md`, and `STATE.md`:

- keep the project-specific content
- replace the weak sections with the protocol gate language from this starter
- add the missing `verification/`, `audits/`, `handoff/`, and `experience/` directories

## Practical Rule

If a future agent can understand the real state of the task without reading prior chat history, the protocol is doing its job.
