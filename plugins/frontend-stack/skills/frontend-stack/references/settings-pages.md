# Settings with many sections: sites, desktop apps, CLIs and TUIs

Read during Direction and Build when a product has a settings or preferences
area large enough to need its own navigation, in a web app, a desktop app, a
CLI or a TUI. These are product patterns, not a visual preset: take the
mechanism, never the signature.

Researched on 2026-11-21 from official product docs, design-system guidance
and two captures of the Claude desktop app's settings (Code and Account
pages, Linux, taken by the maintainer). Settings live behind a login, so the
web entries were not inspected in a browser the way `reference-gallery.md`
entries were. Rows marked "from memory" had no primary doc confirming the
detail; open the real screen before citing them as evidence.

## Decide these first

1. **Scope.** List who each setting belongs to: the person (account,
   preferences), this device only, the organization or workspace (members,
   billing, security), the project or resource. Each scope gets its own area
   and URL, or a visible badge on the row. Mixing a personal preference with
   an admin control is the most common mistake.
2. **Size of the catalog.** Up to about 15-20 sections, a grouped sidebar
   with group labels or dividers works. Past that, open on an index page of
   grouped cards with search, and keep the sidebar for inside a group.
3. **Save model, per control.** Toggles and selects save on change with a
   quiet "Saved" confirmation. Text fields and changes with consequences sit
   in a card with its own Save button; leaving with unsaved edits asks first.
   Match the feedback to the weight of the change (Primer "Customize").
4. **Inheritance.** If a value can come from a higher scope, say so on the
   field ("inherited from the organization") and offer override and reset.

## Layout rules

- **Search across every setting.** A result opens the section and highlights
  the field. People know the name of the thing, not where it lives.
- **One URL per section**, so support, docs and the product can deep-link.
- **Contextual entry points.** A gear next to a feature opens its section;
  do not bury local options only in a global settings page (Primer, Apple HIG).
- **Group by the user's task**, not by the internal data model or the team
  that owns the code. Label groups in plain words (Polaris app-settings layout).
- **Danger zone last.** Irreversible actions (delete, transfer, change
  visibility) sit at the end of the section, in the danger color, and ask
  for a typed confirmation such as the resource name.
- **Missing permission:** show the control disabled with the reason ("Only
  admins can change this") instead of hiding it, so the feature does not
  look absent.
- **Advanced options collapsed** under a disclosure, with a short line on
  when you would need them.
- **Narrow screens:** the list-detail layout becomes drill-in pages (Primer
  layout, Android settings pattern).

## The settings row

The Claude desktop app's settings are a clean model of one row, worth copying
as a mechanism:

- Label on the left, one line of description under it, the control aligned
  right. The description says what the setting does **and what it costs**
  ("uses part of your plan's usage"), so the consequence is read before the
  toggle is flipped.
- The control matches the choice: text field for free text, toggle for
  on/off, a segmented control for 2-4 options visible at once, a select for
  more, a button for an action.
- A small badge on the row marks scope ("local only": this device, not
  synced to the account), instead of a separate page per scope.
- When a setting belongs to another section, the row is a button that opens
  that section ("Open Appearance") rather than a second copy of the control.
- Read-only identifiers (an organization ID) get a copy button, not a
  disabled input.
- Sessions and devices are a table with a "Current" badge on this device and
  the bulk action ("Sign out of all devices") in the section header.
- The sidebar has search on top, groups separated by dividers (account and
  billing; personal experience; extensions; apps) and a link that leaves the
  app pinned at the bottom with an outward arrow (API keys).
- Watch-out seen in the same capture: a long sidebar label truncates
  ("Aplicativo para de..."). Test translated labels at the narrowest width.

## Desktop apps

- Open settings with the platform shortcut (`Cmd+,` on macOS, `Ctrl+,`
  elsewhere) and close with Esc. A modal or a separate window both work; keep
  the sidebar and search in either.
- Offer both a searchable UI and the file behind it for power users, and say
  which one wins when both are edited (VS Code, Zed).
- Appearance: derive a theme from a few inputs instead of exposing dozens of
  color pickers. Linear rebuilt its themes around base color, accent color
  and contrast, including high-contrast options.
- Extension ecosystems: each extension's preferences live in one shared
  place with the same row anatomy (Raycast). Users praise Raycast's
  keyboard-first speed but report a learning curve in setting up commands,
  extensions and settings (r/macapps thread, 2026): show defaults that work
  before asking for setup.

## CLIs

- **Layered config with documented precedence.** Git reads system, global,
  local and worktree files, later overriding earlier; npm goes CLI flag →
  `npm_config_*` env var → project `.npmrc` → user → global → defaults;
  Claude Code goes managed → `--settings` flag → user → project → local.
  Write the order in the help text.
- **Show where a value came from.** `git config --list --show-origin` prints
  the file behind every value; `k9s info` prints where config loads from.
- **`config get | set | list` subcommands** so nobody has to edit a file to
  change one value (`gh config`, `npm config`).
- **Dump the defaults with docs.** `ghostty +show-config --default --docs`
  prints every option with its default and explanation.
- **One env var to move the config** (`K9S_CONFIG_DIR`, `STARSHIP_CONFIG`)
  and XDG paths by default.

## TUIs

- An in-app options screen on a known key (`F2` in htop and btop, `o` in
  btop), or a command that opens the config file in the editor (`:config-open`
  in Helix, `e` on the lazygit status panel).
- Runtime changes without restart for what is safe to change live (`:set` in
  Helix), and say which ones need a restart.
- Keep the same row anatomy as the GUI: label, current value, short help on
  the selected row. Claude Code's `/config` is a short tabbed list of the
  common options, not the whole settings file: expose the frequent ones and
  point to the file for the rest.

## Reference patterns

| Reference | Pattern to learn from |
|---|---|
| Claude desktop app | Row anatomy with cost in the description, "local only" scope badge, cross-section buttons, search plus divided sidebar. See "The settings row". |
| GitHub (account, organization, repository) | Each scope has its own settings area and URL; the sidebar is grouped under labels; a Danger Zone at the end confirms visibility changes and deletes. |
| VS Code, Zed | Searchable settings editor plus the JSON file; VS Code adds User and Workspace scopes side by side and a "modified" filter. |
| Vercel (team and project) | Team and project settings are separate sidebars; `vercel.json` can override dashboard values. Per-card Save with a help footer: from memory. |
| Linear | Personal preferences and workspace administration are separate groups; admin sections depend on role; themes from base, accent and contrast. |
| Slack | A global notification preference with per-channel overrides: the inherited rule and the exception are both visible. |
| Raycast | Per-extension preferences in one place; the Store makes extensions searchable and browsable by featured, recent and popular. |
| Stripe Dashboard | With dozens of sections, the entry is an index of grouped cards, not one long sidebar. From memory. |
| Git, npm, Ghostty | CLI layering, show-origin and documented defaults. See "CLIs". |
| Counter-example: macOS System Settings (Ventura and later) | Moving the iPhone list model to the desktop made categories harder to find; reviewers criticized placement and inconsistency. |

## Sources

- GitHub Primer, [Customize](https://primer.style/product/scenario-patterns/customize/) and [Layout](https://primer.style/product/getting-started/foundations/layout/)
- Shopify Polaris, [App settings layout](https://polaris-site-prod-kit.shopify.prod.shopifyapps.com/patterns/app-settings-layout)
- Apple HIG, [Settings](https://developer.apple.com/design/human-interface-guidelines/settings); Android, [Settings pattern](https://developer.android.com/design/ui/mobile/guides/patterns/settings)
- Nielsen Norman Group, [7 Tips for Successful Customization](https://www.nngroup.com/articles/customization/)
- GitHub Docs, [Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)
- VS Code, [Settings](https://code.visualstudio.com/docs/configure/settings); Zed, [All settings](https://zed.dev/docs/reference/all-settings)
- Vercel, [Project settings](https://vercel.com/docs/project-configuration/project-settings)
- Linear, [Account preferences](https://linear.app/docs/account-preferences) and [How we redesigned the Linear UI](https://linear.app/now/how-we-redesigned-the-linear-ui)
- Raycast, [Settings](https://manual.raycast.com/settings) and [Store](https://www.raycast.com/store); r/macapps, [Raycast: the good, the bad and the best](https://www.reddit.com/r/macapps/comments/1rdcoo2/raycast_the_good_the_bad_and_the_best/)
- [git-config](https://git-scm.com/docs/git-config), [npm config](https://docs.npmjs.com/using-npm/config/), [gh config](https://cli.github.com/manual/gh_config), [Claude Code settings](https://code.claude.com/docs/en/settings), [Ghostty config](https://ghostty.org/docs/config), [k9s config](https://k9scli.io/topics/config/), [Helix configuration](https://docs.helix-editor.com/configuration.html), [lazygit config](https://lazygit.dev/docs/configuration/), [htop manual](https://linuxman7.org/linux/man-pages/man1/htop.1.html)
- Ars Technica, [macOS 13 Ventura review](https://arstechnica.com/gadgets/2022/10/macos-13-ventura-the-ars-technica-review/); Macworld, [System Settings problems](https://www.macworld.com/article/836295/macos-ventura-system-settings-preferences-problems.html)
