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

## Before opening a PR

```bash
python3 scripts/sync.py --check
python3 -m unittest discover -s tests
pip install tiktoken && python3 scripts/token_budget.py
claude plugin validate .
```
