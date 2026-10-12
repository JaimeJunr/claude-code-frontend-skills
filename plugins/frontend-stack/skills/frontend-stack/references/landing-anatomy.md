# Landing anatomy: questions every marketing page answers

Read during Direction and Build for any landing, product page or marketing
site, after the brand exists. These are the questions strong pages answer,
taken from the sites in `reference-gallery.md` (inspected 2026-10-12). They
are questions, not a layout: the identity flow, the chosen concept and the
project's system decide how each answer looks. A page that answers them all
with the most common pattern becomes a template; answer at least one in a
way the category does not.

## 1. Story order

Most strong pages move through the same questions, in roughly this order.
Skip what the product cannot honestly answer; never fill a slot with filler.

| Step | The visitor asks | Typical answer seen |
|---|---|---|
| News | "Is anything new?" | A dated announcement bar ("through October 19") |
| Promise | "What is this, for whom?" | H1 of 8 words or fewer that names the category; the subtitle explains |
| Proof of the thing | "Is it real?" | The product itself in the first viewport: code, UI, its own output |
| Proof of use | "Who uses it?" | Live catalog numbers, named customers, community projects |
| Path | "How do I start?" | 3 numbered steps from account to first result |
| Depth | "What else can it do?" | Claim + real product fragment, alternating |
| Control | "Can I trust it?" | Named controls and limits, not badges |
| Price | "What does it cost?" | Real billing unit and limits, linked to full pricing |
| Freshness | "Is it alive?" | Recent ships, changelog, release notes |
| Doubt | "What about…?" | FAQ with real answers |
| Close | "OK, what now?" | The primary action again, with its object named |

## 2. Navigation

- Top level holds 4-5 items. Pricing and Docs (or their equivalent) are
  reachable from the top level, never buried.
- A product with several surfaces gets a sticky sub-nav on its own page
  (overview, catalog, docs), with the primary action at its end.
- The logo returns home; the nav's last item is the one action that matters.

## 3. Actions

- Pair one *act* action with one *understand* action: "Get API key" with
  "Read the docs", "Open account" with "Watch demo". The primary names its
  object; "Get started" alone hides what happens next.
- Give each audience its own install path when they differ: detected OS and
  package, a package-manager line, "copy for agent" with real install steps,
  or an AI-assisted setup. Coding agents are now an audience; see
  `devtool-landing.md` for what the agent copy must contain.
- One accent color marks the primary action everywhere. Other colors live
  inside product content (logos, data, illustrations), not on chrome.

## 4. Making it understood

Pick the device that matches what the visitor cannot picture yet:

| The visitor cannot picture… | Show it with |
|---|---|
| Their own use case | Tabs per scenario, team or SDK, each with genuinely different content |
| Invisible logic (routing, rules, pipelines) | A diagram whose edges carry real conditions and values |
| Change over time | A short narrative: "a day with…", before/after on the same task |
| Scale or popularity | Sourced numbers with units and scope, or a live list |
| How it feels | The real interaction, playable or recorded at legible scale |

A device that shows the same content in every state (tabs that swap one
sentence, a flowchart with decorative boxes) explains nothing; cut it.

## 5. Type and color budget

- One text family; a mono only for real code, identifiers and values (see
  the mono-labels ruling in `conflicts.md`). A third face, if any, appears
  once: the H1 or a single brand claim.
- Large display type usually tightens tracking; check it at mobile width.
- Ground, text and one accent carry the page; tints of the ground separate
  sections. Pure black is a choice for photo/video-led worlds, not a default.

## 6. First-viewport check

Before Build ends, answer from the desktop and mobile captures:

1. Can a stranger say what it is and who it is for in five seconds?
2. Is something real from the product visible without scrolling?
3. Is the primary action's object named, and is it the only accent?
4. Does the page still show its content with motion disabled and before any
   scroll reveal runs?
5. What here could not appear on a competitor's page?
