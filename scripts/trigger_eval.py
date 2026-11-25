#!/usr/bin/env python3
"""Does the router load on its own for UI requests, and stay out of the rest?

    python3 scripts/trigger_eval.py --run     # calls the model, writes results.json
    python3 scripts/trigger_eval.py --check   # no model: is results.json current and passing?

Which skill loads depends on every description in the listing, so a change to
any of them makes the recorded results stale. CI has no model credential (the
repo is public and fork PRs get no secrets): it runs --check, and --run is done
locally by whoever changed a description. Exit 1 on any problem.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
from typing import Any, Callable, Iterable

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "plugins"
SUITE_FILE = ROOT / "evals/trigger/cases.json"
RESULTS_FILE = ROOT / "evals/trigger/results.json"
WRITES = {"Write", "Edit", "NotebookEdit"}
# A redirect to a file (not to /dev/null or another descriptor, not `=>`), tee, or an in-place edit.
SHELL_WRITE = re.compile(r"(?<![=\-])>{1,2}\s*(?!&|>|\s|/dev/null)|\btee\s|\bsed\s+(-\S+\s+)*-\w*i")
MAX_TURNS = "4"
RUN_SECONDS = 240
STOP_SECONDS = 10
PARALLEL = 4


def fingerprint(suite: dict[str, Any], plugins: Path) -> str:
    digest = hashlib.sha256(json.dumps(suite, sort_keys=True).encode())
    for path in sorted(plugins.rglob("SKILL.md")):
        front = re.match(r"---\n(.*?)\n---", path.read_text(), re.S)
        if front is None:
            raise ValueError(f"invalid skill: {path} has no frontmatter, expected a --- block")
        digest.update(f"\0{path.relative_to(plugins)}\0{front.group(1)}".encode())
    return digest.hexdigest()


def writes_code(block: dict[str, Any]) -> bool:
    if block["name"] == "Bash":
        return bool(SHELL_WRITE.search(block["input"].get("command", "")))
    return block["name"] in WRITES


def classify(lines: Iterable[str], router: str) -> bool | None:
    """True: router loaded. False: answered or wrote code without it. None: invalid run."""
    for line in lines:
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("parent_tool_use_id"):
            continue  # a subagent's event says nothing about the main agent
        if event.get("type") == "assistant":
            for block in event["message"]["content"]:
                if block["type"] != "tool_use":
                    continue
                if block["name"] == "Skill" and block["input"].get("skill") == router:
                    return True
                if writes_code(block):
                    return False
        elif event.get("type") == "result":
            if event.get("subtype") == "error_max_turns":
                return False
            return None if event.get("is_error") else False
    return None


def problems(suite: dict[str, Any], results: dict[str, Any], current: str) -> list[str]:
    found = []
    if results.get("fingerprint") != current:
        found.append("stale results: a skill description or a case changed, "
                     "expected a new `python3 scripts/trigger_eval.py --run`")
    if results.get("model") != suite["model"]:
        found.append(f"model is {results.get('model')!r}, expected {suite['model']!r}")
    for case in suite["cases"]:
        hits = results.get("hits", {}).get(case["id"], [])
        if len(hits) != suite["runs"] or any(type(h) is not bool for h in hits):
            found.append(f"{case['id']}: runs are {hits!r}, expected {suite['runs']} valid runs")
        elif case["expect"] and sum(hits) < suite["min_hits_when_expected"]:
            found.append(f"{case['id']}: router loaded {sum(hits)}/{len(hits)}, "
                         f"expected at least {suite['min_hits_when_expected']}")
        elif not case["expect"] and sum(hits) > suite["max_hits_when_not_expected"]:
            found.append(f"{case['id']}: router loaded {sum(hits)}/{len(hits)}, "
                         f"expected at most {suite['max_hits_when_not_expected']}")
    return found


def stop(process: subprocess.Popen[str]) -> None:
    """Ends the run and what it started: SIGTERM lets the CLI clean up, SIGKILL is the last resort."""
    for sig in (signal.SIGTERM, signal.SIGKILL):
        try:
            os.killpg(process.pid, sig)
        except ProcessLookupError:
            break
        try:
            process.wait(STOP_SECONDS)
        except subprocess.TimeoutExpired:
            continue
    process.wait()


def run_case(suite: dict[str, Any], prompt: str, plugins: Path) -> bool | None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as project:
        Path(project, "package.json").write_text('{"name":"notaviva","private":true,"dependencies":{"react":"^19.0.0"}}')
        Path(project, "README.md").write_text("# Notaviva: desktop app that transcribes meetings\n")
        # `--` keeps a variadic flag from swallowing the prompt.
        process = subprocess.Popen(
            ["claude", "-p", "--setting-sources", "project", "--plugin-dir", str(plugins),
             "--model", suite["model"], "--output-format", "stream-json", "--verbose",
             "--max-turns", MAX_TURNS, "--permission-mode", "bypassPermissions", "--", prompt],
            cwd=project, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, text=True, start_new_session=True)
        killer = threading.Timer(RUN_SECONDS, stop, [process])
        killer.start()
        try:
            # Stops reading, and paying, at the first decisive event.
            return classify(process.stdout or [], suite["router"])
        finally:
            killer.cancel()
            stop(process)
            if process.stdout:
                process.stdout.close()


def measure(suite: dict[str, Any], plugins: Path,
            run: Callable[[dict[str, Any], str, Path], bool | None], version: str) -> dict[str, Any]:
    measured = fingerprint(suite, plugins)
    with ThreadPoolExecutor(PARALLEL) as pool:
        futures = {c["id"]: [pool.submit(run, suite, c["prompt"], plugins)
                             for _ in range(suite["runs"])] for c in suite["cases"]}
        hits = {case: [f.result() for f in runs] for case, runs in futures.items()}
    if fingerprint(suite, plugins) != measured:
        raise RuntimeError(f"a description in {plugins} changed during the run, expected no edits; run again")
    return {"fingerprint": measured, "model": suite["model"], "claude_code": version,
            "measured": date.today().isoformat(), "hits": hits}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--run", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--plugins", type=Path, default=PLUGINS)
    parser.add_argument("--results", type=Path, default=RESULTS_FILE)
    parser.add_argument("--only", help="with --run, one case id; prints, does not write results")
    args = parser.parse_args()
    if args.only and args.check:
        parser.error("--only goes with --run: the recorded results cover the full suite")
    return args


def select(suite: dict[str, Any], only: str | None) -> dict[str, Any]:
    cases = [c for c in suite["cases"] if only in (None, c["id"])]
    if not cases:
        raise SystemExit(f"--only {only!r} is not a case id in {SUITE_FILE}")
    return {**suite, "cases": cases}


def load_results(args: argparse.Namespace, suite: dict[str, Any]) -> dict[str, Any]:
    if args.check:
        if not args.results.exists():
            raise SystemExit(f"error: {args.results} is missing, expected a `--run` result")
        return json.loads(args.results.read_text())
    version = subprocess.run(["claude", "--version"], capture_output=True, text=True, check=True).stdout.split()[0]
    results = measure(suite, args.plugins.resolve(), run_case, version)
    for case, hits in results["hits"].items():
        print(f"  {case}: {hits}")
    if not args.only:
        args.results.write_text(json.dumps(results, indent=2) + "\n")
    return results


def main() -> int:
    args = parse_args()
    suite = select(json.loads(SUITE_FILE.read_text()), args.only)
    results = load_results(args, suite)
    found = problems(suite, results, fingerprint(suite, args.plugins.resolve()))
    for problem in found:
        print(f"error: {problem}")
    if not found:
        print(f"trigger eval: {len(suite['cases'])} cases ok")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
