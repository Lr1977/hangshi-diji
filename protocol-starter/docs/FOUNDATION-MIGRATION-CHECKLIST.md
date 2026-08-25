# Foundation Migration Checklist

## Goal

Move existing Hangshi Diji material into the four-layer structure without mixing scopes.

## Steps

- [ ] Identify the current project
- [ ] Create `PROJECT-BOOTSTRAP.md`
- [ ] List active requirements
- [ ] List authoritative KB entries
- [ ] Move stable protocol rules to `Foundation-Core`
- [ ] Move project-specific notes to `Foundation-Project`
- [ ] Move experiments and pitfall notes to `Foundation-Learnings`
- [ ] Move replaced material to `Foundation-Deprecated`
- [ ] Mark each item with status
- [ ] Attach verification targets to every promoted rule

## Classification Rules

### Foundation-Core

Use for rules that must remain true across projects.

### Foundation-Project

Use for one project's requirements, KB, and implementation notes.

### Foundation-Learnings

Use for experiments, observations, and pitfall records.

### Foundation-Deprecated

Use for old content that is kept only for traceability.

## Migration Output

Each migrated project should end with:

- one project bootstrap file
- one active requirement index
- one KB index
- one learning index if needed
- one deprecated index if needed

