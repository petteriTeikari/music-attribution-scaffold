# fig-ecosystem-02: Three Integration Archetypes

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-02 |
| **Title** | Three Integration Archetypes |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Shows how Simple MCP vs Platform Integration vs CMO Federation determine engineering investment and partnership economics. Answers: "What are the three ways external systems can integrate with the scaffold?"

## Key Message

Three integration archetypes -- Simple MCP (lightweight API adapters), Platform Integration (bidirectional data exchange), CMO Federation (institutional infrastructure) -- determine engineering investment from weeks to quarters.

## Visual Concept

Three vertical columns of increasing size and complexity. Left column (Simple MCP) is the smallest, showing lightweight adapter nodes. Center column (Platform Integration) is medium, showing bidirectional data exchange. Right column (CMO Federation) is the largest, showing institutional infrastructure. Each column shows applicable PRD nodes and engineering effort indicator.

```
+-----------------------------------------------------------------------+
|  THREE INTEGRATION ARCHETYPES                                          |
|  ■ Engineering Investment: Weeks to Quarters                           |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. SIMPLE MCP           II. PLATFORM           III. CMO               |
|  Lightweight Adapters     INTEGRATION             FEDERATION            |
|  ─────────────────        Bidirectional            Institutional        |
|                           Data Exchange            Infrastructure      |
|  ┌───────────────┐       ┌───────────────┐       ┌───────────────┐    |
|  │               │       │               │       │               │    |
|  │ SoundExchange │       │ Musical AI    │       │ CMO Licensing  │    |
|  │ Registry      │       │ Partnership   │       │ Integration    │    |
|  │               │       │               │       │               │    |
|  │ Fairly Trained│       │ Sureel AI     │       │ STIM CMO      │    |
|  │ Certification │       │ Partnership   │       │ Pilot         │    |
|  │               │       │               │       │               │    |
|  │ Metadata      │       │ Suno/Udio     │       │ Compliance    │    |
|  │ Registry      │       │ Licensing     │       │ Pipeline      │    |
|  │               │       │               │       │               │    |
|  │ Content ID    │       │               │       │               │    |
|  │ System        │       │               │       │               │    |
|  └───────────────┘       └───────────────┘       └───────────────┘    |
|                                                                        |
|  EFFORT: Weeks            EFFORT: Months          EFFORT: Quarters     |
|  ────────────             ──────────────          ────────────────     |
|  API key + rate limit     Schema mapping +        Federation protocol  |
|  Structured I/O           webhook handlers        + audit trails +     |
|  Runs in FastAPI          Shared state +           multi-CMO queries   |
|                           reconciliation                               |
|                                                                        |
|  ◄──────────── Increasing complexity + investment ──────────────►      |
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
    content: "THREE INTEGRATION ARCHETYPES"
    role: title

  - id: panel_simple_mcp
    bounds: [60, 160, 560, 680]
    role: content_area
    label: "I. SIMPLE MCP"

  - id: panel_platform
    bounds: [680, 160, 560, 680]
    role: content_area
    label: "II. PLATFORM INTEGRATION"

  - id: panel_cmo
    bounds: [1300, 160, 560, 680]
    role: content_area
    label: "III. CMO FEDERATION"

  - id: effort_bar
    bounds: [60, 860, 1800, 100]
    role: callout_bar
    label: "Engineering investment axis"

  - id: complexity_axis
    bounds: [60, 980, 1800, 60]
    role: data_flow
    label: "Increasing complexity + investment"

anchors:
  - id: soundexchange_node
    position: [160, 280]
    size: [360, 60]
    role: decision_point
    label: "SoundExchange Registry"

  - id: fairly_trained_node
    position: [160, 360]
    size: [360, 60]
    role: decision_point
    label: "Fairly Trained Certification"

  - id: metadata_registry_node
    position: [160, 440]
    size: [360, 60]
    role: decision_point
    label: "Metadata Registry Integration"

  - id: content_id_node
    position: [160, 520]
    size: [360, 60]
    role: decision_point
    label: "Content ID System"

  - id: musical_ai_node
    position: [780, 280]
    size: [360, 60]
    role: decision_point
    label: "Musical AI Partnership"

  - id: sureel_node
    position: [780, 360]
    size: [360, 60]
    role: decision_point
    label: "Sureel AI Partnership"

  - id: suno_udio_node
    position: [780, 440]
    size: [360, 60]
    role: decision_point
    label: "Suno/Udio Licensing"

  - id: cmo_licensing_node
    position: [1400, 280]
    size: [360, 60]
    role: decision_point
    label: "CMO Licensing Integration"

  - id: stim_node
    position: [1400, 360]
    size: [360, 60]
    role: decision_point
    label: "STIM CMO Pilot"

  - id: compliance_node
    position: [1400, 440]
    size: [360, 60]
    role: decision_point
    label: "Compliance Reporting Pipeline"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Simple MCP panel | `content_area` | Lightweight API adapter archetype with 4 nodes |
| Platform Integration panel | `content_area` | Bidirectional data exchange archetype with 3 nodes |
| CMO Federation panel | `content_area` | Institutional infrastructure archetype with 3 nodes |
| SoundExchange Registry | `decision_point` | Read-only ISRC lookup via MCP tool |
| Fairly Trained Certification | `decision_point` | Binary certification status check |
| Metadata Registry Integration | `decision_point` | Multi-registry query adapter |
| Content ID System | `decision_point` | Fingerprint query interface |
| Musical AI Partnership | `decision_point` | Training-time attribution data exchange |
| Sureel AI Partnership | `decision_point` | Identification results + attribution graphs |
| Suno/Udio Licensing | `decision_point` | Platform metadata ingestion |
| CMO Licensing Integration | `decision_point` | Multi-CMO federation protocol |
| STIM CMO Pilot | `decision_point` | Initial collective licensing pilot |
| Compliance Reporting Pipeline | `decision_point` | Regulatory reporting infrastructure |
| Engineering effort indicators | `data_mono` | Weeks / Months / Quarters |
| Complexity axis | `data_flow` | Horizontal axis showing increasing investment |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Simple MCP panel | Platform Integration panel | arrow | "increasing complexity" |
| Platform Integration panel | CMO Federation panel | arrow | "increasing complexity" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "SIMPLE MCP" | API key + rate limit, structured I/O, runs in existing FastAPI process | bottom of left panel |
| "PLATFORM INTEGRATION" | Schema mapping, webhook handlers, shared state with reconciliation | bottom of center panel |
| "CMO FEDERATION" | Federation protocol, audit trails, multi-CMO queries, regulatory compliance | bottom of right panel |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Simple MCP"
- Label 2: "Platform Integration"
- Label 3: "CMO Federation"
- Label 4: "Weeks"
- Label 5: "Months"
- Label 6: "Quarters"

### Caption (for embedding in documentation)

Three integration archetypes determine engineering investment: Simple MCP adapters require weeks, Platform Integration requires months of bidirectional data exchange work, and CMO Federation demands quarters of institutional infrastructure development.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `content_area`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Simple MCP nodes: soundexchange_registry, fairly_trained_certification, metadata_registry_integration, content_id_system. These are from docs/planning/expand-probabilistic-prd-to-discussion.md Section 4.
10. Platform Integration: musical_ai_partnership, sureel_ai_partnership, suno_udio_licensing.
11. CMO Federation: cmo_licensing_integration, stim_cmo_pilot, compliance_reporting_pipeline.
12. Do NOT add nodes to archetypes that are not listed in the planning document Section 4.
13. Engineering effort estimates (weeks/months/quarters) are approximate and should be shown as relative scale, not precise timelines.

## Alt Text

Three integration archetypes from lightweight MCP adapters to institutional CMO federation

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-02",
    "title": "Three Integration Archetypes",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Three integration archetypes determine engineering investment from weeks to quarters.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Simple MCP Panel",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["Simple MCP", "Lightweight Adapters", "Weeks"]
      },
      {
        "name": "Platform Integration Panel",
        "role": "content_area",
        "is_highlighted": true,
        "labels": ["Platform Integration", "Bidirectional Exchange", "Months"]
      },
      {
        "name": "CMO Federation Panel",
        "role": "content_area",
        "is_highlighted": true,
        "labels": ["CMO Federation", "Institutional Infrastructure", "Quarters"]
      }
    ],
    "relationships": [
      {
        "from": "Simple MCP",
        "to": "Platform Integration",
        "type": "arrow",
        "label": "increasing complexity"
      },
      {
        "from": "Platform Integration",
        "to": "CMO Federation",
        "type": "arrow",
        "label": "increasing complexity"
      }
    ],
    "callout_boxes": [
      {
        "heading": "SIMPLE MCP",
        "body_text": "API key + rate limit, structured I/O, runs in existing FastAPI process",
        "position": "bottom-left"
      },
      {
        "heading": "PLATFORM INTEGRATION",
        "body_text": "Schema mapping, webhook handlers, shared state with reconciliation",
        "position": "bottom-center"
      },
      {
        "heading": "CMO FEDERATION",
        "body_text": "Federation protocol, audit trails, multi-CMO queries",
        "position": "bottom-right"
      }
    ]
  }
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
- [x] Audience level correct (L2)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
