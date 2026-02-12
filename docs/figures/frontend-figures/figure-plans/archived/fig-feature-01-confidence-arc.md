# fig-feature-01: Confidence Arc

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-feature-01 |
| **Title** | Confidence Arc — Calibrated Uncertainty |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Feature I section |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Large circular arc visualization showing confidence scoring with conformal prediction bands. Communicates: "we quantify uncertainty with mathematical precision."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│        ╭───────────────╮             │
│      ╭─╯               ╰─╮          │
│    ╭─╯    confidence      ╰─╮        │
│   ─╯       arc  95%         ╰─       │
│                                      │
│   ── outer band (coverage) ──        │
│   ── inner band (calibration) ──     │
│                                      │
│   ■ CONFORMAL   ■ BAYESIAN          │
│   ■ CALIBRATED  ■ PREDICTION SET    │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Main arc | `data_primary` | Large 270-degree arc, coral red |
| Outer band | `data_secondary` | Prediction interval band, navy |
| Inner band | `data_tertiary` | Calibration band, teal |
| Score number | `typography_display` | "95" in Instrument Serif, large |
| Method labels | `label_editorial` | ALL-CAPS with accent square markers |

## Alt Text

Circular arc visualization showing a 95% confidence score with two surrounding bands representing conformal prediction coverage and Bayesian calibration. Labels identify the scoring methods.
