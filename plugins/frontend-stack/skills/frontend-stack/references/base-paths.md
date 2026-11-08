# Base paths for vague requests

A broad word ("UX", "usability", "experience", "design", "identity",
"navigation", "ugly") names an area, not a problem. The request is still vague,
but the area picks a base path: what to load first, what to ask, and where each
answer goes. Use the path in SKILL.md step 2 ("Vague complaint: ask before
loading").

Every path starts the same way: `frontend-design:frontend-design` loaded, the
project read (SKILL.md step 1), the current render looked at when a browser is
at hand. Ask the path's questions in one message, with options, at most four.
Skip any question the context already answers: "this screen" is the screen in
a pasted screenshot, the open URL, or the page the session changed last; ask
"where" only when none of these points to one.
Load the routed skills only after the answers. An answer that fits another path
switches to it. Several answers become phases (SKILL.md step 3).

If the request names no area ("the site is bad"), first ask which area, with the
paths below as options.

Route by the owner of the subject (SKILL.md step 6, rule 5), not by whichever
skill has a command for it:

- **Marketing page** (landing, site, portfolio): `taste:design-taste-frontend`
  leads look, hierarchy and identity work; `hallmark:hallmark` instead only
  when the user names Hallmark or asks for a theme.
- **Product screen** (app, dashboard, forms): `frontend-design:frontend-design`
  leads direction; `impeccable:impeccable` owns critique, audit and its own
  commands (`harden`, `distill`, `onboard`, `shape`, `layout`).
- **Palette, fonts, design system, stack UX rules:** `ui-ux-pro-max`.
- **Motion, touch feel, native feel, trying versions:** Emil's skills.
- **What real users do or say:** `ux-research`.

A route made of one pack only loses what only the other packs know:
Impeccable's critique and hardening commands, Taste's live-page inspector, UI
UX Pro Max's palette, font and stack data, Emil's motion and touch craft, UX
Research's methods. When one pack has a skill or command that applies, still
pair it with the owner above when that owner is another pack (SKILL.md step 7).

## UX (general)

Words: UX, usability, experience, "hard to use", "confusing".

Ask:
- Where: which page, screen or flow.
- What part of the experience:
  - finding things, menus, getting lost → **Navigation**
  - reading order, what comes first, hierarchy → **Reading and hierarchy**
  - how a flow starts and moves, steps, first use → **Flows and forms**
  - forms and tasks that fail or tire → **Flows and forms**
  - feedback: loading, error, empty, success → `impeccable:impeccable` (`harden`);
    transitions and press feedback → `emil-design-eng:animate`
  - stuck or unresponsive to touch and clicks → `emil-design-eng:apple-design`
    for gestures and springs, `emil-design-eng:review-animations` for motion
    that drags
  - "doesn't feel like a real app" → `emil-design-eng:mobile-native`
  - too much on the screen, clutter → `impeccable:impeccable` (`distill`)
  - unclear text, labels, errors → **Copy**
  - broken or awkward on phones → **Mobile**
  - slow → `impeccable:impeccable` (`optimize`)
  - keyboard, contrast, screen reader → `impeccable:impeccable` (`audit`)
  - "I don't know, users complain" → `ux-research:research-synthesis` with the
    complaints, or `ux-research:user-research` to plan how to find out
- Fix what exists, or rethink the flow. Rethinking a component or screen with
  options to compare → `emil-design-eng:prototype`.

"I don't know" or "you decide" on the part: run `impeccable:impeccable`
(`critique`) on the main flow, scoped to UX, then ask which finding to fix first.
Support everywhere: `ui-ux-pro-max:ui-ux-pro-max` for UX and stack rules.

## Navigation

Words: navigation, menu, "can't find", "get lost", sitemap, information
architecture.

Ask:
- Which navigation: main menu, footer, in-page sections, search, moving between
  app screens, back and breadcrumbs.
- Symptom: can't find a page; too many items; don't know where I am; links lead
  to the wrong place; awkward on phones.
- Are the destinations right and only the presentation is wrong, or the
  structure itself.

Routes:
- structure (what pages exist, how they group, labels) → `impeccable:impeccable`
  (`shape`) to map destinations and labels, then `layout`
- presentation following the stack's patterns (menu, tabs, active state,
  placement) → `ui-ux-pro-max:ui-ux-pro-max` navigation rules, with
  `impeccable:impeccable` (`layout`) for a product screen or
  `taste:design-taste-frontend` for a marketing site
- labels → **Copy**
- phones → **Mobile**

## Reading and hierarchy

Words: "reading position", "nothing stands out", "where do I look", "wall of
text", hierarchy, order.

Ask:
- Which page, and what the visitor should notice or do first.
- Symptom: everything has the same weight; the main action is lost; too long to
  reach the point; text hard to read.
- Kind of page: read (docs, article), operate (app, dashboard), persuade
  (landing).

Routes: landing or marketing page → `taste:design-taste-frontend` with
[landing-anatomy.md](landing-anatomy.md); product screen or docs →
`impeccable:impeccable` (`layout`), telling it the kind of page (read, operate);
text size and rhythm → `impeccable:impeccable` (`typeset`) with
`ui-ux-pro-max:ui-ux-pro-max` font pairings; clutter → `distill`.

## Flows and forms

Words: flow, onboarding, signup, checkout, form, "how it starts", steps.

Ask:
- Which flow, and where people drop or get stuck.
- Symptom: the start is unclear; too many steps; errors appear late or are
  vague; people don't reach the first useful result.
- New flow or existing flow.

Routes: where people drop is unknown → `ux-research:research-synthesis` on
tickets or analytics notes, or `ux-research:user-research` for a usability test,
before changing the flow; new or rethought flow → `impeccable:impeccable`
(`shape`) first, no code; first use and time to value → `onboard`; validation, errors and edge cases
→ `harden`; step layout → `layout`; motion between steps →
`emil-design-eng:animate`.

## Starting a product identity

Words: "no identity", "no brand yet", "new product", "give it a face".

Ask:
- The product in one sentence, and for whom.
- Two or three sites or apps the user likes, and one to avoid.
- What exists already: name, logo, colors, nothing.
- Scope: landing only, or landing and app.

Route: [identity-flow.md](identity-flow.md) from step 1; brand assets →
`ui-ux-pro-max:brand`.

## Improving an existing identity

Words: "no personality", "generic", "looks AI-made", "dated", "inconsistent",
"doesn't look like us".

Ask:
- What must stay: name, logo, colors, anything the user likes.
- What is wrong: generic or AI-made; dated; inconsistent between screens; too
  loud or too bland; only color or only type.
- Scope: landing, app, or both.
- A site or app the user finds good, and what in it.

Routes:
- generic, AI-made, no personality → the identity flow, replacing the visual
  world inside the scope (SKILL.md step 3 gate)
- inconsistent → `ui-ux-pro-max:design-system` leads, `impeccable:impeccable`
  (`extract`) pulls the tokens
- dated → Diagnose + Direction (product: `frontend-design:frontend-design`,
  marketing: `taste:design-taste-frontend`, or `hallmark:hallmark` when named)
- too loud or too bland → `impeccable:impeccable` (`quieter` / `bolder`)
- only color or only type → `ui-ux-pro-max:ui-ux-pro-max` leads with palettes
  or font pairings, `impeccable:impeccable` (`colorize` / `typeset`) applies
  them

## Looks

Words: ugly, "looks bad", "not pretty", "cheap".

Ask where, what bothers (colors, type, spacing, images, the whole thing), fix
or new direction, and a screen or site the user finds good. The reference
seeds the board (SKILL.md step 3); without one, use
[reference-gallery.md](reference-gallery.md). Then run the looks gate in SKILL.md step 3; "the whole
thing" and "new direction" go to **Improving an existing identity**. Only
colors or only type → `ui-ux-pro-max:ui-ux-pro-max` leads. A marketing page →
`taste:design-taste-frontend` as the Direction lead (`hallmark:hallmark` when
named). Offer a mockup image before code when the session can generate images:
`taste-imagegen:imagegen-frontend-web` (or `-mobile`), optional plugin.

## Copy

Words: text, labels, "confusing message", microcopy, tone.

Ask which screen and whether the problem is meaning (people misunderstand) or
voice (sounds wrong). Routes: new text → `ux-research:ux-copy`; fixing text in a
screen → `impeccable:impeccable` (`clarify`); voice →
`ui-ux-pro-max:brand`.

## Mobile

Words: phone, mobile, "breaks on small screens", touch.

Ask which pages, and whether the layout breaks or only feels non-native.
Routes: layout → `impeccable:impeccable` (`adapt`); native feel, gestures →
`emil-design-eng:mobile-native`.
