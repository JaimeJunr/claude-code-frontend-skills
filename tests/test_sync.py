"""Tests for the compatibility patches applied by scripts/sync.py.

    python3 -m unittest discover -s tests
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("sync", ROOT / "scripts" / "sync.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

SKILL = """---
name: review-animations
description: Reviews animation code.
disable-model-invocation: true
---

Run `python3 scripts/search.py "x"` then `node scripts/tokens.cjs --dir src/`.
"""


class ApplyPatchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.skill_md = Path(self.tmp.name) / "SKILL.md"
        self.skill_md.write_text(SKILL)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_drop_keys_removes_frontmatter_key_and_keeps_the_rest(self) -> None:
        sync.apply_patch(self.skill_md, {"drop_keys": ["disable-model-invocation"]})
        text = self.skill_md.read_text()
        self.assertNotIn("disable-model-invocation", text)
        self.assertTrue(text.startswith("---\nname: review-animations\ndescription: Reviews animation code.\n---\n"))

    def test_drop_keys_fails_when_key_is_missing_upstream(self) -> None:
        with self.assertRaises(SystemExit):
            sync.apply_patch(self.skill_md, {"drop_keys": ["user-invocable"]})

    def test_replace_rewrites_body_only(self) -> None:
        sync.apply_patch(self.skill_md, {"replace": [{
            "pattern": r"\b(python3?|node) (scripts/[\w./-]+)",
            "with": r'\1 "${CLAUDE_SKILL_DIR}/\2"',
        }]})
        text = self.skill_md.read_text()
        self.assertIn('python3 "${CLAUDE_SKILL_DIR}/scripts/search.py" "x"', text)
        self.assertIn('node "${CLAUDE_SKILL_DIR}/scripts/tokens.cjs" --dir src/', text)
        self.assertIn("name: review-animations\n", text)

    def test_replace_fails_when_pattern_matches_nothing(self) -> None:
        with self.assertRaises(SystemExit):
            sync.apply_patch(self.skill_md, {"replace": [{"pattern": "ruby scripts/", "with": "x"}]})

    def test_description_and_drop_keys_combine(self) -> None:
        sync.apply_patch(self.skill_md, {
            "description": "Use ONLY when asked.",
            "drop_keys": ["disable-model-invocation"],
        })
        text = self.skill_md.read_text()
        self.assertIn('description: "Use ONLY when asked."\n', text)
        self.assertNotIn("disable-model-invocation", text)


if __name__ == "__main__":
    unittest.main()
