# Support + recovery prompts

## Failed build / `npm run verify`

```text
ROLE
Systematic debugger.

TASK
Diagnose the current npm run verify failure.

RULES
- Do not change code until you identify which gate failed.
- Read the exact failing output.
- Check whether the failure reproduces with the narrow gate.
- Read README.md and AGENTS.md for known Windows/verification traps.
- Distinguish stale server/environment failure from an application regression.
- Do not weaken or delete a quality gate to get green.

RETURN
1. failing gate
2. minimal reproduction command
3. likely cause ranked by evidence
4. exact files/processes involved
5. smallest repair
6. how to prove the repair
```

## Stale Windows dev/prod server

```text
The verification/browser result looks like stale Next.js assets or a port is
already occupied.

Inspect current listening Node processes and the repo's Windows verification
logic. Do not delete build output or reset Git until the process issue is ruled
out.

Explain what process is serving the port and propose the least destructive way
to stop only the relevant process tree.
```

The current repo's `AGENTS.md` already documents a Windows shell-spawned server
trap. Read it before improvising.

## Bad agent edit, not committed

```text
Inspect git status and git diff.

I believe the latest agent edit is wrong.

Do not reset the whole repository.

Identify:
- files changed by the bad edit
- any unrelated pre-existing changes
- the safest session rewind or file-specific Git restore option

Wait before destructive Git commands.
```

## Quota/provider outage

```text
The preferred model/provider is unavailable.

Do not change project code.

Classify the interrupted task:
- planning
- implementation
- review
- visual QA
- docs/support

Recommend the closest currently available role-compatible fallback from my
configured resources.

Preserve the current handoff/context and do not switch model halfway through an
uncommitted edit unless the previous writer has stopped and summarized state.
```

## Debugging escalation

```text
Two disciplined attempts have failed.

Build a minimal evidence package:
- exact symptom
- reproduction command
- error/output
- files involved
- changes already tried and reverted/kept
- current git diff
- relevant architecture constraints

Ask GLM for diagnosis only. Do not request a rewrite of the whole feature.
Return 1-3 hypotheses and the cheapest discriminating test for each.
```

## PC → laptop handoff

```text
Create a machine handoff.

Include:
- current branch
- latest commit SHA
- whether everything is pushed
- uncommitted files (must be none for simple handoff)
- current task/result
- tests run
- next exact action on the other machine

Do not include secrets or local .env contents.
```

## Next

See [Troubleshooting](../reference/troubleshooting.md) or
[Track 8 — Maintenance](../tracks/08-maintenance.md).
