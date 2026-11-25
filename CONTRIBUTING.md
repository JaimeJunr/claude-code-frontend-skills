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

## Change a skill description

Which skill loads depends on every description in the listing, so changing
any of them (an upstream sync included) makes `evals/trigger/results.json`
stale and fails `validate`. Measure again and commit the result:

```bash
python3 scripts/trigger_eval.py --run
```

It asks a real model each prompt of `evals/trigger/cases.json` three times
(about a minute, on your Claude login). UI prompts must load the router
without naming it; the others must not. A run that never reached the model
counts as invalid, not as a miss. Never edit `results.json` by hand. When a
request fails in real use, add it as a case first, then fix the description.

## Deploy

Users install from `main`, so a merge is the deploy. After it, the `deployed`
job installs every plugin from the published marketplace and fails when one
does not install or is not the merged commit. Revert the merge to roll back.

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

It runs, in CI order: `sync.py --check`, the unit tests, the trigger eval
check, the token budget
(through `uv` when tiktoken is not importable; `pip install -r
requirements-dev.txt` otherwise) and `claude plugin validate` on the
marketplace and on every plugin.
