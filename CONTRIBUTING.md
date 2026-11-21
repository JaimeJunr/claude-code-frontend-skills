# Contributing

## Add or change an upstream skill

1. Edit [`stack.json`](stack.json): add a `copy` entry to an existing source, or
   a new source with `repo`, `ref`, `license`, `author`, `plugin`,
   `description` and `license_files`.
2. Run `python3 scripts/sync.py`. It regenerates `plugins/<plugin>`, the
   marketplace, `THIRD_PARTY_NOTICES.md`, `UPSTREAM.lock` and the README table.
3. Add the skill to the routing table in
   `plugins/frontend-stack/skills/frontend-stack/SKILL.md`.
4. If it contradicts a rule another pack already has, add a ruling to
   `references/conflicts.md`.

Never edit files under a generated plugin by hand; the next sync overwrites
them. Put changes in `stack.json` as a `patches` entry instead, with a `why`.
A patch targets one `file` and can combine:

- `description`: replace the frontmatter description (single-line only).
- `drop_keys`: remove frontmatter keys, e.g. `disable-model-invocation`.
- `replace`: `[{ "pattern": <regex>, "with": <replacement> }]` on the body.

Every patch fails the sync if upstream no longer has what it targets, so a
fix never silently stops applying.

A skill gets in if it is actively maintained, permissively licensed (MIT,
Apache-2.0, BSD or similar), and does something the stack does not already
cover.

## Change the router or agents

`plugins/frontend-stack/` is hand-written. Keep the router short: it is loaded
at the start of every frontend task.
`scripts/token_budget.py` fails CI when a SKILL.md there passes 8k tokens or an
agent passes 20k (tiktoken `o200k_base`).

## Commit, push and PR

Turn on the hooks once per clone:

```bash
git config core.hooksPath .githooks
```

- `pre-commit` (seconds): gitleaks on the staged changes, then
  `sync.py --check`. Without gitleaks installed it warns and the scan runs in CI.
- `pre-push` (about 15 s): `scripts/check.sh`, the same gate CI runs.

Work on a branch, never on `main`; `main` requires the `validate` check. Open
PRs with the `ship` project skill (`.claude/skills/ship/`): it runs the gate,
commits, pushes and writes the PR body.

## Before opening a PR

```bash
sh scripts/check.sh
```

It runs, in CI order: `sync.py --check`, the unit tests, the token budget
(through `uv` when tiktoken is not importable; `pip install -r
requirements-dev.txt` otherwise) and `claude plugin validate` on the
marketplace and on every plugin.
