# fig-repo-23: MCP Authentication Crisis

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-23 |
| **Title** | MCP Authentication Crisis: 85% of Servers Insecure |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/mcp-security-production-research.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Data-Viz) |

## Purpose

Visualize the authentication distribution across 500+ deployed MCP servers, highlighting that 85% use inadequate authentication methods (none or static secrets), with only 8.5% implementing the recommended OAuth standard.

## Key Message

85% of deployed MCP servers fail basic authentication standards — the Nov 2025 MCP spec mandates OAuth 2.1 but adoption lags by 6-12 months.

## Visual Concept

Data-viz layout with horizontal bar chart showing authentication method distribution, a split bar highlighting the 85% insecure vs 15% adequate divide, and a timeline showing the spec mandate vs actual adoption gap.

```
+-----------------------------------------------------------------------+
|  MCP AUTHENTICATION CRISIS                                             |
|  ■ Survey of 500+ Deployed Servers (Guo et al. 2025)                  |
+-----------------------------------------------------------------------+
|                                                                        |
|  ████████████████████████████████  32%  No auth (CRITICAL)             |
|  ██████████████████████████████████████████████████████  53%  Static   |
|  ████████  8.5%  OAuth 2.0/2.1 (RECOMMENDED)                          |
|  ████  4%  mTLS / certificate-based                                    |
|  ██  2.5%  Other                                                       |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │          85% INSECURE                    15% ADEQUATE           │   |
|  │  ████████████████████████████████████  │  ██████████           │   |
|  └─────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  MCP SPEC MANDATE TIMELINE:                                            |
|  ─────────────────────────                                             |
|  Mar 2025: OAuth 2.1 mandated in spec                                  |
|  Nov 2025: RFC 8707 resource indicators added                          |
|  Feb 2026: Only 8.5% compliance                                        |
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
    content: "MCP AUTHENTICATION CRISIS"
    role: title

  - id: chart_zone
    bounds: [80, 160, 1760, 400]
    role: data_visualization

  - id: summary_zone
    bounds: [80, 600, 1760, 140]
    role: callout_box

  - id: timeline_zone
    bounds: [80, 780, 1760, 240]
    role: data_flow

anchors:
  - id: bar_no_auth
    position: [120, 180]
    size: [1120, 60]
    role: processing_stage
    label: "32% No auth (CRITICAL)"

  - id: bar_static
    position: [120, 260]
    size: [1856, 60]
    role: processing_stage
    label: "53% Static secrets"

  - id: bar_oauth
    position: [120, 340]
    size: [298, 60]
    role: processing_stage
    label: "8.5% OAuth 2.0/2.1"

  - id: bar_mtls
    position: [120, 420]
    size: [140, 60]
    role: processing_stage
    label: "4% mTLS"

  - id: bar_other
    position: [120, 500]
    size: [88, 60]
    role: processing_stage
    label: "2.5% Other"

  - id: summary_bar
    position: [80, 620]
    size: [1760, 100]
    role: callout_box
    label: "85% INSECURE | 15% ADEQUATE"

  - id: timeline_mar_2025
    position: [200, 820]
    size: [400, 60]
    role: data_flow
    label: "Mar 2025: OAuth 2.1 mandated"

  - id: timeline_nov_2025
    position: [700, 820]
    size: [400, 60]
    role: data_flow
    label: "Nov 2025: RFC 8707 added"

  - id: timeline_feb_2026
    position: [1200, 820]
    size: [400, 60]
    role: data_flow
    label: "Feb 2026: 8.5% compliance"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| No auth bar | `processing_stage` | 32% of servers with no authentication |
| Static secrets bar | `processing_stage` | 53% of servers using static API keys/tokens |
| OAuth bar | `processing_stage` | 8.5% of servers implementing OAuth 2.0/2.1 |
| mTLS bar | `processing_stage` | 4% of servers using certificate-based auth |
| Other bar | `processing_stage` | 2.5% of servers using other methods |
| Summary split bar | `callout_box` | 85% insecure vs 15% adequate visual split |
| Spec mandate timeline | `data_flow` | Three key dates showing mandate vs adoption gap |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| No auth + Static | Summary insecure | grouping | "85% INSECURE" |
| OAuth + mTLS + Other | Summary adequate | grouping | "15% ADEQUATE" |
| Mar 2025 | Nov 2025 | timeline | "spec evolution" |
| Nov 2025 | Feb 2026 | timeline | "adoption lag" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "SECURITY DIVIDE" | 85% insecure (no auth + static secrets) vs 15% adequate (OAuth, mTLS, other) | middle-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "32% No auth"
- Label 2: "53% Static secrets"
- Label 3: "8.5% OAuth 2.0/2.1"
- Label 4: "4% mTLS"
- Label 5: "2.5% Other"
- Label 6: "85% INSECURE"
- Label 7: "15% ADEQUATE"
- Label 8: "CRITICAL"
- Label 9: "RECOMMENDED"
- Label 10: "Mar 2025: OAuth mandated"
- Label 11: "Nov 2025: RFC 8707 added"
- Label 12: "Feb 2026: 8.5% compliance"

### Caption (for embedding in documentation)

MCP authentication distribution across 500+ deployed servers showing 85% insecure (32% no auth, 53% static secrets) vs 8.5% OAuth compliance, from Guo et al. 2025 survey.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color.
5. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 23." or any numbered academic caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. All percentages are from Guo et al. 2025 survey of 500+ servers. Do NOT fabricate sources.
9. 32% no auth, 53% static secrets, 8.5% OAuth, 4% mTLS, 2.5% other. These are EXACT values.
10. The 85% "insecure" categorization combines no-auth (32%) + static secrets (53%).
11. OAuth 2.1 was mandated in the March 2025 MCP spec update. Do NOT say "2024."
12. Do NOT show specific server names or companies as insecure.

## Alt Text

Horizontal bar chart showing MCP authentication distribution across 500-plus deployed servers: 32 percent with no authentication, 53 percent using static secrets, 8.5 percent implementing OAuth, 4 percent using mTLS, highlighting that 85 percent of servers are insecure.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![MCP authentication distribution showing 85% of servers are insecure.](docs/figures/repo-figures/assets/fig-repo-23-mcp-auth-crisis.jpg)

*Figure 23. MCP authentication crisis: 85% of 500+ deployed servers use inadequate authentication, from Guo et al. 2025 survey.*

### From this figure plan (relative)

![MCP authentication crisis](../assets/fig-repo-23-mcp-auth-crisis.jpg)

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided
- [x] Audience level correct (L3)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
