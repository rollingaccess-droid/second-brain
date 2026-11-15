---
title: "This Claude Fable 5-Minute Scalping Bot is SO GOOD It's Almost Illegal (Yours FREE)"
channel: "Trading with DaviddTech"
url: "https://www.youtube.com/watch?v=LjULWl4NhyI"
date_digested: 2026-06-25
tags: [ai, trading, mcp, backtesting, pine-script, claude, fable]
domain: [personal, ai-tools]
status: digested
---

# This Claude Fable 5-Minute Scalping Bot (Trading with DaviddTech)

## What It's About
DaviddTech shares 5 free 5-minute scalping strategies that were built and backtested using Claude Fable (Anthropic's model). The "banned by US government" hook is clickbait — the real payload is practical: Pine Script strategy templates, a free MCP server that lets Claude backtest without TradingView, and a community member (Vlad) who ran 23,000 backtests using AI to find a Gold trading edge.

## The 5 Free Strategies

| # | Strategy | Ticker | Return | Drawdown | Win Rate | Notes |
|---|----------|--------|--------|----------|----------|-------|
| 1 | Momentum Breakout Filter | Ford (5-min) | +196% | 12% | 44% | Solid. Profit factor 1.8 |
| 2 | Simple MA Scalp | Tire Group (5-min) | +103% | 11% | — | 534 trades. Sharpe below 1 |
| 3 | Z-Score Reversion | USDT (5-min) | +103% | 16% | — | Steady equity curve |
| 4 | Trend Following Breakout | COIN (5-min) | +1,156% | 60% | — | ❌ Too risky as-is |
| 5 ⭐ | VWAP Buy The Dip | (5-min) | **+5,381%** | 47% | **72%** | The marquee strategy. High drawdown but strong |

## Key Tool: Trader Dev MCP Server

This is the most relevant piece for Eric's stack.

- **What it is:** An MCP server you plug into Claude
- **What it does:** Builds Pine Script strategies and runs backtests — NO TradingView account needed
- **Setup:** Paste a code snippet into Claude → it installs automatically
- **Community:** 87,000+ backtests, 32,000+ strategies already shared
- **Loop feature:** Claude iterates through settings to mass-generate backtests automatically
- **Get it:** https://strategyfactory.ai/

This is directly wireable into Hermes via the MCP system — the same way OpenRouter MCP was added today.

## Vlad's Contribution
- Non-developer community member
- Built a full AI trading dashboard using Claude Fable 5 + Opus 4.8
- Ran 23,000 backtests
- Best result: Gold 1-hour strategy, up 0.21% in early live forward testing
- Gets access when you comment "AI AGENT" on the video

## How This Applies to Eric

Eric already has Claude (via Hermes) and the MCP infrastructure wired. The Trader Dev MCP Server is a direct add-on — same pattern as OpenRouter MCP that was installed today.

**What Eric could actually do:**
1. Install Trader Dev MCP into Hermes/Claude → backtest strategies without TradingView
2. Use Strategy 5 (VWAP Buy The Dip, 72% win rate) as a starting template
3. Use Claude's loop function to mass-generate and backtest variations automatically
4. Access the community's 32,000+ existing strategies as a starting point

**Realistic caution:** These are backtested results — forward testing always differs. The 47–60% drawdowns on some strategies are significant. Start with paper trading, not real money.

## Ideas to Explore
- [ ] Install Trader Dev MCP server into Hermes (same pattern as OpenRouter MCP)
- [ ] Test Strategy 5 (VWAP Buy The Dip) in paper trading first
- [ ] Use Claude loop to mass-backtest variations of Strategy 1 (lowest drawdown)
- [ ] Join the community at strategyfactory.ai to access 32,000+ backtested strategies

## Quotes Worth Keeping
> "The edge is not blindly asking AI to trade. The edge is giving AI the right tools, testing everything properly, and building systems instead of following hype."

> "Keep it simple stupid is maybe the right answer to trading too."

## Free Resources
- Workbook + strategies: https://app.strategyfactory.ai/resources/
- All bots: https://strategyfactory.ai/
- Comment "AI AGENT" on video for Vlad's 2 bonus charts (7 total)

## Related Notes
- Tools/Hermes
- Tools/MPP

## Status
- Digested: 2026-06-25
- Action taken: None yet
- Next step: Decide whether to install Trader Dev MCP (quick win — 30 min)
