# Foundation Migration Map

## Purpose

Map older Hangshi Diji content into the new four-layer structure so future agents can migrate without guessing.

## Classification Rules

### Put into Foundation-Core when

- the rule applies across projects
- the rule controls how agents should work in general
- the rule is stable and not tied to one repo

### Put into Foundation-Project when

- the content belongs to one product or one repo
- the content depends on project-specific paths, APIs, ports, or UI behavior
- the content is a project requirement, project KB, or project implementation note

### Put into Foundation-Learnings when

- the content comes from an experiment, a failed attempt, or a validated observation
- the content is useful but still contextual
- the content may influence future work without becoming a hard rule

### Put into Foundation-Deprecated when

- the content was replaced
- the content is no longer recommended
- the content is kept only for traceability

## Migration Table

| Old Content Type | New Layer | Notes |
|---|---|---|
| workflow protocol / agent operating rule | Foundation-Core | Example: plan -> implement -> verify -> audit |
| requirement binding guidance | Foundation-Core | Stable operating rule |
| session recovery / handoff read order | Foundation-Core | Stable operating rule for re-entering a project without chat history |
| project requirement docs | Foundation-Project | Keep isolated per project |
| project KB entries | Foundation-Project | Bind to concrete requirement points |
| experiment notes | Foundation-Learnings | Keep evidence and scope attached |
| pitfall logs | Foundation-Learnings | Useful, but not automatic rules |
| old failed prompt strategies | Foundation-Learnings or Foundation-Deprecated | Use Learnings if still informative; otherwise Deprecated |
| replaced templates | Foundation-Deprecated | Preserve history only |
| repo paths, ports, env names | Foundation-Project | Never promote to Core unless truly universal |
| upstream-specific quirks | Foundation-Project or Foundation-Learnings | Promote to Core only after repeated cross-project proof |

## Recommended Current Split for This Starter

### Already suitable for Foundation-Core

- `README.md` protocol framing
- `STATE.md` next-session read order
- plan / verification / audit discipline
- requirement-to-knowledge binding discipline

### Already suitable for Foundation-Project

- current project requirements
- current project KB index
- current handoff files and session entry hints
- repo-local operational notes
- local capability notes

### Already suitable for Foundation-Learnings

- trial outcomes
- bug repro notes
- prompt comparison outcomes
- upstream behavior observations

### Already suitable for Foundation-Deprecated

- superseded workflows
- old templates that should no longer be used
- failed protocol variants

## Promotion Checklist

Before moving any item upward, confirm:

1. Is it stable across projects?
2. Is it independent of one repo or one upstream quirk?
3. Does it change how future agents should operate in general?
4. Has it been verified more than once?

If any answer is no, keep it out of Foundation-Core.

## Recommended Naming

- Core: `CORE-*`
- Project: project-native naming
- Learnings: `LEARN-*` or dated notes
- Deprecated: `DEPRECATED-*` or archived original names
