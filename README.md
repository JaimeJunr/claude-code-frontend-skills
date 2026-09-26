# Claude Code Frontend Skills

**The frontend design stack for Claude Code, in one marketplace.** The best
frontend design skills, plugins and agents for Claude Code, curated,
de-conflicted and synced weekly from upstream:

- [**frontend-design**](https://github.com/anthropics/skills/tree/main/skills/frontend-design) by Anthropic
- [**Impeccable**](https://github.com/pbakaus/impeccable) by Paul Bakaus
- [**UI UX Pro Max**](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) by Next Level Builder
- [**Taste**](https://github.com/leonxlnx/taste-skill) by Leonxlnx
- [**Emil Kowalski's skills**](https://github.com/emilkowalski/skills) (design engineering and animation)

Plus a small glue plugin, **`frontend-stack`**, that makes them work
together: a router skill that picks the right skill for each task, a written
ruling for every rule the packs disagree on, and two agents
(`design-director`, `ui-reviewer`).

[Português](README.pt-BR.md)

## Why this exists

Each of these packs is great alone, and each one assumes it is the only design
skill installed. Install all five by hand and Claude loads four rulebooks for
the same "build me a landing page" prompt, and they disagree:

- Taste wants perpetual micro-motion; Emil Kowalski asks whether it should
  animate at all and keeps UI motion under 300 ms.
- Taste's `design-taste-frontend` says it is not for dashboards; nothing stops
  it from being loaded for one.
- Impeccable and Taste's Stitch skill both write `DESIGN.md`, in different
  formats.
- One Taste preset uses purple mesh gradients that another Taste skill bans.
- Aesthetic presets (minimalist, brutalist, "expensive") trigger on every UI
  task and average each other into generic output.

This repo fixes that:

| Problem | Fix |
|---|---|
| Five install commands, five repos to watch | One marketplace, weekly upstream sync PR |
| Skills fight over the same prompt | `frontend-stack` router: one lead skill + at most two supporting per task |
| Contradicting rules | [Precedence ladder and conflict rulings](plugins/frontend-stack/skills/frontend-stack/references/conflicts.md) |
| Presets hijack every task | Their descriptions are narrowed so they only fire on explicit request |
| Duplicates and model-specific skills | `taste-skill-v1` and `gpt-tasteskill` left out; image-gen skills are an optional plugin |
| Scripts break when files move | Upstream layout kept as-is inside each plugin, so bundled scripts still resolve |

## Install

In Claude Code:

```
/plugin marketplace add JaimeJunr/claude-code-frontend-skills
```

Then install the core stack:

```
/plugin install frontend-stack@frontend-stack
/plugin install frontend-design@frontend-stack
/plugin install impeccable@frontend-stack
/plugin install ui-ux-pro-max@frontend-stack
/plugin install taste@frontend-stack
/plugin install emil-design-eng@frontend-stack
```

Optional extras:

```
/plugin install taste-imagegen@frontend-stack
/plugin install emil-native@frontend-stack
```

Already have one of these installed from its original repo? Uninstall that
copy first so the skill is not loaded twice.

Every plugin is independent. Install only the ones you want; the router
falls back gracefully when a pack is missing.

### For a team project

To share the stack with everyone on a repo, commit this to
`.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "frontend-stack": {
      "source": {
        "source": "github",
        "repo": "JaimeJunr/claude-code-frontend-skills"
      }
    }
  },
  "enabledPlugins": {
    "frontend-stack@frontend-stack": true,
    "frontend-design@frontend-stack": true,
    "impeccable@frontend-stack": true,
    "ui-ux-pro-max@frontend-stack": true,
    "taste@frontend-stack": true,
    "emil-design-eng@frontend-stack": true
  }
}
```

**Enabled is not installed.** That file says which plugins the project wants.
The install itself is recorded per machine in
`~/.claude/plugins/installed_plugins.json`, which is not in git. So on every
new machine (a teammate, a fresh laptop, CI), the plugins show up as enabled
but do not load until they are installed there once. From the repo root:

```bash
for p in frontend-stack frontend-design impeccable ui-ux-pro-max taste emil-design-eng; do claude plugin install "$p@frontend-stack" --scope project; done
```

The command may rewrite the formatting of `.claude/settings.json` without
changing its content; `git checkout .claude/settings.json` keeps the diff
clean. Then check with `claude plugin list` and **start a new session**: plugins
load when a session starts, so the one you ran the install from will not see
them.

## What's inside

<!-- SKILLS:START -->
| Plugin | Skills | Count |
|---|---|---|
| `frontend-stack` | `frontend-stack` | 1 |
| `frontend-design` | `frontend-design` | 1 |
| `impeccable` | `impeccable` | 1 |
| `ui-ux-pro-max` | `banner-design`, `brand`, `design`, `design-system`, `slides`, `ui-styling`, `ui-ux-pro-max` | 7 |
| `taste` | `industrial-brutalist-ui`, `minimalist-ui`, `full-output-enforcement`, `redesign-existing-projects`, `high-end-visual-design`, `stitch-design-taste`, `design-taste-frontend` | 7 |
| `taste-imagegen` | `brandkit`, `image-to-code`, `imagegen-frontend-mobile`, `imagegen-frontend-web` | 4 |
| `emil-design-eng` | `animate`, `animation-vocabulary`, `apple-design`, `ask-sonner`, `emil-design-eng`, `find-animation-opportunities`, `improve-animations`, `mobile-native`, `pick-ui-library`, `prototype`, `review-animations` | 11 |
| `emil-native` | `animate-expo`, `write-swift` | 2 |
| **Total** | | **34** |
<!-- SKILLS:END -->

| Plugin | Best for |
|---|---|
| `frontend-stack` | Routing, conflict rules, `design-director` and `ui-reviewer` agents |
| `frontend-design` | Aesthetic direction for any new UI, anti-template checklist |
| `impeccable` | Plan (`shape`), critique, audit, polish, harden, adapt, clarify copy; 24 commands, design agents and live hooks |
| `ui-ux-pro-max` | Lookup database: styles, palettes, font pairings, charts, per-stack UX rules; tokens, shadcn/ui + Tailwind, brand, slides |
| `taste` | Landing pages and redesigns that do not look AI-generated; opt-in aesthetic presets |
| `emil-design-eng` | Animation craft, motion review, interaction polish, prototypes, native-feeling mobile web, library picks |
| `taste-imagegen` | Optional: generate a design image first, then code it (needs an image-generation tool) |
| `emil-native` | Optional: React Native / Expo animation, modern Swift |

## How to use it

You do not need to name skills. Ask for the work and the router picks:

```
Build a landing page for a coffee subscription startup
Redesign our settings page, it feels cluttered
Audit the checkout flow before we ship
The dropdown animation feels off, fix it
Which palette and font pairing fit a fintech dashboard?
```

Or call things directly:

```
/impeccable shape     plan UX before code
/impeccable audit     accessibility, performance, responsive
/impeccable polish    final pass before shipping
```

Or use the agents:

- **design-director**: turns a vague brief into a one-page direction (type,
  color, layout, motion, libraries) before any code is written.
- **ui-reviewer**: one prioritized review that combines Impeccable's audit,
  Emil's motion review and the anti-template checks. Read-only.

### Which skill leads

| Task | Lead |
|---|---|
| Landing page, portfolio, marketing site | Taste `design-taste-frontend` |
| Product UI: dashboards, tables, flows | Anthropic `frontend-design` + UI UX Pro Max |
| Plan / critique / audit / polish | Impeccable |
| Style, palette, fonts, charts | UI UX Pro Max |
| Anything that moves | Emil Kowalski |

Full routing table in the [router skill](plugins/frontend-stack/skills/frontend-stack/SKILL.md).

## Keeping up with upstream

Everything under `plugins/` except `frontend-stack` is generated from
[`stack.json`](stack.json) by [`scripts/sync.py`](scripts/sync.py). A GitHub
Action runs it every Monday and opens a PR when an upstream changed, so you
get new skills and fixes without watching five repos. Pinned commits are in
[`UPSTREAM.lock`](UPSTREAM.lock).

```bash
python3 scripts/sync.py          # pull upstreams and rebuild
python3 scripts/sync.py --check  # validate only
```

## Contributing

Suggest a skill, a routing change or a new conflict ruling in an issue or PR.
See [CONTRIBUTING.md](CONTRIBUTING.md). A skill gets in if it is actively
maintained, permissively licensed, and does something the stack does not
already cover.

## Credits and licenses

All credit for the bundled skills goes to their authors. Each plugin keeps its
upstream license file; the list of sources, licenses and every modification is
in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The glue plugin and
scripts are MIT.

If this saves you time, star the original repos too.

---

Keywords: Claude Code plugins, Claude Code skills, Claude skills frontend,
frontend design skill, UI design AI, UX design Claude, design system, Tailwind,
shadcn/ui, React, Next.js, web animation, anti AI slop, agent skills,
Claude Code marketplace.
