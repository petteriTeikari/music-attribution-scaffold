# fig-topic-01: Calibrated Confidence

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-01 |
| **Title** | Calibrated Confidence — Reliability Diagram |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card I (Confidence & Uncertainty group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Calibration curve (reliability diagram) showing the difference between well-calibrated and overconfident predictions. Communicates: "when our system says 90% confident, it really means 90%."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  1.0 ┤          /                    │
│      │        /    /-- uncalibrated  │
│  acc │      /   /     (overconfident)│
│  u   │    /  /                       │
│  r   │  / /                          │
│  a   │ //        ── ideal diagonal   │
│  c   │/          ── calibrated       │
│  y   │           ── uncalibrated     │
│  0.0 ├──────────────────             │
│      0.0   predicted   1.0          │
│                                      │
│  ■ IDEAL  ■ CALIBRATED  ■ RAW      │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Ideal diagonal | `line_reference` | Dashed navy line, 45-degree |
| Calibrated curve | `data_primary` | Teal solid line, close to diagonal |
| Uncalibrated curve | `data_warning` | Orange solid line, above diagonal (overconfident) |
| Axes | `line_subtle` | Thin grey, labeled in IBM Plex Mono |
| Legend | `label_editorial` | ALL-CAPS with accent square markers |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "CALIBRATED CONFIDENCE", "PREDICTED CONFIDENCE", "ACTUAL ACCURACY", "IDEAL", "CALIBRATED", "RAW MODEL", axis numbers 0.0–1.0.

## Alt Text

Reliability diagram showing three curves: an ideal 45-degree diagonal, a calibrated model closely following the diagonal in teal, and an overconfident uncalibrated model curving above it in orange. Demonstrates that calibrated confidence matches actual accuracy.
