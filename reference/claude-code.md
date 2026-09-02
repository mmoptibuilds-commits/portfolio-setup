# Claude Code

**What it is:** a terminal coding-agent harness.

**Why it exists here:** use your existing AgentRouter-backed Claude Code setup
as the main technical workspace for GLM planning/review and DeepSeek
implementation.

**Last verified:** 2026-09-02  
Official docs: <https://code.claude.com/docs>

## Install / verify — Windows PowerShell

```powershell
irm https://claude.ai/install.ps1 | iex
claude --version
claude doctor
```

`claude doctor` checks installation/settings health without starting a normal
coding session.

Official setup: <https://code.claude.com/docs/en/setup>

## Start it correctly

**Where:** PowerShell inside the portfolio folder.

```powershell
claude
```

Before meaningful work:

```text
/status
/context
```

Type `/` if you are unsure whether a command exists in your installed version.

> [!IMPORTANT]
> You use a third-party gateway. Features that depend on Anthropic account/model
> support may differ. Do not break a working AgentRouter profile just to match a
> screenshot from official Claude docs.

## The commands you actually need

| Command | Use it when |
|---|---|
| `/doctor` | Claude Code/install/config behaves strangely |
| `/status` | Check session/model/account state |
| `/usage` | Check usage if your current provider/config exposes it |
| `/plan` | Make a substantial change only after inspecting first |
| `/goal` | Continue autonomously until a **measurable** condition becomes true |
| `/loop` | Repeat a check while this Claude session remains open |
| `/run` | Launch/drive a project after the project recipe is configured |
| `/verify` | Verify the running result after the recipe is configured |
| `/run-skill-generator` | Teach `/run` and `/verify` the repo recipe if needed |
| `/diff` | Review changes before commit |
| `/review` or `/code-review` | Independent code/diff review |
| `/security-review` | Security-focused review of code changes |
| `/debug` | Diagnose a Claude/runtime problem |
| `/context` | See what is consuming the context window |
| `/compact` | Compress a long useful session |
| `/clear` | Start clean when the current task is over or polluted |
| `/resume` | Continue a previous session |
| `/rewind` | Restore a conversation/code checkpoint |
| `/permissions` | Inspect/change tool permissions |
| `/mcp` | Inspect MCP servers **only when you have configured one** |
| `/btw` | Ask a side question without derailing the main work |
| `/subtask` | Fork an isolated side investigation/background helper |
| `/batch` | Rare: split 5–30 genuinely independent units into worktrees |
| `/agents` | Discover/manage configured custom agents/subagents |

### `/goal`: use a finish line

Good:

```text
/goal Continue until npm run verify passes, the homepage has no horizontal
overflow at the required breakpoints, and every issue introduced by this task is
fixed. Do not change unrelated routes.
```

Bad:

```text
/goal Make the site world class.
```

The second prompt has no objective stop condition.

Official docs describe `/goal` as a persistent completion condition evaluated
after turns. Always make the condition testable.

### `/loop`: use it for repeated checks, not endless design

Good:

```text
/loop 5m Check whether the preview deployment has finished. If status changed,
summarize it. Do not edit code.
```

Good:

```text
/loop 10m Re-run the external availability check and report only a change.
```

Do not use:

```text
/loop Keep improving the homepage.
```

`/loop` works while the current session remains alive. It is a scheduler inside
the session, not a replacement for a task plan.

## Permissions: recommended setup

Claude Code permission modes include `default`, `acceptEdits`, `plan`,
`dontAsk`, `auto` (where available) and `bypassPermissions`.

For this project on your **normal Windows host**:

1. Use `/plan` or plan mode for architecture/read-only planning.
2. For implementation, prefer `acceptEdits` plus project allow/deny rules that
   let the agent read/edit the repo and run verification commands.
3. Keep deployment, secret access, force push, broad deletion and database
   destructive writes out of automatic allow rules.

> [!WARNING]
> Do **not** make `bypassPermissions` the normal Windows-host mode.
>
> Official Claude docs state that bypass mode should be used only in isolated
> environments such as containers/VMs. Native Windows does not provide Claude's
> sandbox. Bypass can write protected paths including `.git` and `.claude`.

If you intentionally create a disposable/snapshotted VM/WSL2 container:

```powershell
claude --permission-mode bypassPermissions
```

or the explicit legacy-style flag:

```powershell
claude --dangerously-skip-permissions
```

Use that only when the whole environment is disposable or otherwise contained.

Official permissions:
<https://code.claude.com/docs/en/permissions>

### Important AgentRouter note about `auto`

Do not make **auto mode** a dependency of this guide. Its availability depends
on the provider/account/model surface, and third-party gateway setups can differ.
A carefully scoped `acceptEdits`/allow-rule setup is the reliable base.

## Normal mmoptibuilds session

1. Pull/branch first.
2. Start Claude in the repo.
3. GLM reads the task-sized context and plans.
4. Paste Gemini's critique back to GLM.
5. Stop the planning session or hand off clearly.
6. DeepSeek becomes the **only writer**.
7. Run targeted checks during work.
8. Run `npm run verify`.
9. GLM reviews the diff read-only.
10. DeepSeek fixes confirmed findings.
11. Antigravity performs visual/browser QA.
12. Commit only after verification.

Use copy-paste prompts from
[Core workflow prompts](../prompts/core-workflow.md).

## Subagents

Use subagents for read-only reconnaissance, tests, research and diff review when
that keeps the main session smaller.

Example:

```text
Use a read-only reviewer subagent to inspect the current diff for accessibility
regressions. Return only evidence-backed findings. Do not edit files.
```

Use `/batch` only when independent work can be isolated by worktree. It is not a
faster homepage redesign button.

## Skills

Install skills when they solve a current task. The curated set is in
[UI, motion + skills](ui-motion-and-skills.md).

## MCP

Start with none. `/mcp` is for live external context/actions when a task proves
you need them. See [Subagents, MCP + hooks](subagents-mcp-and-hooks.md).

## Undo / recover

1. Use `/rewind` if the bad edit is in the current Claude checkpoint history.
2. Inspect `/diff`.
3. If needed, use Git to restore/revert specific files.
4. Never “fix” a confused session by force-resetting Git without understanding
   what would be deleted.

## Update / uninstall

Native Claude installs normally auto-update. Check:

```powershell
claude doctor
claude update
```

WinGet alternative:

```powershell
winget install Anthropic.ClaudeCode
winget upgrade Anthropic.ClaudeCode
```

## Next

Return to [Track 3 — First safe agent session](../tracks/03-first-safe-agent-session.md).
