# Playwright + Context7

These are two high-value utilities because they reduce guessing without adding a
large permanent agent context.

## Playwright CLI

**What it is:** browser automation from the terminal.

Use it for:

- opening the local site;
- clicking through flows;
- checking browser-visible behavior;
- screenshots;
- reproducible UI verification.

**Last verified:** 2026-09-02.

Install globally, **PowerShell**:

```powershell
npm install -g @playwright/cli@latest
playwright-cli --help
playwright-cli install --skills
```

Official project/docs:
<https://github.com/microsoft/playwright-cli>

The portfolio also already has `@playwright/test` and custom browser scripts.
Do not replace the repo's `npm run verify` with ad-hoc Playwright commands.
Playwright CLI is a helper during diagnosis and visual investigation.

## Context7 CLI

**What it is:** a tool that retrieves current library documentation for agents
and developers.

Use it when:

- Next.js/GSAP/Lenis/Supabase/Cloudflare APIs may have changed;
- the model is uncertain about a library;
- you are about to use an API based only on model memory.

Prefer CLI/skill use before adding a permanent MCP server.

**PowerShell:**

```powershell
npx ctx7@latest library nextjs "Server Actions current guidance"
```

Then use the returned library ID:

```powershell
npx ctx7@latest docs <LIBRARY_ID> "Server Actions forms validation"
```

Optional install:

```powershell
npm install -g ctx7
```

Official project:
<https://github.com/upstash/context7>

## When to use Context7 in the pipeline

Good:

> DeepSeek is about to add GSAP ScrollTrigger → retrieve current GSAP React
> cleanup/integration guidance first.

Unnecessary:

> Change one line of local CSS → no external docs needed.

## No MCP by default

Both tools can already provide useful context without permanently exposing a
large MCP tool catalog to every session.

## Next

Return to the track that linked here.
