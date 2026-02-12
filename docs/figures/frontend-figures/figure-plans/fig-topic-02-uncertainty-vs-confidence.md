# fig-topic-02: Uncertainty vs. Confidence

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-02 |
| **Title** | Uncertainty vs. Confidence — Aleatoric & Epistemic Split |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card II (Confidence & Uncertainty group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Two-column visualization separating epistemic (reducible) from aleatoric (irreducible) uncertainty. Communicates: "confidence and uncertainty are distinct — we handle both."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  EPISTEMIC          ALEATORIC        │
│  (reducible)        (irreducible)    │
│                                      │
│  ████████           ████████████     │
│  ██████             ████████████     │
│  ████               ████████████     │
│  ██                 ████████████     │
│  ↓                                   │
│  shrinks with       constant,        │
│  more evidence      inherent noise   │
│                                      │
│       ───── CONFIDENCE ─────         │
│            net result: 0.82          │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Epistemic column | `data_primary` | Teal bars, decreasing height (shrinks with data) |
| Aleatoric column | `data_warning` | Orange bars, constant height (irreducible) |
| Confidence score | `typography_display` | "0.82" in Instrument Serif, centered |
| Labels | `label_editorial` | ALL-CAPS "EPISTEMIC" / "ALEATORIC" headers |
| Divider | `line_accent` | Coral vertical accent line between columns |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "EPISTEMIC", "ALEATORIC", "REDUCIBLE", "IRREDUCIBLE", "CONFIDENCE", "0.82".

## Alt Text

Two-column comparison showing epistemic uncertainty as teal bars that shrink with more evidence, and aleatoric uncertainty as constant orange bars representing irreducible noise. A confidence score of 0.82 appears below as the net result.
