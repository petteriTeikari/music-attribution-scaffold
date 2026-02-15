# fig-repo-31: AAIF Governance Structure

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-31 |
| **Title** | AAIF Governance Structure: MCP Under Linux Foundation |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/mcp-security-production-research.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Show the governance structure of the Agentic AI Foundation (AAIF) under the Linux Foundation, including platinum members, the Technical Steering Committee, and how specification changes flow from RFC to release.

## Key Message

MCP governance moved from single-company (Anthropic) to multi-stakeholder (AAIF with 5 platinum members) -- specification changes now require consensus across competing interests.

## Visual Concept

Steps layout showing the hierarchical governance structure flowing from Linux Foundation umbrella through AAIF to its constituent parts: platinum members, Technical Steering Committee, specification lifecycle, and governed protocols. A callout bar at the bottom highlights the single-company to multi-stakeholder transition timeline.

```
+-----------------------------------------------------------------------+
|  AAIF GOVERNANCE STRUCTURE                                             |
|  ■ MCP Under Linux Foundation (Dec 2025)                               |
+-----------------------------------------------------------------------+
|                                                                        |
|  LINUX FOUNDATION                                                      |
|  └── AGENTIC AI FOUNDATION (AAIF)                                      |
|       │                                                                |
|       ├── PLATINUM MEMBERS                                             |
|       │   ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐                              |
|       │   │AWS│ │ANT│ │GOO│ │MSF│ │OAI│                              |
|       │   └───┘ └───┘ └───┘ └───┘ └───┘                              |
|       │                                                                |
|       ├── TECHNICAL STEERING COMMITTEE                                 |
|       │   Elected maintainers                                          |
|       │   Formal RFC process                                           |
|       │                                                                |
|       └── SPECIFICATION LIFECYCLE                                      |
|           RFC → Review → Vote → Release                                |
|                                                                        |
|  GOVERNED PROTOCOLS:                                                   |
|  ┌──────────────┐  ┌──────────────┐                                   |
|  │ MCP          │  │ A2A          │                                   |
|  │ Tool layer   │  │ Coordination │                                   |
|  └──────────────┘  └──────────────┘                                   |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  Single-company → Multi-stakeholder governance in 13 months    │   |
|  └─────────────────────────────────────────────────────────────────┘   |
+-----------------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 120]
    content: "AAIF GOVERNANCE STRUCTURE"
    role: title

  - id: hierarchy_zone
    bounds: [80, 140, 1760, 540]
    role: governance_hierarchy

  - id: protocols_zone
    bounds: [80, 720, 1760, 160]
    role: protocol_panel

  - id: callout_zone
    bounds: [80, 920, 1760, 100]
    role: callout_box

anchors:
  - id: linux_foundation
    position: [80, 160]
    size: [1760, 50]
    role: governance_tier
    label: "LINUX FOUNDATION"

  - id: aaif
    position: [160, 230]
    size: [1600, 50]
    role: governance_tier
    label: "AGENTIC AI FOUNDATION (AAIF)"

  - id: platinum_heading
    position: [240, 310]
    size: [600, 40]
    role: section_heading
    label: "PLATINUM MEMBERS"

  - id: member_aws
    position: [260, 370]
    size: [200, 60]
    role: entity
    label: "AWS"

  - id: member_anthropic
    position: [500, 370]
    size: [200, 60]
    role: entity
    label: "Anthropic"

  - id: member_google
    position: [740, 370]
    size: [200, 60]
    role: entity
    label: "Google"

  - id: member_microsoft
    position: [980, 370]
    size: [200, 60]
    role: entity
    label: "Microsoft"

  - id: member_openai
    position: [1220, 370]
    size: [200, 60]
    role: entity
    label: "OpenAI"

  - id: tsc_heading
    position: [240, 470]
    size: [600, 40]
    role: section_heading
    label: "TECHNICAL STEERING COMMITTEE"

  - id: tsc_elected
    position: [260, 520]
    size: [500, 30]
    role: data_flow
    label: "Elected maintainers"

  - id: tsc_rfc
    position: [260, 555]
    size: [500, 30]
    role: data_flow
    label: "Formal RFC process"

  - id: spec_heading
    position: [240, 620]
    size: [600, 40]
    role: section_heading
    label: "SPECIFICATION LIFECYCLE"

  - id: spec_rfc
    position: [260, 670]
    size: [160, 40]
    role: processing_stage
    label: "RFC"

  - id: spec_review
    position: [460, 670]
    size: [160, 40]
    role: processing_stage
    label: "Review"

  - id: spec_vote
    position: [660, 670]
    size: [160, 40]
    role: processing_stage
    label: "Vote"

  - id: spec_release
    position: [860, 670]
    size: [160, 40]
    role: processing_stage
    label: "Release"

  - id: flow_rfc_review
    from: spec_rfc
    to: spec_review
    type: arrow
    label: ""

  - id: flow_review_vote
    from: spec_review
    to: spec_vote
    type: arrow
    label: ""

  - id: flow_vote_release
    from: spec_vote
    to: spec_release
    type: arrow
    label: ""

  - id: protocols_heading
    position: [80, 730]
    size: [600, 40]
    role: section_heading
    label: "GOVERNED PROTOCOLS:"

  - id: protocol_mcp
    position: [100, 790]
    size: [400, 80]
    role: processing_stage
    label: "MCP — Tool layer"

  - id: protocol_a2a
    position: [560, 790]
    size: [400, 80]
    role: processing_stage
    label: "A2A — Coordination"

  - id: timeline_bar
    position: [80, 920]
    size: [1760, 100]
    role: callout_box
    label: "Single-company to multi-stakeholder in 13 months"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Linux Foundation | `governance_tier` | Top-level umbrella organization |
| AAIF | `governance_tier` | Agentic AI Foundation, sub-foundation under Linux Foundation |
| Platinum Members | `entity` | AWS, Anthropic, Google, Microsoft, OpenAI |
| Technical Steering Committee | `section_heading` | Elected maintainers with formal RFC process |
| Specification Lifecycle | `processing_stage` | RFC to Review to Vote to Release pipeline |
| MCP Protocol | `processing_stage` | Model Context Protocol — tool layer |
| A2A Protocol | `processing_stage` | Agent-to-Agent — coordination layer |
| Timeline callout | `callout_box` | 13-month transition from single-company to multi-stakeholder |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Linux Foundation | AAIF | hierarchy | "umbrella" |
| AAIF | Platinum Members | hierarchy | "members" |
| AAIF | TSC | hierarchy | "governance body" |
| AAIF | Spec Lifecycle | hierarchy | "process" |
| RFC | Review | arrow | "submit" |
| Review | Vote | arrow | "approve" |
| Vote | Release | arrow | "ratify" |
| AAIF | MCP | governance | "governs" |
| AAIF | A2A | governance | "governs" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "TRANSITION" | Single-company (Anthropic) to multi-stakeholder governance in 13 months (Nov 2024 to Dec 2025) | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "LINUX FOUNDATION"
- Label 2: "AGENTIC AI FOUNDATION"
- Label 3: "PLATINUM MEMBERS"
- Label 4: "AWS"
- Label 5: "Anthropic"
- Label 6: "Google"
- Label 7: "Microsoft"
- Label 8: "OpenAI"
- Label 9: "TECHNICAL STEERING COMMITTEE"
- Label 10: "Elected maintainers"
- Label 11: "Formal RFC process"
- Label 12: "SPECIFICATION LIFECYCLE"
- Label 13: "RFC"
- Label 14: "Review"
- Label 15: "Vote"
- Label 16: "Release"
- Label 17: "GOVERNED PROTOCOLS:"
- Label 18: "MCP — Tool layer"
- Label 19: "A2A — Coordination"
- Label 20: "13 months transition"

### Caption (for embedding in documentation)

AAIF governance structure under Linux Foundation with five platinum members (AWS, Anthropic, Google, Microsoft, OpenAI), Technical Steering Committee, and formal RFC-to-release specification lifecycle governing both MCP and A2A protocols.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color.
5. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 31." or any numbered academic caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. AAIF platinum members are: AWS, Anthropic, Google, Microsoft, OpenAI. Do NOT add or remove members.
9. The AAIF was formed in December 2025. Do NOT claim earlier dates.
10. Both MCP and A2A are under AAIF governance. Do NOT add other protocols.
11. The Technical Steering Committee uses an elected maintainer model with formal RFC process.
12. Do NOT claim specific voting procedures -- the governance details are still being formalized.
13. "13 months" refers to Nov 2024 (MCP launch) to Dec 2025 (AAIF donation).

## Alt Text

AAIF governance structure showing Linux Foundation umbrella over Agentic AI Foundation with five platinum members AWS Anthropic Google Microsoft and OpenAI, Technical Steering Committee with elected maintainers and formal RFC process, governing both MCP tool protocol and A2A coordination protocol.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![AAIF governance structure with five platinum members and RFC-based specification lifecycle.](docs/figures/repo-figures/assets/fig-repo-31-aaif-governance.jpg)

*Figure 31. AAIF governance: MCP moved from single-company (Anthropic) to multi-stakeholder (Linux Foundation) governance in 13 months.*

### From this figure plan (relative)

![AAIF governance structure](../assets/fig-repo-31-aaif-governance.jpg)

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided
- [x] Audience level correct (L2)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
