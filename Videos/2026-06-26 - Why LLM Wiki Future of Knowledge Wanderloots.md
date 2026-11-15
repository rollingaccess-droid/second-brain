---
title: "Why LLM Wiki? Future Of Knowledge For Agentic AI & Humans"
channel: "Wanderloots"
url: "https://www.youtube.com/watch?v=n4EVksU_EOs"
date_digested: 2026-06-26
tags: [ai, knowledge-graph, llm-wiki, obsidian, second-brain, karpathy, rag, agentic-ai]
domain: [general-ai, ahs, tailgait]
status: digested
---

# Why LLM Wiki? Future of Knowledge (Wanderloots)

## What It's About
Wanderloots explains why Karpathy's LLM Wiki concept is the future of knowledge management for both humans and AI agents. The core insight: instead of each AI tool having its own siloed memory, a shared structured knowledge graph (the LLM Wiki) becomes the persistent brain that ALL your AI tools read from. This is exactly what we're building with the second brain + auto-research system.

> "Instead of the context being fractured across all of these different tools, it lived in a structure of its own — a shared brain for all of your different AI tools."

## The Core Problem It Solves
Every AI tool starts from zero. Hermes, Codex, Claude Code, ChatGPT — they all have separate memories. You explain the same things over and over. The LLM Wiki fixes this by being a **neutral, shared knowledge layer** that every tool reads from.

## Knowledge Graph = Nodes + Edges

| Element | What It Is | Example |
|---------|-----------|---------|
| **Node** | A thing | "Eric Anderson", "AHS", "Liberty Mutual" |
| **Edge** | A relationship | "works with", "founded by", "refers to" |
| **Triple** | Subject → Relation → Object | The whole model |

Obsidian wikilinks `like this` create nodes and edges automatically. You're building a knowledge graph just by writing specific notes.

## RAG vs Graph RAG

| Method | How It Works | Weakness |
|--------|-------------|---------|
| Standard RAG | Finds similar text chunks | Fails when answer lives *between* documents |
| **Graph RAG** | Follows relationships | Handles complex multi-source questions, more token-efficient |

Graph RAG outperforms standard RAG significantly on complex, high-volume data. Eric's second brain uses wikilinks = Graph RAG-ready.

## The Recommended Architecture: Two-Vault System

| Vault | Purpose |
|-------|---------|
| **Human Vault** | Your own thinking, ideas, personal notes |
| **Agentic Vault** | AI-generated/maintained knowledge all AI tools read from |

**This is exactly what we built.** `~/workspaces/second-brain/` is the agentic vault. The auto-research loop maintains it overnight.

## How This Applies to Eric

**We already have this.** The second brain built yesterday + auto-research loop running every 5 minutes IS the LLM Wiki. The pieces:

- `~/workspaces/second-brain/` = the wiki (71 notes, all four business domains)
- `auto-research/loop.py` = the maintenance agent (runs every 5 min)
- `score.py` = the honest scoring file (currently 72/100, improving overnight)
- All Hermes sessions can query it via `session_search` or direct file read

**What we could add:**
- Web Clipper workflow — Eric clips an article → drops into `raw/` → auto-research ingests it into the wiki automatically
- Two-vault split — create a `human-notes/` folder for Eric's own thinking vs the AI-maintained wiki

## Wiring Opportunities

| Tool | Status | Effort | Notes |
|------|--------|--------|-------|
| Obsidian Web Clipper | Not set up | Quick | Browser extension → clips to `raw/` folder |
| Auto-ingest from raw/ | Not built | Moderate | Loop detects new files in raw/, compiles into wiki |
| Two-vault structure | Partial | Low | Add `human-notes/` folder to separate Eric's thinking from AI-compiled wiki |
| Graph RAG queries | Future | Heavy | Would need vector DB; current wikilink structure already approximates it |

## Ideas to Explore
- [ ] Add Obsidian Web Clipper → save to `raw/` → auto-research ingests
- [ ] Create `human-notes/` for Eric's walk memos and personal thinking (separate from AI wiki)
- [ ] Extend auto-research loop to process `raw/` files into wiki pages
- [ ] Eventually: point all AI tools (Codex, Claude, Hermes) at same second brain

## Quotes Worth Keeping
> "You don't just need a chatbot giving you an answer — you need a reference librarian."
> "I didn't try to build the graph. I just wrote about the relationship between different concepts."
> "Your human vault is where your thinking lives. Your agentic vault is where your AI tools work from."

## Related Notes
- Tools/Hermes
- Tools/Obsidian
- [[2026-06-26 - The Karpathy System 701x AI Workflows Dream Labs AI]]

## Status
- Digested: 2026-06-26
- Action taken: Second brain already built — this video validates our architecture
- Next step: Add raw/ ingestion to auto-research loop + Obsidian Web Clipper setup
