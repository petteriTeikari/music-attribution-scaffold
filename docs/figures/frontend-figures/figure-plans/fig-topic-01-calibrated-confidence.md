# fig-topic-01: Calibrated Confidence

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-01 |
| **Title** | Calibrated Confidence — What "90% Confident" Actually Means |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card I (Confidence & Uncertainty group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Combined infographic explaining calibration to both ML experts and music domain experts. Left side: a reliability diagram (calibration curve) showing the gap between claimed confidence and actual accuracy. Right side: a laypeople-friendly "what this means for you" panel with concrete music attribution examples. Communicates: "when our system says 90% confident that Imogen Heap is the songwriter, it's correct 90% of the time — not 60% like an uncalibrated system."

Key insight from Beigi et al. (arXiv:2410.20199): Confidence is a *model output* (predicted probability), not a ground truth measure. High confidence does NOT necessarily mean low uncertainty. Calibration ensures the two align.

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  LEFT PANEL (55%)              RIGHT PANEL (45%)         │
│  ──────────────────            ──────────────────        │
│                                                          │
│  1.0 ┤         /               WHAT THIS MEANS          │
│      │       / ../uncal        ─────────────────        │
│  A   │     / ./                                          │
│  C   │   / /    gap = ECE      "Says 90% → correct 90%" │
│  T   │  //                     ✓ CALIBRATED (teal)       │
│  U   │ //     ── ideal                                   │
│  A   │/       ── calibrated    "Says 90% → correct 60%" │
│  L   │        ── uncalibrated  ✗ OVERCONFIDENT (orange)  │
│  0.0 ├──────────────                                     │
│      0.0  PREDICTED  1.0      MUSIC EXAMPLE              │
│                                ─────────────             │
│  ECE = Σ |acc - conf|         "Songwriter: Imogen Heap"  │
│  weighted by bin count         Calibrated: 0.91 → ✓      │
│                                Uncalibrated: 0.91 → ?    │
│                                (actually correct 62%)    │
│                                                          │
│  ■ IDEAL  ■ CALIBRATED  ■ OVERCONFIDENT  ■ ECE GAP    │
│                                                          │
│  RELIABILITY = confidence scores match actual accuracy   │
│  (Guo et al. 2017; Beigi et al. 2025)                  │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Ideal diagonal | `line_reference` | Dashed navy 45° line |
| Calibrated curve | `data_primary` | Teal solid line, close to diagonal |
| Uncalibrated curve | `data_warning` | Orange solid line, curving away from diagonal |
| ECE gap shading | `region_warning` | Semi-transparent orange area between curves |
| Axes | `line_subtle` | Thin grey axes with 0.0–1.0 labels |
| Laypeople panel | `region_secondary` | Right panel with concrete music examples |
| Checkmark | `status_allow` | Teal check for calibrated result |
| Cross mark | `status_deny` | Orange cross for overconfident result |
| Music example | `data_accent` | Concrete songwriter attribution scenario |
| ECE formula | `typography_mono` | Expected Calibration Error formula |
| Legend | `label_editorial` | ALL-CAPS with accent square markers |
| Citation strip | `label_subtle` | Small reference text at bottom |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "CALIBRATED CONFIDENCE", "PREDICTED CONFIDENCE", "ACTUAL ACCURACY", "IDEAL", "CALIBRATED", "OVERCONFIDENT", "ECE GAP", "WHAT THIS MEANS", "RELIABILITY", "MUSIC EXAMPLE", "Songwriter: Imogen Heap", axis numbers 0.0–1.0, ECE formula, confidence scores.

## Alt Text

Split infographic with a reliability diagram on the left showing three curves: an ideal 45-degree diagonal, a calibrated model in teal closely following it, and an overconfident uncalibrated model curving away in orange with the ECE gap shaded. On the right, a laypeople explanation panel shows what calibration means in practice: a calibrated system saying 90% confident is correct 90% of the time, while an uncalibrated system claiming 90% may only be correct 62% of the time. A concrete music attribution example using Imogen Heap's songwriting credit demonstrates the difference.
