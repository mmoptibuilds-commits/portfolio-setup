# Track 3 — First safe agent session

**Goal:** Run the complete planning handoff once without allowing competing
agents to edit the repository.

This track teaches the exact handoff. Track 4 is the reusable version you use
for real implementation.

## Before you start

**GitHub Desktop**

1. Pull `main`.
2. Create a branch for the next milestone, for example:
   `feat/gateway-art-direction`.
3. Confirm the working tree is clean before agents edit.

**Antigravity**

Open the SAME local branch/folder as the Project.

**Terminals**

```text
Terminal A → npm run dev
Terminal B → claude
```

Do not start OpenCode as another writer.

## 1. Clarify the goal if you are unsure

If **you cannot clearly describe the feature yet**, use Antigravity first.

**Open:** Antigravity agent on the portfolio Project.  
**Mode:** Local, but tell it read-only.  
**Use:** Gemini 3.1 Pro.  
**Give it:** `@README.md`, `@AGENTS.md`, `@DESIGN.md`,
`@docs/PROJECT-BRIEF.md`, `@docs/PROJECT-STATE.md` if those files exist.

### Paste this prompt

```text
/grill-me

I need to define the next portfolio milestone before anyone edits code.

CURRENT IDEA
<DESCRIBE WHAT YOU WANT IN NORMAL WORDS>

PROJECT GOALS
- / = memorable portfolio/brand gateway; Studio + Systems obvious
- /studio = distinctive website-client conversion
- /systems = technical trust + hardware enquiry conversion
- /admin = fast owner operations
- mobile, accessibility, performance and truthful proof are mandatory

READ the attached/current project source-of-truth files.

Ask me only questions that materially affect:
- page goal
- hierarchy
- content
- interaction/motion
- responsive behavior
- conversion
- accessibility
- performance
- implementation scope

Do not edit files.
When the requirements are clear, return a short TASK DEFINITION containing:
OUTCOME
ROUTE
MUST PRESERVE
MUST CHANGE
SUCCESS CONDITIONS
OUT OF SCOPE
```

### What you check yourself

The task definition must be one coherent milestone, not “redo everything.”

### Pass to the next tool

Copy **only `TASK DEFINITION`** into GLM in the next step.

If your task was already clear, skip `/grill-me` and write the task definition
yourself.

## 2. GLM creates the technical plan

**Open:** Terminal B → Claude Code in portfolio root.  
**Use:** GLM-5.3.  
**Permission:** read-only/plan.  
**Give it:**

- task definition;
- `README.md`;
- `AGENTS.md`;
- compact source-of-truth docs;
- only relevant code.

### Paste this prompt

```text
ROLE
You are the senior technical planner for the existing mmoptibuilds portfolio.

TASK DEFINITION
<PASTE THE TASK DEFINITION HERE>

READ FIRST
- README.md
- AGENTS.md
- docs/PROJECT-BRIEF.md if present
- docs/PROJECT-STATE.md if present
- docs/ROADMAP.md if present
- DESIGN.md if present
- only source files relevant to this task

RULES
- Do not edit.
- Preserve the existing engineering foundation.
- Do not redesign unrelated routes.
- Do not install dependencies.
- A dependency may be proposed only with a concrete reason.
- Respect all documented codebase traps.
- Keep mobile, accessibility, performance, SEO and truthful content as floors.
- npm run verify is the final project gate.

RETURN ONE IMPLEMENTATION PLAN
1. Desired user/business outcome.
2. Current behavior/evidence.
3. Exact files the writer may edit.
4. Exact files that are read-only context.
5. Ordered implementation steps.
6. Responsive/mobile behavior.
7. Accessibility/reduced-motion/no-JS requirements.
8. Performance/bundle requirements.
9. Whether any dependency is needed and why.
10. Targeted checks after each logical part.
11. Final success conditions.
12. Explicit out-of-scope items.
13. Risks that require owner choice.

Do not write implementation code.
```

### What you check yourself

Before continuing:

- Are owned files specific?
- Is the task bounded?
- Are mobile and accessibility included?
- Is `npm run verify` included?
- Did GLM avoid unrelated refactors?

### Pass to the next tool

Copy the **whole final GLM plan** to Gemini.

## 3. Gemini critiques the plan

**Open:** Gemini App, not the coding terminal.  
**Use:** Gemini 3.1 Pro Extended/strongest appropriate Pro mode.  
**Give it:**

- GLM plan;
- `PROJECT-BRIEF.md` and `DESIGN.md` if available;
- screenshots of the affected route;
- visual references only if they represent the direction you want.

Do not upload `.env.local`, customer data, or the whole Git repo.

### Paste this prompt

```text
You are the independent product, visual-design, UX, conversion and technical
critic for mmoptibuilds.

I am giving you:
1. the GLM implementation plan
2. the project brief/design rules
3. screenshots/references when relevant

ROUTE GOALS
- / = memorable, authored portfolio/brand experience with obvious Studio + Systems entry
- /studio = credible proof + differentiation + website-client conversion
- /systems = technical credibility + requirement-led conversion
- /admin = operational clarity, not visual spectacle

NON-NEGOTIABLES
- mobile is designed intentionally, not simply stacked
- accessible keyboard/reduced-motion behavior
- performance remains strong
- no invented clients, awards, metrics, stock or prices
- preserve useful current architecture
- avoid generic AI-template aesthetics
- advanced effects must have a named purpose

CRITIQUE THE PLAN, NOT THE AUTHOR.

RETURN
KEEP
CHANGE
DELETE
MISSING
RISKS
RECOMMENDED DIRECTION

For every CHANGE/MISSING item, explain why it matters.
Keep this within the current task. Do not redesign unrelated routes.

GLM PLAN:
<PASTE GLM PLAN>
```

### What you check yourself

Reject Gemini suggestions that:

- hide Studio/Systems access;
- add spectacle without benefit;
- invent proof;
- ignore mobile;
- require giant unrelated rewrites.

### Pass to the next tool

Copy **Gemini's complete critique** back to the same GLM Claude session.

## 4. GLM reconciles

### Paste this prompt

```text
Reconcile the Gemini critique below with the repository and your original plan.

For each meaningful Gemini suggestion mark:
- ACCEPT
- MODIFY
- REJECT

Give one short evidence-based reason.

Then return one FINAL IMPLEMENTATION BRIEF containing:
- outcome
- owned files
- read-only files
- exact implementation order
- dependency decision
- responsive/mobile requirements
- accessibility/reduced-motion/no-JS requirements
- performance/bundle requirements
- content/conversion requirements
- targeted checks
- final npm run verify requirement
- documentation/handoff files to update
- explicit exclusions

Do not edit files.

GEMINI CRITIQUE:
<PASTE GEMINI CRITIQUE>
```

### What you check yourself

This final brief—not Gemini's raw critique—is what the writer follows.

### Pass to the next tool

Save/copy the **FINAL IMPLEMENTATION BRIEF**. Track 4 starts from that brief.

## 5. Name the writer

Put this in your task notes:

```text
PRIMARY WRITER: DeepSeek V4 Flash in Claude Code
READ-ONLY REVIEWER: GLM-5.3
VISUAL REVIEWER: Gemini in Antigravity
SUPPORT/SECONDARY: OpenCode only when explicitly assigned
PARALLEL WRITERS: none
```

## `/goal` and `/loop`

Use `/goal` only after the brief has measurable completion conditions.

Good:

```text
/goal Continue until the approved task is implemented, its targeted checks pass,
npm run verify passes, and no files outside the approved scope are modified.
```

Use `/loop` for repeated checking, not creative iteration.

Good:

```text
/loop 5m Check the preview/deployment status. Report only when it changes. Do not modify code.
```

## Permissions

On a normal Windows host, prefer high autonomy inside the repo plus deny rules.
Read [Claude Code](../reference/claude-code.md) before using raw
`bypassPermissions`.

## Done when

- [ ] The task is clear.
- [ ] GLM produced a bounded technical plan.
- [ ] Gemini critiqued it.
- [ ] GLM reconciled the critique.
- [ ] You personally checked the final brief.
- [ ] One writer is named.
- [ ] No code has been changed by competing agents.

## Next

→ [Track 4 — Design and build loop](04-design-and-build-loop.md)
