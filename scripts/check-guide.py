from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

TRACKS = [
    f"tracks/{i:02d}-{name}.md" for i, name in [
        (1, "first-time-setup"),
        (2, "open-and-understand-project"),
        (3, "first-safe-agent-session"),
        (4, "design-and-build-loop"),
        (5, "quality-and-polish"),
        (6, "backend-admin-and-data"),
        (7, "seo-security-and-launch"),
        (8, "maintenance"),
    ]
]

REQUIRED = [
    "README.md",
    *TRACKS,
    "reference/glossary.md",
    "reference/git-and-github-desktop.md",
    "reference/claude-code.md",
    "reference/antigravity.md",
    "reference/models-and-routing.md",
    "reference/opencode-and-omniroute.md",
    "reference/ui-motion-and-skills.md",
    "reference/playwright-and-context7.md",
    "reference/subagents-mcp-and-hooks.md",
    "reference/project-source-of-truth.md",
    "reference/supabase-backend-and-admin.md",
    "reference/hosting-cloudflare-and-domain.md",
    "reference/security-and-strix.md",
    "reference/troubleshooting.md",
    "prompts/core-workflow.md",
    "prompts/visual-and-quality.md",
    "prompts/seo-security-launch.md",
    "prompts/support-and-recovery.md",
]

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^```", re.MULTILINE)
MERGE_MARKERS = ("<<<<<<<", "=======", ">>>>>>>")
PLACEHOLDERS = re.compile(r"\b(?:TBD|TODO|FIXME)\b", re.IGNORECASE)

errors: list[str] = []

for rel in REQUIRED:
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"missing required file: {rel}")

markdown_files = [
    p for p in ROOT.rglob("*.md")
    if "docs/superpowers" not in p.as_posix()
]

for path in markdown_files:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")

    if any(marker in text for marker in MERGE_MARKERS):
        errors.append(f"{rel}: unresolved merge marker")

    if PLACEHOLDERS.search(text):
        errors.append(f"{rel}: unresolved placeholder token")

    if len(FENCE_RE.findall(text)) % 2:
        errors.append(f"{rel}: unbalanced fenced code blocks")

    if rel.startswith("tracks/"):
        if "\n## Next\n" not in text:
            errors.append(f"{rel}: missing '## Next' section")
        if "### Paste this prompt" not in text:
            errors.append(f"{rel}: missing inline copy-paste prompt")
        if "### What you check yourself" not in text:
            errors.append(f"{rel}: missing human verification step")
        if "Pass to the next tool" not in text:
            errors.append(f"{rel}: missing explicit tool handoff")

    for match in LINK_RE.finditer(text):
        raw = match.group(1).strip()
        if raw.startswith(("http://", "https://", "mailto:", "#")):
            continue
        raw = raw.split("#", 1)[0]
        if not raw:
            continue
        target = (path.parent / unquote(raw)).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{rel}: link escapes repository: {match.group(1)}")
            continue
        if not target.exists():
            errors.append(f"{rel}: broken relative link: {match.group(1)}")

if errors:
    print("Guide checks failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(
    f"Guide checks passed: {len(REQUIRED)} required files, "
    f"{len(markdown_files)} Markdown files. "
    "All tracks include inline prompts, human checks, explicit handoffs and Next steps."
)
