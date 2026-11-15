#!/usr/bin/env python3
"""
Auto Research loop — one improvement round per run.
Called by Hermes cron every 5 minutes.

Priority order:
  1. Ingest new files from raw/ into the wiki
  2. Fix broken wikilinks
  3. Add Related Notes sections
  4. Add missing frontmatter
  5. Score and log
"""

import os, sys, re, json, shutil, subprocess
from pathlib import Path
from datetime import date

VAULT = Path("/home/eric/workspaces/second-brain")
SCORE_SCRIPT = VAULT / "auto-research/score.py"
LOG = VAULT / "auto-research/results.log"
STATE_FILE = VAULT / "auto-research/state.json"
RAW_DIR = VAULT / "raw"
PROCESSED_DIR = VAULT / "raw/processed"
SKIP_DIRS = {"auto-research", ".git", ".obsidian", "raw"}
SYSTEM_FILES = {"COMPLETION-AUDIT", "INGESTION-LOG", "README", "BRAIN-PROMPT",
                "VALIDATION-REPORT", "SOURCE-MANIFEST"}

# Domain keyword mapping for auto-tagging
DOMAIN_KEYWORDS = {
    "ahs": ["accessible housing", "ahs", "workers comp", "liberty mutual", "travelers",
            "psow", "modification", "contractor", "accessible"],
    "usa-rehab": ["usa rehab", "mhic", "exhibit a", "remodel", "construction", "contractor"],
    "tailgait": ["tailgait", "bills", "sabres", "tailgate", "insta360", "video clip"],
    "big-tree": ["big tree", "hamburg", "barbara", "pamela", "4956"],
    "investing": ["stock", "trading", "fidelity", "401k", "options", "market", "polymarket"],
    "general-ai": ["ai", "llm", "claude", "hermes", "codex", "obsidian", "second brain"],
}


def run_score():
    result = subprocess.run(["python3", str(SCORE_SCRIPT)], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if line.startswith("SCORE:"):
            return int(line.split(":")[1].strip().split("/")[0])
    return 0


def get_notes():
    notes = []
    for f in VAULT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in f.parts):
            # raw/ holds pending ingests (skip), but raw/processed/ files
            # are already-compiled sources the scorer still counts — keep them.
            if not (PROCESSED_DIR in f.parents):
                continue
        notes.append(f)
    return notes


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"round": 0, "baseline_score": None, "ingested": []}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def log_round(round_num, hypothesis, change, before, after, kept):
    result = "✅ KEPT" if kept else "❌ REVERTED"
    line = f"| {round_num} | {hypothesis[:60]} | {change[:60]} | {before} | {after} | {result} |\n"
    with open(LOG, "a") as f:
        f.write(line)


# ── RAW INGESTION ────────────────────────────────────────────────────────────

def get_pending_raw_files():
    """Return files in raw/ that haven't been processed yet."""
    if not RAW_DIR.exists():
        return []
    pending = []
    for f in RAW_DIR.iterdir():
        if f.is_file() and f.suffix in (".md", ".txt", ".pdf") and f.parent == RAW_DIR:
            pending.append(f)
    return pending


def detect_domains(content: str) -> list:
    content_lower = content.lower()
    found = []
    for domain, keywords in DOMAIN_KEYWORDS.items():
        if any(kw in content_lower for kw in keywords):
            found.append(domain)
    return found or ["general-ai"]


def detect_tags(content: str, filename: str) -> list:
    tags = []
    combined = (content + " " + filename).lower()
    tag_map = {
        "trading": ["trading", "stock", "options", "market"],
        "ai": ["ai", "llm", "claude", "hermes", "agent"],
        "knowledge-base": ["wiki", "obsidian", "second brain", "knowledge"],
        "video-digest": ["youtube", "video"],
        "investing": ["invest", "fidelity", "401k", "portfolio"],
        "ahs": ["accessible housing", "psow", "modification"],
        "automation": ["automation", "workflow", "cron", "loop"],
    }
    for tag, keywords in tag_map.items():
        if any(kw in combined for kw in keywords):
            tags.append(tag)
    return tags or ["general"]


def ingest_raw_file(raw_file: Path, notes: list) -> tuple:
    """
    Compile a raw file into a proper wiki note.
    Returns (wiki_path, success).
    """
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    raw_content = raw_file.read_text(encoding="utf-8", errors="ignore").strip()
    if not raw_content:
        shutil.move(str(raw_file), str(PROCESSED_DIR / raw_file.name))
        return None, False

    today = str(date.today())
    title = raw_file.stem.replace("-", " ").replace("_", " ").title()
    domains = detect_domains(raw_content)
    tags = detect_tags(raw_content, raw_file.stem)

    # Determine target folder
    if "ahs" in domains:
        folder = VAULT / "Domains"
        dest_name = f"{title}.md"
    elif "investing" in domains or "trading" in tags:
        folder = VAULT / "Opportunities"
        dest_name = f"{today} - {title}.md"
    else:
        folder = VAULT / "wiki"
        dest_name = f"{today} - {title}.md"

    folder.mkdir(parents=True, exist_ok=True)
    wiki_path = folder / dest_name

    # Find related notes
    all_stems = {n.stem for n in notes}
    related = []
    for stem in all_stems:
        if stem.lower() in raw_content.lower() and stem not in SYSTEM_FILES:
            related.append(f"- [[{stem}]]")
        if len(related) >= 4:
            break

    related_section = "\n## Related Notes\n" + "\n".join(related) if related else ""

    # Build wiki note
    wiki_note = f"""---
title: "{title}"
source_file: "{raw_file.name}"
date_ingested: {today}
tags: [{", ".join(tags)}]
domain: [{", ".join(domains)}]
status: ingested
---

# {title}

{raw_content}
{related_section}
"""

    wiki_path.write_text(wiki_note, encoding="utf-8")

    # Move raw file to processed
    shutil.move(str(raw_file), str(PROCESSED_DIR / raw_file.name))

    return wiki_path, True


# ── WIKI IMPROVEMENTS ────────────────────────────────────────────────────────

def find_improvement_target(notes):
    all_stems = {f.stem.lower() for f in notes}

    # Priority 1: broken wikilinks
    for note in notes:
        content = note.read_text(encoding="utf-8", errors="ignore")
        links = re.findall(r'\[\[([^\]]+)\]\]', content)
        for link in links:
            target = link.split("|")[0].split("#")[0].strip().lower()
            if target and target not in all_stems:
                return "fix_broken_link", note, link

    # Priority 2: missing Related Notes section
    for note in notes:
        if note.stem in SYSTEM_FILES:
            continue
        content = note.read_text(encoding="utf-8", errors="ignore")
        if "## Related" not in content:
            return "add_related_notes", note, None

    # Priority 3: missing frontmatter (scorer deducts -1 per note)
    for note in notes:
        content = note.read_text(encoding="utf-8", errors="ignore")
        if not content.startswith("---"):
            return "add_frontmatter", note, None

    return None, None, None


def fix_broken_link(note, broken_link):
    content = note.read_text(encoding="utf-8", errors="ignore")
    display = broken_link.split("|")[-1].split("#")[0].strip()
    new_content = content.replace(f"[[{broken_link}]]", display, 1)
    if new_content != content:
        note.write_text(new_content, encoding="utf-8")
        return True
    return False


def add_related_notes(note, all_notes):
    content = note.read_text(encoding="utf-8", errors="ignore")
    stem_lower = note.stem.lower()
    related = []
    for other in all_notes:
        if other == note:
            continue
        other_content = other.read_text(encoding="utf-8", errors="ignore")
        if stem_lower in other_content.lower() or note.stem in other_content:
            related.append(f"[[{other.stem}]]")
        if len(related) >= 4:
            break
    if not related:
        for domain in ["AHS Domain", "USA Rehab Domain", "Tailgait Domain", "Big Tree Rd Domain"]:
            if (VAULT / "Domains" / f"{domain}.md").exists():
                related.append(f"[[{domain}]]")
                break
    if not related:
        return False
    section = "\n\n## Related Notes\n" + "\n".join(f"- {r}" for r in related) + "\n"
    note.write_text(content.rstrip() + section, encoding="utf-8")
    return True


def add_frontmatter(note):
    content = note.read_text(encoding="utf-8", errors="ignore")
    if content.startswith("---"):
        return False
    folder = note.parent.relative_to(VAULT).as_posix()
    ntype = "system" if note.stem in SYSTEM_FILES else "note"
    fm = (f"---\ntitle: {note.stem}\ntype: {ntype}\n"
          f"folder: {folder}\ncreated: {date.today().isoformat()}\n---\n\n")
    note.write_text(fm + content, encoding="utf-8")
    return True


# ── MAIN LOOP ────────────────────────────────────────────────────────────────

def main():
    state = load_state()
    state["round"] = state.get("round", 0) + 1
    round_num = state["round"]

    before_score = run_score()
    if state.get("baseline_score") is None:
        state["baseline_score"] = before_score

    notes = get_notes()

    # ── PRIORITY 0: Ingest raw files first ──────────────────────────────────
    pending = get_pending_raw_files()
    if pending:
        raw_file = pending[0]
        hypothesis = f"Ingest raw file: {raw_file.name}"
        wiki_path, success = ingest_raw_file(raw_file, notes)
        if success:
            after_score = run_score()
            kept = after_score >= before_score
            change_desc = f"Compiled to {wiki_path.relative_to(VAULT) if wiki_path else 'wiki'}"
            log_round(round_num, hypothesis, change_desc, before_score, after_score, kept)
            save_state(state)
            print(f"Round {round_num}: {hypothesis} | {before_score} → {after_score} | ✅ INGESTED")
            return
        else:
            print(f"Round {round_num}: Skipped empty raw file {raw_file.name}")

    # ── PRIORITY 1+: Wiki improvements ──────────────────────────────────────
    action, target_note, extra = find_improvement_target(notes)

    if not action or target_note is None:
        print(f"Round {round_num}: Vault fully optimized. Score: {before_score}/100")
        save_state(state)
        return

    backup = target_note.read_text(encoding="utf-8", errors="ignore")
    changed = False
    hypothesis = ""
    change_desc = ""

    if action == "fix_broken_link":
        hypothesis = f"Fix broken wikilink [[{extra}]] in {target_note.stem}"
        change_desc = f"Removed broken [[{extra}]]"
        changed = fix_broken_link(target_note, extra)

    elif action == "add_related_notes":
        hypothesis = f"Add Related Notes to {target_note.stem}"
        change_desc = f"Added ## Related Notes to {target_note.stem}"
        changed = add_related_notes(target_note, notes)

    elif action == "add_frontmatter":
        hypothesis = f"Add frontmatter to {target_note.stem}"
        change_desc = f"Added YAML frontmatter to {target_note.stem}"
        changed = add_frontmatter(target_note)

    if not changed:
        print(f"Round {round_num}: No change applied.")
        save_state(state)
        return

    after_score = run_score()
    kept = after_score >= before_score

    if not kept:
        target_note.write_text(backup, encoding="utf-8")
        after_score = before_score

    log_round(round_num, hypothesis, change_desc, before_score, after_score, kept)
    save_state(state)

    status = "KEPT" if kept else "REVERTED"
    print(f"Round {round_num}: {hypothesis[:80]} | {before_score} → {after_score} | {status}")


if __name__ == "__main__":
    main()
