# Track 7 — SEO, security and launch

**Goal:** Launch only after the site is persuasive **and** technically safe to
operate.

## 1. Freeze feature work

A release candidate is not the moment to redesign another section.

Create/finalize a release branch and stop unrelated feature additions.

## 2. Full local verification

**Where:** PowerShell, portfolio root.

```powershell
npm run verify
```

Fix failures before moving forward.

## 3. SEO review

Use:
[SEO audit prompt](../prompts/seo-security-launch.md).

The repo already has typed content, metadata helpers, sitemap/robots and
structured-data foundations. Improve those; do not bolt on an SEO plugin because
“SEO” sounds separate.

Key rules:

- one useful page per search intent;
- no thin city-page spam;
- no fake local/client proof;
- indexable text must exist outside canvas effects;
- admin/private pages stay out of sitemap/index;
- canonicals must use the real production origin.

## 4. Security review

Run the least-invasive checks first:

```powershell
npm audit
npm run verify
```

Then use Claude `/security-review` or the
[security prompt](../prompts/seo-security-launch.md).

Use [Strix](../reference/security-and-strix.md) only if an active security scan
adds value and the target is owned/authorized.

## 5. Truth + legal launch gate

The code cannot decide these facts for you:

- legal business identity/address;
- GST/invoice requirements;
- final privacy/terms/warranty/cancellation wording;
- supplier/logistics representations;
- case-study permissions;
- any customer/result claim.

Do not let an AI invent certainty. Mark unresolved commercial/legal facts as
**launch blockers**, not plausible text.

## 6. Database/admin release check

If production Supabase is in use:

- migrations reviewed/applied;
- RLS tested;
- owner authorization tested;
- synthetic enquiry round trip tested;
- backup/export/rollback plan known.

See [Supabase, backend + admin](../reference/supabase-backend-and-admin.md).

## 7. Cloudflare preview

Read [Cloudflare, hosting + domain](../reference/hosting-cloudflare-and-domain.md).

**Where:** PowerShell.

```powershell
npm run cf:preview
```

Smoke-test the preview before touching the live deployment.

## 8. Production deployment

Only after the release checklist is green:

```powershell
npm run cf:deploy
```

> [!CAUTION]
> This is a real production action. Never put it into an autonomous `/goal`,
> hook or “fix everything” prompt without an explicit release decision.

## 9. Post-deploy smoke test

Use Antigravity browser with the
[Launch Smoke Test prompt](../prompts/seo-security-launch.md).

Test synthetic data only.

Record:

- deployed commit SHA;
- time;
- migration version if relevant;
- result;
- known issues;
- rollback point.

## Launch checklist

- [ ] `npm run verify` passes on release candidate.
- [ ] No unresolved blocker/high code-review finding.
- [ ] Mobile/browser visual QA passes.
- [ ] SEO audit/fixes reviewed.
- [ ] No fake/unverified public proof.
- [ ] Security review complete.
- [ ] Secrets are in managed storage, not Git.
- [ ] Supabase RLS/owner auth tested if production DB is enabled.
- [ ] Cloudflare preview smoke test passes.
- [ ] Legal/tax/business blockers resolved by appropriate human/professional review.
- [ ] Production deployment is tied to a known commit.
- [ ] Post-deploy smoke test passes.
- [ ] Rollback point recorded.

## Next

→ [Track 8 — Maintenance](08-maintenance.md)
