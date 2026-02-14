# fig-repo-25: MCP Protocol Evolution Timeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-25 |
| **Title** | MCP Protocol Evolution: From Anthropic Lab to Linux Foundation |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/mcp-security-production-research.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Show the chronological evolution of MCP from initial release through specification updates to AAIF governance, with key milestones marked.

## Key Message

MCP evolved from a single-company project to Linux Foundation-governed standard in 13 months, with security becoming a focus only after adoption.

## Visual Concept

Horizontal timeline with six milestone markers spanning November 2024 to December 2025. Each milestone has a vertical stem connecting to a detail panel below. The final milestone (AAIF donation) is visually emphasized. A callout bar at the bottom highlights the adoption-vs-security gap.

```
+-----------------------------------------------------------------------+
|  MCP PROTOCOL EVOLUTION                                                |
|  ■ From Anthropic Lab to Linux Foundation                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  Nov 2024         Mar 2025         Jun 2025         Sep 2025          |
|     ●──────────────●──────────────●──────────────●                    |
|     │              │              │              │                    |
|  Initial        OAuth 2.1      Streamable     MCP Registry            |
|  Release        Mandated       HTTP Transport  Preview                 |
|  JSON-RPC 2.0                  Elicitation                            |
|                                                                        |
|  Nov 2025                    Dec 2025                                  |
|     ●──────────────────────────●                                      |
|     │                          │                                      |
|  OAuth Resource             AAIF/Linux                                |
|  Server, RFC 8707           Foundation                                 |
|  SEP-1024                   Governance                                |
|  Async Execution            AWS, Google,                              |
|                             Microsoft,                                 |
|                             OpenAI join                                |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  4000+ open-source servers  ·  Major IDE integration           │   |
|  │  Security research lags adoption by 6-12 months                │   |
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
    content: "MCP PROTOCOL EVOLUTION"
    role: title

  - id: timeline_upper
    bounds: [80, 140, 1760, 400]
    role: content_area

  - id: timeline_lower
    bounds: [80, 560, 1760, 280]
    role: content_area

  - id: callout_zone
    bounds: [80, 880, 1760, 140]
    role: callout_box

anchors:
  - id: milestone_nov2024
    position: [160, 200]
    size: [200, 60]
    role: processing_stage

  - id: milestone_mar2025
    position: [520, 200]
    size: [200, 60]
    role: processing_stage

  - id: milestone_jun2025
    position: [880, 200]
    size: [200, 60]
    role: processing_stage

  - id: milestone_sep2025
    position: [1240, 200]
    size: [200, 60]
    role: processing_stage

  - id: milestone_nov2025
    position: [160, 580]
    size: [200, 60]
    role: processing_stage

  - id: milestone_dec2025
    position: [680, 580]
    size: [280, 60]
    role: primary_outcome

  - id: detail_nov2024
    position: [120, 300]
    size: [280, 160]
    role: detail_panel

  - id: detail_mar2025
    position: [480, 300]
    size: [280, 120]
    role: detail_panel

  - id: detail_jun2025
    position: [840, 300]
    size: [280, 120]
    role: detail_panel

  - id: detail_sep2025
    position: [1200, 300]
    size: [280, 120]
    role: detail_panel

  - id: detail_nov2025
    position: [120, 680]
    size: [280, 160]
    role: detail_panel

  - id: detail_dec2025
    position: [640, 680]
    size: [360, 160]
    role: detail_panel

  - id: flow_1
    from: milestone_nov2024
    to: milestone_mar2025
    type: timeline_segment

  - id: flow_2
    from: milestone_mar2025
    to: milestone_jun2025
    type: timeline_segment

  - id: flow_3
    from: milestone_jun2025
    to: milestone_sep2025
    type: timeline_segment

  - id: flow_4
    from: milestone_nov2025
    to: milestone_dec2025
    type: timeline_segment
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Nov 2024 milestone | `processing_stage` | Initial public release -- JSON-RPC 2.0 protocol |
| Mar 2025 milestone | `processing_stage` | OAuth 2.1 mandated (2025-03-26 spec update) |
| Jun 2025 milestone | `processing_stage` | Streamable HTTP transport, Elicitation (2025-06-18) |
| Sep 2025 milestone | `processing_stage` | MCP Registry preview launched |
| Nov 2025 milestone | `processing_stage` | OAuth Resource Server, RFC 8707, SEP-1024, async execution |
| Dec 2025 milestone | `primary_outcome` | AAIF/Linux Foundation governance -- AWS, Anthropic, Google, Microsoft, OpenAI as platinum |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Nov 2024 | Mar 2025 | timeline | 4 months |
| Mar 2025 | Jun 2025 | timeline | 3 months |
| Jun 2025 | Sep 2025 | timeline | 3 months |
| Sep 2025 | Nov 2025 | timeline | 2 months |
| Nov 2025 | Dec 2025 | timeline | 1 month |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ADOPTION vs. SECURITY" | 4000+ open-source servers and major IDE integration as of early 2026. Security research lags adoption by 6-12 months. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Initial Release"
- Label 2: "OAuth 2.1 Mandated"
- Label 3: "Streamable HTTP Transport"
- Label 4: "MCP Registry Preview"
- Label 5: "Resource Server, RFC 8707"
- Label 6: "AAIF/Linux Foundation"
- Label 7: "4000+ open-source servers"
- Label 8: "Security lags adoption"

### Caption (for embedding in documentation)

MCP protocol evolution from November 2024 initial release to December 2025 Linux Foundation governance, showing 13 months of rapid specification development with security research lagging adoption.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color.
5. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 25." or any numbered academic caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. Nov 2024 is the initial PUBLIC release of MCP. Do NOT say it was created in 2024 -- internal development preceded this.
9. OAuth 2.1 was mandated in the March 2025 (2025-03-26) spec update. Do NOT use a different date.
10. Streamable HTTP transport was added in June 2025 (2025-06-18). Do NOT confuse with earlier SSE transport.
11. MCP Registry preview launched September 2025. Do NOT claim it was fully launched.
12. AAIF donation was December 2025. Platinum members: AWS, Anthropic, Google, Microsoft, OpenAI.
13. 4000+ servers is as of early 2026. Do NOT claim higher numbers.

## Alt Text

Timeline showing MCP protocol evolution from November 2024 initial release through March 2025 OAuth 2.1 mandate, June 2025 streamable HTTP, September 2025 registry preview, November 2025 resource indicators, to December 2025 AAIF Linux Foundation governance with AWS, Google, Microsoft, and OpenAI as platinum members.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![MCP protocol evolution timeline from November 2024 to December 2025 Linux Foundation governance.](docs/figures/repo-figures/assets/fig-repo-25-mcp-evolution-timeline.jpg)

*Figure 25. MCP protocol evolution from single-company release to Linux Foundation-governed standard in 13 months.*

### From this figure plan (relative)

![MCP protocol evolution timeline](../assets/fig-repo-25-mcp-evolution-timeline.jpg)

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
