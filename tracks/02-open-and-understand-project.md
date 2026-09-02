# Track 2 — Open and understand the existing project

**Goal:** Know what already works and create a compact source of truth before
asking any model to redesign the site.

You do **not** need to understand the code line by line.

## 1. Pull the newest `main`

**Where:** GitHub Desktop.

1. Open `mmoptibuilds-portfolio-yin-yang`.
2. Click **Fetch origin**.
3. Click **Pull origin** if shown.
4. Confirm the branch is `main`.
5. Confirm there are no unexpected local changes.

## 2. Open the project the same way every time

**Antigravity:** open/create a Project whose folder is the local portfolio root.

Keep these surfaces:

```text
Antigravity
├── Editor → portfolio root
├── Terminal A → npm run dev
└── Terminal B → claude

GitHub Desktop
└── same repository → branch/change/push/pull control

Gemini App
└── separate browser/app → receives only curated context you explicitly attach
```

Do not open a second independent copy of the repo unless you intentionally use a
worktree.

## 3. Read these files yourself first

Open in the editor:

1. `README.md`
2. `AGENTS.md`
3. `package.json`

You only need to understand the headlines:

- how to run it;
- how to verify it;
- important codebase traps;
- available scripts.

The project map is:

```text
app/
├── (gateway)/             homepage /
├── (systems)/systems/     Systems pages
├── (studio)/studio/       Studio pages and work
├── (legal)/               about/contact/privacy/terms
└── admin/                 owner dashboard

components/
├── shared/                behavior/accessibility only
├── systems/               visible Systems patterns
└── studio/                visible Studio patterns

content/                   typed page copy/data
lib/                       schemas, auth, storage, SEO, utilities
supabase/migrations/       production database structure/rules
scripts/                   verification suite
```

## 4. Run the site while you inspect it

**Terminal A — PowerShell in portfolio root:**

```powershell
npm run dev
```

Open:

- <http://localhost:3000/>
- <http://localhost:3000/studio>
- <http://localhost:3000/systems>
- <http://localhost:3000/admin>

Use only synthetic/test enquiries.

## 5. Ask GLM for the first repo audit

**Open:** Terminal B in Antigravity, portfolio root.  
**Start:** `claude` and select your GLM-5.3 AgentRouter profile.  
**Mode:** read-only / planning.  
**Give it:** no giant chat transcript. Let it read `README.md`, `AGENTS.md`,
`package.json` and only relevant code.

### Paste this prompt

```text
ROLE
You are the technical auditor for the existing mmoptibuilds Yin-Yang portfolio.

READ FIRST
- README.md
- AGENTS.md
- package.json
- app/(gateway)/
- app/(studio)/studio/
- app/(systems)/systems/
- admin/ and related admin files
- only other files needed to verify a claim

CURRENT OWNER GOALS
- Keep the existing engineering foundation; do not rebuild from scratch.
- / should feel like a memorable world-class portfolio/brand gateway.
- Studio and Systems must be obvious and easy to enter.
- /studio should be distinctive and conversion-ready for website clients.
- /systems should be clear, trustworthy and conversion-ready for hardware enquiries.
- /admin should stay fast, usable and secure.
- Mobile, responsive behavior, accessibility, SEO and performance are mandatory.
- No invented clients, testimonials, awards, prices, stock or metrics.
- Advanced motion is allowed only when it materially improves the result.
- npm run verify is the final project gate.

TASK
Audit the current repository and current implementation state.

DO NOT
- edit files
- install dependencies
- propose a rewrite from scratch
- dump a giant wishlist
- treat the old roadmap package as more authoritative than current owner instructions

RETURN
1. What already works and must be preserved.
2. What is technically incomplete.
3. What is visually/UX-wise weakest by route: /, /studio, /systems, /admin.
4. What documentation/source-of-truth files already exist.
5. What compact source-of-truth files are missing.
6. The highest-value next milestone only.
7. Evidence: exact files/routes.
8. The exact verification commands for that milestone.
```

### What you check yourself

Do not continue until the answer:

- clearly says **preserve**, not rebuild;
- recognizes `npm run verify`;
- treats `/`, `/studio`, `/systems`, `/admin` differently;
- does not invent business proof;
- identifies evidence instead of giving only aesthetic opinions.

### Pass to the next tool

Keep this GLM audit. You will use its **documentation/source-of-truth findings**
in the next step.

## 6. Create the compact agent source of truth — one time

The website `roadmap.mmoptibuilds.com` is useful for you, but agents need current
local files that travel with the exact commit.

Create a branch in GitHub Desktop:

```text
chore/agent-source-of-truth
```

**Writer:** DeepSeek V4 Flash in Claude Code.  
**Give it:** the GLM repo audit plus current `README.md`, `AGENTS.md`, and the
old authoritative pack only where it contains facts still valid today.

The target is compact files such as:

```text
DESIGN.md
CHANGELOG.md
docs/
├── PROJECT-BRIEF.md
├── PROJECT-STATE.md
├── ROADMAP.md
├── ARCHITECTURE.md
├── DECISIONS.md
├── WORKFLOW.md
├── TESTING.md
├── DEPLOYMENT.md
└── agent-log/
```

Do not create empty bureaucracy. If a file already exists and is good, improve
it rather than duplicate it.

### Paste this prompt

```text
You are the ONLY writer for a documentation-only task.

READ FIRST
- README.md
- AGENTS.md
- the GLM repository audit I paste below
- existing project documentation
- current source code only when needed to verify a factual statement

GOAL
Create or improve a compact local source-of-truth layer so a future agent can
understand this exact repository without reading old chats or depending on
roadmap.mmoptibuilds.com.

REQUIRED INFORMATION
- what mmoptibuilds is
- /, /studio, /systems and /admin goals
- current architecture
- current factual project state
- important decisions and traps
- current roadmap / next milestone
- how to run and verify
- deployment architecture
- exact multi-model workflow
- truthful-content rules
- performance/accessibility floors

DOCUMENTATION RULES
- Do not copy the old giant manual into the repo.
- Keep each file short enough to scan.
- Do not duplicate README.md or AGENTS.md unless a fact belongs in a different file.
- Current owner instructions override old pack decisions.
- Record date in IST and UTC where a session log needs time.
- Create docs/agent-log only for meaningful session handoffs.
- Do not edit application source code.
- Do not install packages.

AFTER WRITING
- list every created/changed documentation file
- explain why it exists in one sentence
- show any old statement you intentionally superseded
- run a link/Markdown sanity check if one exists
- show git diff --stat

GLM AUDIT:
<PASTE THE RELEVANT GLM AUDIT HERE>
```

### What you check yourself

Open the new docs and ask:

- Can I understand the current site in five minutes?
- Are there duplicate walls of text?
- Does `PROJECT-STATE.md` describe **now**, not an old plan?
- Does `ROADMAP.md` tell an agent what is next?
- Are old “build from scratch” instructions superseded where necessary?
- Are there no secrets/customer data?

### Pass to the next tool

Give the documentation diff to GLM-5.3 for read-only review.

### Paste this prompt

```text
Review this documentation-only diff.

Check:
- factual consistency with the current repository
- current owner instructions override older pack decisions
- no duplicate/bloated documentation
- no missing critical source-of-truth item
- no stale "build from scratch" instruction
- no secret/customer data
- clear next milestone

Do not edit files.

Return only:
BLOCKER
HIGH
MEDIUM
LOW

Each finding must cite the file and smallest fix.
```

If GLM has blocker/high findings, give only those findings back to DeepSeek to
fix. Then review the diff yourself and commit/push the documentation branch.

## 7. Your normal context pack from now on

For a meaningful coding task, the planner normally receives:

```text
README.md
AGENTS.md
docs/PROJECT-BRIEF.md
docs/PROJECT-STATE.md
docs/ROADMAP.md
DESIGN.md
+ files directly relevant to the task
```

Do **not** attach all docs to every tiny task.

## 8. Know the main verification commands

```powershell
npm run typecheck
npm run lint
npm run test
npm run check:a11y
npm run check:keyboard
npm run check:responsive
npm run check:bundle
npm run check:perf
npm run verify
```

## Done when

- [ ] You pulled current `main`.
- [ ] The same repo folder is open in GitHub Desktop and Antigravity.
- [ ] `npm run dev` works.
- [ ] GLM produced a factual read-only audit.
- [ ] The compact source-of-truth layer exists or its existing equivalent was confirmed.
- [ ] The docs were reviewed for bloat/staleness.
- [ ] You know which files form the normal context pack.
- [ ] You know the next real milestone.

## Next

→ [Track 3 — First safe agent session](03-first-safe-agent-session.md)
