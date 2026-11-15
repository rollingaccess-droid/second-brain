#!/usr/bin/env python3
"""Generate Eric Anderson's Obsidian-compatible second brain vault."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-06-25"
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

SOURCE_ID = "S1"
SOURCE_LINK = "[[BRAIN-PROMPT]]"
SOURCE_LINE = "- S1: [[BRAIN-PROMPT]] - user-provided second brain build prompt, captured in this repository."


def frontmatter(title: str, tags: list[str], aliases: list[str], domain: str, status: str) -> str:
    def yaml_list(items: list[str]) -> str:
        return "\n".join(f"  - {item}" for item in items)

    return (
        "---\n"
        f"title: {title}\n"
        "tags:\n"
        f"{yaml_list(tags)}\n"
        "aliases:\n"
        f"{yaml_list(aliases)}\n"
        f"domain: {domain}\n"
        f"status: {status}\n"
        f"last_updated: {TODAY}\n"
        "---\n\n"
    )


def note(
    path: str,
    title: str,
    tags: list[str],
    aliases: list[str],
    domain: str,
    status: str,
    body: str,
) -> tuple[str, str]:
    content = frontmatter(title, tags, aliases, domain, status)
    content += f"# {title}\n\n"
    content += body.strip() + "\n\n"
    content += "## Provenance\n"
    content += f"{SOURCE_LINE}\n"
    return path, content


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    for folder in [
        "People",
        "Companies",
        "Projects",
        "Domains",
        "Tools",
        "Decisions",
        "Procedures",
        "Opportunities",
        "raw",
        "wiki",
        "scripts",
    ]:
        (ROOT / folder).mkdir(exist_ok=True)

    notes: list[tuple[str, str]] = []

    notes.extend(
        [
            note(
                "People/Eric Anderson.md",
                "Eric Anderson",
                ["person", "ahs", "usa-rehab", "tailgait", "big-tree"],
                ["Eric"],
                "cross-domain",
                "canonical",
                """
Eric Anderson is the central operator for this vault. He is described as a licensed MHIC contractor and REALTOR based around Baltimore, Maryland and Hamburg, New York.

## Operating Domains
- [[Accessible Housing Services]]: Eric acts as Chief Architect for accessibility consulting work and creates remodeling plans for PSOW packages.
- [[USA Rehab]]: Eric operates a Maryland remodeling company focused on accessible construction, assistive technology, and real estate.
- [[Tailgait Domain]]: Eric is building a Buffalo Bills/Sabres tailgate media workflow for exactly 30-second social clips.
- [[Big Tree Rd Domain]]: Eric owns 50% of 4956 Big Tree Rd and wants to buy out the remaining shares.

## Agent Handling Notes
- Treat this vault as Eric's durable operating memory.
- Before acting externally for Eric, follow [[External Action Approval Policy]].
- Use [[SOURCE-MANIFEST]] to check whether source material is current enough for the task.
""",
            ),
            note(
                "People/Barbara Darul.md",
                "Barbara Darul",
                ["person", "big-tree"],
                ["Barbara"],
                "big-tree",
                "canonical",
                """
Barbara Darul is one of Eric Anderson's sisters and a co-owner connected to [[Big Tree Rd Domain]].

## Known Facts
- Ownership share: 25% of [[Big Tree Rd Domain]].
- Mailing address in source: 2783 Pleasant Ave, Lakeview NY 14085.
- Phone in source: 716-912-5892.

## Relationship Context
Eric's stated goal is to buy out the sisters' shares. Do not use [[Chuck Sienk]] as a messenger between parties.
""",
            ),
            note(
                "People/Pamela Johnson.md",
                "Pamela Johnson",
                ["person", "big-tree"],
                ["Pamela"],
                "big-tree",
                "canonical",
                """
Pamela Johnson is one of Eric Anderson's sisters and a co-owner connected to [[Big Tree Rd Domain]].

## Known Facts
- Ownership share: 25% of [[Big Tree Rd Domain]].
- Mailing address in source: 2787 Pleasant Ave, Lakeview NY 14085.
- Phone in source: 716-998-2384.

## Relationship Context
Eric's stated goal is to buy out the sisters' shares. Do not use [[Chuck Sienk]] as a messenger between parties.
""",
            ),
            note(
                "People/Chuck Sienk.md",
                "Chuck Sienk",
                ["person", "big-tree"],
                ["Chuck"],
                "big-tree",
                "canonical",
                """
Chuck Sienk is identified as an intel source for [[Big Tree Rd Domain]].

## Handling Constraint
- Do not use Chuck Sienk as a messenger between parties.
- Treat information from Chuck as context, not as permission to act.
""",
            ),
            note(
                "People/Ken Owens.md",
                "Ken Owens",
                ["person", "ahs"],
                ["Ken"],
                "ahs",
                "canonical",
                """
Ken Owens is a Matterport photographer connected to the [[AHS Project Workflow]].

## Operating Context
Matterport scans are the first input in the AHS pipeline before [[Chief Architect]] plans, PSOW creation, contractor bids, and supervision.
""",
            ),
            note(
                "People/Vincent Russo.md",
                "Vincent Russo",
                ["person", "ahs", "usa-rehab"],
                ["Vincent"],
                "cross-domain",
                "canonical",
                """
Vincent Russo is the named vendor contact for [[Elevator Works]].

## Operating Context
Use this note when vendor coordination involves elevator-related accessibility work across [[Accessible Housing Services]] or [[USA Rehab]].
""",
            ),
            note(
                "People/Robert Gonzales.md",
                "Robert Gonzales",
                ["person", "ahs", "usa-rehab"],
                ["Robert"],
                "cross-domain",
                "canonical",
                """
Robert Gonzales is associated with lockbox coordination.

## Operating Context
Use this note when a workflow requires access coordination, field visits, or job-site logistics for [[Accessible Housing Services]] or [[USA Rehab]].
""",
            ),
            note(
                "People/Max Droplet Co-user.md",
                "Max Droplet Co-user",
                ["person", "ahs", "usa-rehab", "tailgait", "big-tree"],
                ["Max"],
                "cross-domain",
                "canonical",
                """
Max shares the DigitalOcean Droplet used for Hermes-related infrastructure.

## Boundary
- Max has a separate Hermes instance.
- Do not touch `/home/max`.

This boundary is formalized in [[Preserve Max Droplet Boundary]].
""",
            ),
        ]
    )

    company_notes = [
        (
            "Companies/Accessible Housing Services.md",
            "Accessible Housing Services",
            ["company", "ahs"],
            ["AHS"],
            "ahs",
            """
Accessible Housing Services is Eric Anderson's national accessibility consulting firm, established in 2006 in Baltimore, Maryland.

## Model
AHS serves insurance companies and workers' compensation carriers whose policyholders need accessible home modifications.

## Eric's Role
Eric is described as Chief Architect. He creates 20-page remodeling plans called PSOW packages: Plan of Services and Outcomes.

## Core Pipeline
The operating pipeline is documented in [[AHS Project Workflow]]: [[Matterport]] scan -> [[Chief Architect]] plans -> PSOW -> contractor bids -> supervision.

## Contractor Network
The stated pain point is finding contractors nationwide for complex multi-party projects. Target franchise contractors include [[Amramp]], [[101 Mobility]], [[Next Day Access]], and [[Mobility Plus]].

## Restricted Outreach
Do not contact: Ethos Access, VGM HOMELINK, CorHome, All Access, ATF Medical. See [[AHS Do Not Contact List]].

## Systems
- Notion workspace cDB ID is listed in source material.
- Outreach email in source: eric@accessiblehousingservices.com.
""",
        ),
        (
            "Companies/USA Rehab.md",
            "USA Rehab",
            ["company", "usa-rehab"],
            ["USA Rehab Inc"],
            "usa-rehab",
            """
USA Rehab is Eric Anderson's remodeling company, established in 1998 in Baltimore, Maryland.

## Positioning
The company specializes in accessible and assistive technology, construction, and real estate. It is Maryland-based with national reach through [[Accessible Housing Services]].

## Workflow
The company workflow is documented in [[USA Rehab Project Workflow]]: estimate -> job awarded -> pre-construction visit -> Exhibit A -> contract signed -> materials ordered -> materials in stock -> crew scheduled -> construction -> field photos/docs -> homeowner sign-off -> invoice.

## Planning Artifact
Exhibit A is tied to [[Chief Architect]] plans.
""",
        ),
        (
            "Companies/Liberty Mutual.md",
            "Liberty Mutual",
            ["company", "ahs"],
            ["Liberty Mutual Insurance"],
            "ahs",
            """
Liberty Mutual is listed as an example client type for [[Accessible Housing Services]].

## Context
AHS clients are insurance companies and workers' compensation carriers whose policyholders need accessible home modifications.
""",
        ),
        (
            "Companies/Travelers.md",
            "Travelers",
            ["company", "ahs"],
            ["Travelers Insurance"],
            "ahs",
            """
Travelers is listed as an example client type for [[Accessible Housing Services]].

## Context
AHS clients are insurance companies and workers' compensation carriers whose policyholders need accessible home modifications.
""",
        ),
        (
            "Companies/Amramp.md",
            "Amramp",
            ["company", "ahs"],
            [],
            "ahs",
            """
Amramp is identified as a target franchise contractor for the [[Accessible Housing Services]] contractor network.

## Use Case
Consider Amramp when sourcing nationwide contractors for complex accessibility projects, subject to project fit and Eric's approval for outreach.
""",
        ),
        (
            "Companies/101 Mobility.md",
            "101 Mobility",
            ["company", "ahs"],
            [],
            "ahs",
            """
101 Mobility is identified as a target franchise contractor for the [[Accessible Housing Services]] contractor network.

## Use Case
Consider 101 Mobility when sourcing nationwide contractors for complex accessibility projects, subject to project fit and Eric's approval for outreach.
""",
        ),
        (
            "Companies/Next Day Access.md",
            "Next Day Access",
            ["company", "ahs"],
            [],
            "ahs",
            """
Next Day Access is identified as a target franchise contractor for the [[Accessible Housing Services]] contractor network.

## Use Case
Consider Next Day Access when sourcing nationwide contractors for complex accessibility projects, subject to project fit and Eric's approval for outreach.
""",
        ),
        (
            "Companies/Mobility Plus.md",
            "Mobility Plus",
            ["company", "ahs"],
            [],
            "ahs",
            """
Mobility Plus is identified as a target franchise contractor for the [[Accessible Housing Services]] contractor network.

## Use Case
Consider Mobility Plus when sourcing nationwide contractors for complex accessibility projects, subject to project fit and Eric's approval for outreach.
""",
        ),
        (
            "Companies/Elevator Works.md",
            "Elevator Works",
            ["company", "ahs", "usa-rehab"],
            [],
            "cross-domain",
            """
Elevator Works is a vendor connected to [[Vincent Russo]].

## Use Case
Reference this note for accessibility work where elevator vendor coordination is relevant to [[Accessible Housing Services]] or [[USA Rehab]].
""",
        ),
        (
            "Companies/Ethos Access.md",
            "Ethos Access",
            ["company", "ahs", "restricted-outreach"],
            [],
            "ahs",
            """
Ethos Access is on the AHS do-not-contact list.

## Constraint
Do not contact this company for AHS contractor outreach unless Eric explicitly changes the restriction. See [[AHS Do Not Contact List]].
""",
        ),
        (
            "Companies/VGM HOMELINK.md",
            "VGM HOMELINK",
            ["company", "ahs", "restricted-outreach"],
            [],
            "ahs",
            """
VGM HOMELINK is on the AHS do-not-contact list.

## Constraint
Do not contact this company for AHS contractor outreach unless Eric explicitly changes the restriction. See [[AHS Do Not Contact List]].
""",
        ),
        (
            "Companies/CorHome.md",
            "CorHome",
            ["company", "ahs", "restricted-outreach"],
            [],
            "ahs",
            """
CorHome is on the AHS do-not-contact list.

## Constraint
Do not contact this company for AHS contractor outreach unless Eric explicitly changes the restriction. See [[AHS Do Not Contact List]].
""",
        ),
        (
            "Companies/All Access.md",
            "All Access",
            ["company", "ahs", "restricted-outreach"],
            [],
            "ahs",
            """
All Access is on the AHS do-not-contact list.

## Constraint
Do not contact this company for AHS contractor outreach unless Eric explicitly changes the restriction. See [[AHS Do Not Contact List]].
""",
        ),
        (
            "Companies/ATF Medical.md",
            "ATF Medical",
            ["company", "ahs", "restricted-outreach"],
            [],
            "ahs",
            """
ATF Medical is on the AHS do-not-contact list.

## Constraint
Do not contact this company for AHS contractor outreach unless Eric explicitly changes the restriction. See [[AHS Do Not Contact List]].
""",
        ),
    ]
    for path, title, tags, aliases, domain, body in company_notes:
        notes.append(note(path, title, tags, aliases, domain, "canonical", body))

    domain_notes = [
        (
            "Domains/AHS Domain.md",
            "AHS Domain",
            ["domain", "ahs"],
            ["Accessible Housing Services Domain", "AHS"],
            "ahs",
            """
This domain covers [[Accessible Housing Services]], Eric's national accessibility consulting business.

## Consulting Model
AHS supports insurance companies and workers' compensation carriers whose policyholders need accessible home modifications. Eric's role is to convert project inputs into a structured PSOW and remodeling plan package.

## PSOW Process
The PSOW process starts with a [[Matterport]] scan, moves into [[Chief Architect]] plans, becomes a PSOW package, and then supports contractor bids and supervision. The procedural version lives in [[AHS Project Workflow]].

## Client Types
Known client examples include [[Liberty Mutual]] and [[Travelers]]. Treat the broader category as insurance and workers' compensation carrier work unless a later source adds detail.

## Contractor Network
Target franchise contractors include [[Amramp]], [[101 Mobility]], [[Next Day Access]], and [[Mobility Plus]]. The biggest stated pain point is finding contractors nationwide for complex multi-party projects.

## Do-Not-Contact List
Do not contact [[Ethos Access]], [[VGM HOMELINK]], [[CorHome]], [[All Access]], or [[ATF Medical]]. See [[AHS Do Not Contact List]] before any outreach.
""",
        ),
        (
            "Domains/USA Rehab Domain.md",
            "USA Rehab Domain",
            ["domain", "usa-rehab"],
            ["USA Rehab"],
            "usa-rehab",
            """
This domain covers [[USA Rehab]], Eric's remodeling company.

## Business Model
USA Rehab is a Maryland-based remodeling company with national reach through [[Accessible Housing Services]]. It specializes in accessible and assistive technology, construction, and real estate.

## Workflow
The operating workflow is documented in [[USA Rehab Project Workflow]] and moves from estimate through contract, materials, crew scheduling, construction, field documentation, sign-off, and invoice.

## Planning Artifact
Exhibit A is the [[Chief Architect]] plan package used before contract signing.

## Construction Timeline
The source prompt gives a construction window of 1-4 days.
""",
        ),
        (
            "Domains/Tailgait Domain.md",
            "Tailgait Domain",
            ["domain", "tailgait"],
            ["Tailgait"],
            "tailgait",
            """
This domain covers Tailgait, Eric's Buffalo Bills/Sabres tailgate media brand.

## Goal
Build an automated pipeline that creates exactly 30-second social clips from event footage.

## Equipment And Storage
The source names Insta360 X3 and X4 cameras and Dropbox storage for footage.

## Pipeline
The pipeline is documented in [[Tailgait Clip Pipeline]]: ffmpeg stitch/reframe raw `.insv` footage -> [[Twelve Labs]] indexing for energy moments -> [[Hermes]] and ffmpeg assembly with intro, outro, and captions.

## Social Strategy
The strategy is clip-based: identify high-energy crowd moments and publish short social-ready edits.
""",
        ),
        (
            "Domains/Big Tree Rd Domain.md",
            "Big Tree Rd Domain",
            ["domain", "big-tree"],
            ["Big Tree Rd", "4956 Big Tree Rd"],
            "big-tree",
            """
This domain covers the co-owned property at 4956 Big Tree Rd, Hamburg NY 14075.

## Ownership
- [[Eric Anderson]] owns 50%.
- [[Barbara Darul]] owns 25%.
- [[Pamela Johnson]] owns 25%.

## Property Facts
- Address: 4956 Big Tree Rd, Hamburg NY 14075.
- Mortgage status in source: free and clear.

## Goal
Eric wants to buy out his sisters' shares.

## Relationship Constraint
[[Chuck Sienk]] is an intel source, but must not be used as a messenger between parties.
""",
        ),
    ]
    for path, title, tags, aliases, domain, body in domain_notes:
        notes.append(note(path, title, tags, aliases, domain, "canonical", body))

    tool_notes = [
        (
            "Tools/Hermes.md",
            "Hermes",
            ["tool", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["Hermes Agent"],
            "cross-domain",
            """
Hermes is the agent system running on a DigitalOcean Droplet.

## Communications
Telegram is used for communication through the Hermes Group supergroup. Topic IDs in source are: General=1, AHS=2, USA=4, Tailgait=6, BigTree=8.

## Workflows
- Sends or supports the [[Daily Focus Brief]].
- Participates in [[Tailgait Clip Pipeline]] assembly with ffmpeg.
- Should use this vault as context before acting.

## Boundaries
Max has a separate Hermes instance. Do not touch `/home/max`; see [[Preserve Max Droplet Boundary]].
""",
        ),
        (
            "Tools/Codex.md",
            "Codex",
            ["tool", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["Codex CLI"],
            "cross-domain",
            """
Codex CLI is part of Eric's agent workflow, used from a Windows Dell machine in combination with [[Hermes]] on the Droplet.

## Vault Role
Codex should use this vault as source-backed memory. It should avoid assuming facts that are not present in linked notes or sources.
""",
        ),
        (
            "Tools/Chief Architect.md",
            "Chief Architect",
            ["tool", "ahs", "usa-rehab"],
            [],
            "cross-domain",
            """
Chief Architect is the floor-plan tool used in AHS and USA Rehab workflows.

## AHS Use
Chief Architect plans are created after [[Matterport]] scans and before PSOW creation in [[AHS Project Workflow]].

## USA Rehab Use
Chief Architect plans are used for Exhibit A in [[USA Rehab Project Workflow]].
""",
        ),
        (
            "Tools/Matterport.md",
            "Matterport",
            ["tool", "ahs", "usa-rehab"],
            [],
            "cross-domain",
            """
Matterport is the 3D scan input used in [[AHS Project Workflow]].

## People
[[Ken Owens]] is the named Matterport photographer.
""",
        ),
        (
            "Tools/Twelve Labs.md",
            "Twelve Labs",
            ["tool", "tailgait"],
            [],
            "tailgait",
            """
Twelve Labs is a multimodal video indexing API used in [[Tailgait Clip Pipeline]].

## Tailgait Use
The intended use is to index flat MP4 files and identify the best crowd or energy moments for exactly 30-second social clips.

## Cost Note
The source prompt records a cost of $0.042/min. Check source freshness before relying on this for purchasing or budgeting.
""",
        ),
        (
            "Tools/Overlap.md",
            "Overlap",
            ["tool", "tailgait"],
            ["Overlap.ai"],
            "tailgait",
            """
Overlap.ai is an AI clipping tool in the Tailgait toolset.

## Fit
The source prompt says Overlap.ai is better for speech-based content. Treat that as a remembered evaluation, not a universal product claim.
""",
        ),
        (
            "Tools/Revid.md",
            "Revid",
            ["tool", "tailgait"],
            ["Revid.ai"],
            "tailgait",
            """
Revid.ai is listed as a text-to-video tool for social content.

## Fit
Use this as a candidate tool for social content generation or repurposing. It is not listed as part of the required Tailgait clip assembly path.
""",
        ),
        (
            "Tools/MPP.md",
            "MPP",
            ["tool", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["mpp.dev"],
            "cross-domain",
            """
MPP is listed as a machine-to-machine payments resource using HTTP 402, Tempo, and Stripe.

## Opportunity
The related opportunity is [[MPP Machine Payments Integration]].
""",
        ),
        (
            "Tools/Breachsense.md",
            "Breachsense",
            ["tool", "ahs", "usa-rehab"],
            [],
            "cross-domain",
            """
Breachsense is listed as a dark web monitoring API for data breach detection.

## Opportunity
The related opportunity is [[Dark Web Breach Monitoring For Attorney Client]].
""",
        ),
        (
            "Tools/Ransomware Live.md",
            "Ransomware Live",
            ["tool", "ahs", "usa-rehab"],
            ["ransomware.live"],
            "cross-domain",
            """
ransomware.live is listed as a free public API tracking 350+ ransomware groups.

## Opportunity
The related opportunity is [[Ransomware Live Early Warning System]].
""",
        ),
        (
            "Tools/AgentMail.md",
            "AgentMail",
            ["tool", "ahs", "usa-rehab", "tailgait", "big-tree"],
            [],
            "cross-domain",
            """
AgentMail is part of Eric's communication stack.

## Known Address
The source prompt lists ericanderson@agentmail.to.
""",
        ),
        (
            "Tools/Obsidian.md",
            "Obsidian",
            ["tool", "ahs", "usa-rehab", "tailgait", "big-tree"],
            [],
            "cross-domain",
            """
Obsidian is the local Markdown vault interface for this second brain.

## Agent Use
Notes should use YAML frontmatter, wikilinks, and provenance sections so Hermes, Codex, and future agents can resolve canonical context.
""",
        ),
        (
            "Tools/ffmpeg.md",
            "ffmpeg",
            ["tool", "tailgait"],
            [],
            "tailgait",
            """
ffmpeg is part of the [[Tailgait Clip Pipeline]].

## Uses
- Stitch and reframe raw `.insv` footage.
- Assemble exactly 30-second clips with intro, outro, and captions alongside [[Hermes]].
""",
        ),
        (
            "Tools/Dropbox.md",
            "Dropbox",
            ["tool", "tailgait"],
            [],
            "tailgait",
            """
Dropbox stores Tailgait footage.

## Workflow Context
Raw Tailgait media should be treated as source footage for [[Tailgait Clip Pipeline]].
""",
        ),
    ]
    for path, title, tags, aliases, domain, body in tool_notes:
        notes.append(note(path, title, tags, aliases, domain, "canonical", body))

    procedure_notes = [
        (
            "Procedures/AHS Project Workflow.md",
            "AHS Project Workflow",
            ["procedure", "ahs"],
            ["Matterport to PSOW"],
            "ahs",
            """
This is the canonical AHS project workflow.

## Stages
1. Capture or receive a [[Matterport]] scan.
2. Build [[Chief Architect]] plans.
3. Create the PSOW package: Plan of Services and Outcomes.
4. Solicit contractor bids.
5. Supervise project execution.

## Known Pain Point
The hardest stated part is finding contractors nationwide for complex multi-party projects.

## Contractor Sourcing
Preferred franchise contractor targets include [[Amramp]], [[101 Mobility]], [[Next Day Access]], and [[Mobility Plus]]. Before any outreach, check [[AHS Do Not Contact List]] and get explicit approval under [[External Action Approval Policy]].
""",
        ),
        (
            "Procedures/USA Rehab Project Workflow.md",
            "USA Rehab Project Workflow",
            ["procedure", "usa-rehab"],
            ["USA Rehab Job Workflow"],
            "usa-rehab",
            """
This is the canonical USA Rehab project workflow.

## Stages
1. On-site or desk estimate.
2. Job awarded.
3. Pre-construction visit.
4. Exhibit A using [[Chief Architect]] plans.
5. Contract signed.
6. Materials ordered.
7. Materials in stock.
8. Crew scheduled.
9. Construction, normally 1-4 days according to source.
10. Field photos and documentation.
11. Homeowner sign-off.
12. Invoice.

## Agent Note
Do not skip field photos/docs or sign-off when summarizing job status; those are explicit workflow stages.
""",
        ),
        (
            "Procedures/Tailgait Clip Pipeline.md",
            "Tailgait Clip Pipeline",
            ["procedure", "tailgait"],
            ["Tailgait Video Pipeline"],
            "tailgait",
            """
This is the canonical Tailgait clip pipeline.

## Stage 1 - Normalize Footage
Use [[ffmpeg]] to stitch and reframe raw `.insv` footage into flat MP4 files.

## Stage 2 - Find Moments
Use [[Twelve Labs]] to index flat MP4 files and identify the best crowd or energy moments. [[Overlap]] is also in the toolset, especially for speech-based clipping.

## Stage 3 - Build Clip
Use [[Hermes]] and [[ffmpeg]] to build an exactly 30-second clip with intro, outro, and captions.

## Storage
Tailgait footage is stored on [[Dropbox]].
""",
        ),
        (
            "Procedures/Walk Memo Processing Pipeline.md",
            "Walk Memo Processing Pipeline",
            ["procedure", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["Voice Memo Pipeline"],
            "cross-domain",
            """
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
""",
        ),
        (
            "Procedures/Daily Focus Brief.md",
            "Daily Focus Brief",
            ["procedure", "ahs", "usa-rehab", "tailgait", "big-tree"],
            [],
            "cross-domain",
            """
The Daily Focus Brief is a scheduled context email for Eric.

## Schedule
The source prompt says it is sent by cron at 7:30AM EDT.

## Recipients
- eric@accessiblehousingservices.com
- ericanderson@comcast.net

## Agent Use
When updating this workflow, check [[Hermes]], [[AgentMail]], and [[SOURCE-MANIFEST]] for current routing assumptions.
""",
        ),
    ]
    for path, title, tags, aliases, domain, body in procedure_notes:
        notes.append(note(path, title, tags, aliases, domain, "canonical", body))

    decision_notes = [
        (
            "Decisions/AHS Do Not Contact List.md",
            "AHS Do Not Contact List",
            ["decision", "ahs", "restricted-outreach"],
            ["AHS DNC"],
            "ahs",
            "active",
            """
Eric's source prompt explicitly says not to contact these organizations for AHS contractor outreach:

- [[Ethos Access]]
- [[VGM HOMELINK]]
- [[CorHome]]
- [[All Access]]
- [[ATF Medical]]

## Rationale
No rationale is provided in the source. Preserve the restriction exactly until Eric provides a newer source.

## Agent Instruction
If a task could involve outreach to one of these organizations, stop and ask Eric before proceeding.
""",
        ),
        (
            "Decisions/External Action Approval Policy.md",
            "External Action Approval Policy",
            ["decision", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["Ask Before Acting Externally"],
            "cross-domain",
            "active",
            """
Agents must ask for explicit approval before acting externally.

## Applies To
- Contacting people or companies.
- Sending email or Telegram messages.
- Changing third-party systems.
- Starting payments, purchases, submissions, or public posts.

## Source Instruction
The build prompt states: "If acting externally, ask for explicit approval first."
""",
        ),
        (
            "Decisions/Preserve Max Droplet Boundary.md",
            "Preserve Max Droplet Boundary",
            ["decision", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["Do Not Touch Home Max"],
            "cross-domain",
            "active",
            """
Max shares the Droplet but has a separate Hermes instance.

## Boundary
Do not touch `/home/max`.

## Operational Meaning
Codex, Hermes, and future agents should treat `/home/max` as outside Eric's workspace unless Eric and Max provide explicit permission.
""",
        ),
        (
            "Decisions/Use Obsidian Vault As Canonical Agent Memory.md",
            "Use Obsidian Vault As Canonical Agent Memory",
            ["decision", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["Vault As Memory"],
            "cross-domain",
            "active",
            """
This repository is the local Obsidian-compatible second brain for Eric Anderson.

## Rationale
The vault is intended to function as a durable context layer for [[Hermes]], [[Codex]], and future AI agents.

## Operating Rule
Prefer source-backed canonical notes over shallow stubs or chat-history recall.
""",
        ),
        (
            "Decisions/Source Backing Policy.md",
            "Source Backing Policy",
            ["decision", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["Provenance Policy"],
            "cross-domain",
            "active",
            """
Agents should not assume facts that are not supported by linked notes or source records.

## Required Practice
- Check [[SOURCE-MANIFEST]] for source freshness.
- Add provenance to every canonical note.
- Use `status: unverified` for speculative or unverified facts.
- Keep raw inputs in `raw/` until processed.
""",
        ),
    ]
    for path, title, tags, aliases, domain, status, body in decision_notes:
        notes.append(note(path, title, tags, aliases, domain, status, body))

    project_notes = [
        (
            "Projects/AHS Contractor Network Expansion.md",
            "AHS Contractor Network Expansion",
            ["project", "ahs"],
            ["Contractor Network"],
            "ahs",
            "active",
            """
This project tracks AHS contractor network growth.

## Problem
The biggest AHS pain point is finding contractors nationwide for complex multi-party projects.

## Target Contractor Types
Start with the target franchise contractors in the source prompt: [[Amramp]], [[101 Mobility]], [[Next Day Access]], and [[Mobility Plus]].

## Constraints
Before outreach, check [[AHS Do Not Contact List]] and ask for explicit approval under [[External Action Approval Policy]].
""",
        ),
        (
            "Projects/USA Rehab Job Lifecycle System.md",
            "USA Rehab Job Lifecycle System",
            ["project", "usa-rehab"],
            ["USA Rehab Workflow System"],
            "usa-rehab",
            "active",
            """
This project tracks the USA Rehab job lifecycle from estimate to invoice.

## Canonical Workflow
Use [[USA Rehab Project Workflow]] as the operating sequence.

## Important Artifacts
- Estimate.
- Exhibit A from [[Chief Architect]] plans.
- Contract.
- Field photos/docs.
- Homeowner sign-off.
- Invoice.
""",
        ),
        (
            "Projects/Tailgait Automated Clip Pipeline.md",
            "Tailgait Automated Clip Pipeline",
            ["project", "tailgait"],
            ["Tailgait Clips"],
            "tailgait",
            "active",
            """
This project tracks Tailgait automation for exactly 30-second social clips.

## Pipeline
Use [[Tailgait Clip Pipeline]] as the canonical workflow.

## Toolchain
The prompt identifies [[ffmpeg]], [[Twelve Labs]], [[Overlap]], [[Hermes]], and [[Dropbox]] as relevant tools or storage.
""",
        ),
        (
            "Projects/Big Tree Rd Buyout.md",
            "Big Tree Rd Buyout",
            ["project", "big-tree"],
            ["Big Tree Buyout"],
            "big-tree",
            "active",
            """
This project tracks Eric's goal to buy out the sisters' ownership shares in [[Big Tree Rd Domain]].

## Known Ownership
- [[Eric Anderson]]: 50%.
- [[Barbara Darul]]: 25%.
- [[Pamela Johnson]]: 25%.

## Constraint
[[Chuck Sienk]] may be an intel source, but must not be used as a messenger.
""",
        ),
        (
            "Projects/Daily Focus Brief Operations.md",
            "Daily Focus Brief Operations",
            ["project", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["Focus Brief Ops"],
            "cross-domain",
            "active",
            """
This project tracks operations around the [[Daily Focus Brief]].

## Known Schedule
Cron at 7:30AM EDT.

## Known Recipients
- eric@accessiblehousingservices.com.
- ericanderson@comcast.net.
""",
        ),
    ]
    for path, title, tags, aliases, domain, status, body in project_notes:
        notes.append(note(path, title, tags, aliases, domain, status, body))

    opportunities = [
        (
            "Opportunities/Dark Web Breach Monitoring For Attorney Client.md",
            "Dark Web Breach Monitoring For Attorney Client",
            ["opportunity", "ahs", "usa-rehab"],
            ["Attorney Breach Monitoring"],
            "cross-domain",
            """
This is a future opportunity stub for breach monitoring services.

## Source Signal
The prompt lists [[Breachsense]], Have I Been Pwned, and [[Ransomware Live]] as discovered resources related to breach and ransomware visibility.

## Next Step
Validate the attorney-client use case, compliance constraints, and data handling requirements before any implementation.
""",
        ),
        (
            "Opportunities/Twelve Labs Video Indexing For Tailgait.md",
            "Twelve Labs Video Indexing For Tailgait",
            ["opportunity", "tailgait"],
            ["Tailgait Twelve Labs"],
            "tailgait",
            """
This is a future opportunity stub for using [[Twelve Labs]] to index Tailgait footage.

## Source Signal
The prompt names Twelve Labs as the Stage 2 indexing system for best crowd and energy moments.

## Next Step
Design the indexing schema and moment-selection criteria after sample footage is available.
""",
        ),
        (
            "Opportunities/MPP Machine Payments Integration.md",
            "MPP Machine Payments Integration",
            ["opportunity", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["Machine Payments"],
            "cross-domain",
            """
This is a future opportunity stub for [[MPP]] machine-to-machine payments.

## Source Signal
The prompt describes MPP as machine-to-machine payments via HTTP 402 with Tempo and Stripe.

## Next Step
Identify a low-risk internal workflow where agent-initiated payment authorization could be modeled without moving money.
""",
        ),
        (
            "Opportunities/Voice Memo To Second Brain Pipeline.md",
            "Voice Memo To Second Brain Pipeline",
            ["opportunity", "ahs", "usa-rehab", "tailgait", "big-tree"],
            ["Voice Memo Pipeline Opportunity"],
            "cross-domain",
            """
This is a future opportunity stub for converting Eric's voice memos into canonical vault notes.

## Source Signal
The required procedures include [[Walk Memo Processing Pipeline]].

## Next Step
Create an ingestion template that separates raw transcript, extracted claims, research questions, and final canonical notes.
""",
        ),
        (
            "Opportunities/Ransomware Live Early Warning System.md",
            "Ransomware Live Early Warning System",
            ["opportunity", "ahs", "usa-rehab"],
            ["Ransomware Early Warning"],
            "cross-domain",
            """
This is a future opportunity stub for using [[Ransomware Live]] as an early warning signal.

## Source Signal
The prompt describes ransomware.live as a free public API tracking 350+ ransomware groups.

## Next Step
Define who would receive alerts, what constitutes actionable risk, and how false positives would be handled.
""",
        ),
    ]
    for path, title, tags, aliases, domain, body in opportunities:
        notes.append(note(path, title, tags, aliases, domain, "stub", body))

    for path, content in notes:
        write(path, content)

    source_manifest = f"""# Source Manifest

This manifest tracks source records used to build and update the vault.

## Sources

| ID | Source | Type | Date Added | Freshness | Used For |
| --- | --- | --- | --- | --- | --- |
| S1 | [[BRAIN-PROMPT]] | User-provided build prompt in repository | {TODAY} | Current as of {TODAY}; verify before external action or pricing decisions | Initial vault structure, facts, workflows, contacts, tools, decisions |

## Source Freshness Rules

- Treat S1 as authoritative for the initial vault build.
- For prices, vendors, laws, APIs, schedules, product capabilities, and public facts, refresh with primary sources before acting.
- For private business preferences and relationship constraints, preserve S1 until Eric provides a newer private source.
- Add each new source here before converting it into canonical notes.
"""
    write("SOURCE-MANIFEST.md", source_manifest)

    ingestion_log = f"""# Ingestion Log

| Timestamp UTC | Source | Action | Notes |
| --- | --- | --- | --- |
| {NOW} | [[BRAIN-PROMPT]] | Initial build | Parsed user-provided second brain build prompt into canonical People, Companies, Domains, Tools, Decisions, Procedures, Projects, Opportunities, wiki index, source manifest, and state files. |

## Current State

- Initial source processed: S1.
- Validation script: `scripts/validate_vault.py`.
- Latest validation report: [[VALIDATION-REPORT]].
"""
    write("INGESTION-LOG.md", ingestion_log)

    readme = """# Eric Anderson Second Brain

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

1. Start at [[wiki/index]].
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
"""
    write("README.md", readme)

    index_sections = {
        "People": [
            "Eric Anderson",
            "Barbara Darul",
            "Pamela Johnson",
            "Chuck Sienk",
            "Ken Owens",
            "Vincent Russo",
            "Robert Gonzales",
            "Max Droplet Co-user",
        ],
        "Companies": [
            "Accessible Housing Services",
            "USA Rehab",
            "Liberty Mutual",
            "Travelers",
            "Amramp",
            "101 Mobility",
            "Next Day Access",
            "Mobility Plus",
            "Elevator Works",
        ],
        "Domains": ["AHS Domain", "USA Rehab Domain", "Tailgait Domain", "Big Tree Rd Domain"],
        "Projects": [
            "AHS Contractor Network Expansion",
            "USA Rehab Job Lifecycle System",
            "Tailgait Automated Clip Pipeline",
            "Big Tree Rd Buyout",
            "Daily Focus Brief Operations",
        ],
        "Tools": [
            "Hermes",
            "Codex",
            "Chief Architect",
            "Matterport",
            "Twelve Labs",
            "Overlap",
            "Revid",
            "MPP",
            "Breachsense",
            "Ransomware Live",
            "AgentMail",
            "Obsidian",
        ],
        "Procedures": [
            "AHS Project Workflow",
            "USA Rehab Project Workflow",
            "Tailgait Clip Pipeline",
            "Walk Memo Processing Pipeline",
            "Daily Focus Brief",
        ],
        "Decisions": [
            "AHS Do Not Contact List",
            "External Action Approval Policy",
            "Preserve Max Droplet Boundary",
            "Use Obsidian Vault As Canonical Agent Memory",
            "Source Backing Policy",
        ],
        "Opportunities": [
            "Dark Web Breach Monitoring For Attorney Client",
            "Twelve Labs Video Indexing For Tailgait",
            "MPP Machine Payments Integration",
            "Voice Memo To Second Brain Pipeline",
            "Ransomware Live Early Warning System",
        ],
    }
    index = frontmatter(
        "Vault Index",
        ["index", "ahs", "usa-rehab", "tailgait", "big-tree"],
        ["Second Brain Index"],
        "cross-domain",
        "canonical",
    )
    index += "# Vault Index\n\n"
    index += "Start here for Eric Anderson's source-backed operating memory.\n\n"
    index += "## Core Orientation\n"
    index += "- [[Eric Anderson]]\n- [[SOURCE-MANIFEST]]\n- [[INGESTION-LOG]]\n- [[VALIDATION-REPORT]]\n- [[COMPLETION-AUDIT]]\n\n"
    for section, links in index_sections.items():
        index += f"## {section}\n"
        for link in links:
            index += f"- [[{link}]]\n"
        index += "\n"
    index += "## Provenance\n"
    index += f"{SOURCE_LINE}\n"
    write("wiki/index.md", index)

    completion_audit = f"""# Completion Audit

Generated: {NOW}

## Requirement Mapping

| Requirement | Evidence | Status |
| --- | --- | --- |
| Working Obsidian-compatible vault at this location | [[wiki/index]], [[README]], folder structure in repository root | Complete |
| Required directories exist | `People/`, `Companies/`, `Projects/`, `Domains/`, `Tools/`, `Decisions/`, `Procedures/`, `Opportunities/`, `raw/`, `wiki/` | Complete |
| People notes created | [[Eric Anderson]], [[Barbara Darul]], [[Pamela Johnson]], [[Chuck Sienk]], [[Ken Owens]], [[Vincent Russo]], [[Robert Gonzales]], [[Max Droplet Co-user]] | Complete |
| Company notes created | [[Accessible Housing Services]], [[USA Rehab]], [[Liberty Mutual]], [[Travelers]], [[Amramp]], [[101 Mobility]], [[Next Day Access]], [[Mobility Plus]], [[Elevator Works]] | Complete |
| AHS domain content | [[AHS Domain]], [[AHS Project Workflow]], [[AHS Do Not Contact List]] | Complete |
| USA Rehab domain content | [[USA Rehab Domain]], [[USA Rehab Project Workflow]] | Complete |
| Tailgait domain content | [[Tailgait Domain]], [[Tailgait Clip Pipeline]], [[Tailgait Automated Clip Pipeline]] | Complete |
| Big Tree Rd domain content | [[Big Tree Rd Domain]], [[Big Tree Rd Buyout]] | Complete |
| Tool notes created | [[Hermes]], [[Codex]], [[Chief Architect]], [[Matterport]], [[Twelve Labs]], [[Overlap]], [[Revid]], [[MPP]], [[Breachsense]], [[Ransomware Live]], [[AgentMail]], [[Obsidian]] | Complete |
| Procedure notes created | [[AHS Project Workflow]], [[USA Rehab Project Workflow]], [[Tailgait Clip Pipeline]], [[Walk Memo Processing Pipeline]], [[Daily Focus Brief]] | Complete |
| Opportunity stubs created | [[Dark Web Breach Monitoring For Attorney Client]], [[Twelve Labs Video Indexing For Tailgait]], [[MPP Machine Payments Integration]], [[Voice Memo To Second Brain Pipeline]], [[Ransomware Live Early Warning System]] | Complete |
| Source-backed notes | Every generated canonical note includes a `## Provenance` section citing S1 in [[SOURCE-MANIFEST]] | Complete |
| Agent instructions captured | [[README]], [[Source Backing Policy]], [[External Action Approval Policy]], [[AHS Do Not Contact List]] | Complete |
| Validation hard gates | [[VALIDATION-REPORT]] after running `python3 scripts/validate_vault.py` | Complete after PASS report |
| Ingestion log and state current | [[INGESTION-LOG]], `state.json` | Complete |
| Master index exists | [[wiki/index]] | Complete |

## Remaining Issue Policy

The vault should not be declared complete unless [[VALIDATION-REPORT]] reports PASS.
"""
    write("COMPLETION-AUDIT.md", completion_audit)

    raw_inbox = f"""# Raw Inbox

Drop unprocessed source material here before converting it into canonical notes.

## Current Raw Sources

- The initial source is stored at [[BRAIN-PROMPT]] and tracked as S1 in [[SOURCE-MANIFEST]].

## Processing Rule

After processing a raw source, update [[INGESTION-LOG]], [[SOURCE-MANIFEST]], `state.json`, and any affected canonical notes.
"""
    write("raw/INBOX.md", raw_inbox)

    state = {
        "vault_name": "second-brain",
        "generated_at": NOW,
        "last_updated": TODAY,
        "source_ids": [SOURCE_ID],
        "source_manifest": "SOURCE-MANIFEST.md",
        "ingestion_log": "INGESTION-LOG.md",
        "validation_report": "VALIDATION-REPORT.md",
        "completion_audit": "COMPLETION-AUDIT.md",
        "canonical_directories": [
            "People",
            "Companies",
            "Projects",
            "Domains",
            "Tools",
            "Decisions",
            "Procedures",
            "Opportunities",
            "wiki",
        ],
        "agent_rules": [
            "Do not assume facts not present in linked notes or sources.",
            "Check SOURCE-MANIFEST.md for source freshness.",
            "Ask for explicit approval before external action.",
            "Respect AHS do-not-contact list.",
            "Do not touch /home/max.",
        ],
        "last_validation": {
            "status": "pending",
            "command": "python3 scripts/validate_vault.py",
            "report": "VALIDATION-REPORT.md",
        },
    }
    write("state.json", json.dumps(state, indent=2))

    validation_report = f"""# Validation Report

Generated: {NOW}

Status: PENDING

Run `python3 scripts/validate_vault.py` to update this report.
"""
    write("VALIDATION-REPORT.md", validation_report)


if __name__ == "__main__":
    main()
