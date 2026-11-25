# Reference gallery: modern interfaces worth learning from

A seed list for the reference board in `identity-flow.md` step 2 and for
`devtool-landing.md`. Each entry names the device that makes the page work,
so a direction can learn the mechanism without copying the look.

Inspected in a 1440px browser on 2026-10-12: computed fonts, background
colors, heading outline and desktop captures. The payments, education and
Clonvo entries were inspected the same way on 2026-11-15; MeetAssist,
TechScreen and Natively were added, and Perssua and Interview Coder
re-inspected, on 2026-11-24 (1440px, plus the first screen at 390px). Sites change; recheck an
entry before citing it as visual evidence, and record what you re-inspected.

Not inspected: Revolut and Codecademy answered with a bot check (HTTP 403)
on 2026-11-15, so they have no entry. App-first products (Nubank, Monzo)
are judged from their public site only; their app screens need a gallery of
real app captures, not this file.

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
| One system must hold home, docs and blog together | Next.js |
| Too many options to explain (catalog, models, plans) | OpenRouter, Vercel AI Gateway |
| One promise needs to feel tangible | Perssua, Cluely, TechScreen and Interview Coder (mechanics only) |
| Two people see different things (privacy, roles, before/after) | TechScreen, MeetAssist, Natively, Cluely |
| Reviews must be checkable | MeetAssist |
| The product is a loop of steps, not one feature | Final Round AI |
| A consumer feature needs warmth | ChatGPT dots, Mercury |
| Selling to many teams at once | OpenAI Business |
| Brand needs a personality, not a palette | PostHog, Teenage Engineering, SpaceX |
| Product UI must look premium and calm | Linear, Mercury, Raycast |
| Money changes hands and the cost must be clear before the click | Wise, Clonvo pricing, Stripe Checkout |
| Sign-up must start with almost nothing | Nubank, Mercado Pago, Duolingo |
| One product serves several audiences (learner, parent, teacher) | Khan Academy, Brilliant |
| Progress must mean skill, not time watched | Khan Academy, Brilliant |
| A course or plan must show its real cost in time | Coursera, Udemy, Alura |
| Comparing yourself with competitors honestly | Clonvo compare |
| Finance or risk copy must stay plain and complete | Monzo, Mercado Pago FAQ |

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

**[Next.js](https://nextjs.org/)** · React framework (redesign announced 2026-10-13)
- Signature: pure black `rgb(0,0,0)` with `rgb(237,237,237)` text, Geist Sans
  and Geist Mono only, a 40px H1 at weight 450 (light for a headline), and a
  giant outlined "NEXT" wordmark with a blue gradient edge behind the title.
- Lesson: the hero action is the install command itself, a copyable
  `npx create-next-app@latest` pill, so the first click is the product. The
  brand is the wordmark treated as art, not an illustration. The feature list
  is ten short rows (name, arrow, one sentence), with no icons or cards.
- Learn the move: the redesign goal was one consistent design across home,
  docs and blog that "keeps focus on content". Restraint (one family, one
  weight range, no accent color) is what carries that consistency, and I
  confirmed it on `/blog` and `/docs` (same black, same Geist, headings at
  weight 450: 40px home and docs, 48px blog).
- Blog: "The latest Next.js news" is a card grid, each card with a date, a
  category tag (Security), a title, one summary sentence and author avatars.
  The top slot goes to a security notice with a dated promise ("out-of-band
  update next Wednesday"), so urgency is stated as a fact, not a banner.
- Docs: a sidebar with a version switcher ("Latest v16.4.0") and a router
  switcher ("Using App Router"), a "Copy page" button at the top of every
  page, "Ask AI" plus `⌘K` search in the header, and 16px / 28px body text.
  The intro tells readers the three sections (Getting Started, Guides, API
  Reference) before anything else.
- Home sections, top to bottom: hero, a three-column grid of feature cells
  (line-art diagram, then a linked title, then one sentence), a foundation
  trio (React, Turbopack, compiler), customer sites, two quotes, templates,
  a closing "Ready to deploy?" row. The page is mostly empty space; each
  band is about 650-1500px tall, so one idea fills one screen.
- Feature cells: the first three carry monochrome line diagrams on a faint
  grid frame (stacked images being optimized, a browser wireframe, a node
  tree), with one blue dot or line as the only color. The tenth cell is a
  solid blue tile ("Next.js 16 →", `rgb(0,87,255)`, 4px radius) that breaks
  the grid once, so the release is the loudest thing without a banner.
- Proof: customer sites appear as real screenshots in a grayscale frame
  (Notion and a sneaker store), then quotes with a logo, a name and a role. Color is
  withheld so the product shots do not fight the page.
- Templates: cards with a 2px radius, a 1px `rgb(41,41,41)` border and a
  folded top-right corner, a source path in mono at the bottom
  (`examples/nextjs`). The primary button is a blue pill (`rgb(0,87,255)`,
  40px high); the secondary is a dark outlined pill next to it.
- Type: the H1 uses -0.06em letter spacing (-2.88px at 48px) at weight 450,
  so large headings read tight and calm. The blog article body is 18px /
  28px, the docs body 16px / 28px, code blocks 16px with an 8px radius.
- Light theme (measured with a light color scheme): background
  `rgb(250,250,250)`, text `rgb(23,23,23)`, the same blue tile, the same
  wordmark with its blue gradient edge. The identity survives the swap
  because it is shape and one color, not a dark mood.
- Mobile (375px): the wordmark scales to full width, the H1 wraps in three
  lines, the install pill stays whole with its copy icon, and the header
  keeps "Ask AI" plus a round menu button.
- Blog post: date and "Blog" label above the title, an author avatar stack
  ("Next.js Team", 9+), then the problem as a three-item list before any
  heading. Headings carry a "Copy link to heading" control and the right
  column has "On this page".
- Docs: callouts ("Good to know") sit on a `rgb(242,242,242)` panel with a
  6px radius; terminal blocks have a "Terminal" label and a copy button;
  the install page shows the real CLI prompts, including one that asks to
  add an `AGENTS.md` for coding agents.
- Watch: I did not test hover states, keyboard focus or the header menu
  (my click on the menu missed), and the customer-logo grid was blank until
  lazy images loaded, so wait before any screenshot.

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

**[Clonvo](https://clonvo.com/)** · AI gateway for agents
- Signature: warm near-black `rgb(18,17,16)` with warm off-white text
  `rgb(236,232,223)`, an 84px Geist Serif H1 at weight 400 over Inter
  Variable body; section headings stay at weight 400 too.
- Lesson: the home page embeds the product with sample data. A model picker
  drives a Python / Node.js / curl tab set, the response shows its own
  `usage.cost`, and a full dashboard mock ("Good afternoon, Priya", balance,
  spend by model, latest requests) links into real app routes. Features
  are six numbered rows ("01 / 06") with one plain sentence each, and the
  last one is a privacy default ("Prompts aren't stored by default").
- Pricing (`/pricing`): three plans, then "What you'd pay" worked examples:
  one request priced line by line (12,000 input tokens × $2.00 / 1M =
  $0.0240), a table of what each credit purchase costs with its fee, and a
  table of the bring-your-own-key fee at different usage levels. The
  minimum fee's threshold is stated ("applies below $14.55").
- Compare (`/compare`): a feature matrix against five named gateways that
  shows where a rival wins (OpenRouter 600+ models against 150+) and writes
  "Not stated" instead of "No" when a rival's docs are silent. Each
  rival then gets one fair paragraph.
- Learn the move: price with arithmetic, not adjectives; compare with
  "not stated", not with red crosses.
- Watch: the hero captured blank except the heading until its reveal ran,
  the same finish-gate issue as Cloudflare.

### Consumer and business AI

**[Perssua](https://perssua.com/pt)** · real-time meeting copilot (PT-BR)
- Signature: black, a single family (Space Grotesk), the verb "escuta" in a
  pill inside the H1, a waveform with a running timer.
- Lesson: "Veja o Perssua em ação" is a tabbed scenario demo (technical
  interview, cold call, 1:1, call in English); each tab shows the heard
  question and the suggested answer, so the promise is shown in context.
  Download buttons name the visitor's OS and package format, and an
  "unstable" badge sits inside each Linux button.
- Also: the live-translation section is a working-looking session panel
  (original line, translation under it, one audio meter per speaker, the
  `⌘+D` action), so a listener reads both sides at once. The H1's object is
  typed and replaced ("suas reuniões", "suas ch…"); keep a static full
  sentence for reduced motion and screen readers.
- Watch: the cookie card covers the lower-left demo at 1440px and the bottom
  half of the first screen at 390px. Check consent UI in the first-viewport
  capture.

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

**[MeetAssist](https://meetassist.io/)** · interview copilot
- Signature: a near-black hero with a purple glow and a curved bottom edge,
  Russo One 56px for the H1 only, Inter for the rest, then pale
  `rgb(245,245,247)` sections and one violet action `rgb(124,58,237)`.
- Lesson: proof you can check. Reviews carry their source and month ("Chrome
  Web Store · Apr 2026"), the rating is an ordinary 4.1 with its count (27),
  and a line under the wall says how quotes were handled (word for word,
  support-chat names withheld). An imperfect rating with a source beats
  five stars without one.
- Limits sit beside the offer: "(visible on screen share)" next to the
  Chrome extension link, "No auto-renewal" on every paid plan, and a closing
  "Use it where it's welcome" note.
- Learn the move: H2s in two voices, the claim in full color and the
  explanation in gray in the same heading, with no eyebrow. Audio sources,
  model choice and the answer window are joined by one dotted line, so the
  pipeline is the picture. The FAQ has a topic list beside it.
- Watch: the purple glow and floating glyphs are the generic AI look (see
  the accent row below); usage counters have no source. Product images did
  not load in this capture, so they are not judged. Same premise caution as
  Cluely and Interview Coder.

**[TechScreen](https://techscreen.app/)** · interview copilot
- Signature: near-black `rgb(8,9,12)`, Geist only, an 82px H1 at weight 500
  with -3.9px tracking, half of each H2 in gray, white pill as the one loud
  action, periwinkle kept for the logo and ticks.
- Lesson: one draggable divider over one call, "What you see" on the left
  and "What they see" on the right. The visitor operates the promise
  instead of reading it. Works for any two-view product: draft/published,
  admin/customer, original/redacted.
- The feature list is one vertical sequence with a product fragment per
  step, and settings and shortcuts appear as the real panels. Pricing is a
  single three-column table with shared borders; only the middle column
  changes surface, and each plan says whom it fits ("1-2 interviews /
  month").
- Watch: features and text rest at very low contrast until their scroll
  reveal, and several demo panels captured almost blank. "Perfect interface"
  and "Zero detection incidents" are comparison rows nobody can check, and
  many quotes are anonymous. Same premise caution as Cluely and Interview
  Coder.

**[Natively](https://heynatively.com/)** · meeting and interview copilot
- Signature: white to lilac, PP Neue Montreal 70px weight 500 with the second
  H1 line in a violet italic serif, a violet mountain range in mist, and the
  product overlay resting on the peak.
- Lesson: one overlay, the same in every scene. The bar with its five actions
  (What to answer?, Clarify, Recap, Follow Up Question, Answer) appears in the
  hero, inside a scroll-opened laptop and in each feature card, so the page
  teaches the interface by repetition.
- "Four ways" is a sequence of offset cards with a side index that marks the
  current step; each card holds a filled-in artifact (summary, action items,
  a ready follow-up email), not an empty panel. "Nine modes" shows the actual
  prompt behind each mode.
- Learn the move: "View on GitHub" is the hero's second action, so the open
  code is a check the visitor can make before installing.
- Learn the move: testimonials are a pulled phrase at heading size with the
  whole quote beside it, alternating sides.
- Watch: headings and quotes are painted word by word on scroll, so captures
  catch half-gray text; the primary button is pale violet on lilac and weaker
  than the art. Serif italic on a landscape is close to Cluely's device. The
  "0 security breaches" and user counters have no source, and quotes are
  unnamed ("Premium user"). FAQ and footer were not captured. Same premise
  caution as Cluely and Interview Coder.

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
  row on click. The status list (number, app, "last updated", state) borrows
  the status-page form; use it only over real checks.
- Rhythm: sand bands break the black page for proof and the closing CTA, so
  a long page has three landmarks without a second accent.
- Do not learn its proof: repeated "Anonymous User" testimonials and
  absolute "100%" claims (both still there on 2026-11-24) are exactly what
  `devtool-landing.md` forbids. Its product premise (hiding AI use during
  interviews) is not an endorsement.

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

### Payments and banking

**[Nubank](https://nubank.com.br/)** · digital bank (PT-BR)
- Signature: its own face (nuSansDisplay) for display and body, H1 48px
  weight 600 with -1.4px tracking, one purple `rgb(141,13,227)` used only for
  pill buttons (999px radius, 56px tall in the page body).
- Lesson: sign-up starts in the hero with one field ("Digite seu CPF") and
  "Continuar", so the first action costs one number. Products are four
  cards, one sentence each ("Controle total da sua vida financeira").
  Security gets its own block with the emergency path first, in plain words
  ("Me roubaram"), then report and support channels.
- Watch: the real product is the app; this page shows only its marketing.

**[Wise](https://wise.com/br/send-money/)** · international transfers (PT-BR)
- Signature: Wise Sans 88px weight 800 H1 in lime `rgb(159,232,112)`, Inter
  body, lime pill CTAs with dark-green text `rgb(22,51,0)`.
- Lesson: the transfer calculator shows everything before the button: the
  rate (1 EUR = 6,2517 BRL), what the recipient gets, the delivery estimate
  ("Hoje — em segundos"), taxes and fees in BRL, the discount for large
  amounts and the effective rate (VET). The home page compares its cost with
  a credit card on a US$1.000 conversion and states method and date of the
  comparison ("coletadas em 6 de agosto de 2025").
- Learn the move: put the fee, the rate and the arrival time in the same
  card as the amount; a comparison carries its method and date.

**[Stripe Checkout](https://stripe.com/payments/checkout)** · payment pages
- Signature: söhne (sohne-var), a 56px weight 500 H1, violet
  `rgb(153,102,255)` CTA pills, a cyan `rgb(13,228,228)` pill for developer
  actions ("Confira a documentação").
- Lesson: the hero is a working checkout demo in a browser frame: product,
  price, express pay, card fields, and a pay button that repeats the amount
  ("Pagar R$ 350,00"). It cycles through variants (embedded form, address
  autocomplete, localized for the US, the Netherlands, Poland and Japan), so
  each claim ("Feito para reduzir o atrito", "Criado para clientes globais")
  has its own screen.
- Learn the move: the pay button names the amount; never a bare "Pay".

**[Mercado Pago](https://www.mercadopago.com.br/)** · digital bank and payments (PT-BR)
- Signature: Proxima Nova, a 72px weight 700 H2 with -2.88px tracking, a
  celebrity photo hero, dark translucent nav pills `rgba(40,40,52,0.7)`.
- Lesson: like Nubank, the hero holds a CPF field, plus a consent checkbox
  that links the privacy statement before the account starts. The FAQ
  answers money questions directly: is it safe (biometrics, "Modo
  Blindado", alerts), how much it yields (105% / 140% of CDI), does the card
  charge an annual fee (no, nor issue or replacement fees).
- Watch: checkout pages redirected to the home page, so the payment flow
  itself was not inspected.

**[Monzo](https://monzo.com/)** · UK bank
- Signature: MonzoSansDisplay weight 800 headings, MonzoSansText body, navy
  `rgb(9,23,35)` pill buttons, a real photo of the app and card in a hand.
- Lesson: features are named as outcomes with a verb ("Sort your salary",
  "Put bills in their place", "Round up your spare change"). Conditions sit
  next to the product, not in a footer: "Age 18+", "Ages 18-70",
  "investments could go up or down", "Missed payments may negatively impact
  credit scores". The cookie banner gives "Accept all" and "Reject all" the
  same weight.

**[Ramp](https://ramp.com/)** · corporate cards and spend
- Signature: Lausanne at weight 400 for every heading (64px H1), off-black
  text, a lime-yellow CTA in `lab()` color, 6px radius buttons.
- Lesson: the pain is drawn before the cure ("Systems that never spoke": the
  five systems needed to reimburse one flight). A recommendation form asks
  "What would you like to spend less time on?" with chips (chasing
  receipts, approving spend, paying bills), so the visitor picks the problem.
- Watch: the live counters ("RECEIPTS PROCESSED", "TOTAL AI ACTIONS")
  captured empty; numbers loaded by script need a wait before any capture.

### Education

**[Duolingo](https://www.duolingo.com/)** · language and chess lessons
- Signature: duolingo-sans weight 700, lowercase section headings ("grátis.
  divertido. eficaz."), 12px-radius buttons with a thick bottom edge, a
  mascot that also sends the reminders.
- Lesson: "Comece agora" opens "Eu quero aprender..." with learner counts
  per course (Inglês 23,6 mi), then a daily goal, all before any account is
  asked for. The value is learned before the sign-up costs anything.

**[Khan Academy](https://pt.khanacademy.org/)** · free courses and practice
- Signature: Source Serif Pro 40px H1 over Lato body, one blue
  `rgb(24,101,242)`, 4px radius buttons.
- Lesson: sign-up splits by role in three large cards (Aluno, Família,
  Professor). The catalog follows the curriculum people already know (BNCC,
  1° ao 9° ano). A course page shows five mastery levels (Não iniciado,
  Tentativa, Familiar, Proficiente, Dominado) and the total points possible
  (19.400), with a test after each group of lessons and a course challenge.
- Learn the move: measure progress by what the learner can do, and say so.

**[Brilliant](https://brilliant.org/)** · math and coding tutor
- Signature: CoFo Robert 54px weight 500 H1, CoFo Brilliant body, white,
  black pill tabs with a soft 4px shadow.
- Lesson: it answers the parent's fear in the headline of a feature ("A
  visual, interactive tutor, not a cheating machine": it guides without
  giving the answer). Two entry buttons split the audience ("I'm a learner",
  "I'm a parent or teacher"), and trust markers are specific (kidSAFE COPPA,
  accredited by ACS WASC, 5,000 schools).

**[Coursera](https://www.coursera.org/learn/machine-learning)** · university courses
- Signature: Source Sans Pro, a 44px weight 600 H1, blue `rgb(0,86,210)`.
- Lesson: the course header answers "what will this cost me" in time and
  level: "3 semanas em 10 horas uma semana", "Nível Básico", "Cronograma
  flexível", the start date inside the CTA ("Inicia em 15 de nov"), and the
  language with its method ("Português (Dublagem de IA)"). Modules are
  "Semana 1, 2, 3", and the certificate is listed as a deliverable.
- Watch: some strings are machine-translated and read badly; write the
  copy, do not translate it automatically.

**[Udemy](https://www.udemy.com/course/the-complete-web-development-bootcamp/)** · course marketplace
- Signature: Udemy Sans, a 32px weight 500 H1 on a dark band, violet
  `oklch(0.48 0.23 294)` buttons with 8px radius.
- Lesson: the course page is the template: rating with count, students,
  instructor, last updated date, "What you'll learn", what the course
  includes (61 hours, 7 exercises, 194 resources), then "45 sections • 374
  lectures • 61h 53m" with free preview lectures inside the curriculum.
- Do not learn its urgency: a top banner counts down ("Ends in 5h 59m
  58s") a new-student price. Fake or rolling deadlines are a dark pattern.

**[Alura](https://www.alura.com.br/)** · tech school (PT-BR)
- Signature: encodeSans, light (300) display headings, dark promo bands.
- Lesson: a career page opens with its real size ("50 Cursos, 554h de
  Aulas"), and the looping offer banner has a "Pausar animação da oferta"
  control, which is the accessible way to ship a marquee.
- Watch: inspected during "Black November": the home page was a countdown
  (14 days), a prize draw, "278 bônus escolhidos" and an "esgotado" bonus.
  Recheck after the campaign before using it as a structure reference.

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
| Draggable divider between two views | TechScreen, MeetAssist, Natively, Interview Coder | both sides are the same moment and the handle works by keyboard | it compares a mockup with an empty box |
| Two-tone heading (claim, then gray) | TechScreen, MeetAssist, Natively, Rerun | the gray half still passes contrast and adds information | the gray half is filler or unreadable |
| Mono face as a secondary voice | Vercel, Cloudflare, Rerun, Linear | it carries real code, identifiers and values | it decorates section labels and eyebrows (see the mono-labels ruling in `conflicts.md`) |
| Scroll-revealed sections | Cloudflare, Linear, Perssua, Clonvo, TechScreen, Natively | content still loads without motion | screenshots and reduced-motion users see blank space |
| One identity field in the hero (CPF, email) | Nubank, Mercado Pago, Ramp | the next step is short and the consent is visible | it hides a long form behind "Continuar" |
| Cost shown before the action | Wise, Clonvo, Stripe | fee, rate and total are in the same card as the button | the fee appears only on the last step |
| Sign-up split by role | Khan Academy, Brilliant | each role gets a different path | the cards lead to the same form |
| Countdown to a price | Udemy, Alura | a real, dated campaign end | the deadline resets or never ends |

The scroll-reveal row is a finish-gate issue: several of these pages captured
blank until their reveal ran. Build reveals so content is visible without
animation, and wait for loaded content before the screenshot gate.
