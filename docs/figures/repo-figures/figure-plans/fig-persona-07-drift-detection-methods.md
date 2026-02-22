# fig-persona-07: Drift Detection Methods Comparison

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-07 |
| **Title** | Drift Detection Methods Comparison |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/knowledge-base/persona-engineering/, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Compares four distinct drift detection methods -- embedding-based, probe-based, attention-based, and persona vector monitoring -- showing their mechanisms, thresholds, and computational costs. Answers: "What methods can I use to detect persona drift, and what are the trade-offs?"

## Key Message

No single drift detection method catches all drift types -- combining embedding-based (cheap, coarse), probe-based (targeted, periodic), attention-based (interpretable, moderate cost), and persona vector monitoring (precise, expensive) provides robust coverage.

## Visual Concept

Multi-panel layout (Template B) with four equal panels arranged in a 2x2 grid, each labeled with a Roman numeral. Each panel contains the method name, a brief mechanism description, a threshold indicator, and a computational cost rating. The panels are visually distinct but structurally consistent. Accent lines separate each panel. A callout bar at the bottom emphasizes the need for multi-method approaches.

```
+-----------------------------------------------------------------------+
|  DRIFT DETECTION                                                [sq]   |
|  METHODS COMPARISON                                                    |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌────────────────────────────┐  ┌──────────────────────────────┐     |
|  │  I. EMBEDDING-BASED        │  │  II. PROBE-BASED             │     |
|  │                            │  │                              │     |
|  │  Mechanism:                │  │  Mechanism:                  │     |
|  │  Cosine similarity between │  │  Inject test questions that  │     |
|  │  current response embedding│  │  probe persona knowledge     │     |
|  │  and persona reference     │  │  and character consistency   │     |
|  │                            │  │                              │     |
|  │  Threshold: < 0.85 cosine  │  │  Threshold: < 70% correct   │     |
|  │  Cost: LOW                 │  │  Cost: MODERATE              │     |
|  │  Frequency: Every turn     │  │  Frequency: Every N turns    │     |
|  └────────────────────────────┘  └──────────────────────────────┘     |
|                                                                        |
|  ┌────────────────────────────┐  ┌──────────────────────────────┐     |
|  │  III. ATTENTION-BASED      │  │  IV. PERSONA VECTOR          │     |
|  │                            │  │      MONITORING              │     |
|  │  Mechanism:                │  │                              │     |
|  │  Monitor attention ratio   │  │  Mechanism:                  │     |
|  │  on system prompt persona  │  │  Track activation-space      │     |
|  │  tokens vs conversation    │  │  projection onto persona     │     |
|  │  tokens                    │  │  vectors over time           │     |
|  │                            │  │                              │     |
|  │  Threshold: < 0.15 ratio   │  │  Threshold: > 0.3 drift     │     |
|  │  Cost: MODERATE            │  │  Cost: HIGH                  │     |
|  │  Frequency: Every turn     │  │  Frequency: Periodic check   │     |
|  └────────────────────────────┘  └──────────────────────────────┘     |
|                                                                        |
|  COMBINE METHODS -- NO SINGLE APPROACH CATCHES ALL DRIFT TYPES   [sq]  |
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
    content: "DRIFT DETECTION METHODS COMPARISON"
    role: title

  - id: grid_zone
    bounds: [80, 140, 1760, 760]
    role: content_area

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "COMBINE METHODS -- NO SINGLE APPROACH CATCHES ALL DRIFT TYPES"
    role: callout_box

anchors:
  - id: panel_embedding
    position: [100, 160]
    size: [840, 350]
    role: processing_stage
    label: "I. EMBEDDING-BASED"

  - id: panel_probe
    position: [980, 160]
    size: [840, 350]
    role: processing_stage
    label: "II. PROBE-BASED"

  - id: panel_attention
    position: [100, 540]
    size: [840, 350]
    role: processing_stage
    label: "III. ATTENTION-BASED"

  - id: panel_vector
    position: [980, 540]
    size: [840, 350]
    role: processing_stage
    label: "IV. PERSONA VECTOR MONITORING"

  - id: cost_low
    position: [700, 420]
    size: [160, 40]
    role: confidence_high
    label: "LOW"

  - id: cost_moderate_probe
    position: [1580, 420]
    size: [160, 40]
    role: confidence_medium
    label: "MODERATE"

  - id: cost_moderate_attn
    position: [700, 800]
    size: [160, 40]
    role: confidence_medium
    label: "MODERATE"

  - id: cost_high
    position: [1580, 800]
    size: [160, 40]
    role: confidence_low
    label: "HIGH"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "DRIFT DETECTION METHODS COMPARISON" in editorial caps |
| I. Embedding-Based panel | `processing_stage` | Cosine similarity between current response embedding and persona reference. Threshold < 0.85. Cost: LOW. Every turn. |
| II. Probe-Based panel | `processing_stage` | Inject test questions probing persona knowledge and character consistency. Threshold < 70% correct. Cost: MODERATE. Every N turns. |
| III. Attention-Based panel | `processing_stage` | Monitor attention ratio on system prompt persona tokens vs conversation tokens. Threshold < 0.15 ratio. Cost: MODERATE. Every turn. |
| IV. Persona Vector Monitoring panel | `processing_stage` | Track activation-space projection onto persona vectors over time. Threshold > 0.3 drift magnitude. Cost: HIGH. Periodic check. |
| Cost indicators | `confidence_high` / `confidence_medium` / `confidence_low` | LOW (green), MODERATE (amber), HIGH (red) cost ratings per method |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Embedding-Based | Probe-Based | dashed | "complementary coverage" |
| Attention-Based | Persona Vector | dashed | "complementary coverage" |
| All four methods | Combined detection | arrow | "multi-method robustness" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "COMBINE METHODS -- NO SINGLE APPROACH CATCHES ALL DRIFT TYPES" | Embedding-based catches broad semantic drift but misses subtle personality shifts. Probe-based catches knowledge gaps but only at check intervals. Attention-based catches instruction following decay but requires model access. Persona vectors are most precise but computationally expensive. Use at least two methods together. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. EMBEDDING-BASED"
- Label 2: "II. PROBE-BASED"
- Label 3: "III. ATTENTION-BASED"
- Label 4: "IV. PERSONA VECTOR"
- Label 5: "Cosine similarity"
- Label 6: "Test question injection"
- Label 7: "Attention ratio monitoring"
- Label 8: "Activation-space tracking"
- Label 9: "Threshold: < 0.85 cosine"
- Label 10: "Threshold: < 70% correct"
- Label 11: "Threshold: < 0.15 ratio"
- Label 12: "Threshold: > 0.3 drift"
- Label 13: "Cost: LOW"
- Label 14: "Cost: MODERATE"
- Label 15: "Cost: HIGH"
- Label 16: "Every turn"
- Label 17: "Every N turns"
- Label 18: "Periodic check"

### Caption

Four drift detection methods compared: embedding-based (cosine similarity, low cost), probe-based (test questions, moderate cost), attention-based (persona token attention ratio, moderate cost), and persona vector monitoring (activation space tracking, high cost). No single method catches all drift types.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Engineering jargon** -- cosine similarity, attention ratio, activation space are appropriate for L3 audience.
5. **Background MUST be warm cream (#f6f3e6)**.
6. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

9. The four methods represent distinct categories from the literature -- they are NOT all from the same paper.
10. Threshold values (0.85, 70%, 0.15, 0.3) are representative/illustrative -- do NOT present them as universal optimal values.
11. "Cost: LOW/MODERATE/HIGH" refers to computational cost per inference, NOT financial cost.
12. Attention-based and persona vector methods require access to model internals -- they do NOT work with black-box API-only models. Do NOT hide this limitation.
13. Probe-based methods add latency because they require extra generation rounds -- do NOT present them as zero-overhead.
14. Do NOT imply a strict ranking (one method is always better) -- the right combination depends on the use case.
15. Roman numerals (I, II, III, IV) are used for panel labeling per the design system, NOT to indicate ranking or sequence.

## Alt Text

Four-panel comparison of persona drift detection methods for AI systems: embedding-based (cosine similarity, low cost), probe-based (test questions, moderate cost), attention-based (persona token ratio, moderate cost), and persona vector monitoring (activation space tracking, high cost) with thresholds and trade-offs.

## Image Embed

![Four-panel comparison of persona drift detection methods for AI systems: embedding-based (cosine similarity, low cost), probe-based (test questions, moderate cost), attention-based (persona token ratio, moderate cost), and persona vector monitoring (activation space tracking, high cost) with thresholds and trade-offs.](docs/figures/repo-figures/assets/fig-persona-07-drift-detection-methods.jpg)

*Four drift detection methods compared: embedding-based (cosine similarity, low cost), probe-based (test questions, moderate cost), attention-based (persona token attention ratio, moderate cost), and persona vector monitoring (activation space tracking, high cost). No single method catches all drift types.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-07",
    "title": "Drift Detection Methods Comparison",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "No single drift detection method catches all drift types -- combine embedding, probe, attention, and persona vector approaches.",
    "layout_flow": "grid-2x2",
    "key_structures": [
      {
        "name": "I. Embedding-Based",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["I. EMBEDDING-BASED", "Cosine similarity", "Cost: LOW"]
      },
      {
        "name": "II. Probe-Based",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II. PROBE-BASED", "Test question injection", "Cost: MODERATE"]
      },
      {
        "name": "III. Attention-Based",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["III. ATTENTION-BASED", "Attention ratio monitoring", "Cost: MODERATE"]
      },
      {
        "name": "IV. Persona Vector Monitoring",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["IV. PERSONA VECTOR", "Activation-space tracking", "Cost: HIGH"]
      }
    ],
    "relationships": [
      {
        "from": "Embedding-Based",
        "to": "Probe-Based",
        "type": "dashed",
        "label": "complementary coverage"
      },
      {
        "from": "Attention-Based",
        "to": "Persona Vector",
        "type": "dashed",
        "label": "complementary coverage"
      }
    ],
    "callout_boxes": [
      {
        "heading": "COMBINE METHODS -- NO SINGLE APPROACH CATCHES ALL DRIFT TYPES",
        "body_text": "Each method has blind spots. Embedding misses subtle personality shifts. Probes only fire at intervals. Attention requires model access. Vectors are expensive. Use at least two.",
        "position": "bottom-full-width"
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
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
