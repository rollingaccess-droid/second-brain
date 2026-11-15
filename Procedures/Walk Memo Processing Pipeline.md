---
title: Walk Memo Processing Pipeline
tags:
  - procedure
  - ahs
  - usa-rehab
  - tailgait
  - big-tree
aliases:
  - Voice Memo Pipeline
domain: cross-domain
status: canonical
last_updated: 2026-06-25
---

# Walk Memo Processing Pipeline

This pipeline converts spoken context into durable vault knowledge.

## Stages
1. Capture audio.
2. Transcribe with Whisper.
3. Route research questions to agents.
4. Produce a brief.
5. Convert stable facts into canonical notes with provenance.
6. Update [[INGESTION-LOG]], [[SOURCE-MANIFEST]], and `state.json`.

## Guardrails
- Mark speculative or unverified facts with `status: unverified`.
- Do not overwrite existing canonical facts without preserving provenance.
- Ask Eric before external action.

## Provenance
- S1: [[BRAIN-PROMPT]] - user-provided second brain build prompt, captured in this repository.

## Related Notes
- [[COMPLETION-AUDIT]]
- [[BRAIN-PROMPT]]
- [[Voice Memo To Second Brain Pipeline]]
- [[index]]
