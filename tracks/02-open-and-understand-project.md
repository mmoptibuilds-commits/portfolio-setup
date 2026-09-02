# Track 2 — Open and understand the existing project

**Goal:** Know what already works before asking an AI to change anything.

You do **not** need to understand the code line by line.

## 1. Pull the newest version

**Where:** GitHub Desktop.

1. Open `mmoptibuilds-portfolio-yin-yang`.
2. Click **Fetch origin**.
3. Click **Pull origin** if it appears.
4. Confirm the current branch is `main` before inspecting the baseline.

## 2. Open the repository in Antigravity

**Where:** Antigravity desktop/IDE.

1. Create/open a Project.
2. Add the cloned portfolio folder.
3. Choose **Local** mode for normal inspection.
4. Open the integrated terminal.

Do not ask the Antigravity agent to edit anything yet.

## 3. Read only these two files first

**Where:** Antigravity editor.

1. `README.md`
2. `AGENTS.md`

Why:

- `README.md` tells you how this specific project runs and verifies.
- `AGENTS.md` records traps that previous agents already discovered.

The existing repo already documents several costly mistakes: shipping Zod into
client bundles, breaking division token inheritance, making below-fold content
invisible without JavaScript, changing form-validation order, and reintroducing
unnecessary animation/dialog libraries.

## 4. Understand the project map

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

A **typed content model** means important page copy/data lives in structured
TypeScript objects rather than being scattered through arbitrary markup.

## 5. Run the site

**Where:** Antigravity integrated PowerShell terminal, in the project root.

```powershell
npm run dev
```

Open:

- <http://localhost:3000/>
- <http://localhost:3000/studio>
- <http://localhost:3000/systems>
- <http://localhost:3000/admin>

For local admin behavior, the repo's `.env.example` explains the supported
development variables. Never paste real production secrets into an AI prompt.

## 6. Know what is already verified

The project currently exposes:

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

**Fast checks** are useful during a task.  
**`npm run verify`** is the full end-of-task/milestone gate.

## 7. Understand the current design constraint

The project currently uses CSS for its motion and deliberately has **no GSAP,
Lenis, WebGL or custom cursor**. This is not a permanent ban.

It means:

> Add an advanced effect only after you can name the user/design benefit and
> prove the result is still accessible, mobile-safe and within performance
> budgets.

See [UI, motion + skills](../reference/ui-motion-and-skills.md) when you reach a
task that may justify an advanced effect.

## 8. Give agents durable project context

`roadmap.mmoptibuilds.com` is useful for you as a visual companion, but it is
not enough as the only agent source of truth.

Use the committed repository instructions first. The eventual compact source
layer is explained in
[Project source of truth](../reference/project-source-of-truth.md).

## First inspection prompt

**Use:** GLM-5.3 in Claude Code.  
**Where:** Claude Code started inside the portfolio folder.  
**Mode:** read-only planning; do not edit.

Copy the **Repo Audit** prompt from
[Core workflow prompts](../prompts/core-workflow.md).

## Done when

- [ ] You pulled the newest `main`.
- [ ] You opened the correct folder in Antigravity.
- [ ] You read `README.md` and `AGENTS.md`.
- [ ] You can point to gateway, Studio, Systems and admin folders.
- [ ] The local site opens.
- [ ] You know `npm run verify` is the main gate.
- [ ] You have not installed new visual dependencies “just in case.”

## Next

→ [Track 3 — First safe agent session](03-first-safe-agent-session.md)
