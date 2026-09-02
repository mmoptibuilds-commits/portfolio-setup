# Project source of truth

## Is `roadmap.mmoptibuilds.com` enough to give an agent?

**No.** It is useful human context, but an agent working on code needs a stable
versioned snapshot inside the repository.

A web page can change, fail to load or be unavailable to a harness. A committed
Markdown file travels with the exact code revision.

## Authority order

Use this order when information conflicts:

1. Your newest explicit instruction for the current task.
2. Current committed decisions/instructions in the portfolio repo.
3. The task brief and acceptance criteria.
4. The roadmap/manual as supporting context.
5. Old chats/transcripts only when current files do not answer the question.

## Compact layer to maintain in the portfolio

Do not build another 30-file manual inside the source repo. Keep this layer
small:

```text
README.md
AGENTS.md
CLAUDE.md
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
    └── YYYY-MM.md
```

Not every file must exist before the next code task. Add/update them as the
workflow reaches the relevant subject.

## What to give an agent for one task

Do **not** paste the whole history.

```text
TASK
What outcome should exist when finished?

READ FIRST
Exact relevant repo docs and code paths.

OWNED FILES
Which files may this agent edit?

DO NOT
Things it must preserve or avoid.

SUCCESS CONDITIONS
Observable behavior and quality gates.

VERIFY
Exact commands.

HANDOFF
Files changed, tests run, risks, next action.
```

This is **task-sized context**: enough to be correct, not enough to bury the
model.

## Session handoff record

For meaningful sessions, record:

```text
Time: IST + UTC
Machine: PC / laptop
Harness: Claude Code / Antigravity / OpenCode
Model:
Role:
Task:
Files changed:
Commands/tests:
Result:
Known issues:
Next action:
Commit:
```

A typo does not need a formal handoff. A homepage redesign or database change
does.

## Next

Return to [Track 2](../tracks/02-open-and-understand-project.md) or the task that
linked you here.
