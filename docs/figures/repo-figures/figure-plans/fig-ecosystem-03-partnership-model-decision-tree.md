# fig-ecosystem-03: Partnership Model Decision Tree

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-03 |
| **Title** | Partnership Model Decision Tree |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows how the partnership_model choice cascades into company node activations and deployment requirements. Answers: "Which ecosystem partners get activated under each partnership strategy?"

## Key Message

Partnership model cascades into 6 company nodes -- "none" (P=0.40) leaves all deactivated; "api_marketplace" activates SoundExchange/Fairly Trained; "strategic_alliance" adds Musical AI/Sureel; "cmo_federation" adds STIM.

## Visual Concept

Top decision node (partnership_model) branches downward into 4 options arranged horizontally. Each option flows down to different subsets of the 6 company nodes. The "none" branch terminates with no activations. Probability labels on each branch. Company nodes shown as activated (solid) or deactivated (dashed) per path.

```
+-----------------------------------------------------------------------+
|  PARTNERSHIP MODEL DECISION TREE                                       |
|  ■ Company Node Activations by Strategy                                |
+-----------------------------------------------------------------------+
|                                                                        |
|  PARENTS:                                                              |
|  ┌──────────────┐ ┌────────────┐ ┌───────────────┐                    |
|  │Target Market │ │Revenue     │ │Regulatory     │                    |
|  │Segment       │ │Model       │ │Posture        │                    |
|  └──────┬───────┘ └─────┬──────┘ └──────┬────────┘                    |
|         │    (strong)    │ (moderate)     │ (moderate)                  |
|         └───────────┬────┴───────────────┘                             |
|                     ▼                                                  |
|          ┌─────────────────────┐                                       |
|          │  PARTNERSHIP MODEL  │                                       |
|          │  (L2 Architecture)  │                                       |
|          └────┬───┬───┬───┬───┘                                       |
|               │   │   │   │                                            |
|     P=0.40    │   │   │   │  P=0.15                                    |
|     ┌─────────┘   │   │   └──────────┐                                 |
|     │    P=0.25   │   │  P=0.20      │                                 |
|     │    ┌────────┘   └────┐         │                                 |
|     ▼    ▼                 ▼         ▼                                 |
|  ┌──────┐ ┌────────────┐ ┌────────┐ ┌──────────┐                      |
|  │ NONE │ │API         │ │STRAT.  │ │CMO       │                      |
|  │      │ │MARKETPLACE │ │ALLIANCE│ │FEDERATION│                      |
|  └──┬───┘ └─────┬──────┘ └───┬────┘ └────┬─────┘                      |
|     │           │             │           │                            |
|     │     ┌─────┴─────┐  ┌───┴──────┐  ┌─┴─────────┐                  |
|     ×     │           │  │          │  │           │                  |
|  (no      ▼           ▼  ▼          ▼  ▼           ▼                  |
|  nodes)  ┌────────┐┌──────────┐┌────────┐┌──────┐┌─────────┐┌─────┐  |
|          │SndExch ││Fairly    ││Musical ││Sureel││STIM CMO ││Suno/│  |
|          │Registry││Trained   ││AI      ││AI    ││Pilot    ││Udio │  |
|          └────────┘└──────────┘└────────┘└──────┘└─────────┘└─────┘  |
|          ◄─ api_marketplace ─► ◄ strategic ►     ◄── cmo_fed ──►      |
|                                  alliance                              |
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
    content: "PARTNERSHIP MODEL DECISION TREE"
    role: title

  - id: parents_zone
    bounds: [400, 140, 1120, 120]
    role: content_area
    label: "Parent nodes"

  - id: decision_zone
    bounds: [700, 300, 520, 100]
    role: content_area
    label: "Partnership model node"

  - id: options_zone
    bounds: [100, 480, 1720, 120]
    role: content_area
    label: "Four options"

  - id: company_zone
    bounds: [100, 680, 1720, 300]
    role: content_area
    label: "Company node activations"

anchors:
  - id: target_market
    position: [480, 170]
    size: [200, 70]
    role: decision_point
    label: "Target Market Segment"

  - id: revenue_model
    position: [760, 170]
    size: [200, 70]
    role: decision_point
    label: "Revenue Model"

  - id: regulatory_posture
    position: [1040, 170]
    size: [200, 70]
    role: decision_point
    label: "Regulatory Posture"

  - id: partnership_model
    position: [760, 320]
    size: [400, 80]
    role: decision_point
    label: "PARTNERSHIP MODEL"

  - id: opt_none
    position: [200, 500]
    size: [280, 80]
    role: deferred_option
    label: "None (P=0.40)"

  - id: opt_api
    position: [560, 500]
    size: [280, 80]
    role: branching_path
    label: "API Marketplace (P=0.25)"

  - id: opt_strategic
    position: [920, 500]
    size: [280, 80]
    role: branching_path
    label: "Strategic Alliance (P=0.20)"

  - id: opt_cmo
    position: [1280, 500]
    size: [280, 80]
    role: branching_path
    label: "CMO Federation (P=0.15)"

  - id: soundexchange
    position: [460, 720]
    size: [200, 60]
    role: decision_point
    label: "SoundExchange"

  - id: fairly_trained
    position: [700, 720]
    size: [200, 60]
    role: decision_point
    label: "Fairly Trained"

  - id: musical_ai
    position: [940, 720]
    size: [200, 60]
    role: decision_point
    label: "Musical AI"

  - id: sureel_ai
    position: [1180, 720]
    size: [200, 60]
    role: decision_point
    label: "Sureel AI"

  - id: stim_cmo
    position: [1420, 720]
    size: [200, 60]
    role: decision_point
    label: "STIM CMO Pilot"

  - id: suno_udio
    position: [1660, 720]
    size: [200, 60]
    role: decision_point
    label: "Suno/Udio"

  - id: parent_to_decision_1
    from: target_market
    to: partnership_model
    type: arrow
    label: "strong"

  - id: parent_to_decision_2
    from: revenue_model
    to: partnership_model
    type: arrow
    label: "moderate"

  - id: parent_to_decision_3
    from: regulatory_posture
    to: partnership_model
    type: arrow
    label: "moderate"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Target Market Segment | `decision_point` | L1 parent node, strong influence |
| Revenue Model | `decision_point` | L1 parent node, moderate influence |
| Regulatory Posture | `decision_point` | L1 parent node, moderate influence |
| Partnership Model | `decision_point` | L2 architecture decision node (center) |
| None option | `deferred_option` | No partnership, P=0.40 (highest prior) |
| API Marketplace option | `branching_path` | Lightweight integrations, P=0.25 |
| Strategic Alliance option | `branching_path` | Deep partnerships, P=0.20 |
| CMO Federation option | `branching_path` | Institutional integration, P=0.15 |
| 6 company nodes | `decision_point` | SoundExchange, Fairly Trained, Musical AI, Sureel AI, STIM CMO Pilot, Suno/Udio |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Target Market Segment | Partnership Model | arrow | "strong influence" |
| Revenue Model | Partnership Model | arrow | "moderate influence" |
| Regulatory Posture | Partnership Model | arrow | "moderate influence" |
| Partnership Model | None | arrow | "P=0.40" |
| Partnership Model | API Marketplace | arrow | "P=0.25" |
| Partnership Model | Strategic Alliance | arrow | "P=0.20" |
| Partnership Model | CMO Federation | arrow | "P=0.15" |
| API Marketplace | SoundExchange | arrow | "activates" |
| API Marketplace | Fairly Trained | arrow | "activates" |
| Strategic Alliance | Musical AI | arrow | "activates" |
| Strategic Alliance | Sureel AI | arrow | "activates" |
| CMO Federation | STIM CMO Pilot | arrow | "activates" |
| CMO Federation | Suno/Udio | arrow | "activates" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "HIGHEST PRIOR" | None (P=0.40) -- honest uncertainty about which partnerships will materialize | left-margin |
| "CASCADING ACTIVATIONS" | Each strategy activates a different subset of the 6 company nodes | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Partnership Model"
- Label 2: "None (P=0.40)"
- Label 3: "API Marketplace (P=0.25)"
- Label 4: "Strategic Alliance (P=0.20)"
- Label 5: "CMO Federation (P=0.15)"
- Label 6: "Company Node Activations"

### Caption (for embedding in documentation)

The partnership model decision tree shows how each strategy option cascades into different company node activations, with the "none" option holding the highest prior probability (0.40) reflecting honest uncertainty about partnership outcomes.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `branching_path`, `deferred_option` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. partnership_model is L2_architecture. Company nodes: musical_ai_partnership, sureel_ai_partnership, stim_cmo_pilot, soundexchange_registry, fairly_trained_certification, suno_udio_licensing.
10. Parents: target_market_segment (strong), revenue_model (moderate), regulatory_posture (moderate).
11. The "none" option has highest prior (0.40). Do NOT show any other option as the default or most likely.
12. Probabilities must sum to 1.00 across the four options: 0.40 + 0.25 + 0.20 + 0.15 = 1.00.
13. Do NOT imply that company nodes outside the listed 6 are activated by any partnership model option.

## Alt Text

Partnership model decision tree cascading to six company node activations

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-03",
    "title": "Partnership Model Decision Tree",
    "audience": "L2",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Partnership model cascades into 6 company nodes with 'none' (P=0.40) as highest prior.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Partnership Model Node",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["PARTNERSHIP MODEL", "L2 Architecture"]
      },
      {
        "name": "None Option",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["None", "P=0.40"]
      },
      {
        "name": "API Marketplace Option",
        "role": "branching_path",
        "is_highlighted": true,
        "labels": ["API Marketplace", "P=0.25"]
      },
      {
        "name": "Strategic Alliance Option",
        "role": "branching_path",
        "is_highlighted": true,
        "labels": ["Strategic Alliance", "P=0.20"]
      },
      {
        "name": "CMO Federation Option",
        "role": "branching_path",
        "is_highlighted": true,
        "labels": ["CMO Federation", "P=0.15"]
      }
    ],
    "relationships": [
      {
        "from": "Target Market Segment",
        "to": "Partnership Model",
        "type": "arrow",
        "label": "strong influence"
      },
      {
        "from": "Partnership Model",
        "to": "None",
        "type": "arrow",
        "label": "P=0.40"
      },
      {
        "from": "API Marketplace",
        "to": "SoundExchange + Fairly Trained",
        "type": "arrow",
        "label": "activates"
      },
      {
        "from": "Strategic Alliance",
        "to": "Musical AI + Sureel AI",
        "type": "arrow",
        "label": "activates"
      },
      {
        "from": "CMO Federation",
        "to": "STIM CMO Pilot + Suno/Udio",
        "type": "arrow",
        "label": "activates"
      }
    ],
    "callout_boxes": [
      {
        "heading": "HIGHEST PRIOR",
        "body_text": "None (P=0.40) reflects honest uncertainty about partnerships",
        "position": "left-margin"
      },
      {
        "heading": "CASCADING ACTIVATIONS",
        "body_text": "Each strategy activates a different subset of 6 company nodes",
        "position": "bottom-center"
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
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
