---
title: README
type: system
folder: .
created: 2026-09-02
---

# Eric Anderson Second Brain

This folder is an Obsidian-compatible vault and a source-backed context layer for Eric Anderson's agent workflows.

## How The Vault Is Organized

- `People/`: key contacts, partners, co-owners, vendors, and operational boundaries.
- `Companies/`: Eric's companies, clients, target contractors, vendors, and restricted outreach entities.
- `Projects/`: active workstreams that need continuity across agent sessions.
- `Domains/`: canonical knowledge bases for AHS, USA Rehab, Tailgait, and Big Tree Rd.
- `Tools/`: software, APIs, services, and infrastructure used across the businesses.
- `Decisions/`: durable constraints, preferences, and rationale.
- `Procedures/`: workflows and SOPs agents should follow.
- `Opportunities/`: future ideas that are intentionally lighter than canonical operating notes.
- `raw/`: drop zone for unprocessed inputs.
- `wiki/index.md`: master navigation index.

## Agent Operating Rules

1. Start at wiki/index.
2. Check [[SOURCE-MANIFEST]] before relying on a fact, especially for freshness-sensitive tools, prices, vendors, or public claims.
3. Prefer canonical notes over chat memory.
4. Do not assume facts that are not supported by linked notes or source records.
5. Ask for explicit approval before external action. See [[External Action Approval Policy]].
6. Respect restricted outreach and infrastructure boundaries, especially [[AHS Do Not Contact List]] and [[Preserve Max Droplet Boundary]].
7. Add provenance to every canonical note and update [[INGESTION-LOG]] plus `state.json` after ingestion.

## Validation

Run:

```bash
python3 scripts/validate_vault.py
```

The validator checks wikilinks, placeholder source references, invalid paths, empty slugs, copied secret patterns, and provenance coverage. The latest result is written to [[VALIDATION-REPORT]].
