#!/usr/bin/env python3
"""Token budget for the hand-written plugins (stack.json `local_plugins`).

A SKILL.md body is loaded whole every time the skill fires, and the router is
loaded at the start of every frontend task, so their size is a cost paid on
every run. Vendored upstream plugins are not checked: we do not edit them.

    pip install tiktoken
    python3 scripts/token_budget.py

Counts with tiktoken o200k_base. Exit 1 when a file is over its limit.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parent.parent
LIMITS = {"skill": 8000, "agent": 20000}


def budgeted_files(plugin: Path) -> list[tuple[Path, str]]:
    skills = [(p, "skill") for p in sorted(plugin.glob("skills/*/SKILL.md"))]
    agents = [(p, "agent") for p in sorted(plugin.glob("agents/*.md"))]
    return skills + agents


def over_budget(plugins: list[Path], count_tokens: Callable[[str], int],
                limits: dict[str, int]) -> list[tuple[Path, int, int]]:
    found = []
    for plugin in plugins:
        for path, kind in budgeted_files(plugin):
            tokens = count_tokens(path.read_text())
            if tokens > limits[kind]:
                found.append((path, tokens, limits[kind]))
    return found


def main() -> int:
    try:
        import tiktoken
    except ImportError:
        print("token_budget: tiktoken is not installed, expected `pip install tiktoken`")
        return 1
    encoding = tiktoken.get_encoding("o200k_base")
    stack = json.loads((ROOT / "stack.json").read_text())
    plugins = [ROOT / "plugins" / p["plugin"] for p in stack["local_plugins"]]

    def count(text: str) -> int:
        return len(encoding.encode(text))

    for plugin in plugins:
        for path, kind in budgeted_files(plugin):
            print(f"  {count(path.read_text()):6} / {LIMITS[kind]:6}  {path.relative_to(ROOT)}")
    found = over_budget(plugins, count, LIMITS)
    for path, tokens, limit in found:
        print(f"error: {path.relative_to(ROOT)} has {tokens} tokens, expected at most {limit}")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
