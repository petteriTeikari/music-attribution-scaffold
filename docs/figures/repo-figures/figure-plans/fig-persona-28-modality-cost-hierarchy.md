# fig-persona-28: Modality Cost Hierarchy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-28 |
| **Title** | Modality Cost Hierarchy -- From Text to Video |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/persona-coherence.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Shows the four interaction modalities in ascending cost order (Text, Voice, Avatar, Video) with per-unit costs, cost multipliers, and the corresponding pricing tier for each modality. Answers: "How dramatically does cost scale across modalities, and how should pricing tiers map to modality access?"

## Key Message

Each modality upgrade deepens the user relationship and the cost -- video is 10,000-100,000x more expensive than text per interaction, requiring modality-gated pricing tiers (Free=text, Basic=voice, Premium=avatar, Pro=video) to maintain sustainability.

## Visual Concept

Four ascending steps from left to right, each representing a modality. Step height increases dramatically to convey the exponential cost increase. Each step shows the modality name, per-unit cost, and the pricing tier that unlocks it. A vertical cost scale on the left emphasizes the magnitude difference. The 10,000-100,000x multiplier between text and video is prominently displayed.

```
+---------------------------------------------------------------+
|  MODALITY COST HIERARCHY                                       |
+---------------------------------------------------------------+
|                                                                |
|                                              ┌──────────┐     |
|                                              │  IV.      │     |
|                                              │  VIDEO    │     |
|                                              │           │     |
|                                              │ $0.005-   │     |
|                                              │  0.40/sec │     |
|                                 ┌──────────┐│           │     |
|                                 │  III.     ││  Pro tier │     |
|                                 │  AVATAR   │└──────────┘     |
|                                 │           │                  |
|                    ┌──────────┐│  $0/runtime│                  |
|                    │  II.      ││  (client)  │                  |
|                    │  VOICE    │└──────────┘                  |
|   ┌──────────┐   │           │                               |
|   │  I.       │   │ $0.001-   │  Premium                      |
|   │  TEXT      │   │  0.015/   │  tier                         |
|   │           │   │  1K chars  │                               |
|   │ $0.001/   │   └──────────┘                               |
|   │  1K tokens │                                               |
|   │           │   Basic tier                                   |
|   │ Free tier │                                               |
|   └──────────┘                                               |
|                                                                |
|   10,000 -- 100,000x cost increase from text to video          |
|                                                                |
+---------------------------------------------------------------+
|  EACH MODALITY UPGRADE DEEPENS THE RELATIONSHIP AND THE COST   |
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
    content: "MODALITY COST HIERARCHY"
    role: title

  - id: steps_zone
    bounds: [80, 160, 1760, 680]
    role: content_area

  - id: multiplier_zone
    bounds: [80, 860, 1760, 40]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    role: callout_box

anchors:
  - id: step_text
    position: [300, 680]
    size: [360, 160]
    role: confidence_high
    label: "I. TEXT"

  - id: step_voice
    position: [720, 560]
    size: [360, 280]
    role: confidence_high
    label: "II. VOICE"

  - id: step_avatar
    position: [1140, 420]
    size: [360, 420]
    role: confidence_medium
    label: "III. AVATAR"

  - id: step_video
    position: [1560, 260]
    size: [360, 580]
    role: confidence_low
    label: "IV. VIDEO"

  - id: cost_text
    position: [300, 740]
    size: [300, 40]
    role: data_mono
    label: "$0.001/1K tokens"

  - id: cost_voice
    position: [720, 740]
    size: [300, 40]
    role: data_mono
    label: "$0.001-0.015/1K chars"

  - id: cost_avatar
    position: [1140, 740]
    size: [300, 40]
    role: data_mono
    label: "$0 runtime (client-side)"

  - id: cost_video
    position: [1560, 740]
    size: [300, 40]
    role: data_mono
    label: "$0.005-0.40/sec"

  - id: tier_free
    position: [300, 780]
    size: [200, 30]
    role: assurance_a0
    label: "Free tier"

  - id: tier_basic
    position: [720, 780]
    size: [200, 30]
    role: assurance_a1
    label: "Basic tier"

  - id: tier_premium
    position: [1140, 780]
    size: [200, 30]
    role: assurance_a2
    label: "Premium tier"

  - id: tier_pro
    position: [1560, 780]
    size: [200, 30]
    role: assurance_a3
    label: "Pro tier"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "MODALITY COST HIERARCHY" with accent square |
| Step I: Text | `confidence_high` | Cheapest modality: $0.001/1K tokens, Free tier |
| Step II: Voice | `confidence_high` | Mid-range: $0.001-0.015/1K chars, Basic tier |
| Step III: Avatar | `confidence_medium` | $0 runtime (client-side rendering), Premium tier |
| Step IV: Video | `confidence_low` | Most expensive: $0.005-0.40/sec, Pro tier |
| Cost labels | `data_mono` | Per-unit cost figures for each modality |
| Tier labels | `assurance_a0` through `assurance_a3` | Pricing tier that unlocks each modality |
| Multiplier annotation | `problem_statement` | 10,000-100,000x cost increase from text to video |
| Callout bar | `callout_bar` | Each modality upgrade deepens the relationship and the cost |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Step I: Text | Step II: Voice | arrow | "10-15x cost increase" |
| Step II: Voice | Step III: Avatar | arrow | "client-side (no server cost)" |
| Step III: Avatar | Step IV: Video | arrow | "5-400x cost increase" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "COST ESCALATION" | Each modality upgrade deepens the relationship and the cost -- video is 10,000-100,000x more expensive than text | bottom-center |
| "TIER MAPPING" | Free=text, Basic=voice, Premium=avatar, Pro=video -- modality access gates subscription tiers | right-margin |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. TEXT"
- Label 2: "II. VOICE"
- Label 3: "III. AVATAR"
- Label 4: "IV. VIDEO"
- Label 5: "$0.001/1K tokens"
- Label 6: "$0.001-0.015/1K chars"
- Label 7: "$0 runtime (client-side)"
- Label 8: "$0.005-0.40/sec"
- Label 9: "Free tier"
- Label 10: "Basic tier"
- Label 11: "Premium tier"
- Label 12: "Pro tier"
- Label 13: "10,000-100,000x"

### Caption (for embedding in documentation)

Modality cost hierarchy showing four interaction modalities in ascending cost: Text ($0.001/1K tokens), Voice ($0.001-0.015/1K chars), Avatar ($0 runtime, client-side), Video ($0.005-0.40/sec) -- a 10,000-100,000x cost range mapped to modality-gated pricing tiers.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `confidence_high`, `confidence_medium`, `data_mono` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear. This is L2 -- use policy/economics terms.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Cost figures MUST be exact: Text $0.001/1K tokens, Voice $0.001-0.015/1K chars, Avatar $0 runtime, Video $0.005-0.40/sec.
10. Avatar is $0 runtime because rendering is CLIENT-SIDE -- do NOT imply server-side costs.
11. The 10,000-100,000x multiplier is from text to video -- do NOT apply it to other modality pairs.
12. Roman numerals (I, II, III, IV) are used for sequential labeling -- Warp Records homage.
13. Step height MUST increase dramatically to convey exponential cost scaling visually.
14. Tier mapping is exactly: Free=text, Basic=voice, Premium=avatar, Pro=video.
15. Do NOT imply all modalities are available at MVP -- voice is an upsell, avatar/video are future.
16. Video cost range ($0.005-0.40/sec) reflects the wide variance in video generation services.

## Alt Text

Modality cost hierarchy showing four ascending interaction modalities for music attribution agents from Text to Voice to Avatar to Video, spanning a 10,000 to 100,000x cost range mapped to modality-gated pricing tiers from Free through Pro for sustainable voice agent economics

## Image Embed

![Modality cost hierarchy showing four ascending interaction modalities for music attribution agents from Text to Voice to Avatar to Video, spanning a 10,000 to 100,000x cost range mapped to modality-gated pricing tiers from Free through Pro for sustainable voice agent economics](docs/figures/repo-figures/assets/fig-persona-28-modality-cost-hierarchy.jpg)

*Modality cost hierarchy showing four interaction modalities in ascending cost: Text ($0.001/1K tokens), Voice ($0.001-0.015/1K chars), Avatar ($0 runtime, client-side), Video ($0.005-0.40/sec) -- a 10,000-100,000x cost range mapped to modality-gated pricing tiers.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-28",
    "title": "Modality Cost Hierarchy",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Each modality upgrade deepens the relationship and the cost -- video is 10,000-100,000x more expensive than text, requiring modality-gated pricing tiers.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Step I: Text",
        "role": "confidence_high",
        "is_highlighted": false,
        "labels": ["I. TEXT", "$0.001/1K tokens", "Free tier"]
      },
      {
        "name": "Step II: Voice",
        "role": "confidence_high",
        "is_highlighted": false,
        "labels": ["II. VOICE", "$0.001-0.015/1K chars", "Basic tier"]
      },
      {
        "name": "Step III: Avatar",
        "role": "confidence_medium",
        "is_highlighted": false,
        "labels": ["III. AVATAR", "$0 runtime (client-side)", "Premium tier"]
      },
      {
        "name": "Step IV: Video",
        "role": "confidence_low",
        "is_highlighted": true,
        "labels": ["IV. VIDEO", "$0.005-0.40/sec", "Pro tier"]
      }
    ],
    "relationships": [
      {
        "from": "Step I: Text",
        "to": "Step II: Voice",
        "type": "arrow",
        "label": "10-15x cost increase"
      },
      {
        "from": "Step II: Voice",
        "to": "Step III: Avatar",
        "type": "arrow",
        "label": "client-side rendering"
      },
      {
        "from": "Step III: Avatar",
        "to": "Step IV: Video",
        "type": "arrow",
        "label": "5-400x cost increase"
      }
    ],
    "callout_boxes": [
      {
        "heading": "COST ESCALATION",
        "body_text": "Each modality upgrade deepens the relationship and the cost",
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
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
