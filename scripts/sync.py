#!/usr/bin/env python3
"""Sync the frontend stack from its upstream repositories.

Reads stack.json, fetches every upstream at its ref, copies the selected
paths into plugins/<plugin>, applies compatibility patches and regenerates
the marketplace manifest, THIRD_PARTY_NOTICES.md, UPSTREAM.lock and the
skill table in README.md.

    python3 scripts/sync.py                 # fetch upstreams and rebuild
    python3 scripts/sync.py --src ./cache   # reuse clones named <owner>_<repo>
    python3 scripts/sync.py --check         # validate the tree, change nothing

Standard library only, so it runs anywhere Python 3.9+ does.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "plugins"
STACK = json.loads((ROOT / "stack.json").read_text())
LOCK_PATH = ROOT / "UPSTREAM.lock"
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
KEYWORDS = ["frontend", "design", "ui", "ux", "claude-code", "skills"]


def run(*cmd: str, cwd: Path | None = None) -> str:
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def fetch(repo: str, ref: str, src_dir: Path | None, cache: dict[str, Path], tmp: Path) -> Path:
    if repo in cache:
        return cache[repo]
    local = src_dir / repo.replace("/", "_") if src_dir else None
    if local and local.is_dir():
        path = local
    else:
        path = tmp / repo.replace("/", "_")
        run("git", "clone", "--quiet", "--depth", "1", "--branch", ref,
            f"https://github.com/{repo}.git", str(path))
    cache[repo] = path
    return path


def frontmatter(text: str) -> dict[str, str]:
    """Top-level scalar keys of a SKILL.md frontmatter (enough for name/description)."""
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if km:
            out[km.group(1)] = km.group(2).strip().strip('"').strip("'")
    return out


def patch_description(skill_md: Path, description: str) -> None:
    text = skill_md.read_text()
    m = FRONTMATTER.match(text)
    if not m:
        sys.exit(f"patch: {skill_md} has no frontmatter")
    lines = m.group(1).splitlines()
    idx = next((i for i, l in enumerate(lines) if l.startswith("description:")), None)
    if idx is None:
        sys.exit(f"patch: {skill_md} has no description")
    # Only single-line descriptions are patched; a multi-line one means upstream
    # changed shape and the patch must be reviewed by a human.
    if idx + 1 < len(lines) and not re.match(r"^[A-Za-z][\w-]*:", lines[idx + 1]):
        sys.exit(f"patch: {skill_md} description is multi-line, review the patch")
    escaped = description.replace("\\", "\\\\").replace('"', '\\"')
    lines[idx] = f'description: "{escaped}"'
    skill_md.write_text("---\n" + "\n".join(lines) + "\n---\n" + text[m.end():])


def drop_frontmatter_keys(skill_md: Path, keys: list[str]) -> None:
    text = skill_md.read_text()
    m = FRONTMATTER.match(text)
    if not m:
        sys.exit(f"patch: {skill_md} has no frontmatter")
    lines = m.group(1).splitlines()
    for key in keys:
        kept = [l for l in lines if not l.startswith(f"{key}:")]
        if len(kept) == len(lines):
            sys.exit(f"patch: {skill_md} has no frontmatter key {key!r}, review the patch")
        lines = kept
    skill_md.write_text("---\n" + "\n".join(lines) + "\n---\n" + text[m.end():])


def replace_in_body(skill_md: Path, pattern: str, replacement: str) -> None:
    text = skill_md.read_text()
    m = FRONTMATTER.match(text)
    head, body = (text[:m.end()], text[m.end():]) if m else ("", text)
    new_body, count = re.subn(pattern, replacement, body)
    # Zero matches means upstream rewrote the text; a silent no-op would ship the bug again.
    if count == 0:
        sys.exit(f"patch: {skill_md} has no match for {pattern!r}, review the patch")
    skill_md.write_text(head + new_body)


def apply_patch(skill_md: Path, patch: dict) -> None:
    if "description" in patch:
        patch_description(skill_md, patch["description"])
    if "drop_keys" in patch:
        drop_frontmatter_keys(skill_md, patch["drop_keys"])
    for rule in patch.get("replace", []):
        replace_in_body(skill_md, rule["pattern"], rule["with"])


def copy_path(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git", "__pycache__", "node_modules", ".DS_Store"))
    else:
        shutil.copy2(src, dst)


def plugin_manifest(name: str, description: str, author: str, license_: str,
                    homepage: str, skills_path: str | None) -> dict:
    manifest = {
        "name": name,
        "description": description,
        "author": {"name": author},
        "homepage": homepage,
        "repository": STACK["marketplace"]["repository"],
        "license": license_,
        "keywords": KEYWORDS,
    }
    if skills_path:
        manifest["skills"] = skills_path
    return manifest


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def sync(src_dir: Path | None) -> None:
    old_lock = json.loads(LOCK_PATH.read_text()) if LOCK_PATH.exists() else {}
    lock: dict[str, dict] = {}
    cache: dict[str, Path] = {}
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    with tempfile.TemporaryDirectory() as tmp:
        for src in STACK["sources"]:
            upstream = fetch(src["repo"], src["ref"], src_dir, cache, Path(tmp))
            commit = run("git", "rev-parse", "HEAD", cwd=upstream)
            dest = PLUGINS / src["plugin"]
            if dest.exists():
                shutil.rmtree(dest)
            for item in src["copy"]:
                origin = upstream / item["from"]
                if not origin.exists():
                    sys.exit(f"{src['id']}: {item['from']} not found upstream at {commit[:7]}")
                copy_path(origin, dest / item["to"])
            for lic in src.get("license_files", []):
                target = dest / Path(lic).name
                if not target.exists():
                    shutil.copy2(upstream / lic, target)
            for p in src.get("patches", []):
                apply_patch(dest / p["file"], p)
            homepage = src.get("homepage", f"https://github.com/{src['repo']}")
            write_json(dest / ".claude-plugin" / "plugin.json", plugin_manifest(
                src["plugin"], src["description"], src["author"], src["license"],
                homepage, src.get("skills_path")))
            prev = old_lock.get(src["id"], {})
            lock[src["id"]] = {
                "repo": src["repo"],
                "ref": src["ref"],
                "commit": commit,
                "synced_at": prev.get("synced_at", now) if prev.get("commit") == commit else now,
            }
            print(f"  {src['id']:15} {src['repo']:40} {commit[:7]}")

    write_json(LOCK_PATH, lock)
    write_marketplace()
    write_notices(lock)
    write_readme_table()


def write_marketplace() -> None:
    m = STACK["marketplace"]
    entries = []
    for local in STACK["local_plugins"]:
        entries.append({
            "name": local["plugin"],
            "source": f"./plugins/{local['plugin']}",
            "description": local["description"],
            "author": m["owner"],
            "category": local["category"],
            "license": "MIT",
            "homepage": m["repository"],
            "keywords": KEYWORDS,
        })
    for src in STACK["sources"]:
        entries.append({
            "name": src["plugin"],
            "source": f"./plugins/{src['plugin']}",
            "description": src["description"],
            "author": {"name": src["author"]},
            "category": src["category"],
            "license": src["license"],
            "homepage": src.get("homepage", f"https://github.com/{src['repo']}"),
            "keywords": KEYWORDS,
        })
    write_json(ROOT / ".claude-plugin" / "marketplace.json", {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": m["name"],
        "owner": m["owner"],
        "metadata": {"description": m["description"]},
        "plugins": entries,
    })


def write_notices(lock: dict) -> None:
    out = [
        "# Third-party notices",
        "",
        "This repository redistributes skills, agents and hooks from the projects below,",
        "each under its original license. The license file of every project is copied",
        "into its plugin folder. Everything not listed here (the `frontend-stack` plugin,",
        "`scripts/`, docs) is MIT, see [LICENSE](LICENSE).",
        "",
        "_Generated by `scripts/sync.py`, do not edit by hand._",
        "",
    ]
    for src in STACK["sources"]:
        info = lock[src["id"]]
        out += [
            f"## `plugins/{src['plugin']}`",
            "",
            f"- Upstream: https://github.com/{src['repo']} @ `{info['commit'][:7]}`",
            f"- Author: {src['author']}",
            f"- License: {src['license']} (see `plugins/{src['plugin']}/"
            f"{Path(src['license_files'][0]).name}`)",
        ]
        patches = src.get("patches", [])
        if patches:
            out.append("- Modifications: these files were patched for Claude Code compatibility;"
                       " everything else is copied verbatim.")
            out += [f"  - `{p['file']}`: {p['why']}" for p in patches]
        else:
            out.append("- Modifications: none, copied verbatim.")
        out.append("")
    (ROOT / "THIRD_PARTY_NOTICES.md").write_text("\n".join(out))


def all_skills() -> list[tuple[str, Path, dict[str, str]]]:
    found = []
    for plugin in sorted(p for p in PLUGINS.iterdir() if p.is_dir()):
        for skill_md in sorted(plugin.rglob("SKILL.md")):
            if "tests" in skill_md.relative_to(plugin).parts:
                continue
            found.append((plugin.name, skill_md, frontmatter(skill_md.read_text())))
    return found


def write_readme_table() -> None:
    readme = ROOT / "README.md"
    if not readme.exists():
        return
    order = [p["plugin"] for p in STACK["local_plugins"]] + [s["plugin"] for s in STACK["sources"]]
    by_plugin: dict[str, list[str]] = {}
    for plugin, _, fm in all_skills():
        by_plugin.setdefault(plugin, []).append(fm.get("name", "?"))
    total = sum(len(v) for v in by_plugin.values())
    rows = ["| Plugin | Skills | Count |", "|---|---|---|"]
    for plugin in order:
        names = by_plugin.get(plugin, [])
        rows.append(f"| `{plugin}` | {', '.join(f'`{n}`' for n in names)} | {len(names)} |")
    rows.append(f"| **Total** | | **{total}** |")
    block = "<!-- SKILLS:START -->\n" + "\n".join(rows) + "\n<!-- SKILLS:END -->"
    text = readme.read_text()
    new = re.sub(r"<!-- SKILLS:START -->.*?<!-- SKILLS:END -->", block, text, flags=re.S)
    readme.write_text(new)


def check() -> int:
    errors: list[str] = []
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    for entry in market["plugins"]:
        pdir = ROOT / entry["source"]
        if not (pdir / ".claude-plugin" / "plugin.json").exists():
            errors.append(f"{entry['name']}: missing .claude-plugin/plugin.json")
    names: dict[tuple[str, str], Path] = {}
    for plugin, skill_md, fm in all_skills():
        if not fm.get("name") or not fm.get("description"):
            errors.append(f"{skill_md.relative_to(ROOT)}: frontmatter needs name and description")
            continue
        key = (plugin, fm["name"])
        if key in names:
            errors.append(f"duplicate skill {fm['name']} in {plugin}")
        names[key] = skill_md
    for e in errors:
        print(f"error: {e}")
    print(f"checked {len(market['plugins'])} plugins, {len(names)} skills, {len(errors)} errors")
    return 1 if errors else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", type=Path, help="directory with pre-cloned upstreams (<owner>_<repo>)")
    ap.add_argument("--check", action="store_true", help="validate only")
    args = ap.parse_args()
    if args.check:
        return check()
    sync(args.src.resolve() if args.src else None)
    return check()


if __name__ == "__main__":
    sys.exit(main())
