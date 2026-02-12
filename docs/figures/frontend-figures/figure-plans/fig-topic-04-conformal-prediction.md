# fig-topic-04: Conformal & Selective Prediction

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-04 |
| **Title** | Conformal & Selective Prediction — Coverage Sets & Abstention |
| **Audience** | Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card IV (Confidence & Uncertainty group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Concentric arcs showing conformal prediction sets with a selective prediction threshold. Communicates: "prediction sets come with coverage guarantees, and the system can abstain when uncertain."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│        ╭───────────────╮             │
│      ╭─╯  prediction   ╰─╮          │
│    ╭─╯     set {A,B,C}    ╰─╮       │
│   ─╯        ●                ╰─      │
│           point est.                 │
│                                      │
│  coverage: 1−α = 90%                │
│                                      │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─        │
│  SELECTIVE THRESHOLD                 │
│  ↓ below: route to human review     │
│                                      │
│  ■ CONFORMAL SET  ■ ABSTAIN ZONE   │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Prediction set arc | `data_primary` | Teal concentric arc band |
| Point estimate | `data_accent` | Coral dot at center |
| Selective threshold | `line_warning` | Red dashed horizontal line |
| Abstain zone | `region_warning` | Semi-transparent orange below threshold |
| Coverage label | `typography_mono` | "1−α = 90%" in IBM Plex Mono |
| Legend | `label_editorial` | ALL-CAPS labels |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "CONFORMAL PREDICTION", "PREDICTION SET", "SELECTIVE THRESHOLD", "HUMAN REVIEW", "1−α = 90%", "{A, B, C}".

## Alt Text

Concentric arc visualization showing a conformal prediction set as a teal band around a coral point estimate. A red dashed line marks the selective prediction threshold — below it, the system routes uncertain cases to human review rather than making automated decisions.
