# fig-persona-25: Warmth-Competence Matrix

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-25 |
| **Title** | Warmth-Competence Matrix -- Agent Persona Design Trade-offs |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/persona-coherence.md, docs/architecture/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Shows the 2x2 warmth-competence matrix from social psychology applied to AI agent persona design, marking the target quadrant (high warmth + high competence) and the key warning from Ibrahim et al. that warmth training can degrade factual reliability. Answers: "Why is the warmth-competence trade-off the central tension in persona design?"

## Key Message

High warmth + high competence is the target quadrant for music attribution agents, but warmth is the dominant driver of user loyalty -- and Ibrahim et al. warn that training for warmth actively degrades reliability, making this the hardest quadrant to sustain.

## Visual Concept

A 2x2 matrix with Warmth on the Y-axis (low to high) and Competence on the X-axis (low to high). Each quadrant is labeled with its persona archetype and implications. The top-right quadrant (high/high) is highlighted as the target. An annotation arrow from the Ibrahim et al. warning connects the top-left quadrant to the top-right, showing the degradation risk. A callout at the bottom delivers the key trade-off message.

```
+---------------------------------------------------------------+
|  WARMTH-COMPETENCE MATRIX                                      |
+---------------------------------------------------------------+
|                                                                |
|              LOW COMPETENCE        HIGH COMPETENCE              |
|          ┌──────────────────┬──────────────────┐              |
|          │                  │                  │              |
|  HIGH    │ FRIENDLY BUT     │    ★ TARGET      │              |
|  WARMTH  │ UNRELIABLE       │                  │              |
|          │                  │ Music Attribution │              |
|          │ "Feels helpful   │ Agent             │              |
|          │  but gets credits│                  │              |
|          │  wrong"          │ "Warm, competent, │              |
|          │                  │  gets credits     │              |
|          │ !! DANGEROUS for │  right"           │              |
|          │    attribution   │                  │              |
|          ├──────────────────┼──────────────────┤              |
|          │                  │                  │              |
|  LOW     │ USELESS          │ COLD EXPERT       │              |
|  WARMTH  │                  │                  │              |
|          │ "No one uses it, │ "Accurate but    │              |
|          │  no one trusts   │  artists abandon  │              |
|          │  it"             │  it -- bad UX"    │              |
|          │                  │                  │              |
|          └──────────────────┴──────────────────┘              |
|                                                                |
|  ⚠ Ibrahim et al.: warmth training degrades reliability       |
|                                                                |
+---------------------------------------------------------------+
|  WARMTH IS THE DOMINANT DRIVER OF LOYALTY -- BUT MUST NOT      |
|  COMPROMISE ACCURACY                                           |
+---------------------------------------------------------------+
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
    content: "WARMTH-COMPETENCE MATRIX"
    role: title

  - id: matrix_zone
    bounds: [200, 160, 1520, 640]
    role: content_area

  - id: warning_zone
    bounds: [200, 820, 1520, 60]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    role: callout_box

anchors:
  - id: quadrant_high_warmth_low_comp
    position: [560, 380]
    size: [560, 280]
    role: confidence_low
    label: "FRIENDLY BUT UNRELIABLE"

  - id: quadrant_high_warmth_high_comp
    position: [1280, 380]
    size: [560, 280]
    role: confidence_high
    label: "TARGET -- Music Attribution Agent"

  - id: quadrant_low_warmth_low_comp
    position: [560, 660]
    size: [560, 280]
    role: assurance_a0
    label: "USELESS"

  - id: quadrant_low_warmth_high_comp
    position: [1280, 660]
    size: [560, 280]
    role: assurance_a1
    label: "COLD EXPERT"

  - id: axis_warmth
    position: [180, 520]
    size: [40, 560]
    role: data_flow
    label: "WARMTH"

  - id: axis_competence
    position: [920, 160]
    size: [720, 40]
    role: data_flow
    label: "COMPETENCE"

  - id: warning_arrow
    from: quadrant_high_warmth_low_comp
    to: quadrant_high_warmth_high_comp
    type: dashed
    label: "warmth training degrades reliability"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "WARMTH-COMPETENCE MATRIX" with accent square |
| High Warmth + Low Competence | `confidence_low` | "Friendly but unreliable" -- dangerous for attribution |
| High Warmth + High Competence | `confidence_high` | TARGET quadrant -- music attribution agent goal |
| Low Warmth + Low Competence | `assurance_a0` | "Useless" -- no one uses it, no one trusts it |
| Low Warmth + High Competence | `assurance_a1` | "Cold expert" -- accurate but artists abandon it |
| Warmth axis | `data_flow` | Vertical axis label (low to high) |
| Competence axis | `data_flow` | Horizontal axis label (low to high) |
| Ibrahim warning | `problem_statement` | Warning that warmth training degrades reliability |
| Callout bar | `callout_bar` | Warmth drives loyalty but must not compromise accuracy |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Friendly but Unreliable | TARGET quadrant | dashed | "warmth training degrades reliability (Ibrahim et al.)" |
| Cold Expert | TARGET quadrant | dashed | "add warmth without losing competence" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "KEY TRADE-OFF" | Warmth is the dominant driver of user loyalty -- but Ibrahim et al. show that training for warmth actively degrades factual reliability | bottom-center |
| "IBRAHIM WARNING" | Warmth training degrades reliability -- the high-warmth/high-competence quadrant is the hardest to sustain | top-left |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "HIGH WARMTH"
- Label 2: "LOW WARMTH"
- Label 3: "LOW COMPETENCE"
- Label 4: "HIGH COMPETENCE"
- Label 5: "FRIENDLY BUT UNRELIABLE"
- Label 6: "TARGET"
- Label 7: "USELESS"
- Label 8: "COLD EXPERT"
- Label 9: "Music Attribution Agent"
- Label 10: "Ibrahim et al. warning"

### Caption (for embedding in documentation)

Warmth-competence matrix showing 4 agent persona quadrants with High Warmth + High Competence as the target for music attribution agents, highlighting the Ibrahim et al. finding that warmth training degrades reliability -- making the target quadrant the hardest to sustain.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `confidence_high`, `confidence_low`, `assurance_a0` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear. This is L2 -- use academic terms.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Exactly 4 quadrants in a 2x2 matrix -- do NOT add extra dimensions or categories.
10. The target quadrant (High Warmth + High Competence) MUST be visually distinct as the goal.
11. "Ibrahim et al." is a real reference -- do NOT fabricate citation details beyond what is stated.
12. The warmth-competence framework comes from social psychology (Fiske et al.) -- do NOT attribute to AI research.
13. "Friendly but unreliable" is explicitly dangerous for music attribution -- attribution errors have financial consequences.
14. "Cold expert" is explicitly bad UX -- artists will abandon tools that feel clinical.
15. The dashed arrow from Ibrahim warning MUST show warmth training degrading the competence axis.
16. Do NOT imply the matrix is a selection tool -- it describes a design tension, not a menu of choices.

## Alt Text

Warmth-competence 2x2 matrix for AI agent persona design showing high warmth plus high competence as the target quadrant for music attribution agents, with Ibrahim et al. warning that warmth training degrades factual reliability creating the central tension in transparent confidence

## Image Embed

![Warmth-competence 2x2 matrix for AI agent persona design showing high warmth plus high competence as the target quadrant for music attribution agents, with Ibrahim et al. warning that warmth training degrades factual reliability creating the central tension in transparent confidence](docs/figures/repo-figures/assets/fig-persona-25-warmth-competence-matrix.jpg)

*Warmth-competence matrix showing 4 agent persona quadrants with High Warmth + High Competence as the target for music attribution agents, highlighting the Ibrahim et al. finding that warmth training degrades reliability -- making the target quadrant the hardest to sustain.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-25",
    "title": "Warmth-Competence Matrix",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "High warmth + high competence is the target but hardest to sustain -- warmth training degrades reliability (Ibrahim et al.).",
    "layout_flow": "centered",
    "key_structures": [
      {
        "name": "Friendly but Unreliable",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["FRIENDLY BUT UNRELIABLE", "Dangerous for attribution"]
      },
      {
        "name": "TARGET Quadrant",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["TARGET", "Music Attribution Agent", "Warm + Competent"]
      },
      {
        "name": "Useless",
        "role": "assurance_a0",
        "is_highlighted": false,
        "labels": ["USELESS", "No trust, no use"]
      },
      {
        "name": "Cold Expert",
        "role": "assurance_a1",
        "is_highlighted": false,
        "labels": ["COLD EXPERT", "Accurate but abandoned"]
      }
    ],
    "relationships": [
      {
        "from": "Friendly but Unreliable",
        "to": "TARGET Quadrant",
        "type": "dashed",
        "label": "warmth training degrades reliability"
      },
      {
        "from": "Cold Expert",
        "to": "TARGET Quadrant",
        "type": "dashed",
        "label": "add warmth without losing competence"
      }
    ],
    "callout_boxes": [
      {
        "heading": "KEY TRADE-OFF",
        "body_text": "Warmth is the dominant driver of loyalty -- but must not compromise accuracy",
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
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L2)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
