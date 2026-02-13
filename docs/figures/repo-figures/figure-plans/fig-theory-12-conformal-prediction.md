# fig-theory-12: Conformal Prediction Methodology

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-12 |
| **Title** | Conformal Prediction Methodology |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 (statistical concepts, formal methodology) |
| **Location** | docs/theory/confidence-scoring.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 675px (16:9) |

## Purpose & Key Message

This figure shows the conformal prediction pipeline: how calibration data produces nonconformity scores, which yield quantiles that generate prediction sets with formal coverage guarantees. It answers: "How does the system produce confidence intervals with provable coverage?"

The key message is: "Conformal prediction provides distribution-free coverage guarantees -- the prediction set contains the true label with probability >= 1-alpha, regardless of the underlying model."

## Visual Concept (ASCII Layout)

```
+-------------------------------------------------------------------------------+
|  CONFORMAL PREDICTION                                                          |
|  ■ Distribution-Free Coverage Guarantees                                       |
+-------------------------------------------------------------------------------+
|                                                                                |
|  STEP 1              STEP 2              STEP 3              STEP 4            |
|  CALIBRATE           SCORE               QUANTILE            PREDICT           |
|  ─────────           ─────               ────────            ───────           |
|                                                                                |
|  ┌──────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐       |
|  │Calibrate │   │Nonconformity │   │              │   │ Prediction   │       |
|  │Set       │   │Scores        │   │  Quantile    │   │ Set          │       |
|  │──────────│   │──────────────│   │  ─────────   │   │──────────────│       |
|  │          │──►│              │──►│              │──►│              │       |
|  │ (X_cal,  │   │ s_i = 1 -   │   │  q = ceil   │   │ C(X_new) =   │       |
|  │  Y_cal)  │   │  f(X_i)[Y_i]│   │  ((1-alpha)  │   │ {y : s <=   │       |
|  │          │   │              │   │  (1+1/n))   │   │  q_hat}      │       |
|  │ n held-  │   │ Higher s =   │   │              │   │              │       |
|  │ out      │   │ worse fit    │   │  alpha=0.10  │   │ Coverage     │       |
|  │ examples │   │              │   │  → 90% cov.  │   │ >= 1-alpha   │       |
|  └──────────┘   └──────────────┘   └──────────────┘   └──────────────┘       |
|       │                                                       │                |
|       │              ┌────────────────────────┐               │                |
|       │              │  COVERAGE GUARANTEE     │               │                |
|       └─────────────►│  ──────────────────     │◄──────────────┘               |
|                      │  P(Y ∈ C(X)) >= 1 - α  │                               |
|                      │                         │                               |
|                      │  ■ Distribution-free    │                               |
|                      │  ■ Finite-sample valid  │                               |
|                      │  ■ No model assumptions │                               |
|                      └────────────────────────┘                               |
|                                                                                |
|  APPLIED TO ATTRIBUTION:                                                       |
|  ──────────────────────                                                        |
|  X = source evidence features    Y = true creator identity                     |
|  s = nonconformity (1 - model confidence for true label)                       |
|  C(X_new) = set of plausible creators for new query                            |
|  Smaller set = more informative = higher practical confidence                  |
+-------------------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "CONFORMAL PREDICTION" with coral accent square |
| Subtitle | `label_editorial` | "Distribution-Free Coverage Guarantees" |
| Step 1: Calibrate | `processing_stage` | Calibration set (X_cal, Y_cal) of n held-out examples |
| Step 2: Score | `processing_stage` | Nonconformity scores s_i = 1 - f(X_i)[Y_i] |
| Step 3: Quantile | `processing_stage` | Quantile computation with alpha parameter |
| Step 4: Predict | `final_score` | Prediction set C(X_new) with coverage guarantee |
| Flow arrows | `data_flow` | Left-to-right arrows connecting the four steps |
| Coverage guarantee box | `callout_box` | Central: P(Y in C(X)) >= 1-alpha with three properties |
| Formulas | `data_mono` | All mathematical notation in monospace |
| Attribution application | `callout_box` | Bottom mapping: X=evidence, Y=creator, s=nonconformity, C=plausible set |

## Anti-Hallucination Rules

1. The nonconformity score formula is s_i = 1 - f(X_i)[Y_i] -- do NOT alter or simplify.
2. The coverage guarantee is P(Y in C(X)) >= 1-alpha -- this is the EXACT statement. Do NOT weaken to approximate.
3. Three properties: distribution-free, finite-sample valid, no model assumptions. Do NOT add others.
4. alpha=0.10 gives 90% coverage -- do NOT use other alpha values as the primary example.
5. The quantile formula uses ceil((1-alpha)(1+1/n)) -- do NOT simplify to (1-alpha).
6. Do NOT mention specific ML models -- conformal prediction is model-agnostic.
7. Do NOT claim conformal prediction measures "accuracy" -- it guarantees COVERAGE.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Four-step conformal prediction pipeline: calibration set to nonconformity scores to quantile threshold to prediction sets, with central coverage guarantee P of Y in C of X at least 1 minus alpha.
