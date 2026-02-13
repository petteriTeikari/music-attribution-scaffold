# fig-theory-13: Reliability Diagram

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-13 |
| **Title** | Reliability Diagram -- Calibration vs Sharpness |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 (statistical concepts, calibration theory) |
| **Location** | docs/theory/confidence-scoring.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how to evaluate whether confidence scores are well-calibrated using a reliability diagram. It answers: "When the system says '85% confident,' is it actually correct 85% of the time?"

The key message is: "A well-calibrated system's reliability curve follows the diagonal -- deviations mean the system is overconfident (below diagonal) or underconfident (above diagonal). Sharpness measures how decisive the scores are."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  RELIABILITY DIAGRAM                                           |
|  ■ Calibration and Sharpness                                   |
+---------------------------------------------------------------+
|                                                                |
|  Observed                                                      |
|  Frequency  1.0 ┤                                              |
|             │                                              ╱   |
|             │  UNDERCONFIDENT                           ╱      |
|             │  (system says 60%,                     ╱         |
|         0.8 ┤   correct 80%)             .  .    ╱             |
|             │                         .       ╱                |
|             │                      .       ╱                   |
|         0.6 ┤                   . ┌────╱───────────┐           |
|             │                .   │ PERFECT        │           |
|             │              ●    │ CALIBRATION    │           |
|         0.4 ┤           ●      │ (diagonal)     │           |
|             │         ●   ▼    └─────────────────┘           |
|             │       ●                                          |
|         0.2 ┤     ●    OVERCONFIDENT                           |
|             │   ●      (system says 80%,                       |
|             │  ●        correct 50%)                           |
|         0.0 ┼────┬────┬────┬────┬────┬                        |
|             0.0  0.2  0.4  0.6  0.8  1.0                      |
|                  Predicted Confidence                          |
|                                                                |
+-------------------------------+-------------------------------+
|                               |                               |
|  CALIBRATION                  |  SHARPNESS                    |
|  ───────────                  |  ─────────                    |
|                               |                               |
|  ■ How close is the curve     |  ■ How peaked are the         |
|    to the diagonal?           |    predicted probabilities?    |
|                               |                               |
|  Perfect: curve = diagonal    |  Sharp: predictions near      |
|  Overconfident: curve below   |  0 or 1 (decisive)            |
|  Underconfident: curve above  |  Blunt: predictions near      |
|                               |  0.5 (uninformative)          |
|                               |                               |
|  Metric: ECE (Expected        |  Metric: histogram entropy    |
|  Calibration Error)           |  of predicted scores          |
+-------------------------------+-------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "RELIABILITY DIAGRAM" with coral accent square |
| Subtitle | `label_editorial` | "Calibration and Sharpness" |
| Plot axes | `data_mono` | X: "Predicted Confidence" (0-1), Y: "Observed Frequency" (0-1) |
| Perfect calibration diagonal | `confidence_high` | Dashed diagonal line from (0,0) to (1,1) |
| Overconfident curve | `confidence_low` | Curve below diagonal -- system is too confident |
| Underconfident region label | `label_editorial` | "UNDERCONFIDENT" zone above diagonal |
| Overconfident region label | `label_editorial` | "OVERCONFIDENT" zone below diagonal |
| Calibrated data points | `data_mono` | Dots showing a well-calibrated system |
| Calibration definition panel | `callout_box` | Left: how close is curve to diagonal, ECE metric |
| Sharpness definition panel | `callout_box` | Right: how peaked are predictions, histogram entropy |
| Axis tick marks | `data_mono` | 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 in monospace |

## Anti-Hallucination Rules

1. The diagonal from (0,0) to (1,1) represents PERFECT calibration -- do NOT call it something else.
2. BELOW the diagonal = overconfident (system claims high confidence but is wrong more often). Do NOT swap.
3. ABOVE the diagonal = underconfident (system claims low confidence but is right more often). Do NOT swap.
4. ECE = Expected Calibration Error -- this is the standard metric name. Do NOT rename.
5. Sharpness is about the DISTRIBUTION of predictions, not their correctness.
6. A system can be well-calibrated but not sharp (all predictions near 0.5) -- these are independent properties.
7. Do NOT include model-specific calibration methods (temperature scaling, Platt scaling) in this figure.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Reliability diagram with predicted confidence on x-axis and observed frequency on y-axis, showing perfect calibration diagonal, overconfident curve below, and panels defining calibration and sharpness.
