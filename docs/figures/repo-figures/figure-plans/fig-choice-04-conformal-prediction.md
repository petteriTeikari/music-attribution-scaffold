# fig-choice-04: Why Conformal Prediction?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-04 |
| **Title** | Why Conformal Prediction for Confidence Scoring? |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 (algorithmic detail) |
| **Location** | docs/planning/, docs/knowledge-base/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains why the scaffold uses conformal prediction for confidence calibration rather than Bayesian posterior probabilities or bootstrap confidence intervals. Conformal prediction provides distribution-free coverage guarantees -- it does not assume a specific data distribution. This is critical for music attribution where the underlying data distribution is unknown and heterogeneous.

The key message is: "Conformal prediction provides mathematically guaranteed coverage rates without distributional assumptions -- essential for music metadata where data quality varies wildly across sources."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY CONFORMAL PREDICTION?                                     |
|  ■ Distribution-Free Confidence with Coverage Guarantees       |
+---------------------------------------------------------------+
|                                                                |
|  THE PROBLEM                                                   |
|  Music metadata quality varies wildly:                         |
|  MusicBrainz (curated) vs Discogs (community) vs ID3 (chaotic)|
|  No single distribution. No clean calibration set.             |
|                                                                |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ CONFORMAL    │ │ BAYESIAN     │ │ BOOTSTRAP    │          |
|  │ PREDICTION   │ │ POSTERIOR    │ │ CI           │          |
|  │ ■ SELECTED   │ │              │ │              │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Distribution-│ │ Requires     │ │ Asymptotic   │          |
|  │ free         │ │ prior +      │ │ only         │          |
|  │              │ │ likelihood   │ │              │          |
|  │ Coverage     │ │ Prior-       │ │ No finite-   │          |
|  │ guarantee:   │ │ dependent    │ │ sample       │          |
|  │ P(true in    │ │ results      │ │ guarantee    │          |
|  │ set) >= 1-a  │ │              │ │              │          |
|  │              │ │ Computation- │ │ Simple but   │          |
|  │ Exchangeabi- │ │ ally heavy   │ │ no coverage  │          |
|  │ lity only    │ │ (MCMC)       │ │ control      │          |
|  │              │ │              │ │              │          |
|  │ Adaptive set │ │ Point +      │ │ Point +      │          |
|  │ sizes signal │ │ interval     │ │ interval     │          |
|  │ uncertainty  │ │              │ │              │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
|  ATTRIBUTION EXAMPLE                                           |
|  Query: "Who produced 'Speak to Me'?"                          |
|  Conformal set: {Alan Parsons (0.72), Norman Smith (0.15)}     |
|  Coverage: 90% guaranteed the true answer is in the set        |
|  Set size = 2 → model is uncertain (would be 1 if confident)  |
|                                                                |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY CONFORMAL PREDICTION?" with coral accent square |
| Problem statement | `problem_statement` | Heterogeneous data quality across sources |
| Conformal prediction card | `selected_option` | Distribution-free, coverage guarantee, exchangeability |
| Bayesian posterior card | `deferred_option` | Prior-dependent, computationally heavy |
| Bootstrap CI card | `deferred_option` | Asymptotic only, no finite-sample guarantee |
| Attribution example | `data_mono` | Concrete example with conformal set and coverage |
| Set size insight | `callout_bar` | "Set size signals uncertainty" |

## Anti-Hallucination Rules

1. Conformal prediction requires only exchangeability, not i.i.d. -- this is the weakest distributional assumption.
2. Coverage guarantee: P(true value in prediction set) >= 1 - alpha. This is a finite-sample guarantee.
3. The coverage guarantee is EXACT for exchangeable data -- not asymptotic.
4. Bayesian methods require specification of a prior and likelihood -- which is problematic for heterogeneous music metadata.
5. Bootstrap confidence intervals are asymptotic -- they do not have finite-sample coverage guarantees.
6. The attribution example is illustrative -- do not claim this exact query exists in the codebase.
7. Conformal prediction is discussed in the manuscript (SSRN 6109087) under SConU confidence calibration.
8. Do NOT claim conformal prediction is always better than Bayesian -- it produces sets not point estimates, which is a trade-off.
9. Background must be warm cream (#f6f3e6).

## Alt Text

Three-method comparison for confidence scoring: conformal prediction selected for distribution-free coverage guarantees, versus Bayesian posterior and bootstrap intervals.
