# Visual + quality prompts

Use these after there is something rendered to inspect.

---

## Homepage art-direction review — Gemini 3.1 Pro / Antigravity

```text
Use the browser and review the current mmoptibuilds homepage.

ROLE
Senior digital art director + conversion UX reviewer.

GOAL
The homepage should feel like an authored portfolio/Awwwards-level brand
experience while making Studio and Systems easy to discover and enter.

DO NOT EDIT YET.

Review at 320, 375, 768, 1024 and 1440 CSS pixels.

Check:
- first 5-second comprehension
- visual hierarchy
- whether the Yin-Yang duality feels intentional rather than gimmicky
- Studio/Systems balance and discoverability
- personal/portfolio credibility
- typography, rhythm, negative space and composition
- hover/touch parity
- motion purpose and restraint
- reduced-motion fallback
- horizontal overflow/clipping
- CTA clarity
- anything that looks like generic AI-generated agency UI

RETURN ONLY
1. Blockers
2. High-impact changes
3. Optional polish

For each: route/viewport, evidence, expected behavior, smallest useful change.
Do not suggest a new dependency unless you can explain why CSS/current tools are
insufficient.
```

---

## Studio conversion review

```text
Review /studio and its key linked service/work pages as a prospective website
client.

DO NOT EDIT.

Answer:
1. What do I think mmoptibuilds Studio actually sells within 10 seconds?
2. Who is it for?
3. What proof is visible and is it labelled honestly?
4. What makes it different from a generic AI/vibe-coded agency?
5. Is the next action obvious?
6. What information would stop me from enquiring?
7. Does mobile preserve persuasion rather than merely stack desktop?
8. What SEO/search intent is each page serving?
9. Are any effects competing with copy or CTA?

Return prioritized, evidence-backed changes only.
```

---

## Systems conversion review

```text
Review /systems and its key intent pages as:
A. a gaming/workstation buyer who needs guidance
B. an enterprise buyer who already knows exact hardware

DO NOT EDIT.

Check:
- no-stock / quote-after-confirmation model is clear
- no public price or implied availability
- enterprise sourcing-only boundary is clear
- technical credibility without fake benchmarks
- easy path to the correct enquiry
- form friction and private budget handling
- mobile scanability
- SEO/search-intent clarity
- trust language near CTA

Return blockers, high-value improvements and optional polish.
```

---

## Responsive/mobile review — Antigravity `/browser`

```text
Inspect the changed routes at 320, 375, 390, 768, 1024 and 1440 CSS pixels.

DO NOT EDIT.

Check:
- horizontal overflow
- clipped/wrapped headings
- touch targets
- nav fit
- sticky/fixed elements
- input keyboard types
- form labels/errors
- content order
- media crop
- motion/touch behavior
- safe spacing around browser edges
- whether mobile looks intentionally composed

For every finding provide route, width, screenshot/evidence description, severity
and expected behavior.
```

---

## Accessibility review — GLM + Antigravity

```text
Review the changed feature for WCAG 2.2 AA-oriented regressions.

Use code evidence plus browser behavior.

Check:
- semantic headings/landmarks
- keyboard-only complete path
- visible focus
- focus order and restoration
- accessible names
- contrast
- 200% zoom/reflow
- reduced motion
- no-JS meaningful content
- form error announcement/focus
- native semantics before ARIA
- hover not required for discovery

Do not report speculative issues. For each finding include reproduction and the
smallest fix.

Then identify which existing npm checks should catch the issue and which still
needs manual testing.
```

---

## Motion review

```text
Review the proposed/current motion sequence.

State the user/design purpose first.

Then evaluate:
- does it improve hierarchy, orientation, storytelling or feedback?
- can CSS express it cleanly?
- is GSAP justified?
- is Lenis justified?
- is WebGL/3D justified?
- touch behavior
- reduced-motion equivalent
- CPU/GPU/battery cost
- route-level loading
- interruption/navigation behavior
- content availability if JS fails

Recommendation must be one of:
KEEP AS IS
SIMPLIFY
USE GSAP
USE LENIS
USE WEBGL/3D
REMOVE

Give evidence for the choice.
```

---

## Performance review

```text
Inspect the current diff and verification evidence for performance regressions.

Prioritize:
1. first-load JS
2. unnecessary Client Components
3. dependency additions
4. LCP asset
5. layout shift
6. image/video sizing and loading
7. offscreen animation work
8. route-specific code that leaked globally

Compare against the repository's current bundle/performance gates.
Do not optimize code that is not on a measured path.
Return only measurable or strongly evidenced findings.
```

---

## Admin usability review

```text
Review /admin as an owner operations tool, not a portfolio page.

Check:
- sign-in clarity
- enquiry scanning
- status/priority visibility
- safe destructive actions
- mobile emergency usability
- keyboard use
- empty/error/loading states
- data privacy
- accidental decoration that slows work

Do not recommend portfolio-style motion or visual spectacle.
Return the smallest changes that reduce owner time or error risk.
```

## Next

Use these during
[Track 5 — Quality and polish](../tracks/05-quality-and-polish.md).
