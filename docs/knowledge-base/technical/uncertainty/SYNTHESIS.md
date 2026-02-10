# Uncertainty Quantification Synthesis

Key insights from UQ research for the system implementation.

## Core Insight

> LLM-based UQ methods (logits, self-evaluation, consistency) all have limitations. For the system, **source-level explainability** beats black-box confidence scores.

## Beigi Taxonomy Summary

Four UQ approaches for LLMs:

| Method | Pros | Cons | The System Use |
|--------|------|------|--------------|
| Logit-based | Efficient | Requires model access | Not applicable |
| Self-evaluation | Simple | Poor calibration | Secondary only |
| Consistency | Works via API | Expensive, paraphrase issues | High-stakes only |
| Internal-based | Powerful | Requires internals | Not applicable |

**Key finding**: "All methods estimate confidence, but fail to identify specific uncertainty sources."

See: [beigi-taxonomy.md](beigi-taxonomy.md)

## Conformal Prediction Summary

Alternative approach with formal guarantees:

- Returns **prediction sets** instead of point estimates
- Guarantees coverage (e.g., "95% of sets contain truth")
- Requires calibration set (100+ labeled examples)
- Implemented via MAPIE library

**Advantage**: Works without logit access, provides formal guarantees.

See: [conformal-prediction.md](conformal-prediction.md)

## System UQ Strategy

Given research findings, The system uses a hybrid approach:

```
┌─────────────────────────────────────────────────────────────┐
│                  ATTRIBUTION UQ STACK                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PRIMARY: Source-Level Confidence                           │
│  ─────────────────────────────                              │
│  - Count agreeing sources                                   │
│  - Weight by authority (the system > MusicBrainz > Discogs)   │
│  - Track provenance per field                               │
│                                                             │
│  SECONDARY: Conformal Prediction (Phase 2)                  │
│  ─────────────────────────────────────────                  │
│  - Calibration set of 100+ verified attributions            │
│  - Prediction sets for entity resolution                    │
│  - ECE < 0.15 before "calibrated" label                     │
│                                                             │
│  AVOID: LLM Self-Evaluation                                 │
│  ─────────────────────────────                              │
│  - Not used for scoring                                     │
│  - Only for user-facing explanations                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Calibration Requirements

Before claiming "calibrated" confidence:

1. **Validation set**: 100+ manually verified attributions
2. **ECE computation**: Expected Calibration Error < 0.15
3. **smoothECE**: Use Apple's ml-calibration for small samples
4. **Disclaimer**: If uncalibrated, display warning

## Cross-Domain Connection

UQ methods connect to attribution domain challenges:

| Domain Challenge | UQ Solution |
|------------------|-------------|
| Oracle problem | Source-level explainability |
| A0-A3 levels | Conformal prediction sets |
| Historical gaps | Explicit uncertainty display |
| Disputed credits | Consistency sampling |

## Implementation Checklist

- [ ] Authority weights defined (Phase 1)
- [ ] Multi-source aggregation (Phase 1)
- [ ] ECE computation pipeline (Phase 2)
- [ ] Conformal prediction integration (Phase 2)
- [ ] User-facing uncertainty UI (Phase 2)

## Related Knowledge

- [../../domain/attribution/](../../domain/attribution/) - Attribution framework
- [../../../prd/attribution-engine-prd.md](../../../prd/attribution-engine-prd.md) - Implementation
- [MAPIE Documentation](https://mapie.readthedocs.io/)
- [Apple ml-calibration](https://github.com/apple/ml-calibration)
