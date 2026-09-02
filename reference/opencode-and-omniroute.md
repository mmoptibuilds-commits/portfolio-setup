# OpenCode + OmniRoute

This is the **support/free-model path**. It is not the primary writer path.

```text
OpenCode → OmniRoute → selected free/support provider/model
```

Do not put AgentRouter Claude Code, Antigravity or the Gemini app behind
OmniRoute just to make one giant router.

## OpenCode

**What it is:** an open-source coding-agent harness.

Use it for:

- Markdown/docs work;
- independent read-only review;
- cheap test ideas;
- research summaries;
- isolated small tasks;
- benchmarking free models.

**Last verified:** 2026-09-02  
Docs: <https://opencode.ai/docs/>

### Install — Windows

The OpenCode docs recommend WSL as the smoothest Windows path, but npm also
works when your Windows Node environment is healthy.

**PowerShell:**

```powershell
npm install -g opencode-ai
opencode --version
```

Start inside the portfolio:

```powershell
opencode
```

Useful commands:

| Command | Use |
|---|---|
| `/connect` | connect/configure a provider |
| `/models` | inspect/select models |
| `/init` | create agent instructions only if you intentionally need it |
| `/compact` | reduce context |
| `/new` | clean session |
| `/sessions` | switch/resume sessions |
| `/undo` | undo session/file changes |
| `/redo` | reapply undone changes |
| `/help` | current command list |
| `@file` | attach a specific file |
| `!command` | run a safe shell command and attach output |

> [!CAUTION]
> Do not run `/init` over a carefully curated `AGENTS.md` without reading the
> diff. Project instructions are an authority file, not generated boilerplate.

### Permissioned reviewer agent

OpenCode supports allow/ask/deny permissions. A reviewer should be read-only or
nearly read-only.

Example intent:

```text
Review the current diff. You may read files and run read-only Git/test
inspection. Do not edit application files, install packages or deploy.
```

### Custom commands

OpenCode supports project commands in `.opencode/commands/*.md`. Create them
only after you repeat a workflow enough to justify it.

Useful eventual names:

- `/review-diff`
- `/review-md`
- `/handoff`
- `/small-task`

Do not create 30 custom commands on day one.

## OmniRoute

**What it is:** a local OpenAI-compatible multi-provider router.

Use it to give OpenCode a controlled support pool.

**PowerShell:**

```powershell
npm install -g omniroute
omniroute
```

Default local dashboard is commonly:
<http://localhost:20128>

Project:
<https://github.com/diegosouzapw/OmniRoute>

Check the current repo/docs before relying on exact provider fields because
provider APIs and free tiers change.

## Use purpose-specific pools

Do not create one random “free” roulette pool for serious code.

Recommended logical pools:

```text
free-fast
  summaries, logs, docs, simple test ideas

free-code
  proven coding models only

free-reason
  architecture critique, debugging, read-only review

free-long-context
  only models/providers whose actual current context is verified
```

Populate each with a **small** set of models that currently work for you.

## Benchmark before promotion

Give a free model a real isolated task:

1. Read the same few files as a trusted reviewer.
2. Find issues.
3. Compare findings against GLM/Gemini.
4. Give it one small implementation on a branch/worktree.
5. Run the project's real checks.
6. Promote it only to the pool where it proved useful.

Provider quotas change. Do not hard-code a promise that a free provider is
“unlimited.”

## MCP in OpenCode

Add only when needed:

```powershell
opencode mcp add
opencode mcp list
```

MCP servers consume context. OpenCode's own docs explicitly warn against
enabling large tool catalogs without need.

Official MCP docs:
<https://opencode.ai/docs/mcp-servers/>

## When NOT to use OpenCode

- primary homepage writer while Claude/DeepSeek is writing;
- production database administration;
- a second model editing the same files;
- tasks where the free model has not proven reliable.

## Next

Use it during [Track 8 — Maintenance](../tracks/08-maintenance.md) or as an
independent reviewer when a prior track explicitly calls for it.
