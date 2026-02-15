# fig-landscape-29: Regulatory Cascade: EU AI Act to Architecture Requirements

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-29 |
| **Title** | Regulatory Cascade: EU AI Act to Architecture Requirements |
| **Audience** | L3 (Engineer) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

This figure shows how a single legislative clause cascades through four levels -- legislation, codes of practice, technical standards, and architecture requirements -- into specific code-level constraints. It demonstrates that every architecture decision is implicitly a regulatory bet, and that choosing implementation paths now means betting on which regulatory cascade path will dominate.

## Key Message

Every architecture decision is a regulatory bet -- legislation cascades through codes of practice, technical standards, and architecture requirements, creating constraints that compound over time.

## Visual Concept

A top-to-bottom cascade flowchart with four levels, each wider than the one above (inverted pyramid/funnel showing how a single clause expands into many requirements). Level 1 (Legislation) is a single narrow block at the top. Level 2 (Codes of Practice) fans out to 2-3 blocks. Level 3 (Technical Standards) fans out further. Level 4 (Architecture Requirements) is the widest, showing many specific technical constraints. A concrete example trace follows Article 50 (transparency) through all four levels. Coral accent lines connect the cascade paths.

```
+---------------------------------------------------------------+
|  REGULATORY CASCADE                                            |
|  ■ From Legislation to Code-Level Constraints                  |
+---------------------------------------------------------------+
|                                                                |
|  LEVEL 1: LEGISLATION                                          |
|  ┌─────────────────────────────────────────┐                   |
|  │ EU AI Act 2024  │ UK AI Bill │ US EOs    │                   |
|  └────────────┬──────────┬─────────────────┘                   |
|               │          │                                     |
|  LEVEL 2: CODES OF PRACTICE                                    |
|  ┌────────────▼──┐ ┌────▼─────────┐ ┌──────────────┐          |
|  │ GPAI Code of  │ │ Industry     │ │ Voluntary    │          |
|  │ Practice       │ │ Working Grps │ │ Commitments  │          |
|  └───────┬───────┘ └──────┬───────┘ └──────┬───────┘          |
|          │                │                │                   |
|  LEVEL 3: TECHNICAL STANDARDS                                  |
|  ┌───────▼──┐ ┌──────▼──┐ ┌──────▼──┐ ┌──────────┐           |
|  │ ISO/IEC  │ │ IEEE    │ │ W3C     │ │ C2PA     │           |
|  │ 42001    │ │ 3119    │ │ Prov.   │ │ Manifest │           |
|  └────┬─────┘ └───┬────┘ └───┬────┘ └───┬──────┘           |
|       │            │          │           │                    |
|  LEVEL 4: ARCHITECTURE REQUIREMENTS                            |
|  ┌────▼────┐┌─────▼───┐┌────▼────┐┌────▼────┐┌──────────┐   |
|  │Logging  ││Audit    ││Content  ││Provennce││Explain-  │   |
|  │all AI   ││trail    ││labeling ││chain    ││ability   │   |
|  │actions  ││immutble ││at point ││per asset││on demand │   |
|  └─────────┘└─────────┘└─────────┘└─────────┘└──────────┘   |
|                                                                |
|  ─── EXAMPLE TRACE: Article 50 (Transparency) ───             |
|  Art.50 → GPAI Code → C2PA Manifest → Content labeling        |
|         → ISO 42001 → Logging + audit trail                   |
|                                                                |
|  ■ Choosing your architecture NOW = betting on which           |
|    regulatory path will dominate                               |
+---------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: warm_cream

title_block:
  position: [60, 40]
  width: 1800
  height: 80
  elements:
    - type: heading_display
      text: "REGULATORY CASCADE"
    - type: label_editorial
      text: "From Legislation to Code-Level Constraints"

level_1:
  position: [460, 140]
  width: 1000
  height: 100
  label: "LEVEL 1: LEGISLATION"
  elements:
    - { type: decision_point, text: "EU AI Act 2024", x: 0 }
    - { type: decision_point, text: "UK AI Bill", x: 380 }
    - { type: decision_point, text: "US Executive Orders", x: 700 }

level_2:
  position: [260, 280]
  width: 1400
  height: 100
  label: "LEVEL 2: CODES OF PRACTICE"
  elements:
    - { type: processing_stage, text: "GPAI Code of Practice", x: 0 }
    - { type: processing_stage, text: "Industry Working Groups", x: 500 }
    - { type: processing_stage, text: "Voluntary Commitments", x: 1000 }

level_3:
  position: [160, 420]
  width: 1600
  height: 100
  label: "LEVEL 3: TECHNICAL STANDARDS"
  elements:
    - { type: processing_stage, text: "ISO/IEC 42001", x: 0 }
    - { type: processing_stage, text: "IEEE 3119", x: 400 }
    - { type: processing_stage, text: "W3C Provenance", x: 800 }
    - { type: processing_stage, text: "C2PA Manifest", x: 1200 }

level_4:
  position: [60, 560]
  width: 1800
  height: 120
  label: "LEVEL 4: ARCHITECTURE REQUIREMENTS"
  elements:
    - { type: solution_component, text: "Logging all AI actions", x: 0 }
    - { type: solution_component, text: "Immutable audit trail", x: 360 }
    - { type: solution_component, text: "Content labeling at point of creation", x: 720 }
    - { type: solution_component, text: "Provenance chain per asset", x: 1080 }
    - { type: solution_component, text: "Explainability on demand", x: 1440 }

example_trace:
  position: [60, 720]
  width: 1800
  height: 160
  label: "EXAMPLE TRACE: Article 50 (Transparency)"
  elements:
    - { type: data_mono, text: "Article 50 → GPAI Code of Practice → C2PA Manifest → Content labeling at creation" }
    - { type: data_mono, text: "Article 50 → GPAI Code of Practice → ISO 42001 → Logging + immutable audit trail" }
    - { type: callout_bar, text: "One clause, two cascade paths, five architecture requirements" }

insight_callout:
  position: [60, 920]
  width: 1800
  height: 50
  elements:
    - type: callout_bar
      text: "Choosing your architecture NOW = betting on which regulatory path will dominate"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "REGULATORY CASCADE" with coral accent square |
| Subtitle | `label_editorial` | "From Legislation to Code-Level Constraints" |
| Level 1 blocks | `decision_point` | EU AI Act 2024, UK AI Bill, US Executive Orders |
| Level 2 blocks | `processing_stage` | GPAI Code of Practice, Industry Working Groups, Voluntary Commitments |
| Level 3 blocks | `processing_stage` | ISO/IEC 42001, IEEE 3119, W3C Provenance, C2PA Manifest |
| Level 4 blocks | `solution_component` | Logging, audit trail, content labeling, provenance chain, explainability |
| Level labels | `section_numeral` | "LEVEL 1" through "LEVEL 4" |
| Example trace | `data_flow` | Article 50 traced through all four levels |
| Cascade arrows | `data_flow` | Connecting lines from level to level showing expansion |
| Insight callout | `callout_bar` | "Architecture = regulatory bet" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| EU AI Act | GPAI Code of Practice | cascade | "Implements" |
| EU AI Act | Industry Working Groups | cascade | "Interprets" |
| GPAI Code | ISO/IEC 42001 | cascade | "Translates to standard" |
| GPAI Code | C2PA Manifest | cascade | "Translates to standard" |
| ISO/IEC 42001 | Logging | cascade | "Requires" |
| ISO/IEC 42001 | Audit trail | cascade | "Requires" |
| C2PA Manifest | Content labeling | cascade | "Requires" |
| C2PA Manifest | Provenance chain | cascade | "Requires" |
| UK AI Bill | Voluntary Commitments | cascade | "Encourages" |
| Article 50 | GPAI Code | example_trace | "Transparency clause" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Compounding Constraints | "Each level adds requirements -- by Level 4, a single clause generates 5+ architecture constraints" | Right margin, level 3-4 |
| Article 50 Example | "Transparency requirement cascades to both content labeling AND audit logging" | Below example trace |
| The Bet | "Architecture choices made in 2026 will be constrained by regulations finalized in 2027-2028" | Bottom center |

## Text Content

### Labels (Max 30 chars each)

- EU AI Act 2024
- UK AI Bill
- US Executive Orders
- GPAI Code of Practice
- Industry Working Groups
- Voluntary Commitments
- ISO/IEC 42001
- IEEE 3119
- W3C Provenance
- C2PA Manifest
- Logging All AI Actions
- Immutable Audit Trail
- Content Labeling
- Provenance Chain Per Asset
- Explainability on Demand

### Caption (for embedding in documentation)

Regulatory requirements cascade through four levels: legislation (EU AI Act, UK AI Bill, US executive orders) is interpreted by codes of practice (GPAI Code, industry working groups), translated into technical standards (ISO/IEC 42001, IEEE 3119, C2PA), and finally materialized as architecture requirements (logging, audit trails, content labeling, provenance chains, explainability). A single legislative clause like Article 50 (transparency) generates multiple cascade paths, each producing different code-level constraints -- making every architecture decision an implicit regulatory bet.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)**.
5. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

1. There are exactly FOUR levels in the cascade -- do NOT add or remove levels.
2. EU AI Act Article 50 is a SPECIFIC legal provision about transparency -- do NOT generalize.
3. ISO/IEC 42001 is for AI management systems -- do NOT confuse with ISO 27001 (information security).
4. C2PA is the Coalition for Content Provenance and Authenticity -- do NOT expand incorrectly.
5. The cascade direction is TOP-TO-BOTTOM (legislation to code) -- do NOT reverse.
6. Do NOT imply that all regulatory paths lead to the same architecture -- the point is that they DIVERGE.
7. Do NOT present this as a compliance checklist -- it is a DECISION-MAKING framework.
8. The example trace (Article 50) is ILLUSTRATIVE -- do NOT present as the only possible trace.
9. Do NOT include specific code snippets -- Level 4 shows REQUIREMENT types, not implementations.

## Alt Text

Four-level regulatory cascade: legislation to codes of practice to standards to architecture requirements.

## JSON Export Block

```json
{
  "id": "fig-landscape-29",
  "title": "Regulatory Cascade: EU AI Act to Architecture Requirements",
  "audience": "L3",
  "priority": "P1",
  "layout": "C",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Speculate",
  "novelty": 3,
  "cascade_levels": [
    {
      "level": 1,
      "name": "Legislation",
      "items": ["EU AI Act 2024", "UK AI Bill", "US Executive Orders"]
    },
    {
      "level": 2,
      "name": "Codes of Practice",
      "items": ["GPAI Code of Practice", "Industry Working Groups", "Voluntary Commitments"]
    },
    {
      "level": 3,
      "name": "Technical Standards",
      "items": ["ISO/IEC 42001", "IEEE 3119", "W3C Provenance", "C2PA Manifest"]
    },
    {
      "level": 4,
      "name": "Architecture Requirements",
      "items": [
        "Logging all AI actions",
        "Immutable audit trail",
        "Content labeling at point of creation",
        "Provenance chain per asset",
        "Explainability on demand"
      ]
    }
  ],
  "example_trace": {
    "source": "Article 50 (Transparency)",
    "paths": [
      "Art.50 → GPAI Code → C2PA Manifest → Content labeling",
      "Art.50 → GPAI Code → ISO 42001 → Logging + audit trail"
    ]
  },
  "semantic_tags_used": [
    "heading_display", "label_editorial", "decision_point", "processing_stage",
    "solution_component", "data_flow", "section_numeral", "callout_bar", "data_mono"
  ]
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L1/L2/L3/L4)
- [x] Layout template identified (A/B/C/D/E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
