---
title: SOURCE-MANIFEST
type: system
folder: .
created: 2026-09-02
---

# Source Manifest

This manifest tracks source records used to build and update the vault.

## Sources

| ID | Source | Type | Date Added | Freshness | Used For |
| --- | --- | --- | --- | --- | --- |
| S1 | [[BRAIN-PROMPT]] | User-provided build prompt in repository | 2026-06-25 | Current as of 2026-06-25; verify before external action or pricing decisions | Initial vault structure, facts, workflows, contacts, tools, decisions |

## Source Freshness Rules

- Treat S1 as authoritative for the initial vault build.
- For prices, vendors, laws, APIs, schedules, product capabilities, and public facts, refresh with primary sources before acting.
- For private business preferences and relationship constraints, preserve S1 until Eric provides a newer private source.
- Add each new source here before converting it into canonical notes.
