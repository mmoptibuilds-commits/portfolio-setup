# Beginner Operating Playbook Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn this repository into a complete but non-overwhelming beginner operating guide for finishing, polishing, testing, deploying, and maintaining the existing mmoptibuilds Yin-Yang portfolio.

**Architecture:** Keep `README.md` as the only required entry point. Put the chronological build journey in eight `tracks/` files, deeper explanations in focused `reference/` files, and copy-paste agent prompts in a small `prompts/` library. Add one dependency-free guide checker so the documentation can verify itself without creating a toolchain.

**Tech Stack:** GitHub Markdown, Mermaid, Python 3 standard library for guide checks, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-02-portfolio-setup-guide-design.md`

## Global Constraints

- Windows 11 + PowerShell is the primary beginner path.
- The portfolio is `mmoptibuilds-commits/mmoptibuilds-portfolio-yin-yang`; improve it, do not rebuild it from scratch.
- No new paid services are required.
- The main page may be highly art-directed; `/studio` and `/systems` remain clear, conversion-ready, responsive, accessible, and SEO-focused; `/admin` stays operational and restrained.
- One writer owns the main working tree at a time.
- Opus and Sol are optional bonuses, never dependencies.
- GLM-5.3 plans/reviews; Gemini 3.1 Pro critiques and handles multimodal/visual work; DeepSeek V4 Flash is the default implementation worker; OpenCode + OmniRoute is the support/free-model path.
- Advanced dependencies, MCP servers, hooks, subagents, GSAP, Lenis, WebGL, Strix, and parallel worktrees appear only when a task needs them.
- Every technical term is explained at first practical use or linked to the glossary.
- Every track must tell the reader exactly what to do next.
- Commands that change over time carry a `Last verified: 2026-09-02` note and an authoritative source.
- Never place credentials, API keys, personal inquiry data, or production secrets in the guide.

---

### Task 1: Build the beginner entry path

**Files:**
- Create: `README.md`
- Create: `tracks/01-first-time-setup.md`
- Create: `tracks/02-open-and-understand-project.md`
- Create: `reference/glossary.md`
- Create: `reference/git-and-github-desktop.md`

**Interfaces:**
- Consumes: approved design spec and current portfolio README/package scripts.
- Produces: the only mandatory entry path and vocabulary used by every later page.

- [ ] Create a short dashboard README with a visible “YOU ARE HERE” sequence and no reference dump.
- [ ] Teach installation and verification of Git, GitHub Desktop, Node.js, Antigravity, and Claude Code using PowerShell-first steps.
- [ ] Teach clone/open/pull/commit/push and explain repo, branch, commit, push, pull, and working tree in plain English.
- [ ] Teach the current portfolio structure and real `npm run verify` command.
- [ ] Add a glossary for terminology that cannot be explained comfortably inline.
- [ ] Verify every relative link in this first path.

### Task 2: Teach the safe AI working environment

**Files:**
- Create: `tracks/03-first-safe-agent-session.md`
- Create: `reference/claude-code.md`
- Create: `reference/antigravity.md`
- Create: `reference/models-and-routing.md`
- Create: `prompts/core-workflow.md`

**Interfaces:**
- Consumes: Task 1 clone/open state.
- Produces: repeatable GLM → Gemini → GLM → DeepSeek workflow and safe autonomy rules.

- [ ] Explain where Claude Code and Antigravity run and how AgentRouter-backed Claude sessions differ from Google Antigravity/Gemini sessions.
- [ ] Teach only useful slash commands, including `/goal`, `/loop`, `/plan`, `/review`, `/verify`, `/doctor`, `/context`, `/compact`, `/resume`, `/permissions`, `/browser`, and related commands when actually needed.
- [ ] Document high-autonomy configuration without making host-machine `bypassPermissions` the default.
- [ ] Add exact planning, critique, reconciliation, implementation, verification, review, fix, and visual-QA prompts.
- [ ] Make “one writer at a time” concrete with a handoff checklist.

### Task 3: Teach the normal design/build loop

**Files:**
- Create: `tracks/04-design-and-build-loop.md`
- Create: `tracks/05-quality-and-polish.md`
- Create: `reference/ui-motion-and-skills.md`
- Create: `reference/playwright-and-context7.md`
- Create: `reference/subagents-mcp-and-hooks.md`
- Create: `prompts/visual-and-quality.md`

**Interfaces:**
- Consumes: safe session workflow from Task 2.
- Produces: day-to-day build/polish loop with conditional advanced tooling.

- [ ] Explain homepage vs Studio vs Systems vs Admin goals before design prompts.
- [ ] Explain when CSS is enough and when GSAP, Lenis, WebGL, frame sequences, or shaders earn their cost.
- [ ] Teach approved skills as a small core plus just-in-time optional skills; do not install everything.
- [ ] Teach Playwright CLI and Context7 as preferred low-context utilities.
- [ ] Teach subagents, MCP, hooks, `/batch`, and worktrees only for cases that benefit from isolation or deterministic automation.
- [ ] Add exact prompts for visual, responsive, accessibility, motion, performance, Studio conversion, Systems conversion, and admin UX reviews.

### Task 4: Teach backend, admin, database, and hosting

**Files:**
- Create: `tracks/06-backend-admin-and-data.md`
- Create: `reference/supabase-backend-and-admin.md`
- Create: `reference/hosting-cloudflare-and-domain.md`

**Interfaces:**
- Consumes: actual enquiry/admin architecture from the portfolio repository.
- Produces: beginner-safe path from local file storage to Supabase and Cloudflare without forcing migration.

- [ ] Explain frontend, backend, database, auth, environment variable, secret, domain, DNS, hosting, and deployment visually and in plain English.
- [ ] Document current local `.enquiries` fallback and when Supabase becomes necessary.
- [ ] Teach safe `.env.local`, Supabase linking/migrations, owner-account setup, and admin verification without committing secrets.
- [ ] Preserve OpenNext for the existing portfolio; note current Cloudflare vinext recommendation for new projects and make migration optional/separate.
- [ ] Teach preview, production, DNS, smoke-test, and rollback concepts before deployment commands.

### Task 5: Teach launch-quality SEO and security

**Files:**
- Create: `tracks/07-seo-security-and-launch.md`
- Create: `reference/security-and-strix.md`
- Create: `prompts/seo-security-launch.md`

**Interfaces:**
- Consumes: working site, backend, and deployment knowledge.
- Produces: evidence-based launch gate.

- [ ] Teach technical SEO using the existing typed content, metadata, sitemap, robots, canonical, structured-data, and route model.
- [ ] Teach security review from least invasive to Strix; keep Strix optional and scoped only to owned/authorized targets.
- [ ] Teach privacy/truth/legal blockers without generating fake legal certainty.
- [ ] Add SEO audit/fix, security review/fix, deployment-prep, and launch prompts.
- [ ] Require `npm run verify` plus manual visual/content checks before production.

### Task 6: Teach maintenance, support tools, and recovery

**Files:**
- Create: `tracks/08-maintenance.md`
- Create: `reference/opencode-and-omniroute.md`
- Create: `reference/troubleshooting.md`
- Create: `prompts/support-and-recovery.md`

**Interfaces:**
- Consumes: completed launch workflow.
- Produces: sustainable post-launch operating loop and low-cost support path.

- [ ] Teach OpenCode + OmniRoute only as the support/free-model path, with explicit models/pools rather than random routing.
- [ ] Teach a lightweight real-task benchmark before promoting a free model to coding work.
- [ ] Teach PC ↔ GitHub ↔ laptop handoff and explicitly forbid syncing `.git` with Syncthing.
- [ ] Cover failed build, stale dev server, bad agent edit, Git mistake, merge conflict, quota/provider outage, and secret-exposure recovery.
- [ ] Provide weekly/monthly/quarterly maintenance checklists without turning them into bureaucracy.

### Task 7: Add self-verification and CI

**Files:**
- Create: `scripts/check-guide.py`
- Create: `.github/workflows/guide-check.yml`

**Interfaces:**
- Consumes: all guide files.
- Produces: deterministic post-commit checks with no third-party dependency.

- [ ] Verify required files exist.
- [ ] Reject unresolved merge markers and placeholder tokens such as `TBD`/`TODO` outside the design/plan archive.
- [ ] Validate relative Markdown links and anchors to files.
- [ ] Check fenced code blocks are balanced.
- [ ] Check every track contains a `## Next` section.
- [ ] Run the checker in GitHub Actions on pushes and pull requests.

### Task 8: Final review and evidence

**Files:** all new guide files.

**Interfaces:**
- Consumes: Tasks 1–7.
- Produces: reviewable committed guide branch.

- [ ] Scan the complete guide against every section of the approved design spec.
- [ ] Remove repeated explanations, fake certainty, obsolete model labels, and generic AI prose.
- [ ] Confirm every command says where it is typed and dangerous commands include a warning.
- [ ] Confirm README exposes one recommended path rather than all options.
- [ ] Commit the completed guide.
- [ ] After the commit, retrieve the committed tree/diff, run/inspect the guide-check workflow, and re-fetch key files to prove the committed state matches the reviewed state.
