# Product identity before the landing

Use for a product without a brand, a new landing without an identity, or a
request to replace personality, identity or an AI-made look. A local addition
inside an approved world inherits it. A missing `DESIGN.md` alone does not
mean the product has no brand; inspect the actual UI and assets.

Load one lead and at most two supporting skills per phase. Save handoffs in
the plan or design notes so the next phase reads decisions, not every skill.

## 0. Product context and naming

Read `PRODUCT.md` first. Confirm audience, positioning, personality, the
product's unique mechanism, language, primary action and real proof. Separate
confirmed capabilities, prices and customers from assumptions.

If the brief is missing and the companion `indie-dev-stack:product-shaper`
agent is installed, run it and save the brief to `PRODUCT.md`. It is an
optional external agent, not a skill shipped here. Otherwise ask for audience,
positioning and personality, capture the answers, and mention once that
`JaimeJunr/claude-code-indie-dev-stack` covers product shaping.

For a product with no brand, settle naming and a one-sentence positioning
statement before visual directions. Keep an approved name. If unnamed,
propose names tied to the mechanism and audience; the owner chooses. Record
the name's meaning, promise, voice and language in `PRODUCT.md`. Do not imply
that a suggested name has cleared domain or trademark checks.

## 1. Scope and diagnosis

For existing work, load `impeccable:impeccable` (`critique`): navigation,
usability, hierarchy and identity. Skip critique on an empty project.

Read the incumbent `DESIGN.md`, tokens, components and assets. A personality,
identity or AI-look complaint authorizes replacing the affected visual world.
Keep the user's explicitly praised or fixed visual choices, product truth,
working behavior and technical constraints. Record the replacement boundary.

## 2. Research before directions

The `frontend-stack:design-director` agent uses `WebFetch` to inspect 4-6
products in the same category plus 2 outside it. Choose outside references
for an audience, mechanism or communication device that could reveal a gap.
Use screenshots from any browser tool the session has when visual structure
matters. User-supplied screenshots count toward the board.

Seed the board from `reference-gallery.md`: pick 2-4 entries whose lesson
fits this product's problem and re-inspect them. They add to the live
research above; they do not count toward it unless re-inspected now.

Inspect sources before proposing any direction. For each reference, record
its signature element (what distinguishes it from this board), voice (one
short quoted line), hero device and what makes the whole ownable. Keep a URL
or screenshot path and mark the category relation. Save this short table in
the plan or `DESIGN.md` research notes:

| Product / source | Same category or outside | Signature element | Voice: quoted line | Hero device | Why ownable / gap |
|---|---|---|---|---|---|
| ... | ... | ... | "..." | ... | ... |

Report the denominator: same-category references inspected / 4-6, outside
references inspected / 2, and sources unavailable. A text fetch cannot prove
visual details it does not show. Mark them unverified and get captures before
using them as visual evidence. If tools and supplied sources cannot complete
the board, report the gap and request sources; do not fabricate research.

References are input, never a template. A direction may exploit a gap in the
board, but may not copy a reference's signature, composition or copy. Name
the category default the board exposes and what this product can own instead.

## 3. Concept into a visual language

Load `impeccable:impeccable` and its `reference/new-work.md` before direction
work. In this repo that is
`plugins/impeccable/skills/impeccable/reference/new-work.md`. The shipped
concept-seed entry point is `scripts/impeccable`, inside that skill directory,
not a separate skill or a guessed `concept-seed.py`.

Derive candidates from product truth, the audience's world and reference gaps.
Follow new-work's candidate derivation and concept roll before prototype code:

```sh
"<impeccable-skill-dir>/scripts/impeccable" concept-seed --scope direction --mode Persuade
```

Replace the path with the loaded Impeccable skill's directory; keep cwd at the
project. A landing is `Persuade`; use the surface's actual mode for product
UI. Save the seed key, assignment, challenger verdicts and mode rules. If the
launcher is unavailable, follow Impeccable's fallback, disclose the missing
roll and do not invent a seed key or claim its gate ran. Permitted fallback
work can continue, but seed-based finish checks remain incomplete.

Turn each concept into 3-5 ownable devices across these channels:

| Channel | Decide |
|---|---|
| Layout | A composition or reading path tied to the mechanism |
| Data display | A way to show real relationships, states or values |
| Copy voice | Product-specific vocabulary and sentence behavior |
| Iconography | A coherent symbol grammar with a functional role |
| Micro-interaction | A meaningful response or transition, with reduced motion |

If the owner approved a literal reading of the name, keep it, but it must
extend beyond the logo into at least 3 of these 5 channels (e.g. a product
named after a constellation shows its catalog as stars, not only a star logo). Tie the devices to the actual product; decorative
stars alone are not a language. The pinned concept outranks the roll; use the
assignment in dimensions the owner left open.

Otherwise follow Impeccable's literal-reading rule: at most one candidate
comes from the name's literal meaning. Derive the rest elsewhere in the
audience's world. Avoid replacing one category cliché with its obvious opposite.

Taste presets (`taste:minimalist-ui`, `taste:industrial-brutalist-ui`,
`taste:high-end-visual-design`) and `ui-ux-pro-max:ui-ux-pro-max` category
styles are finishing material only. They may refine a concept's type, spacing
or craft after it exists; they never supply the direction or override its
devices. Apply `conflicts.md` to their font, color and mono suggestions.

## 4. Directions and comparison

The `frontend-stack:design-director` agent proposes 2-3 materially different
directions from the research and concept work. Each names:

- Its thesis and concept, 3-5 devices and the channels they cover.
- The specific reference gaps it exploits and signatures it will not copy.
- First viewport, visitor path, key flows and signature interaction.
- Type, color strategy, components, cross-surface reach and honest risk.

Carry the roll's assignment and challenger judgments into the proposal; the
user's choice wins. Preset names alone are not directions.

On this router route, Emil's picker is the single direction-selection surface.
It replaces new-work's direction decision page, not the concept roll. Preserve
the seed key, assignment, challenger verdicts and any user overrides in the
handoff. Do not also run `serve-question` for a second direction choice. A
comp-led composition approval later compares compositions within the chosen
brand, not new identities. See the direction-comparison ruling in `conflicts.md`.

Give `emil-design-eng:prototype` a concrete comparison brief: one key screen
or first viewport per direction, in an isolated picker, with each direction's
devices and provisional tokens. The router's direction brief overrides its
standalone neutral defaults and incumbent tokens inside the replacement scope.
Demonstration data is labeled synthetic; do not invent commercial claims.
Skip the picker only when the user explicitly chooses from the text.

The user picks. Record the choice and pinned devices. Do not silently select
the safest candidate or start another identity tournament during Build.
Selection returns the chosen prototype as the brand input. Defer prototype's
production promotion until brand and system are approved; comparison code
stays isolated. Integrate it only during Build with the approved tokens.

## 5. Brand

For the chosen direction, `ui-ux-pro-max:brand` defines voice and visual
identity, with `frontend-design:frontend-design` as support. Resolve the name,
positioning, messaging, vocabulary, type character, color roles, symbol grammar
and concept devices as one brand. Use the product's confirmed language.

Keep the brand decisions in the plan until the system phase. Do not create a
second source of truth in `docs/brand-guidelines.md` unless the user asks.

## 6. System before the landing

`ui-ux-pro-max:design-system` turns the approved brand into semantic tokens,
component states and `DESIGN.md`. Record the concept devices and reference
board or its note path. Keep one system; no parallel `--persist` output.

This brand-first route establishes the approved system before landing
implementation. It overrides new-work's default of writing a new world's
`DESIGN.md` only at finish. Impeccable's finish documenter later reconciles
that system with the rendered result and maintains `.impeccable/design.json`;
it does not choose another brand. See `conflicts.md`.

## 7. Build the landing

Only after brand and system, load `taste:design-taste-frontend` as the marketing
lead and `impeccable:impeccable` as workflow support. For developer-tool, API
or AI-gateway landings, also read `devtool-landing.md`. For every landing,
answer the questions in `landing-anatomy.md` with the chosen concept.

Explicitly delegate to Impeccable's `reference/new-work.md`, not just `polish`
or `audit`. Reuse the research, seed, chosen direction and pinned brand. Follow
its applicable comp-led or code-led build path and gates. Before production
code, persist the direction contract in the development-only surface brief:
`THESIS`, `OWN-WORLD`, `STORY`, `FIRST VIEWPORT`, `FORM` with seed key, and
`FINISH`, as defined in new-work. Do not ship the contract in page markup.

Use the approved tokens and the project's library. Carry the concept through
the full page, including real product proof, navigation and the close.

## 8. Screenshot finish gate

Follow new-work's inspection and finish handoff. The caller captures and opens
desktop + mobile screenshots with any available browser/screenshot tool;
web defaults are 1440px and 390px wide, saved as
`.impeccable/review/desktop.png` and `.impeccable/review/mobile.png`. Include
the user's viewport when known. Confirm content has loaded and captures show
the intended surface without blank regions or entrance-motion omissions.

Pass the original request, confirmed answers, artifact paths, captures,
reference board, chosen devices, direction contract and new-work's remaining
inputs to `impeccable-finish-reviewer`. Its real definition is
`plugins/impeccable/agents/impeccable-finish-reviewer.md`. The reviewer has no
browser; the caller supplies the images. Follow its disposition:
`recapture`, `rebuild`, `fix` or `ship`. Re-review after fixes as new-work directs.

If agents are unavailable, use Impeccable's
`reference/degraded/finish-reviewer.md` and disclose the substitution. If no
capture tool or current screenshots exist, report the missing desktop/mobile
evidence and leave the visual gate incomplete. A source-only checklist is not
a screenshot pass.

The `frontend-stack:ui-reviewer` also compares captures to the reference board
and concept devices. On personality, identity or AI-look work, a generic
render, missing signature, or interchangeability with a named competitor is
a `Must fix` when supported by screenshot evidence. Keep audit and motion
checks. Report which views and references were actually inspected; finish
documentation after the verdict, without diluting the chosen world.
