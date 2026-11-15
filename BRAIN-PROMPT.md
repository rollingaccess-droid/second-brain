---
title: BRAIN-PROMPT
type: system
folder: .
created: 2026-09-02
---

# Second Brain Build Prompt — Eric Anderson

Based on Nick Vasilescu's viral second brain prompt, adapted for Eric's businesses.

---

/goal Build a mature, source-backed Obsidian vault second brain for Eric Anderson.

## Who Eric Is

Eric Anderson is a licensed MHIC contractor and REALTOR based in Baltimore MD / Hamburg NY. He operates four business domains:

### 1. Accessible Housing Services (AHS) — est. 2006, Baltimore MD
- National accessibility consulting firm
- Clients: insurance companies and workers' comp carriers (Liberty Mutual, Travelers) whose policyholders need accessible home modifications
- Eric's role: Chief Architect — creates 20-page remodeling plans (PSOW — Plan of Services and Outcomes)
- Pipeline: Matterport scan → Chief Architect plans → PSOW → contractor bids → supervision
- Biggest pain point: finding contractors nationwide for complex multi-party projects
- Target franchise contractors: Amramp, 101 Mobility, Next Day Access, Mobility Plus
- Do NOT contact: Ethos Access, VGM HOMELINK, CorHome, All Access, ATF Medical
- Notion workspace: cDB ID 21fdd783-bb59-4863-a5fe-01a2e05fd2a9
- Outreach email: eric@accessiblehousingservices.com

### 2. USA Rehab — est. 1998, Baltimore MD
- Remodeling company, licensed MHIC contractor and REALTOR
- Specializes in accessible/assistive technology, construction, real estate
- Maryland-based, national reach through AHS
- USA Rehab workflow: On-site or desk estimate → Job awarded → Pre-construction visit → Exhibit A (Chief Architect plans) → Contract signed → Materials ordered → Materials in stock → Crew scheduled → Construction (1–4 days) → Field photos/docs → Homeowner sign-off → Invoice

### 3. Tailgait — Buffalo Bills/Sabres tailgate media brand
- Insta360 X3 and X4 cameras capturing tailgate events
- Goal: automated pipeline for 30-second social clips
- Stage 1: ffmpeg stitch + reframe raw .insv footage
- Stage 2: Twelve Labs AI indexes flat MP4s for best crowd/energy moments
- Stage 3: Hermes/ffmpeg builds exactly 30-second clip with intro/outro/captions
- Footage stored on Dropbox
- Key tools: Overlap.ai (AI clipping), Twelve Labs (multimodal video search)

### 4. Big Tree Rd — Co-owned Property
- Address: 4956 Big Tree Rd, Hamburg NY 14075
- Eric owns 50%, two sisters own 25% each
- Sister 1: Barbara Darul, 2783 Pleasant Ave, Lakeview NY 14085, 716-912-5892
- Sister 2: Pamela Johnson, 2787 Pleasant Ave, Lakeview NY 14085, 716-998-2384
- Goal: buyout of sisters' shares
- Intel source: Chuck Sienk (do not use as messenger between parties)
- Property is free and clear (no mortgage)

## Key People & Relationships

- Ken Owens — Matterport photographer
- Vincent Russo — Elevator Works (vendor contact)
- Robert Gonzales — lockbox coordination
- Max — shares the Droplet; separate Hermes instance, do not touch /home/max
- BS — business associate (friend, present during session today)

## Tech Stack

- DigitalOcean Droplet (Linux) running Hermes Agent
- Telegram for communication (Supergroup: Hermes Group, -1003523561365)
- Topics: General=1, AHS=2, USA=4, Tailgait=6, BigTree=8
- Codex CLI (Windows dell) + Hermes (Droplet)
- OneDrive, Dropbox, Notion
- Chief Architect (floor plans)
- Matterport (3D scans)
- AgentMail: ericanderson@agentmail.to
- Daily Focus Brief: cron at 7:30AM EDT, sends to eric@accessiblehousingservices.com + ericanderson@comcast.net

## Tools & Resources Discovered

- MPP (mpp.dev): machine-to-machine payments via HTTP 402, Tempo × Stripe
- Twelve Labs: multimodal video indexing API, $0.042/min
- Overlap.ai: AI video clipping, better for speech-based content
- Revid.ai: text-to-video for social content
- Grill Me (Matt Pocock): structured questioning to stress-test ideas
- Ransomware.live: free public API tracking 350+ ransomware groups
- Breachsense: dark web monitoring API for data breach detection
- Have I Been Pwned: breach database, MCP server available
- Nick Vasilescu second brain: Obsidian + Codex vault system

---

## Primary Objective

Create a local Obsidian-compatible vault that functions as a durable context layer for Hermes, Codex, and future AI agents. The output must be a working vault folder at this location, not merely a report. The vault must be source-backed, resumable, validated by scripts, and organized around canonical knowledge.

## Required Vault Structure

```
second-brain/
├── People/           # Key contacts, clients, contractors, partners
├── Companies/        # AHS, USA Rehab, vendors, insurers, contractors
├── Projects/         # Active projects per business domain
├── Domains/          # AHS, USA Rehab, Tailgait, Big Tree Rd knowledge bases
├── Tools/            # Tech stack, APIs, integrations
├── Decisions/        # Past decisions and rationale
├── Procedures/       # Workflows, SOPs, playbooks
├── Opportunities/    # Ideas surfaced from walk memos and research
├── raw/              # Drop zone for unprocessed inputs
├── wiki/             # Compiled canonical knowledge
│   └── index.md      # Master index with wikilinks
├── SOURCE-MANIFEST.md
├── INGESTION-LOG.md
├── VALIDATION-REPORT.md
├── COMPLETION-AUDIT.md
├── README.md
└── state.json
```

## Note Format

Use Obsidian-compatible Markdown:
- YAML frontmatter (tags, aliases, domain, status, last_updated)
- Wikilinks like this for cross-references
- Source references with provenance
- Prefer durable canonical notes over shallow stubs

## Required Content (build notes for all of these)

**People:** Eric Anderson, Barbara Darul, Pamela Johnson, Chuck Sienk, Ken Owens, Vincent Russo, Robert Gonzales, Max (Droplet co-user)

**Companies:** Accessible Housing Services, USA Rehab, Liberty Mutual, Travelers, Amramp, 101 Mobility, Next Day Access, Mobility Plus, Elevator Works

**Domains:**
- AHS domain note: consulting model, PSOW process, client types, contractor network, DNC list
- USA Rehab domain note: contractor workflow, Exhibit A, construction timeline
- Tailgait domain note: video pipeline, equipment, social strategy
- Big Tree Rd domain note: ownership structure, buyout goal, key facts

**Tools:** Hermes, Codex, Chief Architect, Matterport, Twelve Labs, Overlap, Revid, MPP, Breachsense, ransomware.live, AgentMail, Obsidian

**Procedures:**
- AHS project workflow (Matterport → plans → PSOW → bids)
- USA Rehab project workflow (estimate → Exhibit A → contract → construction → invoice)
- Tailgait clip pipeline (Stage 1 → Stage 2 → Stage 3)
- Walk memo processing pipeline (audio → Whisper → research agents → brief)
- Daily Focus Brief (what it is, cron schedule, recipients)

**Opportunities:** (stub these with tags for future population)
- Dark web breach monitoring for attorney client
- Twelve Labs video indexing for Tailgait
- MPP machine payments integration
- Voice memo → second brain pipeline
- Ransomware.live early warning system

## Agent Instructions

- Do not assume facts not in linked notes
- Check SOURCE-MANIFEST.md for source freshness
- If acting externally, ask for explicit approval first
- Tag all notes with their business domain: #ahs #usa-rehab #tailgait #big-tree
- Mark speculative or unverified facts with status: unverified in frontmatter

## Validation Hard Gates

Do not declare this goal complete unless ALL of these pass:

- [ ] 0 placeholder source references
- [ ] 0 broken internal wikilinks under Obsidian-style resolution
- [ ] 0 empty slugs
- [ ] 0 invalid paths (People/.md, Projects/.md etc.)
- [ ] 0 copied secrets, API keys, tokens, passwords, private keys
- [ ] Every canonical note has provenance
- [ ] README.md explains vault organization and how agents should use it
- [ ] VALIDATION-REPORT.md lists scripts run, pass/fail status, remaining issues
- [ ] COMPLETION-AUDIT.md maps every requirement in this prompt to evidence
- [ ] INGESTION-LOG.md and state.json are current
- [ ] Final vault opens as a normal Obsidian-compatible folder
- [ ] wiki/index.md exists with working wikilinks to all major sections

## Quality Bar

The vault should not be a data dump. It should be a structured, source-backed operating memory that helps future agents (Hermes, Codex) instantly understand:
- Who Eric is and what he is working on
- Who and what matters across all four domains
- What has been decided, what remains open
- What procedures work, what preferences matter
- Which tools are in play and how they connect
