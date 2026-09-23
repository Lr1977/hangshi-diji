import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "tools" / "diji.py"


class DijiCliTests(unittest.TestCase):
    def run_cli(self, project: Path, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(CLI), "--root", str(project), *args],
            text=True,
            capture_output=True,
            check=False,
        )

    def make_project(self, *, git: bool = True) -> Path:
        project = Path(tempfile.mkdtemp(prefix="diji 测试 项目-"))
        if not git:
            return project
        subprocess.run(["git", "init", "-q"], cwd=project, check=True)
        return project

    def test_full_lifecycle_creates_recovery_artifacts(self) -> None:
        project = self.make_project()

        self.assertEqual(self.run_cli(project, "init", "--name", "Demo").returncode, 0)
        self.assertEqual(
            self.run_cli(
                project,
                "change",
                "Add durable checkpoints",
                "--requirements",
                "REQ-001",
            ).returncode,
            0,
        )
        start = self.run_cli(
            project,
            "start",
            "Implement checkpoint flow",
            "--requirement",
            "REQ-001",
            "--step",
            "Create checkpoint writer",
            "--step",
            "Run verification",
        )
        self.assertEqual(start.returncode, 0, start.stderr)
        self.assertEqual(self.run_cli(project, "checkpoint", "--note", "test evidence").returncode, 0)
        recon = self.run_cli(
            project,
            "reconcile",
            "--step-status",
            "1=done",
            "--step-status",
            "2=pending review",
        )
        self.assertEqual(recon.returncode, 0, recon.stderr)
        self.assertEqual(self.run_cli(project, "handoff", "--note", "test handoff").returncode, 0)

        self.assertTrue((project / "STATE.md").exists())
        self.assertTrue((project / "docs/checkpoints/CHECKPOINT-LATEST.md").exists())
        self.assertTrue((project / "docs/handoff/LATEST.md").exists())
        state = (project / "STATE.md").read_text(encoding="utf-8")
        self.assertIn("<!-- diji:managed:start -->", state)
        self.assertIn("## Project Identity", state)
        self.assertTrue(list((project / "docs/changes").glob("CHG-*.md")))
        self.assertTrue(list((project / "docs/plans").glob("PLAN-*.md")))
        self.assertTrue(list((project / "docs/tasks").glob("TASK-*.md")))
        self.assertTrue(list((project / "docs/reconciliation").glob("RECON-*.md")))

        events = (project / ".diji/events.jsonl").read_text(encoding="utf-8").splitlines()
        event_types = [json.loads(line)["type"] for line in events]
        self.assertEqual(
            event_types,
            [
                "PROJECT_INITIALIZED",
                "CHANGE_RECORDED",
                "TASK_STARTED",
                "CHECKPOINT_CREATED",
                "RECONCILIATION_CREATED",
                "HANDOFF_CREATED",
            ],
        )

    def test_commands_reject_non_git_directory(self) -> None:
        project = self.make_project(git=False)
        for command, command_args in (
            ("init", ()),
            ("change", ("new requirement",)),
            ("start", ("new task",)),
            ("checkpoint", ()),
            ("reconcile", ()),
            ("handoff", ()),
            ("status", ()),
        ):
            result = self.run_cli(project, command, *command_args)
            self.assertNotEqual(result.returncode, 0, command)
            self.assertIn("not a Git repository", result.stderr, command)

    def test_corrupt_config_returns_clear_error(self) -> None:
        project = self.make_project()
        self.assertEqual(self.run_cli(project, "init").returncode, 0)
        (project / ".diji" / "config.json").write_text("{broken", encoding="utf-8")

        result = self.run_cli(project, "status")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)
        self.assertIn("config.json", result.stderr)

    def test_handoff_preserves_user_state_content(self) -> None:
        project = self.make_project()
        self.assertEqual(self.run_cli(project, "init").returncode, 0)
        state = project / "STATE.md"
        state.write_text(state.read_text(encoding="utf-8") + "\nUser note: keep this.\n", encoding="utf-8")

        result = self.run_cli(project, "handoff", "--note", "preserve user content")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("User note: keep this.", state.read_text(encoding="utf-8"))

    def test_invalid_step_status_returns_clear_error(self) -> None:
        project = self.make_project()
        self.assertEqual(self.run_cli(project, "init").returncode, 0)
        self.assertEqual(self.run_cli(project, "start", "task").returncode, 0)

        result = self.run_cli(project, "reconcile", "--step-status", "bad")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid --step-status", result.stderr)

    def test_status_is_json(self) -> None:
        project = self.make_project()
        self.assertEqual(self.run_cli(project, "init").returncode, 0)
        result = self.run_cli(project, "status")
        self.assertEqual(result.returncode, 0)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["project"], project.name)
        self.assertIn("git", payload)


if __name__ == "__main__":
    unittest.main()
