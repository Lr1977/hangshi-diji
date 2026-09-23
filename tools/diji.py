#!/usr/bin/env python3
"""Small, dependency-free execution continuity CLI for Hangshi Diji."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Iterable


MANAGED_START = "<!-- diji:managed:start -->"
MANAGED_END = "<!-- diji:managed:end -->"
DOC_DIRS = (
    "docs/changes",
    "docs/plans",
    "docs/tasks",
    "docs/reconciliation",
    "docs/checkpoints",
    "docs/events",
    "docs/verification",
    "docs/handoff",
)


def now() -> datetime:
    return datetime.now().astimezone()


def stamp() -> str:
    return now().strftime("%Y%m%d-%H%M%S")


def iso_now() -> str:
    return now().isoformat(timespec="seconds")


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "item"


def root_path(value: str | None) -> Path:
    root = Path(value or ".").expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"root does not exist: {root}")
    return root


def run_git(root: Path, *args: str) -> tuple[int, str]:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )
    except OSError as exc:
        return 127, str(exc)
    output = (result.stdout or result.stderr).strip()
    return result.returncode, output


def require_git(root: Path) -> None:
    code, _ = run_git(root, "rev-parse", "--show-toplevel")
    if code != 0:
        raise SystemExit(f"not a Git repository: {root}")


def ensure_layout(root: Path) -> None:
    (root / ".diji").mkdir(exist_ok=True)
    for directory in DOC_DIRS:
        (root / directory).mkdir(parents=True, exist_ok=True)


def config_path(root: Path) -> Path:
    return root / ".diji" / "config.json"


def load_config(root: Path) -> dict:
    path = config_path(root)
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid {path}: {exc}")


def save_config(root: Path, config: dict) -> None:
    config_path(root).write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def append_event(root: Path, event_type: str, **metadata: object) -> None:
    event = {"time": iso_now(), "type": event_type, **metadata}
    event_path = root / ".diji" / "events.jsonl"
    with event_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def project_state_template(root: Path) -> str:
    return f"""# Live State

{MANAGED_START}
## Diji Managed Snapshot

- project name: {root.name}
- project root: `{root}`
- last diji update: {iso_now()}
- current task: none
- current checkpoint: none
- next action: initialize a task with `python tools/diji.py start`
{MANAGED_END}

## Project Identity

- project name:
- project root:
- current branch:
- active requirement ids:
- current operator goal:

## Last Handoff

- session title:
- date:
- what was done:
- what was verified:
- what remains:

## Current Focus

-

## Known Risks

-

## Open Questions

-

## Next Session Entry Hint

1. `docs/checkpoints/CHECKPOINT-LATEST.md`
2. `docs/handoff/LATEST.md`
3. current task and plan
4. latest verification and reconciliation
"""


def cmd_init(args: argparse.Namespace) -> int:
    root = root_path(args.root)
    require_git(root)
    ensure_layout(root)
    config = load_config(root)
    if not config:
        config = {
            "project_name": args.name or root.name,
            "project_root": str(root),
            "created_at": iso_now(),
            "current_task": None,
            "last_checkpoint": None,
            "last_reconciliation": None,
        }
        save_config(root, config)
        append_event(root, "PROJECT_INITIALIZED", project=str(root))
    write_if_missing(root / "STATE.md", project_state_template(root))
    write_if_missing(
        root / "docs" / "handoff" / "LATEST.md",
        "# Latest Handoff\n\nInitialized by diji. Run `diji checkpoint` after work begins.\n",
    )
    print(f"initialized {config.get('project_name', root.name)} at {root}")
    return 0


def split_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def unique_path(directory: Path, prefix: str, title: str, suffix: str = "md") -> Path:
    base = f"{prefix}-{stamp()}-{slug(title)}"
    candidate = directory / f"{base}.{suffix}"
    counter = 2
    while candidate.exists():
        candidate = directory / f"{base}-{counter}.{suffix}"
        counter += 1
    return candidate


def cmd_change(args: argparse.Namespace) -> int:
    root = root_path(args.root)
    require_git(root)
    ensure_layout(root)
    path = unique_path(root / "docs/changes", "CHG", args.title)
    requirements = split_csv(args.requirements)
    req_lines = "\n".join(f"- `{item}`" for item in requirements) or "- pending"
    content = f"""# {path.stem}: {args.title}

## Relationship

- {args.relation}

## New Requirement

- {args.title}

## Affected Existing Requirements

{req_lines}

## Impact Analysis

### Must Remain Consistent

- pending review

### Affected Plans

- pending review

### Affected Code Or Files

- pending review

### Verification To Repeat

- pending review

## Decision

- pending

## Evidence

- created by `diji change` at {iso_now()}
"""
    path.write_text(content, encoding="utf-8")
    append_event(
        root,
        "CHANGE_RECORDED",
        change=str(path.relative_to(root)),
        relation=args.relation,
        requirements=requirements,
    )
    print(path)
    return 0


def task_paths(root: Path, task_id: str | None = None) -> list[Path]:
    paths = sorted((root / "docs/tasks").glob("TASK-*.md"), reverse=True)
    if task_id:
        paths = [path for path in paths if task_id in path.name or task_id in path.read_text(encoding="utf-8")]
    return paths


def cmd_start(args: argparse.Namespace) -> int:
    root = root_path(args.root)
    require_git(root)
    ensure_layout(root)
    task_path = unique_path(root / "docs/tasks", "TASK", args.title)
    plan_path = unique_path(root / "docs/plans", "PLAN", args.title)
    task_id = task_path.stem.split("-", 3)[0:3]
    task_id = "-".join(task_id)
    requirements = split_csv(args.requirement)
    steps = args.step or ["Implement the scoped change", "Run verification", "Reconcile plan against actual result"]
    step_lines = "\n".join(f"- [ ] {step}" for step in steps)
    req_lines = "\n".join(f"- `{item}`" for item in requirements) or "- pending"
    plan_ref = plan_path.relative_to(root).as_posix()
    task_content = f"""# {task_id}: {args.title}

## Status

- in progress

## Requirement Bindings

{req_lines}

## Plan Baseline

- plan file: `{plan_ref}`
- plan version: `v1`
- approved at: {iso_now()}

## Intended Scope

{args.scope or '- pending'}

## Implementation Steps

{step_lines}

## Execution Evidence

- changed files: pending
- commands: pending
- tests: pending

## Deviations

- none recorded

## Next Action

- begin implementation and checkpoint before context changes
"""
    plan_content = f"""# {plan_path.stem}: {args.title}

## Goal

{args.scope or args.title}

## Scope

{args.scope or '- pending'}

## Requirement Bindings

{req_lines}

## Implementation Steps

{chr(10).join(f'{index}. {step}' for index, step in enumerate(steps, 1))}

## Verification Matrix

1. Run the relevant test or check.
   expected: evidence is recorded.
2. Reconcile every implementation step against the actual result.
   expected: deviations are explicit.

## Audit Target

The task is not complete until verification and reconciliation records exist.
"""
    task_path.write_text(task_content, encoding="utf-8")
    plan_path.write_text(plan_content, encoding="utf-8")
    config = load_config(root)
    config["current_task"] = {
        "id": task_id,
        "title": args.title,
        "task_file": task_path.relative_to(root).as_posix(),
        "plan_file": plan_path.relative_to(root).as_posix(),
        "started_at": iso_now(),
    }
    save_config(root, config)
    append_event(
        root,
        "TASK_STARTED",
        task=task_id,
        title=args.title,
        task_file=task_path.relative_to(root).as_posix(),
        plan_file=plan_path.relative_to(root).as_posix(),
    )
    print(task_path)
    print(plan_path)
    return 0


def git_evidence(root: Path) -> dict[str, str | list[str]]:
    _, branch = run_git(root, "branch", "--show-current")
    _, status = run_git(root, "status", "--short")
    _, diffstat = run_git(root, "diff", "--stat")
    changed = [line for line in status.splitlines() if line.strip()]
    return {"branch": branch or "(detached)", "status": status or "clean", "diffstat": diffstat or "none", "changed": changed}


def current_task(root: Path) -> dict:
    return load_config(root).get("current_task") or {}


def checkpoint_content(root: Path, note: str) -> str:
    evidence = git_evidence(root)
    task = current_task(root)
    changed = "\n".join(f"- `{item}`" for item in evidence["changed"]) or "- none"
    return f"""# CHECKPOINT-{stamp()}

## Project

- name: {load_config(root).get('project_name', root.name)}
- root: `{root}`
- branch: `{evidence['branch']}`
- captured at: {iso_now()}

## Current Task

- id: {task.get('id', 'none')}
- title: {task.get('title', 'none')}
- status: in progress

## Workspace Evidence

- Git status: `{evidence['status']}`
- Git diff summary: `{evidence['diffstat']}`
- changed files:
{changed}

## Confirmed Facts

- checkpoint generated from the current workspace by `diji checkpoint`
- {note or 'no additional note supplied'}

## Risks And Deviations

- semantic completion is not inferred from Git state
- review the current task and plan before continuing

## Next Action

- complete the next unchecked task step, then run verification and reconciliation

## Read First Next Session

1. `STATE.md`
2. `docs/checkpoints/CHECKPOINT-LATEST.md`
3. current task and plan
4. latest verification and reconciliation
"""


def cmd_checkpoint(args: argparse.Namespace) -> int:
    root = root_path(args.root)
    ensure_layout(root)
    require_git(root)
    content = checkpoint_content(root, args.note or "")
    latest = root / "docs/checkpoints/CHECKPOINT-LATEST.md"
    dated = root / "docs/checkpoints" / f"CHECKPOINT-{stamp()}.md"
    latest.write_text(content, encoding="utf-8")
    dated.write_text(content, encoding="utf-8")
    config = load_config(root)
    config["last_checkpoint"] = latest.relative_to(root).as_posix()
    save_config(root, config)
    append_event(root, "CHECKPOINT_CREATED", checkpoint=str(latest.relative_to(root)))
    print(latest)
    return 0


def extract_steps(path: Path) -> list[str]:
    if not path.exists():
        return []
    steps = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*- \[[ xX]\]\s+(.*)$", line)
        if match:
            steps.append(match.group(1).strip())
    return steps


def parse_step_status(values: Iterable[str]) -> dict[int, str]:
    result: dict[int, str] = {}
    for value in values:
        if "=" not in value:
            raise SystemExit(f"invalid --step-status {value!r}; use N=status")
        number, status = value.split("=", 1)
        try:
            result[int(number)] = status.strip()
        except ValueError as exc:
            raise SystemExit(f"invalid step number in {value!r}") from exc
    return result


def cmd_reconcile(args: argparse.Namespace) -> int:
    root = root_path(args.root)
    require_git(root)
    ensure_layout(root)
    task_candidates = task_paths(root, args.task)
    if not task_candidates:
        raise SystemExit("no matching task file; run diji start first")
    task_path = task_candidates[0]
    task_id = task_path.stem.split(":", 1)[0]
    steps = extract_steps(task_path)
    statuses = parse_step_status(args.step_status)
    rows = []
    if not steps:
        steps = ["Add plan steps to the task file before reconciling"]
    for index, step in enumerate(steps, 1):
        status = statuses.get(index, "pending review")
        rows.append(f"| {index}. {step} |  | {status} |  |  |")
    evidence = git_evidence(root)
    path = unique_path(root / "docs/reconciliation", "RECON", task_id)
    changed = "\n".join(f"- `{item}`" for item in evidence["changed"]) or "- none"
    content = f"""# {path.stem}: {task_id}

## Task

- `{task_id}`
- source: `{task_path.relative_to(root).as_posix()}`
- generated at: {iso_now()}

## Result

- {args.result}

## Plan Versus Actual

| Plan step | Actual result | Status | Deviation | Evidence |
|---|---|---|---|---|
{chr(10).join(rows)}

## Requirement Impact

- review whether any deviation changes the bound requirement.

## Workspace Evidence

- branch: `{evidence['branch']}`
- Git status: `{evidence['status']}`
- Git diff summary: `{evidence['diffstat']}`
- changed files:
{changed}

## Verification Evidence

- add test commands and result links before marking complete.

## Remaining Work

- add actual results and evidence for every pending-review row

## Approval

- reviewer:
- date:
"""
    path.write_text(content, encoding="utf-8")
    config = load_config(root)
    config["last_reconciliation"] = path.relative_to(root).as_posix()
    save_config(root, config)
    append_event(root, "RECONCILIATION_CREATED", reconciliation=str(path.relative_to(root)), task=task_id)
    print(path)
    return 0


def upsert_managed_block(path: Path, block: str) -> None:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    pattern = re.compile(re.escape(MANAGED_START) + r".*?" + re.escape(MANAGED_END), re.S)
    replacement = f"{MANAGED_START}\n{block.rstrip()}\n{MANAGED_END}"
    if pattern.search(existing):
        updated = pattern.sub(lambda _: replacement, existing, count=1)
    else:
        updated = replacement + "\n\n" + existing
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(updated, encoding="utf-8")


def cmd_handoff(args: argparse.Namespace) -> int:
    root = root_path(args.root)
    require_git(root)
    ensure_layout(root)
    checkpoint = root / "docs/checkpoints/CHECKPOINT-LATEST.md"
    config = load_config(root)
    task = current_task(root)
    evidence = git_evidence(root)
    handoff = root / "docs/handoff/LATEST.md"
    content = f"""# Latest Handoff

## Session

- generated at: {iso_now()}
- operator note: {args.note or 'none'}

## Current Task

- id: {task.get('id', 'none')}
- title: {task.get('title', 'none')}
- task file: `{task.get('task_file', 'none')}`
- plan file: `{task.get('plan_file', 'none')}`

## What Was Verified

- checkpoint exists: {'yes' if checkpoint.exists() else 'no'}
- Git branch: `{evidence['branch']}`
- Git status: `{evidence['status']}`
- latest reconciliation: `{config.get('last_reconciliation', 'none')}`

## What Remains

- review the checkpoint and task plan
- complete verification and reconciliation before claiming completion

## Read First Next Time

1. `STATE.md`
2. `docs/checkpoints/CHECKPOINT-LATEST.md`
3. `{task.get('task_file', 'current task file')}`
4. `{task.get('plan_file', 'current plan file')}`
5. latest verification and reconciliation
"""
    handoff.write_text(content, encoding="utf-8")
    state_block = f"""## Diji Managed Snapshot

- project name: {config.get('project_name', root.name)}
- project root: `{root}`
- last diji update: {iso_now()}
- current task: {task.get('id', 'none')} ({task.get('title', 'none')})
- current checkpoint: `{config.get('last_checkpoint', 'none')}`
- current reconciliation: `{config.get('last_reconciliation', 'none')}`
- Git status: `{evidence['status']}`
- next action: read the latest checkpoint and reconcile the current task
"""
    upsert_managed_block(root / "STATE.md", state_block)
    append_event(root, "HANDOFF_CREATED", handoff=str(handoff.relative_to(root)))
    print(handoff)
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    root = root_path(args.root)
    require_git(root)
    config = load_config(root)
    evidence = git_evidence(root)
    payload = {
        "project": config.get("project_name", root.name),
        "root": str(root),
        "task": config.get("current_task"),
        "checkpoint": config.get("last_checkpoint"),
        "reconciliation": config.get("last_reconciliation"),
        "git": evidence,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Hangshi Diji execution continuity CLI")
    parser.add_argument("--root", default=".", help="project root; defaults to current directory")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="initialize the Diji project layout")
    init.add_argument("--name", help="display name for the project")
    init.set_defaults(func=cmd_init)

    change = sub.add_parser("change", help="record a new requirement and its impact relationship")
    change.add_argument("title")
    change.add_argument("--relation", choices=("append", "revise", "replace", "conflict", "unrelated"), default="append")
    change.add_argument("--requirements", help="comma-separated existing requirement ids")
    change.set_defaults(func=cmd_change)

    start = sub.add_parser("start", help="create a task and plan baseline")
    start.add_argument("title")
    start.add_argument("--requirement", help="comma-separated requirement ids")
    start.add_argument("--scope", help="intended scope")
    start.add_argument("--step", action="append", help="repeat for each implementation step")
    start.set_defaults(func=cmd_start)

    checkpoint = sub.add_parser("checkpoint", help="capture current task and Git evidence")
    checkpoint.add_argument("--note", help="short confirmed fact or operator note")
    checkpoint.set_defaults(func=cmd_checkpoint)

    reconcile = sub.add_parser("reconcile", help="create a plan-versus-actual reconciliation draft")
    reconcile.add_argument("--task", help="task id or filename fragment")
    reconcile.add_argument("--result", choices=("consistent", "partially consistent", "deviation approved", "incomplete", "blocked"), default="partially consistent")
    reconcile.add_argument("--step-status", action="append", default=[], help="repeat as N=status")
    reconcile.set_defaults(func=cmd_reconcile)

    handoff = sub.add_parser("handoff", help="generate latest handoff and update managed STATE block")
    handoff.add_argument("--note", help="short operator note")
    handoff.set_defaults(func=cmd_handoff)

    status = sub.add_parser("status", help="show current Diji and Git status")
    status.set_defaults(func=cmd_status)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except BrokenPipeError:
        return 0


if __name__ == "__main__":
    sys.exit(main())
