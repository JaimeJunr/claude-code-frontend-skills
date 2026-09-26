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

A skill gets in if it is actively maintained, permissively licensed (MIT,
Apache-2.0, BSD or similar), and does something the stack does not already
cover.

## Change the router or agents

`plugins/frontend-stack/` is hand-written. Keep the router short: it is loaded
at the start of every frontend task.

## Before opening a PR

```bash
python3 scripts/sync.py --check
claude plugin validate .
```
