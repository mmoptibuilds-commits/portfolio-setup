# Subagents, MCP + hooks

These features are useful because they solve specific problems. They are not a
setup checklist.

## Subagents

A **subagent** is a helper agent that gets a smaller task and returns the result
to the main agent.

### Use a subagent for

- codebase reconnaissance;
- running a long test suite and returning only failures;
- independent diff review;
- accessibility/performance research;
- current documentation lookup;
- parallel **read-only** analysis.

### Do not use one for

- every task;
- overlapping edits to the same files;
- hiding an unclear plan behind “multi-agent” complexity.

### Claude example

```text
Use a read-only subagent to inspect the current homepage diff for keyboard,
reduced-motion and no-JS regressions. Do not edit. Return only evidence-backed
findings with exact file locations.
```

Use `/subtask` for an isolated forked helper where supported.

Use `/batch` only for genuinely independent repo-scale units. Claude's batch
flow can isolate work in worktrees; that is useful for independent migrations,
not two redesign agents fighting over `page.tsx`.

## Worktrees

A **worktree** is a second folder attached to another branch.

Rule:

> If two agents write at the same time, they must own non-overlapping work in
> separate worktrees.

Antigravity's native **New Worktree Mode** is the easiest visual route when
Antigravity coordinates the isolated task.

## MCP

**Model Context Protocol** is a standard bridge that lets an AI harness access a
live external tool/service.

Example: instead of copying a database schema into chat, a read-only Supabase
MCP could expose current schema metadata.

### Start with zero mandatory MCP servers

Why:

- MCP tools consume context.
- Extra tools increase permission/security surface.
- GitHub-style MCP servers can expose large tool catalogs.
- Native repo tools, Playwright and Context7 already cover many needs.

### Add MCP only when the answer is yes

> “Does this task need live context/actions that are awkward or impossible with
> the tools we already have?”

Possible later cases:

- Supabase schema inspection;
- Cloudflare logs/deployment diagnostics;
- GitHub issue/PR automation from a harness;
- Sentry after Sentry actually exists;
- Figma only if the design workflow uses Figma.

### Claude Code

Inside Claude, `/mcp` shows configured MCP state. Use current official setup
instructions for the specific server and keep workspace scope when practical.

Official MCP docs index:
<https://code.claude.com/docs>

### Antigravity IDE

1. Agent side panel → `…`
2. **MCP Servers**
3. Install from the built-in store, or:
4. **Manage MCP Servers → View raw config**

Workspace config:
`.agents/mcp_config.json`

Global config:
`~/.gemini/config/mcp_config.json`

Official:
<https://antigravity.google/docs/mcp>

### OpenCode

Interactive terminal setup:

```powershell
opencode mcp add
opencode mcp list
```

Or configure `mcp` in `opencode.jsonc`.

Official:
<https://opencode.ai/docs/mcp-servers/>

> [!CAUTION]
> Do not put literal API tokens in committed MCP config. Use the provider's
> environment/OAuth mechanism.

## Hooks

A **hook** is deterministic automation triggered by an agent event.

Good hook jobs:

- warn at session start which source-of-truth files matter;
- block dangerous shell patterns;
- run a narrow formatter/lint after relevant edits;
- require verification/handoff before a meaningful task completes.

Bad hook jobs:

- launch another AI reviewer after every keystroke;
- block a typo fix because six docs were not updated;
- auto-deploy production;
- hide destructive behavior inside scripts you do not understand.

### Suggested progression

1. Work without custom hooks until the workflow is stable.
2. Notice a repeated deterministic mistake.
3. Add one hook for that mistake.
4. Test it on a branch.
5. Document how to disable it.

Antigravity plugins can include `hooks.json`. Claude Code exposes hook events in
its settings system. Do not copy hook config from the internet without reading
the exact command it will run.

## Next

Return to [Track 4](../tracks/04-design-and-build-loop.md).
