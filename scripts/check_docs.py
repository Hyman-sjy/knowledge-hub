"""Check authored engineering docs and local Markdown file links using stdlib."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "AGENTS.md", "CHANGELOG.md", "CONTRIBUTING.md",
    "docs/PROJECT_CONTEXT.md", "docs/SOURCE_INTAKE.md", "docs/PHASE_00.md",
    "docs/TASKS.md", "docs/templates/ADR_TEMPLATE.md",
    "docs/templates/VALIDATION_RECORD.md", "docs/templates/G0_REPORT.md",
)


def main():
    errors = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"Missing or empty required file: {name}")

    docs = sorted(ROOT.glob("*.md")) + sorted((ROOT / "docs").rglob("*.md"))
    checked = 0
    for path in docs:
        # Imported originals retain their content; audit them separately at intake.
        if "baselines" in path.relative_to(ROOT).parts:
            continue
        checked += 1
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
            target = target.strip().split(' "', 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"Invalid local link: {path.relative_to(ROOT)} -> {target}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {checked} authored Markdown files; required files and local links checked.")
    print("Scope: repository structure only; original baseline and business validation are pending.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
