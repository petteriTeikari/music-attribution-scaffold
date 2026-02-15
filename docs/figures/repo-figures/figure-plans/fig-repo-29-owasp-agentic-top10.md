# fig-repo-29: OWASP Agentic AI Top 10 (2026)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-29 |
| **Title** | OWASP Agentic AI Top 10 (2026) |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/mcp-security-production-research.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Present the OWASP Agentic AI Top 10 security risks as a reference for engineers building MCP servers, with each risk mapped to its relevance for the Music Attribution Scaffold.

## Key Message

OWASP's Agentic AI Top 10 provides a structured security checklist -- the scaffold's four-layer defense addresses 7 of 10 risks, with 3 requiring additional investment.

## Visual Concept

Hero layout with a two-column split: left column lists the 7 risks addressed by the scaffold's existing four-layer defense (marked with check indicators), right column lists the 3 risks requiring additional investment (marked with warning indicators). A summary callout bar at the bottom shows the 7/10 vs 3/10 ratio.

```
+-----------------------------------------------------------------------+
|  OWASP AGENTIC AI TOP 10 (2026)                                        |
|  ■ Security Checklist for MCP Servers                                   |
+-----------------------------------------------------------------------+
|                                                                        |
|  ADDRESSED BY SCAFFOLD                    REQUIRES INVESTMENT           |
|  ────────────────────                     ───────────────────           |
|                                                                        |
|  1. Prompt Injection          ✓           8. Supply Chain      ▲       |
|  2. Broken Access Control     ✓           9. Agent Identity    ▲       |
|  3. Tool/Function Misuse      ✓          10. Memory/Context    ▲       |
|  4. Excessive Agency          ✓                                        |
|  5. Insecure Tool Config      ✓                                        |
|  6. Data Poisoning            ✓                                        |
|  7. Insufficient Logging      ✓                                        |
|                                                                        |
|  ✓ = Addressed by four-layer defense                                   |
|  ▲ = Requires additional investment                                    |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  7/10 risks addressed by existing architecture                 │   |
|  │  3/10 require zero-trust infrastructure investment             │   |
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
    content: "OWASP AGENTIC AI TOP 10 (2026)"
    role: title

  - id: addressed_zone
    bounds: [80, 160, 900, 600]
    role: checklist_panel

  - id: investment_zone
    bounds: [1020, 160, 820, 600]
    role: checklist_panel

  - id: legend_zone
    bounds: [80, 780, 1760, 60]
    role: legend

  - id: callout_zone
    bounds: [80, 880, 1760, 140]
    role: callout_box

anchors:
  - id: addressed_heading
    position: [80, 170]
    size: [900, 50]
    role: section_heading
    label: "ADDRESSED BY SCAFFOLD"

  - id: risk_1
    position: [100, 250]
    size: [860, 50]
    role: checklist_item
    label: "1. Prompt Injection"

  - id: risk_2
    position: [100, 310]
    size: [860, 50]
    role: checklist_item
    label: "2. Broken Access Control"

  - id: risk_3
    position: [100, 370]
    size: [860, 50]
    role: checklist_item
    label: "3. Tool/Function Misuse"

  - id: risk_4
    position: [100, 430]
    size: [860, 50]
    role: checklist_item
    label: "4. Excessive Agency"

  - id: risk_5
    position: [100, 490]
    size: [860, 50]
    role: checklist_item
    label: "5. Insecure Tool Config"

  - id: risk_6
    position: [100, 550]
    size: [860, 50]
    role: checklist_item
    label: "6. Data Poisoning"

  - id: risk_7
    position: [100, 610]
    size: [860, 50]
    role: checklist_item
    label: "7. Insufficient Logging"

  - id: investment_heading
    position: [1020, 170]
    size: [820, 50]
    role: section_heading
    label: "REQUIRES INVESTMENT"

  - id: risk_8
    position: [1040, 250]
    size: [780, 50]
    role: checklist_item
    label: "8. Supply Chain"

  - id: risk_9
    position: [1040, 310]
    size: [780, 50]
    role: checklist_item
    label: "9. Agent Identity Spoofing"

  - id: risk_10
    position: [1040, 370]
    size: [780, 50]
    role: checklist_item
    label: "10. Memory/Context Manipulation"

  - id: legend_check
    position: [80, 790]
    size: [400, 40]
    role: legend
    label: "Addressed by four-layer defense"

  - id: legend_warning
    position: [520, 790]
    size: [500, 40]
    role: legend
    label: "Requires additional investment"

  - id: summary_bar
    position: [80, 880]
    size: [1760, 140]
    role: callout_box
    label: "7/10 addressed | 3/10 need investment"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Addressed column | `checklist_panel` | Seven risks covered by scaffold's four-layer defense |
| Investment column | `checklist_panel` | Three risks requiring additional zero-trust infrastructure |
| Risk items 1-7 | `checklist_item` | Individual OWASP risks with addressed indicator |
| Risk items 8-10 | `checklist_item` | Individual OWASP risks with investment-needed indicator |
| Summary bar | `callout_box` | 7/10 vs 3/10 coverage ratio |
| Legend | `legend` | Explains check and warning indicators |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Risks 1-7 | Four-layer defense | mapping | "addressed" |
| Risks 8-10 | Zero-trust infra | mapping | "requires investment" |
| Addressed column | Summary bar | grouping | "7/10" |
| Investment column | Summary bar | grouping | "3/10" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "COVERAGE SUMMARY" | 7/10 risks addressed by existing architecture; 3/10 require zero-trust infrastructure investment | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "ADDRESSED BY SCAFFOLD"
- Label 2: "REQUIRES INVESTMENT"
- Label 3: "1. Prompt Injection"
- Label 4: "2. Broken Access Control"
- Label 5: "3. Tool/Function Misuse"
- Label 6: "4. Excessive Agency"
- Label 7: "5. Insecure Tool Config"
- Label 8: "6. Data Poisoning"
- Label 9: "7. Insufficient Logging"
- Label 10: "8. Supply Chain"
- Label 11: "9. Agent Identity Spoofing"
- Label 12: "10. Memory/Context"
- Label 13: "7/10 risks addressed"
- Label 14: "3/10 require investment"
- Label 15: "Four-layer defense"
- Label 16: "Zero-trust infrastructure"

### Caption (for embedding in documentation)

OWASP Agentic AI Top 10 security checklist showing 7 of 10 risks addressed by the scaffold's four-layer defense architecture, with 3 requiring additional zero-trust infrastructure investment.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color.
5. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 29." or any numbered academic caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. The OWASP Agentic AI Top 10 is version 1.0, released 2026. Do NOT claim earlier dates.
9. The exact list is: 1. Prompt Injection, 2. Broken Access Control, 3. Tool/Function Misuse, 4. Excessive Agency, 5. Insecure Tool Config, 6. Data Poisoning, 7. Insufficient Logging, 8. Supply Chain, 9. Agent Identity Spoofing, 10. Memory/Context Manipulation.
10. The 7/10 vs 3/10 split is the report's assessment, not OWASP's categorization.
11. Do NOT alter the order -- OWASP ranks them by severity.
12. Do NOT confuse with the regular OWASP Top 10 for web applications.

## Alt Text

OWASP Agentic AI Top 10 checklist for MCP servers showing seven of ten risks addressed by the scaffold four-layer defense architecture including prompt injection, broken access control, and tool misuse, with three risks requiring additional investment in supply chain security, agent identity, and memory manipulation defenses.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![OWASP Agentic AI Top 10 checklist showing 7 of 10 risks addressed by scaffold architecture.](docs/figures/repo-figures/assets/fig-repo-29-owasp-agentic-top10.jpg)

*Figure 29. OWASP Agentic AI Top 10 (2026) mapped to scaffold coverage: 7 risks addressed by four-layer defense, 3 requiring additional investment.*

### From this figure plan (relative)

![OWASP Agentic AI Top 10](../assets/fig-repo-29-owasp-agentic-top10.jpg)

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided
- [x] Audience level correct (L3)
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
