---
title: "This 'Karpathy System' could 701x your AI Workflows (86,000 GitHub Stars!)"
channel: "Dream Labs AI"
url: "https://www.youtube.com/watch?v=4JpwNnw0-jI"
date_digested: 2026-06-26
tags: [ai, automation, karpathy, auto-research, workflows, business, self-improvement-loop]
domain: [ahs, usa-rehab, tailgait, general-ai]
status: digested
---

# The Karpathy Auto Research System (Dream Labs AI)

## What It's About
Andrej Karpathy open-sourced a self-improvement loop called **Auto Research** — the same system top AI labs spent millions building. 85,000+ GitHub stars. Shopify's CEO pointed it at his codebase overnight: 53% faster, 61% fewer object allocations.

**Primary use case per Eric: Autonomous memory improvement.** The system is designed to continuously improve a knowledge base or second brain — pointing it at your Obsidian vault so it self-improves while you sleep, keeping what makes it more useful and discarding what doesn't.

**The 701x claim:** Most businesses run 30 experiments/year. This system runs 36,500 (5-minute loops, overnight). That's the 701x multiplier.

## The 3-File System

| File | Who Controls | What It Is |
|------|-------------|------------|
| **Instructions** | Human (locked) | What to optimize and rules |
| **Asset** | AI has full access | The thing being improved |
| **Scoring** | Human (locked) | The one honest number AI can't fake |

### The Loop
1. AI reads instructions → makes a hypothesis → changes the asset
2. Scores result against the locked scoring file
3. **Better?** Keep it, loop again
4. **Worse?** Revert, try something else
5. Runs on 5-minute loops all night

## Must-Haves (what to point it at)
1. **Objectively scorable** — one honest number (ms, open rate %, CPC)
2. **Fast feedback** — results in minutes/hours, not weeks
3. **AI can access and change it** — files, APIs, etc.

## Best Business Targets for Eric

| Asset | Score | Applies To |
|-------|-------|-----------|
| AHS outreach email subject lines | 24-hr open rate | AHS |
| AHS email body copy | Reply rate | AHS |
| USA Rehab website load speed | Milliseconds | USA Rehab |
| Tailgait Facebook ads | Cost per click | Tailgait |
| Tailgait YouTube titles | Click-through rate | Tailgait |
| AHS cold email sequences | Booking/intake rate | AHS |

## Live Demo Results
- **Website:** 800ms → 90ms load time overnight (11x improvement)
- **Cold email:** AI generates variants, sends 1,000 each, bins losers, promotes winners
- **Facebook ads:** $10 budget per variant, scores by CPC, auto-promotes winner

## How to Set It Up (No Code)
1. Get the master prompt: `joindreamlabs.com/kaparthyprompt`
2. Paste into Claude Code (or Hermes/Codex)
3. Pick ONE asset + ONE scoring number
4. Let it run overnight

## How This Applies to Eric

This is **directly executable today** using our existing stack:

**AHS — highest impact:**
- Point at outreach email subject lines → score by open rate via AgentMail
- Point at email body → score by reply rate
- We already have 475 AHS contacts and the outreach email template

**Tailgait:**
- Point at YouTube titles → score by CTR (once the channel is active)
- Point at Facebook ad copy → score by CPC

**The key insight:** Eric doesn't need to write code. The master prompt sets up the 3-file system automatically in Claude/Hermes. He just describes the asset and the scoring number.

## Wiring Opportunities

| Tool | Status | Effort | Notes |
|------|--------|--------|-------|
| Auto Research master prompt | Not set up | Quick (30 min) | Get from joindreamlabs.com/kaparthyprompt |
| AgentMail for email scoring | Already wired | Zero | Track open/reply rates as scoring file |
| Hermes cron for overnight loops | Already wired | Low | Run 5-min loops via cron while Eric sleeps |
| Facebook Ads API | Not wired | Moderate | Needed for ad variant testing |
| SmartLead AI | Not wired | Moderate | For email sequence A/B testing at volume |

## Ideas to Explore
- [ ] Get master prompt from joindreamlabs.com/kaparthyprompt
- [ ] First target: AHS email subject lines (easiest to score, most direct revenue impact)
- [ ] Wire AgentMail open-rate tracking as the scoring file
- [ ] Run overnight — wake up to winner subject line
- [ ] Second target: USA Rehab website speed (baseline it first)

## Quotes Worth Keeping
> "The bottleneck is no longer compute — it is your program.md" — Gary Tan, YC
> "Okay, this thing is totally insane." — Tobi Lütke (Shopify CEO)
> "You don't use it directly. It's a recipe. Give it to your agent and apply it to whatever you care about." — Karpathy

## Related Notes
- Tools/Hermes
- 2026-06-25 - This Claude Fable Scalping Bot is SO GOOD
- Procedures/AHS Project Workflow

## Status
- Digested: 2026-06-26
- Action taken: None yet
- Next step: Get master prompt → first test on AHS email subject lines
