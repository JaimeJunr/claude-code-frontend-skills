from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCAL = [p["plugin"] for p in json.loads((ROOT / "stack.json").read_text())["local_plugins"]]


class LocalFrontmatterTest(unittest.TestCase):
    """Claude Code tolerates this, strict YAML loaders do not (no YAML parser in the stdlib)."""

    def test_unquoted_values_have_no_colon_space_or_comment(self) -> None:
        files = [p for name in LOCAL for pattern in ("skills/*/SKILL.md", "agents/*.md")
                 for p in (ROOT / "plugins" / name).glob(pattern)]
        self.assertTrue(files)
        for path in files:
            front = re.match(r"---\n(.*?)\n---", path.read_text(), re.S)
            self.assertIsNotNone(front, path)
            for line in front.group(1).splitlines():
                pair = re.match(r"[\w-]+:\s+([^\"'\s>|\[{].*)", line)
                if pair:
                    self.assertNotRegex(pair.group(1), r":(\s|$)|\s#", f"quote this value in {path}")


if __name__ == "__main__":
    unittest.main()
