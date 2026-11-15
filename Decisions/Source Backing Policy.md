---
title: Source Backing Policy
tags:
  - decision
  - ahs
  - usa-rehab
  - tailgait
  - big-tree
aliases:
  - Provenance Policy
domain: cross-domain
status: active
last_updated: 2026-06-25
---

# Source Backing Policy

Agents should not assume facts that are not supported by linked notes or source records.

## Required Practice
- Check [[SOURCE-MANIFEST]] for source freshness.
- Add provenance to every canonical note.
- Use `status: unverified` for speculative or unverified facts.
- Keep raw inputs in `raw/` until processed.

## Provenance
- S1: [[BRAIN-PROMPT]] - user-provided second brain build prompt, captured in this repository.

## Related Notes
- [[COMPLETION-AUDIT]]
- [[index]]
