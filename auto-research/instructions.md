# Auto Research Instructions — Second Brain Memory Improvement

## Goal
Autonomously improve the quality, completeness, and interconnectedness of Eric Anderson's Obsidian second brain vault located at `/home/eric/workspaces/second-brain/`.

The vault contains notes on four business domains: AHS (Accessible Housing Services), USA Rehab, Tailgait, Big Tree Rd — plus People, Companies, Tools, Procedures, Opportunities, Decisions, and a Videos/ digest folder.

## What You Are Optimizing (ASSET)
The markdown notes inside the vault — specifically:
- Filling knowledge gaps (stub notes, missing wikilinks)
- Adding missing cross-references between related notes
- Improving note completeness (missing frontmatter, missing Related Notes sections)
- Ensuring all canonical notes have provenance

## Rules
- Run in ~5-minute loops, overnight, indefinitely, until I stop you
- Only edit files in `/home/eric/workspaces/second-brain/` (the ASSET)
- NEVER edit `instructions.md` or `score.py` (this file and the scoring file are locked)
- NEVER create notes with placeholder content — only real, accurate information
- NEVER copy secrets, API keys, passwords, or credentials into any note
- NEVER delete existing notes — only improve them
- Each loop: make ONE targeted improvement, score it, keep or revert
- Log every round in `auto-research/results.log`

## Loop Schedule
Run 5-minute loops. Each loop = one hypothesis + one change + one score.

## Stop Conditions
- I explicitly say stop
- Validation score reaches 100 (all hard gates pass, no issues found)
- 100 rounds completed (then report and ask if I want to continue)
