# fig-tech-03: Confidence Scoring Algorithm

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-tech-03 |
| **Title** | Confidence Scoring Algorithm |
| **Audience** | Technical (developers) |
| **Complexity** | L3 (detailed implementation) |
| **Location** | docs/prd/attribution-engine-prd.md, docs/knowledge-base/technical/uncertainty/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:10 |

## Purpose

Show how confidence scores are computed from source agreement and authority weights, and how they map to A0-A3 attribution levels.

## Key Message

"Confidence combines source agreement (60%) and authority weights (40%), mapping to four attribution levels (A0-A3) with explicit uncertainty display."

## Visual Concept

Multi-panel figure: formula breakdown on left, authority weights table in center, A0-A3 threshold diagram on right.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CONFIDENCE SCORING ALGORITHM                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FORMULA                     AUTHORITY WEIGHTS         A0-A3 MAPPING        │
│  ───────                     ────────────────         ──────────────        │
│                                                                             │
│  ┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐   │
│  │                     │     │ Source    Weight│     │                 │   │
│  │  confidence =       │     ├─────────────────┤     │  1.0 ┬─────────│   │
│  │                     │     │ the system   1.0  │     │      │   A3    │   │
│  │  (agreement × 0.6)  │     │ MusicBrainz 0.8 │     │ 0.85 ├─────────│   │
│  │         +           │     │ Discogs    0.6  │     │      │   A2    │   │
│  │  (authority × 0.4)  │     │ Wikipedia  0.4  │     │ 0.70 ├─────────│   │
│  │                     │     │ User sub   0.2  │     │      │   A1    │   │
│  └─────────────────────┘     └─────────────────┘     │ 0.40 ├─────────│   │
│                                                       │      │   A0    │   │
│  agreement_ratio =           Higher weight =          │ 0.0  └─────────│   │
│  sources_agree / total       more trusted source      │                 │   │
│                                                       └─────────────────┘   │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  EXAMPLE: "Producer" field                                                   │
│  ─────────────────────────                                                   │
│  Sources: System="Alice", MusicBrainz="Alice", Discogs="Bob"              │
│  Agreement: 2/3 sources agree = 0.67                                         │
│  Weighted authority: (1.0 + 0.8) / (1.0 + 0.8 + 0.6) = 0.75                 │
│  Confidence: (0.67 × 0.6) + (0.75 × 0.4) = 0.40 + 0.30 = 0.70 → A2          │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Formula Panel | `primary_pathway` | Main confidence equation |
| Authority Table | `processing_stage` | Source weight lookup |
| A0-A3 Scale | `primary_pathway` | Threshold visualization |
| A3 Zone | `attribution_verified` | Green, 0.85+ |
| A2 Zone | `attribution_corroborated` | Blue, 0.70-0.85 |
| A1 Zone | `attribution_claimed` | Amber, 0.40-0.70 |
| A0 Zone | `attribution_unknown` | Gray, 0.00-0.40 |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Agreement | Formula | Arrow | "× 0.6" |
| Authority | Formula | Arrow | "× 0.4" |
| Formula | A0-A3 Scale | Arrow | "maps to" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "EXAMPLE" | Worked example with "Producer" field | Bottom panel |

## Text Content

### Labels (Max 30 chars each)

- "confidence ="
- "agreement × 0.6"
- "authority × 0.4"
- "the system: 1.0"
- "MusicBrainz: 0.8"
- "Discogs: 0.6"
- "A3: Verified (0.85+)"
- "A2: Corroborated (0.70+)"
- "A1: Claimed (0.40+)"
- "A0: Unknown (<0.40)"

### Caption (for embedding)

Confidence scoring algorithm: combines source agreement ratio (60% weight) with authority-weighted consensus (40% weight). Scores map to A0-A3 attribution levels: A3 (verified, 0.85+), A2 (corroborated, 0.70-0.85), A1 (claimed, 0.40-0.70), A0 (unknown, <0.40). Higher authority sources (the system=1.0) carry more weight than lower (user submissions=0.2).

## Prompts for Nano Banana Pro

### Style Prompt

Technical algorithm diagram on warm off-white background (#F8F6F0).
Clean mathematical layout, Economist-style data visualization.
Three-panel layout: formula on left, authority table in center, vertical scale on right.
Use green/blue/amber/gray for A3/A2/A1/A0 levels respectively.
Clear typography for equations, table formatting for weights.
Worked example in bottom callout panel.

### Content Prompt

Create a confidence scoring algorithm diagram:
- LEFT PANEL: Formula breakdown
  - "confidence = (agreement × 0.6) + (authority × 0.4)"
  - Brief explanation of agreement_ratio
- CENTER PANEL: Authority weights table
  - The system: 1.0, MusicBrainz: 0.8, Discogs: 0.6, Wikipedia: 0.4, User: 0.2
- RIGHT PANEL: Vertical A0-A3 scale
  - A3 (green): 0.85-1.0 "Verified"
  - A2 (blue): 0.70-0.85 "Corroborated"
  - A1 (amber): 0.40-0.70 "Claimed"
  - A0 (gray): 0.00-0.40 "Unknown"
- BOTTOM: Worked example with "Producer" field calculation

### Refinement Notes

- Formula should be prominently displayed
- Authority weights should look like a lookup table
- A0-A3 scale should be a clear vertical gradient/bar
- Example should show step-by-step calculation

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "tech-03",
    "title": "Confidence Scoring Algorithm",
    "audience": "technical"
  },
  "content_architecture": {
    "primary_message": "Confidence combines agreement (60%) and authority (40%), mapping to A0-A3 levels",
    "layout_flow": "three-panel-horizontal",
    "key_structures": [
      {
        "name": "Formula Panel",
        "role": "primary_pathway",
        "is_highlighted": true,
        "labels": ["confidence =", "(agreement × 0.6) + (authority × 0.4)"]
      },
      {
        "name": "Authority Table",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["the system: 1.0", "MusicBrainz: 0.8", "Discogs: 0.6"]
      },
      {
        "name": "A3 Zone",
        "role": "attribution_verified",
        "is_highlighted": false,
        "labels": ["Verified", "0.85+"]
      },
      {
        "name": "A2 Zone",
        "role": "attribution_corroborated",
        "is_highlighted": false,
        "labels": ["Corroborated", "0.70-0.85"]
      },
      {
        "name": "A1 Zone",
        "role": "attribution_claimed",
        "is_highlighted": false,
        "labels": ["Claimed", "0.40-0.70"]
      },
      {
        "name": "A0 Zone",
        "role": "attribution_unknown",
        "is_highlighted": false,
        "labels": ["Unknown", "<0.40"]
      }
    ],
    "callout_boxes": [
      {
        "heading": "EXAMPLE",
        "body_text": "Producer field: 2/3 agree (0.67) × 0.6 + weighted auth (0.75) × 0.4 = 0.70 → A2",
        "position": "bottom-full-width"
      }
    ]
  }
}
```

## Alt Text

Confidence scoring algorithm: formula shows agreement ratio times 0.6 plus authority weight times 0.4. Authority table lists source weights from the system (1.0) to user submissions (0.2). Vertical scale maps scores to A3 verified (green), A2 corroborated (blue), A1 claimed (amber), A0 unknown (gray).

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Embedded in documentation
