# Reference gallery: modern interfaces worth learning from

A seed list for the reference board in `identity-flow.md` step 2 and for
`devtool-landing.md`. Each entry names the device that makes the page work,
so a direction can learn the mechanism without copying the look.

Inspected in a 1440px browser on 2026-10-12: computed fonts, background
colors, heading outline and desktop captures. Sites change; recheck an entry
before citing it as visual evidence, and record what you re-inspected.

## How to use it

- Pick 2-4 entries whose **lesson** fits the product's problem, not whose
  look you like. Add them to the board next to live research; they do not
  replace the 4-6 same-category + 2 outside references.
- Take the mechanism ("the hero is the product's own output"), never the
  signature (Vercel's pixel numerals, PostHog's desktop, SpaceX's type).
- Every lesson below still obeys the honesty rules in `devtool-landing.md`:
  real product, real numbers, real customers, or nothing.
- `conflicts.md` still applies: a site doing something (mono labels, a
  tech-default font) does not override a ruling. The generalized questions
  these pages answer live in `landing-anatomy.md`.

## Lessons by problem

| Problem the page has | Learn from |
|---|---|
| The product is invisible (API, infra, agent) | Vercel AI Gateway, Cloudflare AI Gateway, Rerun, Modal |
| Too many options to explain (catalog, models, plans) | OpenRouter, Vercel AI Gateway |
| One promise needs to feel tangible | Perssua, Cluely, Interview Coder (mechanics only) |
| The product is a loop of steps, not one feature | Final Round AI |
| A consumer feature needs warmth | ChatGPT dots, Mercury |
| Selling to many teams at once | OpenAI Business |
| Brand needs a personality, not a palette | PostHog, Teenage Engineering, SpaceX |
| Product UI must look premium and calm | Linear, Mercury, Raycast |

## Entries

### Developer tools, APIs and AI infrastructure

**[OpenRouter](https://openrouter.ai/)** · AI model router
- Signature: near-black `rgb(3,8,10)`, one acid-lime CTA, Plus Jakarta Sans
  with a separate display face for the H1.
- Lesson: the catalog *is* the proof. "Featured models" cards show token
  volume and weekly trend per model, so live usage replaces testimonials.
  Onboarding is three numbered steps (sign up, buy credits, get key).
- Watch: the four big stat counters only work because they are real and
  current; never imitate them with placeholder numbers.

**[Vercel AI Gateway](https://vercel.com/ai-gateway)** · AI gateway
- Signature: black, Geist Sans + Geist Mono + a pixel face (Geist Pixel)
  reserved for one huge "100%" claim; the product name sits in an outlined
  pill inside the H1.
- Lesson: the hero is a tabbed code editor (AI SDK, Chat Completions,
  Responses, Claude Code…) with a "Copy for agent" action. Pricing is the
  centerpiece: a model table with provider price, strikethrough discounts
  and "show more", framed by the single claim "no markup on tokens".
- Learn the move: give one brand-level promise its own typographic voice,
  used once.

**[Cloudflare AI Gateway](https://www.cloudflare.com/products/ai-gateway/)** · AI control plane
- Signature: warm near-black `rgb(25,24,23)` instead of cold black, the brand
  orange as the only accent, a mono face (Apercu Mono) for most body text,
  dotted grid frame lines around sections.
- Lesson: routing is drawn as a node graph with real conditions on the edges
  ("Pro user?", "Fallback", 90%/10% split), so the abstract product becomes a
  diagram a developer can read like config.
- Watch: its scroll-reveal sections render blank until animated; captures
  must wait for content (see the finish gate).

**[Rerun](https://rerun.io/)** · data layer for robotics / physical AI
- Signature: black, system sans + JetBrains Mono uppercase labels, a 3D robot
  gripper trailing rainbow trajectory streaks.
- Lesson: the hero art is what the product renders, so the visual is a
  product demo, not decoration. Second CTA is "Try in browser". Open-source
  proof is a live list of recent community pull requests, and named projects
  built on it (LeRobot, Project Aria) replace logo walls.

**[Modal](https://modal.com/)** · serverless AI compute
- Signature: charcoal `rgb(24,24,24)`, ABC Diatype + DM Mono, one green
  accent; the hero mark is built from glowing dots in a grid.
- Lesson: an abstract unit (containers, GPUs) becomes a particle visual
  built from that unit; the page carries real code samples and closes on
  "Ship your first app in minutes".

### Consumer and business AI

**[Perssua](https://perssua.com/pt)** · real-time meeting copilot (PT-BR)
- Signature: black, a single family (Space Grotesk), the verb "escuta" in a
  pill inside the H1, a waveform with a running timer.
- Lesson: "Veja o Perssua em ação" is a tabbed scenario demo (technical
  interview, cold call, 1:1, call in English); each tab shows the heard
  question and the suggested answer, so the promise is shown in context.
  Download buttons name the visitor's OS and package format.

**[Cluely](https://cluely.com/)** · real-time meeting assistant
- Signature: white Geist body, an 80px EB Garamond (serif) H1 in white over a
  pale-blue alpine illustration with a sun, then plain white sections; the
  product is a small floating overlay shown with its `⌘ ↵` shortcut.
- Lesson: the one promise (undetectable) is split into three claims, each
  drawn as a tiny product scene: "No bots detected" in a participant list,
  an "Invisible to others / Visible to you" split view, and a movable window
  that "follows your eyes". Each claim is a short title plus one behavior
  sentence ("Doesn't join meetings"), so the proof is the picture.
- Learn the move: a serif H1 on a calm landscape makes a utility tool feel
  trustworthy, and the keyboard shortcut is part of the mock, not a footnote.
- Watch: the "300ms" and "95%" figures and "fastest available" are
  self-claimed with no source; copy the stat row's layout, never the
  unsourced numbers. Same premise caution as Interview Coder below.

**[Final Round AI](https://www.finalroundai.com/)** · interview copilot
- Signature: white page, near-black text, Inter 58px semibold H1 with the
  key phrase ("#1 AI Interview Assistant") highlighted in orange, one dark
  CTA plus one outlined secondary ("See plans"), a three-number proof row.
- Lesson: it sells a loop, not a feature. "Prepare. Perform. Review." is a
  clickable three-step diagram where each step opens a real product fragment
  (a Goal checklist, a suggested answer, a scored debrief), and the line
  "each round compounds on the last" explains why the steps belong together.
  Five features sit under one tab set ("not five products to stitch
  together"), and pricing says plainly "no free trial" and what is free.
- Learn the move: the stealth claim is shown as two panes, "What they see"
  and "What you see", and the OS requirement sits under the CTA.
- Watch: its testimonial wall (dated, but short and generic) and "10M+",
  "#1" claims have no source; do not imitate them without real data. Same
  premise caution as Cluely and Interview Coder.

**[ChatGPT dots](https://chatgpt.com/pt-BR/features/dots/)** · always-on agents
- Signature: OpenAI Sans, black page, each feature row on its own saturated
  gradient tile (orange, blue, violet) with real UI in front.
- Lesson: the name becomes the symbol (a ring "dot") and then a character;
  the page tells "a day with your dot" and shows the agent where people
  already work (ChatGPT, Slack, Teams). Safety gets its own section with
  concrete controls ("your limits", "checks that matter").

**[OpenAI Business](https://openai.com/pt-BR/business/)** · enterprise AI
- Signature: OpenAI Sans only, a highlighted phrase block in the H1, a curved
  carousel of customer video stills (BNY, Uber) as the hero.
- Lesson: named customers in their own footage are the first viewport.
  Below, tabs by team (Finance, Sales, Engineering, Security…) and a product
  switcher (ChatGPT Work, Codex, API) let one page sell to many buyers.

**[Interview Coder](https://www.interviewcoder.co/)** · desktop AI assistant
- Learn the conversion mechanics only: one yellow accent `rgb(239,200,58)`,
  Geist at 85px, OS-specific download buttons, a "how it works" list where
  each claim is a concrete behavior, and a competitor matrix that demos a
  row on click.
- Do not learn its proof: repeated "Anonymous User" testimonials and
  absolute "100%" claims are exactly what `devtool-landing.md` forbids. Its
  product premise (hiding AI use during interviews) is not an endorsement.

### Product UI and fintech

**[Linear](https://linear.app/)** · product development system
- Signature: `rgb(8,9,10)`, Inter Variable + Berkeley Mono, a quiet
  two-column rhythm: short claim left, explanation right.
- Lesson: each section pairs one sentence with a live fragment of the real
  app (a Slack thread becoming an issue, a board, a review), rendered in
  HTML at legible scale. The product UI is the art direction.

**[Mercury](https://mercury.com/)** · business banking
- Signature: custom Arcadia / Arcadia Display, a painterly landscape with a
  desk on a hill, violet CTA, then the full dashboard at near-full width.
- Lesson: for money, calm comes first (an image of quiet), then exact
  product truth (balances, cards, treasury yield with its percentage).
  Company facts (valuation, revenue, funding) are cited as news items.

**[Raycast](https://www.raycast.com/)** · launcher for macOS
- Signature: `rgb(7,8,10)`, Inter + Geist Mono, every heading a short
  imperative ("Take shortcuts, not detours.", "Don't repeat yourself.").
- Lesson: the voice is the system. Under the main CTA a mono line offers
  "Install via Homebrew" for the audience that prefers it.

### Brands with a world of their own (outside references)

**[PostHog](https://posthog.com/)** · product analytics
- Signature: off-white `rgb(238,239,233)`, its own rounded face (RoundHog),
  the whole site as a desktop with icons and windows, a hedgehog mascot.
- Lesson: personality as interface. Even the setup card ("Install with AI",
  free-tier checklist) and the cookie notice speak in the brand voice.
  Proves a B2B tool can be funny without hiding the product.

**[Teenage Engineering](https://teenage.engineering/)** · hardware
- Signature: black, its own faces (te-20/te-40), navigation as a row of
  line glyphs with tiny spec text, monochrome documentary photography.
- Lesson: navigation itself can carry the identity; restraint everywhere
  else lets one idiosyncratic system stand out.

**[SpaceX](https://www.spacex.com/)** · aerospace
- Signature: D-DIN uppercase only, full-bleed real photography and video per
  section, one ghost button per section, no cards, no accent color.
- Lesson: when the product is physical and spectacular, documentary media
  carries the brand; the latest mission (date + name) leads like a news
  ticker. Works only with real footage; stock imagery breaks it.

## Patterns that recur, and what they cost

| Pattern | Seen at | Works when | Fails when |
|---|---|---|---|
| A product word in a pill inside the H1 | Vercel, Perssua | the word is the product's verb or category | every heading gets a pill |
| Tabs per SDK, scenario or team | Vercel, Perssua, OpenAI Business | each tab shows real, different content | tabs swap one sentence |
| Live usage numbers as proof | OpenRouter, Rerun | the data is real and current | numbers are placeholders |
| Node graph of the product's logic | Cloudflare | edges carry real conditions | it is a decorative flowchart |
| One accent color on near-black | OpenRouter, Cloudflare, Modal, Interview Coder | the accent marks the one action | the accent is a generic "AI" purple |
| Mono face as a secondary voice | Vercel, Cloudflare, Rerun, Linear | it carries real code, identifiers and values | it decorates section labels and eyebrows (see the mono-labels ruling in `conflicts.md`) |
| Scroll-revealed sections | Cloudflare, Linear, Perssua | content still loads without motion | screenshots and reduced-motion users see blank space |

The last row is a finish-gate issue: several of these pages captured blank
until their reveal ran. Build reveals so content is visible without
animation, and wait for loaded content before the screenshot gate.
