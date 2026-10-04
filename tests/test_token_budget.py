"""Tests for scripts/token_budget.py.

    python3 -m unittest discover -s tests
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("token_budget", ROOT / "scripts" / "token_budget.py")
token_budget = importlib.util.module_from_spec(spec)
spec.loader.exec_module(token_budget)


def count_words(text: str) -> int:
    return len(text.split())


class OverBudgetTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.plugin = Path(self.tmp.name) / "frontend-stack"
        (self.plugin / "skills" / "router").mkdir(parents=True)
        (self.plugin / "agents").mkdir()
        self.skill = self.plugin / "skills" / "router" / "SKILL.md"
        self.agent = self.plugin / "agents" / "reviewer.md"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_files_within_budget_pass(self) -> None:
        self.skill.write_text("one two three")
        self.agent.write_text("one two")
        limits = {"skill": 3, "agent": 2}
        self.assertEqual(token_budget.over_budget([self.plugin], count_words, limits), [])

    def test_skill_over_budget_is_reported_with_count_and_limit(self) -> None:
        self.skill.write_text("one two three four")
        self.agent.write_text("one")
        limits = {"skill": 3, "agent": 2}
        found = token_budget.over_budget([self.plugin], count_words, limits)
        self.assertEqual(found, [(self.skill, 4, 3)])

    def test_agent_uses_its_own_limit(self) -> None:
        self.skill.write_text("one")
        self.agent.write_text("one two three")
        limits = {"skill": 10, "agent": 2}
        found = token_budget.over_budget([self.plugin], count_words, limits)
        self.assertEqual(found, [(self.agent, 3, 2)])

    def test_reference_files_are_not_budgeted(self) -> None:
        self.skill.write_text("one")
        refs = self.skill.parent / "references"
        refs.mkdir()
        (refs / "conflicts.md").write_text("word " * 50)
        limits = {"skill": 10, "agent": 10}
        self.assertEqual(token_budget.over_budget([self.plugin], count_words, limits), [])


if __name__ == "__main__":
    unittest.main()
