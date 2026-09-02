# UI, motion + skills

This page exists to stop two opposite mistakes:

1. never using advanced tools even when they would materially improve the work;
2. installing every visual library and turning the site into a demo reel.

## Start with the user/design problem

Before choosing a library, complete this sentence:

> “The current experience fails because ________. The proposed effect improves
> ________. We will prove that using ________.”

If you cannot fill that in, do not add the effect yet.

## Current portfolio baseline

The portfolio intentionally uses CSS for current motion and has removed unused
animation libraries. Existing engineering notes explicitly say:

- no opacity-dependent reveals;
- no scroll hijacking;
- no custom cursor;
- no WebGL by default;
- no smooth-scroll library by default;
- advanced effects must survive performance/accessibility review.

That is the starting point, not a permanent ban.

## Which motion tool?

| Need | First choice |
|---|---|
| hover/press/focus state | CSS transition |
| simple entrance/transform | CSS |
| complex multi-element timeline | Consider GSAP |
| scroll-scrubbed narrative with precise orchestration | Consider GSAP ScrollTrigger |
| global smooth scrolling feel | Consider Lenis **only after native scroll is judged insufficient** |
| 3D scene/shader | WebGL/Three.js only for one high-value scene |
| image/frame scroll sequence | Use only if visual payoff justifies media/CPU cost |

## GSAP gate

Use GSAP only if all are true:

- a named route/sequence needs timeline orchestration that CSS does not express cleanly;
- touch/mobile behavior is designed;
- reduced-motion has a complete alternative;
- the sequence does not delay navigation or hide content;
- bundle/performance impact is measured before and after;
- the dependency is route-scoped where possible.

If approved, check current docs with Context7 before implementation rather than
coding from model memory.

## Lenis gate

Lenis changes scroll behavior. Use it only if:

- the intended design genuinely needs the feel;
- anchors/history still work;
- keyboard and touch remain native-feeling;
- `prefers-reduced-motion` is honored;
- it does not fight browser restoration or route navigation;
- performance improves or stays acceptable.

Package, only after approval:

```powershell
npm install lenis
```

Official project: <https://github.com/darkroomengineering/lenis>

## WebGL / 3D gate

A 3D scene needs:

- static fallback;
- reduced-motion fallback;
- weak-GPU/data-saving strategy;
- lazy/dynamic loading;
- no essential text inside the canvas;
- route-specific loading;
- before/after performance evidence.

Do not put WebGL on every route to create “consistency.”

## Curated skills

A **skill** is a reusable instruction/workflow package an agent can load.

### Core design/quality skills

Install/use only where the harness supports the skill format.

**Impeccable** — frontend quality/design critique.

```powershell
npx impeccable install
```

Project: <https://github.com/pbakaus/impeccable>

**Vercel React Best Practices** and **Web Interface Guidelines** — React/web
implementation and interface review.

```powershell
npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-best-practices
npx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines
```

Project: <https://github.com/vercel-labs/agent-skills>

**Playwright CLI skill** — browser verification. See
[Playwright + Context7](playwright-and-context7.md).

### Conditional skills

Use these only when the matching task appears.

- **Scroll Craft** — high-end scroll storytelling:
  <https://github.com/nateherk/scroll-craft>
- **Emil Kowalski motion skills** — animation design/review:
  <https://github.com/emilkowalski/skills>
- **Taste Skill** — independent anti-template design critique:
  <https://github.com/Leonxlnx/taste-skill>
- **Checklist Design** — structured milestone visual audit:
  <https://github.com/checklist-design/skills>
- **GSAP Skills** — after a GSAP sequence is approved:
  <https://github.com/greensock/gsap-skills>
- **Strix** — security milestone, not design work:
  see [Security + Strix](security-and-strix.md)

### Optional, not default

- UI/UX Pro Max: useful as another design knowledge base, but overlaps the core
  set. Add it only if the current core is missing something.
- Hermes Agent: later maintenance/orchestration if a repeated workflow proves
  it saves work.
- OpenDesign experiments: use only for a defined design task.

## Never install all skills everywhere

Too many skill instructions can:

- consume context;
- contradict one another;
- make every agent produce the same “best practice” look;
- create more decisions for you.

Keep the harness lean.

## Visual review order

1. Static hierarchy and copy.
2. Mobile composition.
3. Interaction feedback.
4. Motion.
5. Decorative effects.
6. Final performance/accessibility check.

Do not polish an effect before the page hierarchy works.

## Next

Return to [Track 4](../tracks/04-design-and-build-loop.md) or continue to
[Track 5](../tracks/05-quality-and-polish.md).
