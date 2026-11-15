---
title: Tailgait Clip Pipeline
tags:
  - procedure
  - tailgait
aliases:
  - Tailgait Video Pipeline
domain: tailgait
status: canonical
last_updated: 2026-06-25
---

# Tailgait Clip Pipeline

This is the canonical Tailgait clip pipeline.

## Stage 1 - Normalize Footage
Use [[ffmpeg]] to stitch and reframe raw `.insv` footage into flat MP4 files.

## Stage 2 - Find Moments
Use [[Twelve Labs]] to index flat MP4 files and identify the best crowd or energy moments. [[Overlap]] is also in the toolset, especially for speech-based clipping.

## Stage 3 - Build Clip
Use [[Hermes]] and [[ffmpeg]] to build an exactly 30-second clip with intro, outro, and captions.

## Storage
Tailgait footage is stored on [[Dropbox]].

## Provenance
- S1: [[BRAIN-PROMPT]] - user-provided second brain build prompt, captured in this repository.

## Related Notes
- [[COMPLETION-AUDIT]]
- [[BRAIN-PROMPT]]
- [[Tailgait Domain]]
- [[Hermes]]
