# SEO, security + launch prompts

## SEO audit — GLM or strong free reviewer, read-only

```text
Audit the current mmoptibuilds routes for technical and intent-level SEO.

READ FIRST
- README.md
- AGENTS.md
- content/
- lib/seo.ts and metadata helpers
- sitemap.ts / robots.ts
- changed route code

DO NOT EDIT.

For every public route, check:
- distinct search/user intent
- unique title/description/H1
- canonical URL
- indexability
- internal links/breadcrumbs
- useful server-rendered text
- image dimensions/alt decisions
- JSON-LD only where visible facts support it
- duplicate/thin/cannibalizing content
- admin/private routes excluded
- no invented location/client/results claims

Prioritize findings by likely user/search impact.
Return exact file/route evidence and a minimal fix plan.
```

## SEO fix — DeepSeek

```text
Implement only the accepted SEO findings.

Rules:
- Do not mass-generate city pages.
- Do not invent keywords into unreadable copy.
- Do not add schema for facts not visible/verified.
- Preserve typed content architecture.
- Keep admin/noindex exclusions.
- Run targeted metadata/sitemap tests, then npm run verify.
```

## Security review — GLM

```text
Perform a read-only security review of the current task/diff.

Map trust boundaries:
browser -> Server Action -> validation/abuse controls -> storage -> admin.

Check:
- secret exposure
- authorization, not only authentication
- Supabase RLS assumptions
- server/client boundaries
- validation order
- duplicate/idempotency behavior
- rate-limit/Turnstile bypass
- CSRF/origin assumptions where relevant
- logs/error leakage
- dependency risk introduced by this task
- unsafe file/attachment behavior if relevant

For every finding provide severity, exact evidence, exploit/precondition,
smallest fix and verification method.

Do not invent vulnerabilities from package names alone.
```

## Security fix — DeepSeek

```text
Fix only confirmed security findings accepted for this branch.

Do not weaken existing abuse controls to make tests pass.
Do not change production secrets.
Do not deploy.

For each fix:
- add/update a regression test where practical
- run the narrow test
- run npm run verify at the end

Return a finding-by-finding FIXED / NOT FIXED table with evidence.
```

## Deployment preparation — GLM read-only

```text
Prepare a production-release checklist for the current mmoptibuilds commit.

Verify from the repo, do not assume:
- npm run verify status
- Cloudflare/OpenNext scripts
- environment variable names
- Supabase migrations/RLS status
- Turnstile configuration needs
- canonical production URL
- sitemap/robots
- admin noindex
- secrets that must exist but must not be printed
- legal/content/truth blockers
- backup/rollback point

Return:
1. blockers
2. commands to run locally
3. dashboard/manual steps
4. smoke-test routes/actions
5. rollback trigger and procedure

Do not deploy.
```

## Launch smoke test — Antigravity browser

```text
DO NOT EDIT CODE.

Smoke-test the production deployment using synthetic, non-sensitive data.

Check:
- /
- /studio
- /systems
- /contact
- legal routes
- 404
- one approved synthetic enquiry flow
- owner/admin sign-in behavior without exposing private data
- mobile viewport
- console/network failures
- canonical host
- sitemap and robots accessibility

Return PASS/FAIL per check with exact evidence.
If a failure could risk data integrity or user submissions, mark it BLOCKER.
```

## Next

Use these in
[Track 7 — SEO, security and launch](../tracks/07-seo-security-and-launch.md).
