# Where the packs disagree

Each entry names the conflicting rules, where they come from, and the ruling
the stack applies. Rulings follow the precedence ladder in `../SKILL.md`.

## Motion: how much, and when

- **taste** (`design-taste-frontend`, `high-end-visual-design`,
  `stitch-design-taste`) pushes "perpetual micro-motion", kinetic type, GSAP
  scroll hijacks and staggered reveals as part of a premium feel.
- **Emil** (`emil-design-eng`, `animate`) starts from "should this animate at
  all", keeps UI motion short (roughly 125-300 ms), never uses `ease-in` for UI,
  and treats motion as functional first.
- **Ruling:** in product UI (anything a user operates repeatedly), Emil wins:
  purposeful, short, interruptible, `ease-out`, respects
  `prefers-reduced-motion`. On a marketing page, taste may lead the hero and
  scroll storytelling, but every interactive control (buttons, menus, dialogs,
  toasts) still follows Emil's timing rules.

## Motion library

- **taste** reaches for GSAP for scroll and kinetic effects; **UI UX Pro Max**
  ships GSAP presets (`--domain gsap`).
- **Emil** uses CSS transitions first and Motion (Framer Motion) springs, and
  warns that Motion's `x`/`y` shorthands run on the main thread.
- **Ruling:** CSS first. Use the library the project already has. Add GSAP only
  for scroll-driven storytelling on marketing pages; add Motion for springs and
  gestures in React. Never both in the same component.

## Fonts

- **taste** `design-taste-frontend` discourages Inter as a default (allowed on
  request or for neutral / accessibility-first briefs).
  `high-end-visual-design` bans Inter, Roboto, Arial, Open Sans and Helvetica
  outright.
- **frontend-design** asks for distinctive type chosen for the subject.
- **UI UX Pro Max** font-pairing search can return Inter-based pairings.
- **Ruling:** brand / existing system first. For a fresh project, avoid Inter as
  an unconsidered default, but it is fine when the user asks, when the product
  is dense and neutral (admin, data tools), or when the project already uses
  it. The outright ban in `high-end-visual-design` only applies when that preset
  was explicitly chosen.

## Purple and gradients

- **taste** "Lila rule": no default AI-purple glows or neon gradients.
- **taste** `high-end-visual-design` "Ethereal Glass" archetype uses purple and
  emerald radial mesh gradients on OLED black.
- **Ruling:** the Lila rule is the default. The preset's gradient look only
  applies when the user picked that preset or the brand is purple.

## Near-black grounds

- **taste** `design-taste-frontend` asks for off-black, charcoal or `zinc-950`
  instead of pure black.
- **frontend-design** `frontend-design` lists neutral near-black `#0B0B0B`
  and `#111` standing in for black as template chrome. **Impeccable**
  `reference/new-work.md` derives neutrals from the chosen world's palette.
- **Ruling:** frontend-design's anti-template rule wins for a fresh world.
  Near-black is allowed when visibly tinted toward the approved brand hue,
  with a named color role and a reason tied to the scene. Neutral `#0B0B0B`,
  `#111` and automatic `zinc-950` are not a brand strategy. Pure black is
  allowed when the chosen world calls for it, as in photo- or video-led
  worlds (6 of the 15 sites in `reference-gallery.md` use it this way). Existing tokens or explicit
  user color choices still win. This stops dark-tech defaults deciding identity.

## Centered hero

- **taste** `design-taste-frontend` avoids centered hero / H1 sections when
  `DESIGN_VARIANCE > 4` and lists "centered hero over dark mesh" as an LLM
  default, with an override for editorial or launch briefs.
- **Observed:** 8 of the 15 sites in `reference-gallery.md` (OpenRouter,
  Cloudflare, Rerun, Perssua, ChatGPT dots, OpenAI Business, Raycast, Modal)
  center the H1 and put real product proof directly below it.
- **Ruling:** the cliché is centered text over decoration, not centering.
  A centered hero is allowed when the first viewport also shows something
  real from the product (code, UI, its own output, named customer footage).
  Centered text over a mesh, glow or empty field stays a template tell.
  Asymmetric layouts remain taste's default when nothing real can sit below.

## Tech-default fonts

- **UI UX Pro Max** `data/typography.csv` recommends Space Grotesk + DM Sans
  for tech/startups, and JetBrains Mono + IBM Plex Sans for developer tools.
- **Impeccable** `reference/new-work.md` lists Space Grotesk, DM Sans and IBM
  Plex among training-data defaults; it also rejects "tech wants mono" as a
  reason. **frontend-design** asks for subject-specific type.
- **Ruling:** Impeccable's anti-default direction wins for new identities.
  Space Grotesk, DM Sans, JetBrains Mono and IBM Plex are allowed only when
  the project already uses them or the user asks. Category lookup is not that
  permission. Choose new brand type from the concept, legibility and required
  language coverage; "developer tool" alone does not choose a face.

## Mono labels

- **UI UX Pro Max** developer and dashboard pairings suggest monospace UI;
  **taste** includes mono pairings and technical treatments.
- **frontend-design** calls small monospace data labels a template tell;
  **Impeccable** warns against tracked mono labels in editorial defaults.
- **Ruling:** frontend-design wins. Mono is for real code, identifiers or
  values where fixed-width alignment helps. Use the UI/text face for section
  labels, nav, eyebrows and metadata captions. Technical subject matter does
  not justify decorative mono. Explicit user type choices still win; the
  font-family restriction above applies separately.

## Who owns `DESIGN.md`

- **Impeccable** reads `PRODUCT.md` and `DESIGN.md` as project context and writes
  `DESIGN.md` via `document` / the `impeccable-documenter` agent.
- **taste** `stitch-design-taste` also writes a `DESIGN.md`, in Google Stitch
  format.
- **Ruling:** Impeccable owns `DESIGN.md`. The Stitch skill only runs on
  explicit request, and then writes to `DESIGN.stitch.md` unless the user says
  otherwise, so Impeccable's context is not overwritten. The brand-first
  ruling below defines the identity flow's initial system handoff.

## Brand-first system and finish documentation

- The router's identity flow runs `brand` → `design-system` → landing.
- **Impeccable** `reference/new-work.md` normally writes a new world's
  `DESIGN.md` at finish through `impeccable-documenter`.
- **Ruling:** the router's brand-first order wins on this route. Establish
  approved brand decisions, `DESIGN.md` and tokens before landing code. The
  finish documenter reconciles them with the render and maintains
  `.impeccable/design.json`; it cannot silently replace the approved identity.
  Impeccable still owns the final durable documentation. A missing filename
  alone never erases an established brand visible in code.

## Direction comparison

- The router uses `emil-design-eng:prototype` for 2-3 key-screen directions.
- **Impeccable** `reference/new-work.md` uses concept-seed's dealt hand and a
  `serve-question` decision page for direction selection.
- **Ruling:** the router's picker owns selection on the identity route. Run
  the concept roll first and retain its assignment, seed key, challenger
  judgments and user overrides, then present the directions through Emil.
  Do not open a second direction decision page. Reuse the recorded pick in
  new-work's Build. Comp-led composition approval still runs inside that world.
  Prototype's immediate promotion step is deferred: selection hands the chosen
  variant to brand and system; production integration happens only in Build.
  This gives the user one identity choice grounded in a working key screen.

## Identity replacement with an existing system

- The router defaults to extending the incumbent system. **Impeccable**
  `reference/new-work.md` replaces the visual world on redesign.
- **Ruling:** a personality, identity or AI-look complaint is authorization
  for replacement within its scope. Existing `DESIGN.md` is evidence of the
  rejected world there. Keep the visual choices the user explicitly praised
  or fixed, product truth and working behavior; retain technical constraints
  and unaffected surfaces. This is replacement of identity, not permission
  to change libraries or capabilities.

## Scope of design-taste-frontend

- Its own header: "Landing pages, portfolios, and redesigns. Not dashboards,
  not data tables, not multi-step product UI."
- **Ruling:** binding. For product UI the lead is `frontend-design` with UI UX
  Pro Max's UX guidelines, and Impeccable `harden` at the end.

## Component libraries

- **taste**: one design system per project, never ship shadcn/ui in default
  state.
- **UI UX Pro Max** `ui-styling`: shadcn/ui + Tailwind as the main path.
- **Emil** `pick-ui-library`: opinionated per-problem picks (Sonner, cmdk,
  Vaul...).
- **Ruling:** these agree once combined. Keep the project's system; shadcn/ui is
  the default for new React + Tailwind projects and must be themed (radius,
  color, type) before shipping; use Emil's picks for the problems shadcn does
  not cover.

## UX copy

- `ux-research:ux-copy` writes and reviews microcopy, errors, empty states and
  CTAs as its whole job.
- `impeccable:impeccable` `clarify` rewrites copy while working on a screen.
- `ui-ux-pro-max:brand` defines the voice.
- **Ruling:** `ux-copy` leads any copy task and follows the voice from `brand`
  (or `PRODUCT.md`) when one exists. Use `clarify` only inside an Impeccable
  pass on a screen. The em-dash ruling below applies to both.

## Em dashes in UI copy

- **taste** bans the em dash (`—`) anywhere on the page, calling it the top "AI
  tell".
- Nobody else has a rule.
- **Ruling:** apply it to UI copy the stack writes. Do not rewrite copy the user
  supplied.

## Review before shipping

- **Impeccable** `audit` / `critique` / `polish`, **Emil** `review-animations`,
  **taste** pre-flight checklist and **frontend-design**'s anti-template list
  all review the same page from different angles.
- **Ruling:** do not run all of them. Impeccable `audit` always; Emil's review
  when the diff touches motion; taste's checklist only on marketing pages it
  led. New marketing pages also follow Impeccable `reference/new-work.md`'s
  direction contract and `impeccable-finish-reviewer` screenshot gate. The
  caller supplies desktop/mobile captures; audit alone cannot pass identity.
  On personality, identity or AI-look requests, a missing signature or
  screenshot-backed interchangeability with a named competitor can be
  `Must fix`. Outside that scope, taste preferences remain non-blocking.
