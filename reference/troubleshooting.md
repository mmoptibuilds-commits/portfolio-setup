# Troubleshooting

Use this page when the expected result does not happen.

The rule is:

> **Identify the failing layer before changing code.**

## `npm run verify` fails

1. Read the first failing gate.
2. Run that gate alone.
3. If a browser/server gate fails, check whether the expected server is actually
   running.
4. Read `AGENTS.md` for known Windows traps.
5. Only then change source code.

Use:
[Failed build prompt](../prompts/support-and-recovery.md).

## Port 3000 is already in use / stale site appears

The current portfolio has already encountered Windows process-tree problems
where killing the shell leaves the real server listening.

Do not immediately delete `.next`.

Inspect:

```powershell
Get-NetTCPConnection -LocalPort 3000 -ErrorAction SilentlyContinue
```

Then identify the owning process before stopping anything.

The repo's verification script has Windows-specific process cleanup. Prefer
letting `npm run verify` manage its own server rather than manually starting
another production server in the same port.

## Claude Code is broken

**PowerShell:**

```powershell
claude --version
claude doctor
```

Then inside Claude:

```text
/status
/context
```

If AgentRouter-specific model routing fails but Claude itself is healthy, treat
it as provider configuration—not a portfolio code bug.

## `agy` is not found

1. Close/reopen PowerShell.
2. Confirm Antigravity CLI install succeeded.
3. Check its official Windows PATH troubleshooting:
   <https://antigravity.google/docs/cli/troubleshooting/>

Do not randomly edit machine PATH entries copied from an unrelated install.

## Git says there are conflicts

Stop all agents.

In GitHub Desktop, inspect **exactly which files conflict**.

If you do not understand both sides, do not click “accept all current/incoming.”

For an AI-assisted resolution:

```text
Read the conflict markers and the recent commits on both sides.
Explain what each side was trying to preserve.
Propose a merged result that keeps both non-conflicting intentions.
Do not edit until I can see the proposed resolution.
```

## I edited on PC and laptop at the same time

1. Stop writing on both machines.
2. Commit or safely stash **only if you understand the local changes**.
3. Push neither machine blindly over the other.
4. Compare branches/commits.
5. Merge one coherent branch at a time.

For normal use, finish/push on one machine before the other starts.

## An agent changed too much

1. Stop the agent.
2. Use agent `/diff` or GitHub Desktop diff.
3. Separate intended files from unrelated edits.
4. Use session `/rewind` if available and appropriate.
5. Otherwise restore specific uncommitted files.
6. Do not force-reset the whole repo by default.

## Secret accidentally committed

Treat it as compromised even if the repo is private.

1. Revoke/rotate the credential at the provider.
2. Remove it from current source.
3. Confirm `.gitignore` prevents recurrence.
4. Decide whether Git history cleanup is required.
5. Never “solve” it by only deleting the visible line while leaving the key active.

Do not paste the leaked secret into an AI chat while asking how to rotate it.

## Model suddenly becomes worse mid-task

Possible causes:

- model/provider changed;
- context is polluted/full;
- stale instructions conflict;
- task expanded beyond the original brief.

Try:

1. `/context`
2. `/compact` if the session is still coherent
3. clean handoff + `/clear`/new session
4. task-sized context
5. same role model again or role-compatible fallback

Do not keep adding more prompts to a confused session indefinitely.

## A design looks good but verification fails

Verification wins.

Find the exact regression and redesign the effect. Do not weaken the test unless
you can prove the test is wrong.

## A check passes but the page still looks bad

Automated checks cannot judge art direction or persuasion.

Use Antigravity/Gemini visual review with
[Visual + quality prompts](../prompts/visual-and-quality.md).

## Next

Return to the track you were following once the baseline is stable.
