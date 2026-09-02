# Track 4 — The exact design + build loop

**Goal:** Use one predictable sequence for every meaningful portfolio task so
you never wonder which model comes next or what to give it.

> [!IMPORTANT]
> This is the track you return to whenever you build a new feature, redesign a
> section, change a conversion flow, add serious motion, or modify architecture.

## First: choose the route's job

| Route | Optimize for |
|---|---|
| `/` | memorability, credibility, art direction, obvious Studio + Systems entry |
| `/studio` | proof, positioning, differentiation, website-client conversion |
| `/systems` | clarity, technical trust, requirement-led enquiry conversion |
| `/admin` | speed, scanability, low error rate, privacy |

## Keep the project open like this

```text
GitHub Desktop
└── current task branch

Antigravity Project
├── portfolio root
├── Terminal A → npm run dev
├── Terminal B → Claude Code
└── Browser agent → later visual QA

Gemini App
└── separate browser/app for plan/design critique
```

Before any writer edits, pull `main` and create one task branch.

---

# Phase A — Define the task

If you already have a precise outcome, skip to Phase B.

If you only know “this page feels bad” or “make it more Awwwards-like,” use
Antigravity `/grill-me` exactly as shown in Track 3.

Ready-made task definitions:

<details>
<summary><strong>Homepage / gateway task starter</strong></summary>

```text
OUTCOME
Improve the homepage gateway so a first-time visitor immediately understands
that mmoptibuilds has Studio and Systems, sees both paths without hunting, and
gets a memorable portfolio-level impression.

MUST PRESERVE
- easy Studio + Systems entry
- current route behavior
- responsive/accessibility/performance floors
- truthful brand/business content

DESIGN DIRECTION
- keep the Yin-Yang duality concept
- stronger art direction, depth, typography and interaction are allowed
- advanced motion/GSAP/Lenis/WebGL only if justified and tested
- mobile must have its own intentional composition

SUCCESS
A visitor can understand the brand and enter either division immediately, while
the page feels authored and distinctive rather than template-like.
```

</details>

<details>
<summary><strong>Studio task starter</strong></summary>

```text
OUTCOME
Improve /studio so it proves design capability, feels distinctive, and makes a
qualified website client understand what mmoptibuilds Studio can do and what to
do next.

MUST PRESERVE
- honest project labels
- clear inquiry path
- mobile/accessibility/performance/SEO
- separate Studio visual identity

SUCCESS
The page has strong portfolio storytelling and clear conversion without generic
agency copy, fake proof or effects that interrupt reading.
```

</details>

<details>
<summary><strong>Systems task starter</strong></summary>

```text
OUTCOME
Improve /systems so a hardware buyer quickly understands the requirement-led,
no-stock sourcing model and can choose the correct enquiry path with confidence.

MUST PRESERVE
- no public pricing
- no implied stock
- exact enterprise service boundaries
- accessible, mobile-friendly conversion

SUCCESS
The page feels technically credible and premium, but information remains easy to
scan and the inquiry CTA is obvious.
```

</details>

<details>
<summary><strong>Admin task starter</strong></summary>

```text
OUTCOME
Improve /admin so the owner can scan enquiries, understand state and perform the
next action quickly with fewer mistakes.

MUST PRESERVE
- privacy/security
- owner-only behavior
- keyboard usability
- noindex/private boundaries

SUCCESS
The admin is clear, fast and dependable. Do not add decorative complexity that
slows the owner down.
```

</details>

---

# Phase B — GLM plans

**Open:** Antigravity Terminal B, portfolio root.  
**Use:** Claude Code → GLM-5.3.  
**Permission:** read-only/plan.  
**Give it:**

```text
README.md
AGENTS.md
docs/PROJECT-BRIEF.md
docs/PROJECT-STATE.md
docs/ROADMAP.md
DESIGN.md
+ the task definition
+ only source files related to that route/feature
```

If a listed doc does not exist yet, use Track 2 first.

### Paste this prompt

```text
ROLE
You are the senior technical planner for the existing mmoptibuilds portfolio.

TASK
<PASTE THE TASK DEFINITION>

READ FIRST
- README.md
- AGENTS.md
- docs/PROJECT-BRIEF.md
- docs/PROJECT-STATE.md
- docs/ROADMAP.md
- DESIGN.md
- only relevant source/tests

PRESERVE
- existing engineering foundation
- current working admin/enquiry architecture unless this task explicitly changes it
- route-specific Studio/Systems identity separation
- truthful proof/business claims
- mobile, accessibility, SEO and performance floors
- documented AGENTS.md traps

DO NOT
- edit files
- install packages
- rewrite unrelated architecture
- add a dependency because it is fashionable
- assume a visual idea is technically safe without checking
- expand this task into a site-wide redesign

RETURN ONE PLAN WITH
1. outcome
2. current evidence
3. exact owned files
4. read-only files
5. ordered implementation steps
6. content/conversion changes
7. desktop + mobile behavior
8. keyboard/reduced-motion/no-JS behavior
9. performance/bundle implications
10. dependency decision
11. targeted verification commands
12. final npm run verify requirement
13. documentation to update
14. explicit exclusions
15. risks/owner decisions

Do not write implementation code.
```

### What you check yourself

Stop if:

- GLM lists dozens of unrelated files;
- it proposes rebuilding the app;
- mobile is an afterthought;
- it removes existing verification;
- it installs packages without a concrete sequence that needs them.

### Pass to the next tool

Copy the **entire plan** to Gemini App.

---

# Phase C — Gemini critiques the plan

**Open:** Gemini App.  
**Use:** Gemini 3.1 Pro Extended / strongest appropriate Pro reasoning mode.  
**Give it:**

- GLM plan;
- `PROJECT-BRIEF.md`;
- `DESIGN.md`;
- current desktop/mobile screenshots of the affected route;
- 1–5 useful visual references, if any.

Do not give the entire repo or secrets.

### Paste this prompt

```text
You are the independent product, art-direction, UX, conversion and technical
critic for mmoptibuilds.

INPUT
- GLM technical plan
- project brief/design rules
- current screenshots
- selected references if provided

ROUTE GOAL
<PASTE THE ROUTE/TASK GOAL>

PRIORITIES
1. distinctive art direction / credibility
2. conversion and clear communication
3. performance
4. accessibility
5. maintainability

RULES
- performance/accessibility are floors, not optional polish
- Studio and Systems must remain easy to access
- mobile must be deliberately composed
- no fake clients, awards, testimonials, metrics, stock or prices
- avoid generic AI-template visuals
- do not copy reference components unchanged
- advanced motion/effects need a purpose

CRITIQUE THE PLAN.

RETURN
KEEP
CHANGE
DELETE
MISSING
MOBILE RISKS
CONVERSION RISKS
VISUAL/ART-DIRECTION RISKS
TECHNICAL RISKS
RECOMMENDED DIRECTION

Be finite and specific. Do not expand unrelated scope.

GLM PLAN:
<PASTE GLM PLAN>
```

### What you check yourself

Ask yourself:

- Would this still let someone quickly enter Studio/Systems?
- Is Gemini suggesting a fashionable component rather than a mmoptibuilds idea?
- Is the recommendation possible on mobile?
- Does it preserve truthful proof?

### Pass to the next tool

Copy Gemini's full critique back to the **same GLM session**.

---

# Phase D — GLM reconciles into the final brief

### Paste this prompt

```text
Reconcile the Gemini critique with the real repository.

For each meaningful suggestion:
ACCEPT / MODIFY / REJECT
+ one sentence of evidence/reason.

Then return ONE FINAL IMPLEMENTATION BRIEF.

The brief must contain:
- exact outcome
- owned files
- read-only files
- ordered steps
- content/conversion requirements
- desktop/mobile requirements
- keyboard/accessibility/reduced-motion/no-JS requirements
- dependency decision
- performance/bundle requirements
- targeted checks after logical parts
- final npm run verify
- documentation/handoff updates
- explicit out-of-scope items

Do not edit code.

GEMINI CRITIQUE:
<PASTE CRITIQUE>
```

### What you check yourself

This is the **contract** for DeepSeek. Read it once.

Do not continue if it has unresolved blocker questions.

### Pass to the next tool

Copy only the **FINAL IMPLEMENTATION BRIEF**.

---

# Phase E — DeepSeek implements

**Open:** Claude Code in Terminal B, same branch/repo.  
**Switch model/profile:** DeepSeek V4 Flash.  
**Writer rule:** no other agent edits the working tree.  
**Give it:**

- final implementation brief;
- `README.md`;
- `AGENTS.md`;
- relevant source files;
- source-of-truth docs.

### Paste this prompt

```text
ROLE
You are the ONLY writer for this task.

FINAL IMPLEMENTATION BRIEF
<PASTE FINAL BRIEF>

READ FIRST
- README.md
- AGENTS.md
- relevant source files/tests
- relevant current project docs

RULES
- Implement the approved brief, not a new interpretation of the project.
- Do not edit files outside approved scope unless a required dependency forces a
  tiny documented change.
- Do not install a package unless the final brief explicitly approved it.
- Preserve documented Next.js/codebase traps.
- Preserve keyboard, no-JS and reduced-motion behavior.
- Keep Studio and Systems visual identity boundaries.
- Do not invent public claims.
- Do not deploy.
- Do not commit yet.

WORK
1. Inspect before editing.
2. Implement the smallest coherent part.
3. Run the narrowest relevant check.
4. Fix task-caused failures before continuing.
5. Repeat until the brief is complete.
6. Run all targeted checks from the brief.
7. Run npm run verify.

DOCUMENTATION
For meaningful work update only what is genuinely affected:
- docs/PROJECT-STATE.md
- docs/ROADMAP.md if milestone status changed
- CHANGELOG.md for user-visible/meaningful changes
- DESIGN.md or docs/DECISIONS.md only for an actual decision
- current docs/agent-log/YYYY-MM.md entry

Use IST and UTC timestamps in the agent log.
Keep docs concise.

RETURN
- files changed
- what changed for the user
- commands/tests run and exact result
- documentation updated
- anything not completed
- risks
- exact areas GLM should review

Do not claim completion if npm run verify is failing.
```

### What you check yourself

Before review:

- Open GitHub Desktop → **Changes**.
- Look for unrelated files.
- Confirm no `.env.local`, `.enquiries`, secrets or customer data are staged.
- Open the changed page locally.
- Check that the task actually looks/behaves different in the intended way.

### Pass to the next tool

Do **not** commit yet.

Switch Claude back to GLM-5.3 and give it the current diff plus the final brief.

---

# Phase F — GLM reviews code

**Use:** GLM-5.3, read-only.  
**Give it:** final implementation brief + `git diff`/branch changes.

### Paste this prompt

```text
Review the current uncommitted/branch diff against the FINAL IMPLEMENTATION BRIEF.

DO NOT EDIT FILES.

Review in this order:
1. functional correctness
2. missing brief requirements
3. regressions against README.md / AGENTS.md traps
4. accessibility / keyboard / no-JS / reduced motion
5. responsive/mobile behavior
6. bundle/performance cost
7. truthful content/business boundaries
8. SEO impact where relevant
9. maintainability only where it affects this task

For each finding:
SEVERITY: BLOCKER / HIGH / MEDIUM / LOW
FILE + LOCATION
EVIDENCE
WHY IT MATTERS
SMALLEST SAFE FIX
HOW TO VERIFY

Do not report preference-only style comments as bugs.
Do not edit.
If there are no evidence-backed blocker/high findings, explicitly say that.
```

### What you check yourself

Only accept findings with evidence.

### Pass to the next tool

Copy accepted **BLOCKER/HIGH** findings, plus any MEDIUM you personally want, to
DeepSeek.

---

# Phase G — DeepSeek fixes code-review findings

### Paste this prompt

```text
You are still the ONLY writer.

Below are the accepted review findings.

For each finding:
1. verify it against the actual current code
2. fix it only if it is real
3. run the narrowest relevant check

Do not blindly implement an incorrect reviewer suggestion.
Do not broaden scope.

After all accepted fixes:
- run the targeted task checks
- run npm run verify
- update project docs only if the fixes changed documented state/decisions
- report each finding as FIXED / REJECTED WITH EVIDENCE / NOT FIXED

ACCEPTED FINDINGS:
<PASTE FINDINGS>
```

### What you check yourself

Use GitHub Desktop again. Confirm fixes did not create unrelated changes.

---

# Phase H — Antigravity reviews the real running page

**Terminal A:** keep `npm run dev` running.  
**Open:** Antigravity agent on the same Project.  
**Use:** Gemini 3.7 Flash for routine multi-breakpoint checks; use Gemini 3.1 Pro
for difficult art-direction/interaction critique.  
**Mode:** read-only/report-only for this pass.  
**Give it:** relevant source-of-truth files with `@`, the route/task goal, and
current local site.

### Paste this prompt

```text
/browser

Perform a read-only visual/browser QA review of:
<ROUTE OR ROUTES>

PROJECT GOAL
<PASTE THE TASK OUTCOME>

DO NOT EDIT APPLICATION FILES.

Inspect the actual running page at approximately:
320
375
390
430
768
1024
1280
1440
1920 px

Check:
- first-screen hierarchy
- Studio/Systems discoverability where relevant
- typography and line breaks
- spacing/rhythm
- image/media crop
- clipping/overflow
- touch targets
- hover/press/focus states
- navigation
- scroll behavior
- animation timing
- reduced-motion behavior
- content readability
- conversion clarity
- mobile composition
- obvious generic/template patterns
- loading/error states relevant to the task

For /:
prioritize memorable portfolio art direction without hiding the two divisions.

For /studio:
prioritize proof, differentiation and website-client conversion.

For /systems:
prioritize clarity, technical trust and enquiry conversion.

For /admin:
prioritize operational speed, privacy and low error risk.

RETURN
P0 BROKEN
P1 HIGH IMPACT
P2 POLISH
P3 OPTIONAL EXPERIMENT

For each item give:
- viewport
- exact location
- what you observed
- why it matters
- suggested outcome, not arbitrary implementation code

Also list WHAT ALREADY WORKS so the fixer does not damage it.
```

### What you check yourself

Open the page yourself at desktop and phone-sized width.

Do not accept “make everything animate more” as a valid finding.

### Pass to the next tool

Give **P0/P1 plus selected P2 findings** to DeepSeek. Keep Antigravity read-only.

---

# Phase I — DeepSeek fixes visual findings

### Paste this prompt

```text
You are the ONLY writer.

Here are the accepted Antigravity browser/visual findings.

Before changing code:
- verify every finding yourself in the current implementation
- preserve the approved task brief and code-review fixes

Fix accepted P0/P1 findings and only the P2 items explicitly selected.

RULES
- no unrelated redesign
- no new dependency unless already approved
- preserve responsive/accessibility/performance behavior
- mobile fixes must not break desktop and vice versa

After fixes run:
- relevant targeted checks
- npm run check:responsive when layout changed
- npm run check:a11y / check:keyboard when interaction changed
- npm run check:bundle / check:perf when motion/media/dependencies changed
- npm run verify at the end

Return:
- finding → fix mapping
- tests/results
- residual visual issues
```

### What you check yourself

Look at the final page again, not only test output.

---

# Phase J — final verification and documentation

**Where:** PowerShell in portfolio root.

```powershell
npm run verify
```

If it fails, do not commit. Use
[Troubleshooting](../reference/troubleshooting.md).

Then ask the writer for the final handoff.

### Paste this prompt

```text
Create the final concise handoff for this task.

First inspect the final diff and current project docs.

Update only documentation genuinely affected by this task.

HANDOFF MUST INCLUDE
- IST time
- UTC time
- machine: PC or laptop
- branch
- primary writer/model/harness
- task outcome
- files changed
- user-visible behavior
- tests/commands + final results
- visual/browser QA performed
- decisions made
- dependencies added/removed
- known issues
- next recommended task
- commit SHA if already committed, otherwise "not committed"

Do not repeat the entire project history.
```

### What you check yourself

- `npm run verify` is green.
- no secrets/private enquiry data in diff.
- docs match the final code.
- no blocker/high findings remain.
- you know what the next task is.

---

# Phase K — commit and push

**Where:** GitHub Desktop.

1. Review **Changes** one last time.
2. Write a clear outcome-based summary.
3. Commit.
4. Push.
5. Confirm the branch is on GitHub.

Do not merge a major task just because it has a commit; use your normal review
decision.

## When advanced motion is proposed

Do not let DeepSeek install GSAP/Lenis/WebGL by itself.

Use the approval flow in
[Track 5 — Quality and polish](05-quality-and-polish.md).

## Done when

- [ ] One branch had one coherent outcome.
- [ ] GLM planned.
- [ ] Gemini critiqued.
- [ ] GLM reconciled.
- [ ] DeepSeek was the one writer.
- [ ] Targeted checks passed.
- [ ] GLM reviewed code.
- [ ] DeepSeek fixed accepted findings.
- [ ] Antigravity inspected the actual page.
- [ ] DeepSeek fixed accepted visual findings.
- [ ] Final `npm run verify` passed.
- [ ] Docs/handoff reflect final state.
- [ ] You personally reviewed the final page and diff.
- [ ] Commit/push happened only after those checks.

## Next

→ [Track 5 — Quality and polish](05-quality-and-polish.md)
