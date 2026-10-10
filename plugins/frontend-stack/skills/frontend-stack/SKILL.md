---
name: frontend-stack
description: Router for the frontend design stack. Use at the start of any frontend UI task (build a page or component, redesign or restyle an app, "it looks ugly / generic / AI-made", migrate to a component library or design system, pick a style or palette, polish, audit, animate, review UI) to decide which installed skills lead each phase of the work, which ones support, and which rule wins when the packs disagree. Also use when two design skills give contradicting advice.
---

# Frontend Stack router

Five design packs are installed side by side. Each is good alone and each
assumes it is the only one in the room. This skill decides who leads in each
phase of the work, so the agent loads one lead and at most two supporting
skills at a time instead of five competing rulebooks.

## 1. Read the project first

Before picking anything, look for what the project already decided:

- `PRODUCT.md` / `DESIGN.md` at the repo root (Impeccable's context files)
- `design-system/*/MASTER.md` (UI UX Pro Max `--persist` output)
- `docs/brand-guidelines.md`, `assets/design-tokens.*` (UI UX Pro Max `brand`
  and `design-system`)
- an existing design system: tokens, `tailwind.config.*`, `components/ui/`, a
  component library in `package.json`
- a brand guide the user pointed at

If any of these exist, they outrank every skill below (see rules 1 and 2 of
the precedence ladder). Your job becomes extending that system, not replacing it.

Keep one source of truth. If two of these files exist and disagree (palette,
fonts, spacing), ask the user which one wins before writing code. When the
project has none, `DESIGN.md` is the one to create (Impeccable `init`); do not
also run `--persist` or generate `docs/brand-guidelines.md` unless the user
asks, and if they do, keep the values identical to `DESIGN.md`.

## 2. Classify the request

Answer three questions before picking skills:

1. **Job.** Build something new; change something that exists (redesign,
   restyle, migrate to a library); review only (critique, audit, polish); one
   craft (motion, copy, color, type, layout, tokens); or assets (brand, logo,
   banners, slides).
2. **Surface.** Marketing (landing, portfolio, site); product (dashboard, chat,
   forms, settings, tables, flows); a single component; mobile web; native app.
3. **Stack signals** from step 1: a component library in `package.json`, shadcn
   (`components.json`, `components/ui/`), Tailwind, React Native/Expo, Swift.

Complaints about looks ("ugly", "generic", "looks AI-made", "slop", "cluttered")
mean the job is *change*, not *review*: the user wants a new direction, not only
a list of problems.

## 3. Work in phases

Bigger tasks run in phases, in this order. Load each phase's skills when the
phase starts, not all up front. Skip a phase that the task does not need.

| Phase | When | Lead | Support |
|---|---|---|---|
| Diagnose | the job is *change* | `impeccable:impeccable` (`critique`) | `impeccable:impeccable` (`audit`) for a11y/perf debt |
| Direction | new work, or any complaint about looks | product: `frontend-design:frontend-design`; marketing: `taste:design-taste-frontend` | `ui-ux-pro-max:ui-ux-pro-max` for palette/font/style lookup when the project has no system |
| Build | always | the project's component library (its docs, components, tokens, MCP server if any) | `ui-ux-pro-max:ui-styling` when shadcn/Tailwind; the craft skill from the table below |
| Motion | the change moves | `emil-design-eng:animate` | `emil-design-eng:animation-vocabulary` |
| Review | anything user-facing | see step 8 | - |

At the start, tell the user the phase plan with the skills of each phase, so
they see the whole route even though only the first phase is loaded.

When the user complains about looks, Diagnose and Direction run together: load
`impeccable:impeccable` (`critique`), the Direction lead and
`ui-ux-pro-max:ui-ux-pro-max` at the start, always, even when the request names
no stack or style. A critique alone is a list of problems, not the new direction
the user asked for, and UI UX Pro Max supplies the UX guidelines and the
style/palette options for this kind of product. When the project already has a
design system, use UI UX Pro Max for UX and stack rules only, not to replace
the palette or fonts (rule 2 of the ladder).

Write what Diagnose and Direction decided (in `DESIGN.md` or the plan) before
Build, so later phases do not need the earlier skills loaded.

## 4. Pick the skills for the task

| The task is... | Lead | Support |
|---|---|---|
| New landing page, portfolio, marketing site | `taste:design-taste-frontend` | `frontend-design:frontend-design` for direction, `ui-ux-pro-max:ui-ux-pro-max` for palette/font lookup |
| New product UI: dashboard, settings, tables, multi-step flows | `frontend-design:frontend-design` | `ui-ux-pro-max:ui-ux-pro-max` (stack + UX guidelines), `impeccable:impeccable` for `harden` at the end |
| Redesign or restyle an existing product app | phases: Diagnose → Direction (`frontend-design:frontend-design`) → Build → Review | `ui-ux-pro-max:ui-styling` in Build when shadcn/Tailwind |
| Redesign an existing marketing site | `taste:redesign-existing-projects` | `impeccable:impeccable` (`critique`) first |
| "Looks generic / AI-made / slop" | `frontend-design:frontend-design` (anti-template checks) | `impeccable:impeccable` (`critique`); `taste:design-taste-frontend` on marketing pages |
| Adopt or migrate to a component library or design system ("use our kit", "move to shadcn") | the library itself: its docs, components, tokens | `ui-ux-pro-max:ui-styling` for Tailwind/shadcn mapping, `impeccable:impeccable` (`extract`) to pull tokens |
| Chat or AI assistant UI | `frontend-design:frontend-design` + the library's chat components if it has them | `impeccable:impeccable` (`harden`) for empty, error, loading and streaming states; `emil-design-eng:animate` for streaming motion |
| Forms, onboarding, first-run | `impeccable:impeccable` (`onboard`, `harden`) | `frontend-design:frontend-design` |
| Empty, error, loading states, edge cases | `impeccable:impeccable` (`harden`) | - |
| Only critique or audit, no rebuild asked | `impeccable:impeccable` (`critique` then `audit`) | - |
| "Plan it before coding", discovery, UX flow | `impeccable:impeccable` (`shape`) | - |
| Vague brief, no direction yet | `frontend-stack:design-director` agent, then route its result here | - |
| Review a page, component or PR diff | `frontend-stack:ui-reviewer` agent | - |
| Set up design context for a repo | `impeccable:impeccable` (`init`, then `document`) | - |
| Polish before shipping | `impeccable:impeccable` (`polish`) | `emil-design-eng:review-animations` for interaction details |
| Accessibility, performance, responsive checks | `impeccable:impeccable` (`audit`, `optimize`, `adapt`) | - |
| Too loud, or too bland | `impeccable:impeccable` (`quieter` / `bolder`) | - |
| Only typography / only color / only layout | `impeccable:impeccable` (`typeset` / `colorize` / `layout`) | `ui-ux-pro-max:ui-ux-pro-max` for font pairings or palettes |
| Choose a style, palette, font pairing, chart type | `ui-ux-pro-max:ui-ux-pro-max` | - |
| Charts and data visualization | `ui-ux-pro-max:ui-ux-pro-max` (chart guidance) | `emil-design-eng:pick-ui-library` for the chart library |
| Dark mode, theming | `ui-ux-pro-max:design-system` | `impeccable:impeccable` (`colorize`) |
| Design tokens / design system architecture | `ui-ux-pro-max:design-system` | `impeccable:impeccable` (`extract`) |
| shadcn/ui + Tailwind component work | `ui-ux-pro-max:ui-styling` | `emil-design-eng:pick-ui-library` |
| Screenshot or mockup image to code | `taste-imagegen:image-to-code` (optional plugin) | `frontend-design:frontend-design` |
| Build an animation | `emil-design-eng:animate` | `emil-design-eng:animation-vocabulary` when the user describes motion vaguely |
| Review or fix existing motion | `emil-design-eng:review-animations` / `improve-animations` | - |
| "Where should this animate?" | `emil-design-eng:find-animation-opportunities` | - |
| Gesture, spring, Apple-feel UI | `emil-design-eng:apple-design` | - |
| Web app should feel native on phones | `emil-design-eng:mobile-native` | `impeccable:impeccable` (`adapt`) |
| Try several versions of a component | `emil-design-eng:prototype` | - |
| Which library for X (charts, OTP, virtual lists...) | `emil-design-eng:pick-ui-library` | - |
| Toasts with Sonner | `emil-design-eng:ask-sonner` | - |
| UX copy, errors, microcopy | `impeccable:impeccable` (`clarify`) | - |
| Brand voice, visual identity, brand guidelines | `ui-ux-pro-max:brand` | `ui-ux-pro-max:design-system` for tokens |
| Logo, icons, corporate identity (CIP), social photos | `ui-ux-pro-max:design` | - |
| Banners, ads, social images, website hero art | `ui-ux-pro-max:banner-design` | - |
| Slides, pitch deck | `ui-ux-pro-max:slides` | - |
| Brand-kit board as a generated image | `taste-imagegen:brandkit` (optional plugin, needs image generation) | - |
| Explicit look: minimalist, brutalist, "expensive agency" | `taste:minimalist-ui` / `industrial-brutalist-ui` / `high-end-visual-design` | `taste:design-taste-frontend` pre-flight checklist |
| Google Stitch DESIGN.md | `taste:stitch-design-taste` | - |
| React Native / Expo motion, Swift | `emil-native:animate-expo` / `write-swift` (optional plugin) | - |
| Mockup image first, then code | `taste-imagegen:imagegen-frontend-web` / `imagegen-frontend-mobile` (optional plugin, needs image generation) | - |

A request that mixes jobs ("redesign it and add animations") is several rows:
run them as phases in the order of step 3.

## 5. Cases the table does not cover

New skills arrive with every upstream sync, and requests will not always match
a row.

- **No row fits:** use the job and surface from step 2, give the lead to the
  domain owner (rule 5 of the ladder), then check the session's skill list for
  a skill whose description fits better.
- **A named skill is not in the session's skill list:** skip it and use the
  next row's lead or `frontend-design:frontend-design`. Never guess a name.
- **A skill not listed here fits better:** a row still wins unless the user
  names the other skill. Use it as support and tell the user this router has no
  row for it yet.

## 6. Precedence ladder

When two loaded skills disagree, the higher rule wins:

1. **The user's explicit request and brand.** "Use Inter", "purple is our
   brand", "keep it like Linear" beat every skill ban.
2. **The project's existing system.** `DESIGN.md`, tokens, the component
   library already in use. Extend it; do not swap libraries or mix systems.
3. **Accessibility and correctness.** Contrast, focus states, reduced motion,
   keyboard access, no layout shift. Impeccable `audit` is the referee.
4. **Scope of the lead skill.** A skill's own "not for X" line is binding:
   `design-taste-frontend` says it is not for dashboards, tables or multi-step
   product UI, so it does not lead those.
5. **Domain owner.** Motion questions go to Emil's skills, style/palette data to
   UI UX Pro Max, critique/audit/polish to Impeccable, aesthetic direction to
   frontend-design or taste.
6. **The lead skill's taste defaults.**

The rules that actually collide between packs, and how each is settled, are in
[references/conflicts.md](references/conflicts.md). Read it when a supporting
skill contradicts the lead.

## 7. Load budget

- Per phase: one lead and at most two supporting skills. Big skills
  (`design-taste-frontend`, `ui-ux-pro-max`, `impeccable`) are long; loading all
  of them at once burns context and produces averaged, generic output.
- Say in one line which skills each phase loaded, so the user can correct the
  routing early.
- Aesthetic presets (`minimalist-ui`, `industrial-brutalist-ui`,
  `high-end-visual-design`) never stack with each other. Pick one or none.
- `taste:full-output-enforcement` only when the user asks for complete output.
- The brand, logo, banner and slides skills above overlap (`ui-ux-pro-max:design`
  and `design-system` also cover slides and branding). Load only the row's lead.
- Prefer the specific Emil skill over `emil-design-eng:emil-design-eng` as
  support: without a direct question the umbrella replies with a stock greeting.

## 8. Finish the same way every time

For anything user-facing, end with a review pass before calling it done:

1. `impeccable:impeccable` `audit` (or delegate to the `ui-reviewer` agent)
2. if the change has motion, `emil-design-eng:review-animations`
3. fix what they flag, then summarize what changed and what was left as-is
