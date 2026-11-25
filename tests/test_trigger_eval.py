from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import trigger_eval as te

ROUTER = "frontend-stack:frontend-stack"
SUITE = {
    "model": "sonnet", "runs": 3, "min_hits_when_expected": 2,
    "max_hits_when_not_expected": 1, "router": ROUTER,
    "cases": [{"id": "build", "expect": True, "prompt": "p"},
              {"id": "backend", "expect": False, "prompt": "q"}],
}


def tool(name: str, **tool_input: str) -> str:
    return json.dumps({"type": "assistant", "message": {"content": [
        {"type": "tool_use", "name": name, "input": tool_input}]}})


def result(subtype: str = "success", is_error: bool = False) -> str:
    return json.dumps({"type": "result", "subtype": subtype, "is_error": is_error})


def recorded(build: int = 3, backend: int = 0) -> dict:
    return {"fingerprint": "abc", "model": "sonnet",
            "hits": {"build": [True] * build + [False] * (3 - build),
                     "backend": [True] * backend + [False] * (3 - backend)}}


class ClassifyRunTest(unittest.TestCase):
    def test_router_loaded_is_a_hit(self) -> None:
        self.assertIs(te.classify([tool("Skill", skill=ROUTER)], ROUTER), True)

    def test_answer_from_memory_is_a_miss(self) -> None:
        self.assertIs(te.classify([result()], ROUTER), False)

    def test_code_written_before_the_router_is_a_miss(self) -> None:
        lines = [tool("Write", file_path="a"), tool("Skill", skill=ROUTER)]
        self.assertIs(te.classify(lines, ROUTER), False)

    def test_turn_limit_without_the_router_is_a_miss(self) -> None:
        self.assertIs(te.classify([tool("Bash"), result("error_max_turns", True)], ROUTER), False)

    def test_run_that_never_reached_the_model_is_invalid_not_a_miss(self) -> None:
        # A swallowed prompt once scored 0 everywhere and looked like a measurement.
        self.assertIsNone(te.classify(['{"type":"system","subtype":"init"}', "Error: no prompt"], ROUTER))

    def test_api_error_is_invalid(self) -> None:
        self.assertIsNone(te.classify([result("success", True)], ROUTER))


class CheckTest(unittest.TestCase):
    def test_current_and_passing_results_have_no_problems(self) -> None:
        self.assertEqual(te.problems(SUITE, recorded(), "abc"), [])

    def test_changed_description_needs_a_new_measurement(self) -> None:
        self.assertIn("stale", te.problems(SUITE, recorded(), "other")[0])

    def test_router_that_stopped_loading_fails(self) -> None:
        self.assertIn("build", te.problems(SUITE, recorded(build=1), "abc")[0])

    def test_router_that_fires_on_backend_fails(self) -> None:
        self.assertIn("backend", te.problems(SUITE, recorded(backend=2), "abc")[0])

    def test_missing_runs_fail(self) -> None:
        short = recorded()
        short["hits"]["build"] = [True, True]
        self.assertIn("build", te.problems(SUITE, short, "abc")[0])

    def test_other_model_fails(self) -> None:
        self.assertIn("model", te.problems(SUITE, {**recorded(), "model": "opus"}, "abc")[0])


class FingerprintTest(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.skill = self.root / "p" / "skills" / "s" / "SKILL.md"
        self.skill.parent.mkdir(parents=True)

    def write(self, description: str, body: str = "body") -> str:
        self.skill.write_text(f"---\nname: s\ndescription: {description}\n---\n{body}\n")
        return te.fingerprint(SUITE, self.root)

    def test_description_change_changes_it(self) -> None:
        self.assertNotEqual(self.write("one"), self.write("two"))

    def test_body_change_does_not(self) -> None:
        self.assertEqual(self.write("one"), self.write("one", "other body"))

    def test_rival_skill_changes_it(self) -> None:
        before = self.write("one")
        rival = self.root / "q" / "skills" / "r" / "SKILL.md"
        rival.parent.mkdir(parents=True)
        rival.write_text("---\nname: r\ndescription: rival\n---\n")
        self.assertNotEqual(before, te.fingerprint(SUITE, self.root))

    def test_skill_in_a_custom_directory_changes_it(self) -> None:
        # ui-ux-pro-max ships its skills under .claude/skills.
        before = self.write("one")
        custom = self.root / "q" / ".claude" / "skills" / "r" / "SKILL.md"
        custom.parent.mkdir(parents=True)
        custom.write_text("---\nname: r\ndescription: rival\n---\n")
        self.assertNotEqual(before, te.fingerprint(SUITE, self.root))

    def test_skill_without_frontmatter_is_an_error(self) -> None:
        self.skill.write_text("no frontmatter")
        with self.assertRaises(ValueError):
            te.fingerprint(SUITE, self.root)


if __name__ == "__main__":
    unittest.main()
