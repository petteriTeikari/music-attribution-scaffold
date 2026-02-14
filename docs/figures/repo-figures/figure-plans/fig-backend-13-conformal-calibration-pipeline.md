# fig-backend-13: Conformal Calibration Pipeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-13 |
| **Title** | Conformal Calibration: Adaptive Prediction Sets (APS) |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 |
| **Location** | docs/architecture/, docs/attribution/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure explains the conformal prediction calibration step that wraps attribution confidence in statistically valid prediction sets. It covers the APS method, calibration reporting with Expected Calibration Error (ECE), and the distinction between claimed confidence and actual coverage.

The key message is: "Conformal prediction ensures that '90% confident' actually means 90% coverage -- the APS method sorts role predictions by confidence, accumulates until the target coverage is reached, and reports calibration error so the system knows when its confidence estimates are miscalibrated."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  CONFORMAL CALIBRATION                                         |
|  ■ Adaptive Prediction Sets (APS)                              |
+---------------------------------------------------------------+
|                                                                 |
|  SCORING: ConformalScorer.score()                              |
|  ────────────────────────────────                              |
|                                                                 |
|  Input: [(PERFORMER, 0.45), (SONGWRITER, 0.30),               |
|          (PRODUCER, 0.15), (ENGINEER, 0.10)]                   |
|                                                                 |
|  Step 1: Sort by confidence (descending)                       |
|  Step 2: Accumulate until sum >= coverage (0.90)               |
|                                                                 |
|  PERFORMER:   0.45  cumulative: 0.45  (< 0.90, continue)      |
|  SONGWRITER:  0.30  cumulative: 0.75  (< 0.90, continue)      |
|  PRODUCER:    0.15  cumulative: 0.90  (>= 0.90, stop)         |
|                                                                 |
|  Prediction set: {PERFORMER, SONGWRITER, PRODUCER}             |
|  Set size: 3                                                    |
|  Marginal coverage: 0.90 / 1.00 = 0.90                        |
|  Calibration error: |0.90 - 0.90| = 0.00                      |
|                                                                 |
|  ─────────────────────────────────────────────────────         |
|                                                                 |
|  CALIBRATION: ConformalScorer.calibrate()                      |
|  ────────────────────────────────────────                      |
|                                                                 |
|  Input: [(predicted_prob, actual_outcome), ...]                |
|                                                                 |
|  ┌─────────────────────────────────────────┐                   |
|  │  RELIABILITY DIAGRAM                    │                   |
|  │                                          │                   |
|  │  1.0 ┤                        x         │                   |
|  │      │               x                  │                   |
|  │  0.5 ┤      x                           │                   |
|  │      │ x          (perfect = diagonal)  │                   |
|  │  0.0 ┤────────────────────────────      │                   |
|  │      0.0         0.5         1.0        │                   |
|  │      predicted confidence               │                   |
|  └─────────────────────────────────────────┘                   |
|                                                                 |
|  ECE = Σ (bin_weight * |accuracy - confidence|)                |
|  10 bins, weighted by fraction of samples per bin              |
|                                                                 |
+---------------------------------------------------------------+
|  ■ Target coverage: 0.90 (default)                             |
|  ■ Calibration method: "APS"                                   |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "CONFORMAL CALIBRATION" |
| Scoring walkthrough | `final_score` | Step-by-step APS accumulation with example roles |
| Prediction set result | `primary_outcome` | {PERFORMER, SONGWRITER, PRODUCER} with set size 3 |
| Marginal coverage | `data_mono` | Computed achieved coverage |
| Calibration error | `data_mono` | Absolute difference from target |
| Reliability diagram | `processing_stage` | Scatter plot of predicted vs actual (calibration curve) |
| ECE formula | `data_mono` | Expected Calibration Error formula |
| Bin explanation | `label_editorial` | 10 bins, weighted by sample fraction |
| CalibrationReport fields | `data_mono` | ece, marginal_coverage, target_coverage, bin_accuracies |
| Footer notes | `callout_box` | Default coverage 0.90, method "APS" |

## Anti-Hallucination Rules

1. The method is APS (Adaptive Prediction Sets), the calibration_method string is "APS".
2. Default coverage target is 0.90, from ConformalScorer.score() default parameter.
3. The scoring algorithm: sort predictions descending, accumulate confidence, include roles until cumulative >= coverage.
4. Calibration uses 10 bins (n_bins = 10 in calibrate()).
5. ECE formula is: sum((bin_count/total) * |accuracy - confidence|) across bins.
6. The CalibrationReport has fields: ece, marginal_coverage, target_coverage, calibration_method, calibration_set_size, bin_accuracies, bin_confidences, timestamp.
7. CreditRoleEnum has 14 values (PERFORMER through REMIXER) -- the example should use valid role names.
8. The class is ConformalScorer in `music_attribution.attribution.conformal`.

## Alt Text

Pipeline diagram of conformal prediction calibration for music attribution confidence scoring, showing the Adaptive Prediction Sets (APS) method accumulating role predictions sorted by confidence until 90% coverage is reached, with a reliability diagram plotting predicted versus actual accuracy and the Expected Calibration Error (ECE) formula — ensuring that confidence scores in the open-source attribution scaffold are statistically valid and not overconfident.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Pipeline diagram of conformal prediction calibration for music attribution confidence scoring, showing the Adaptive Prediction Sets (APS) method accumulating role predictions sorted by confidence until 90% coverage is reached, with a reliability diagram plotting predicted versus actual accuracy and the Expected Calibration Error (ECE) formula — ensuring that confidence scores in the open-source attribution scaffold are statistically valid and not overconfident.](docs/figures/repo-figures/assets/fig-backend-13-conformal-calibration-pipeline.jpg)

*Figure 13. Conformal prediction ensures that "90% confident" actually means 90% coverage: the APS method wraps attribution confidence in statistically valid prediction sets while the ECE metric across 10 bins monitors whether the system's confidence estimates are well-calibrated.*

### From this figure plan (relative)

![Pipeline diagram of conformal prediction calibration for music attribution confidence scoring, showing the Adaptive Prediction Sets (APS) method accumulating role predictions sorted by confidence until 90% coverage is reached, with a reliability diagram plotting predicted versus actual accuracy and the Expected Calibration Error (ECE) formula — ensuring that confidence scores in the open-source attribution scaffold are statistically valid and not overconfident.](../assets/fig-backend-13-conformal-calibration-pipeline.jpg)
