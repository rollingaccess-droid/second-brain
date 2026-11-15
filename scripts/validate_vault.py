#!/usr/bin/env python3
"""Validate hard gates for Eric Anderson's second brain vault."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
CANONICAL_DIRS = {
    "People",
    "Companies",
    "Projects",
    "Domains",
    "Tools",
    "Decisions",
    "Procedures",
    "Opportunities",
    "wiki",
}
REQUIRED_ROOTS = [
    "People",
    "Companies",
    "Projects",
    "Domains",
    "Tools",
    "Decisions",
    "Procedures",
    "Opportunities",
    "raw",
    "wiki",
]


def iter_markdown() -> list[Path]:
    ignored_parts = {".git"}
    return sorted(
        p
        for p in ROOT.rglob("*.md")
        if not any(part in ignored_parts for part in p.relative_to(ROOT).parts)
    )


def strip_code_blocks(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return re.sub(r"`[^`\n]+`", "", text)


def obsidian_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return target


def build_link_index(markdown_files: list[Path]) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = defaultdict(list)
    for path in markdown_files:
        rel = path.relative_to(ROOT).as_posix()
        stem = path.stem
        index[stem.lower()].append(path)
        index[rel[:-3].lower()].append(path)
    return index


def has_frontmatter(text: str) -> bool:
    return text.startswith("---\n") and "\n---\n" in text[4:]


def frontmatter_value(text: str, key: str) -> str | None:
    if not has_frontmatter(text):
        return None
    fm = text.split("\n---\n", 1)[0][4:]
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", fm, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def validate() -> tuple[bool, list[tuple[str, bool, list[str]]]]:
    files = iter_markdown()
    link_index = build_link_index(files)
    checks: list[tuple[str, bool, list[str]]] = []

    missing_dirs = [d for d in REQUIRED_ROOTS if not (ROOT / d).is_dir()]
    checks.append(("required directories exist", not missing_dirs, missing_dirs))

    invalid_paths = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if rel.endswith("/.md") or path.stem.strip() == "":
            invalid_paths.append(rel)
    checks.append(("0 invalid paths and empty slugs", not invalid_paths, invalid_paths))

    placeholder_patterns = [
        r"SOURCE NEEDED",
        r"TODO[: ]+source",
        r"citation needed",
        r"\[\[SOURCE\]\]",
    ]
    placeholder_hits = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for pattern in placeholder_patterns:
            if re.search(pattern, text, flags=re.IGNORECASE):
                placeholder_hits.append(f"{path.relative_to(ROOT)}: {pattern}")
    checks.append(("0 placeholder source references", not placeholder_hits, placeholder_hits))

    secret_patterns = [
        r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----",
        r"\bsk-[A-Za-z0-9_-]{20,}\b",
        r"\bAKIA[0-9A-Z]{16}\b",
        r"\bAIza[0-9A-Za-z_-]{30,}\b",
        r"\bghp_[0-9A-Za-z]{30,}\b",
        r"\bglpat-[0-9A-Za-z_-]{20,}\b",
        r"\bxox[baprs]-[0-9A-Za-z-]{20,}\b",
        r"(?i)(api[_-]?key|access[_-]?token|secret[_-]?key|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{16,}",
    ]
    secret_hits = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for pattern in secret_patterns:
            if re.search(pattern, text):
                secret_hits.append(f"{path.relative_to(ROOT)}: matched secret pattern")
    checks.append(("0 copied secrets/API keys/tokens/passwords/private keys", not secret_hits, secret_hits))

    broken_links = []
    ambiguous_links = []
    link_pattern = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
    for path in files:
        if path.name == "VALIDATION-REPORT.md":
            continue
        text = strip_code_blocks(path.read_text(encoding="utf-8"))
        for match in link_pattern.finditer(text):
            raw = match.group(1)
            target = obsidian_target(raw)
            if not target:
                broken_links.append(f"{path.relative_to(ROOT)}: empty wikilink target in [[{raw}]]")
                continue
            matches = link_index.get(target.lower(), [])
            if not matches:
                broken_links.append(f"{path.relative_to(ROOT)}: [[{raw}]]")
            elif len(set(matches)) > 1:
                ambiguous_links.append(f"{path.relative_to(ROOT)}: [[{raw}]] -> {[m.relative_to(ROOT).as_posix() for m in matches]}")
    checks.append(("0 broken internal wikilinks", not broken_links, broken_links))
    checks.append(("0 ambiguous internal wikilinks", not ambiguous_links, ambiguous_links))

    provenance_missing = []
    frontmatter_missing = []
    canonical_files = [
        p
        for p in files
        if p.relative_to(ROOT).parts[0] in CANONICAL_DIRS
    ]
    for path in canonical_files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        if not has_frontmatter(text):
            frontmatter_missing.append(rel)
        if "## Provenance" not in text or "S1:" not in text:
            provenance_missing.append(rel)
        for key in ["tags", "aliases", "domain", "status", "last_updated"]:
            if key not in text.split("\n---\n", 1)[0]:
                frontmatter_missing.append(f"{rel}: missing {key}")
    checks.append(("every canonical note has frontmatter", not frontmatter_missing, frontmatter_missing))
    checks.append(("every canonical note has provenance", not provenance_missing, provenance_missing))

    readme = ROOT / "README.md"
    readme_ok = readme.exists() and "How The Vault Is Organized" in readme.read_text(encoding="utf-8") and "Agent Operating Rules" in readme.read_text(encoding="utf-8")
    checks.append(("README explains organization and agent use", readme_ok, [] if readme_ok else ["README.md missing required sections"]))

    index = ROOT / "wiki" / "index.md"
    index_ok = index.exists() and "[[Eric Anderson]]" in index.read_text(encoding="utf-8") and "[[AHS Domain]]" in index.read_text(encoding="utf-8")
    checks.append(("wiki/index.md exists with major section wikilinks", index_ok, [] if index_ok else ["wiki/index.md missing or incomplete"]))

    for required_file in ["SOURCE-MANIFEST.md", "INGESTION-LOG.md", "COMPLETION-AUDIT.md", "state.json"]:
        exists = (ROOT / required_file).exists()
        checks.append((f"{required_file} exists", exists, [] if exists else [required_file]))

    state_file = ROOT / "state.json"
    state_ok = False
    state_details: list[str] = []
    if state_file.exists():
        try:
            json.loads(state_file.read_text(encoding="utf-8"))
            state_ok = True
        except Exception as exc:  # pragma: no cover - defensive validation path
            state_details.append(str(exc))
    checks.append(("state.json is valid JSON and updated", state_ok, state_details))

    passed = all(ok for _, ok, _ in checks)
    return passed, checks


def update_state(passed: bool) -> None:
    state_file = ROOT / "state.json"
    if not state_file.exists():
        return
    state = json.loads(state_file.read_text(encoding="utf-8"))
    state["last_validation"] = {
        "status": "pass" if passed else "fail",
        "validated_at": NOW,
        "command": "python3 scripts/validate_vault.py",
        "report": "VALIDATION-REPORT.md",
    }
    state_file.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def write_report(passed: bool, checks: list[tuple[str, bool, list[str]]]) -> None:
    lines = [
        "# Validation Report",
        "",
        f"Generated: {NOW}",
        "",
        f"Status: {'PASS' if passed else 'FAIL'}",
        "",
        "## Scripts Run",
        "",
        "| Command | Result |",
        "| --- | --- |",
        f"| `python3 scripts/validate_vault.py` | {'PASS' if passed else 'FAIL'} |",
        "",
        "## Hard Gates",
        "",
        "| Gate | Result | Details |",
        "| --- | --- | --- |",
    ]
    for name, ok, details in checks:
        detail = "None" if not details else "<br>".join(str(d).replace("|", "\\|") for d in details[:20])
        if len(details) > 20:
            detail += f"<br>... {len(details) - 20} more"
        lines.append(f"| {name} | {'PASS' if ok else 'FAIL'} | {detail} |")
    lines.extend(
        [
            "",
            "## Remaining Issues",
            "",
            "None." if passed else "See failed hard gates above.",
        ]
    )
    (ROOT / "VALIDATION-REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    passed, checks = validate()
    update_state(passed)
    write_report(passed, checks)
    print("PASS" if passed else "FAIL")
    for name, ok, details in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
        for detail in details[:10]:
            print(f"  - {detail}")
        if len(details) > 10:
            print(f"  - ... {len(details) - 10} more")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
