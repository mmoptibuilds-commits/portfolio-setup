# Antigravity

**What it is:** Google's agent development environment with editor, terminal,
browser/visual tooling and autonomous agents.

**Why it exists here:** use it as the **home-base IDE and visual/browser QA
surface**, not as a second simultaneous writer competing with Claude Code.

**Last verified:** 2026-09-02  
Official docs: <https://antigravity.google/docs>

## Install — Windows

Desktop/IDE:
<https://antigravity.google/download>

Optional CLI, **PowerShell**:

```powershell
irm https://antigravity.google/cli/install.ps1 | iex
```

Verify CLI:

```powershell
agy --version
```

Official install:
<https://antigravity.google/docs/cli/install/>

## Recommended project layout

Open the portfolio folder as an Antigravity Project.

Normal workspace:

```text
Antigravity IDE
├── editor/browser
├── Terminal 1 → Claude Code writer/planner
├── Terminal 2 → normal PowerShell (dev server/tests)
└── native Antigravity agent → visual/browser/research review
```

The Antigravity native agent stays **read-only while DeepSeek is writing** unless
you intentionally give it a separate worktree.

## Local vs Worktree mode

- **Local Mode:** work directly in the project folder. Normal default.
- **New Worktree Mode:** Antigravity makes an isolated Git worktree. Use when an
  independent agent truly needs to edit in parallel.

Do not use Worktree Mode simply because it exists.

## High-value slash commands

| Command | Use it when |
|---|---|
| `/goal` | Give a bounded autonomous finish condition |
| `/plan` | Request a reviewable implementation plan before edits |
| `/grill-me` | Requirements/design are ambiguous and you want the agent to interview you |
| `/browser` | Live UI, browser research or visual QA needs the browser subagent |
| `/boost` | Paid deep reasoning for unusually hard debugging/refactoring—not normal work |
| `/teamwork-preview` | Rare repo-scale independent tracks; not normal portfolio iteration |
| `/learn` | Save a repeated correction/pattern into durable customization |
| `/btw` | Ask a side question |
| `/schedule` | Scheduled maintenance/checks, not feature implementation |
| `/permissions` | Review autonomy/security behavior |
| `/agents` | Manage/inspect agents where the surface exposes it |
| `/resume` | Resume a session |
| `/rewind` | Return to an earlier checkpoint |
| `/rename` | Give an important session a useful name |
| `/model` | Select the reasoning model in Antigravity CLI |
| `/diff` | Inspect changes in Antigravity CLI |
| `/mcp` | Open the MCP manager in Antigravity CLI |

Official command/features reference:
<https://antigravity.google/docs/cli/features/>

## `@` references — use them to narrow context

In Antigravity CLI, typing `@` in the prompt opens path suggestions. Select a
file/path instead of vaguely saying “look around the repo.”

Example:

```text
Review @app/(gateway)/page.tsx and @app/globals.css for the approved homepage
hierarchy task. Read-only first.
```

In Antigravity workspace **Rules**, `@filename` can also reference another rule
or file. Use that for durable project instructions only when it keeps a rule
small.

Use `@` for:
- exact files;
- exact rule/context files;
- reducing unnecessary repo-wide search.

Do not attach ten directories when two files answer the question.

Official best practices:
<https://antigravity.google/docs/cli/best-practices/>

## Model choice

Use **Gemini 3.1 Pro** for:

- final design critique;
- screenshot/reference comparison;
- route-wide visual consistency;
- browser QA;
- difficult multimodal reasoning.

Use a faster Gemini model for cheap iterations when Pro reasoning is not needed.

Do not spend the strongest model on renaming files or trivial copy edits.

## Permissions

For a trusted project folder, Antigravity can run with high terminal autonomy.

Recommended principle:

- **Inside the project folder:** allow normal code/test commands.
- **Outside the project folder:** deny by default.
- **Secrets/destructive commands/deployment:** require deliberate action.
- **Parallel agent edits:** use Worktree Mode.

Antigravity Project Settings include terminal execution policy, outside-folder
file policy and sandbox options. Review them rather than clicking “allow
everything everywhere.”

Settings docs:
<https://antigravity.google/docs/settings>

## Browser QA prompt pattern

Use `/browser`, then:

```text
Review the running mmoptibuilds site at localhost.

Do not edit code yet.

Check /, /studio, /systems and the relevant changed route at:
320, 375, 768, 1024 and 1440 CSS pixels.

Inspect:
- visual hierarchy
- Studio/Systems discoverability
- touch targets
- horizontal overflow
- text clipping
- focus visibility
- reduced-motion behavior
- loading/layout shifts
- confusing or decorative-only interaction
- conversion clarity

Return:
1. critical blockers
2. high-value improvements
3. optional polish

For every finding give route, viewport, evidence and exact expected behavior.
Do not suggest a visual effect without explaining what user/design problem it solves.
```

More prompts:
[Visual + quality prompts](../prompts/visual-and-quality.md).

## MCP

Antigravity has a built-in MCP Store.

IDE path:

1. Agent side panel → `…`
2. **MCP Servers**
3. Install from the store, or **Manage MCP Servers → View raw config** for a
   custom server.

Workspace config can live under `.agents/mcp_config.json`; global config under
`~/.gemini/config/mcp_config.json`.

Start with **zero mandatory MCP servers**. See
[Subagents, MCP + hooks](subagents-mcp-and-hooks.md).

Official MCP docs:
<https://antigravity.google/docs/mcp>

## When Antigravity should edit

Good:

- isolated visual fix after its review;
- an explicitly assigned route in a worktree;
- asset/reference experiments outside the primary writer's file set.

Bad:

- DeepSeek is currently editing the homepage and Antigravity also starts
  “improving” it in Local Mode.

## Undo

Use session rewind/diff first. If a separate worktree experiment is not useful,
do not merge it. Never let “autonomous” mean “unreviewed production deploy.”

## Next

Return to [Track 3](../tracks/03-first-safe-agent-session.md).
