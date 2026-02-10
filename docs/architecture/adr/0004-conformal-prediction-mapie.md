# ADR-0004: Conformal Prediction via MAPIE

## Status

Accepted

## Context

Uncertainty quantification (UQ) for LLM outputs is challenging:
- No access to model logits (API-based models)
- Self-evaluation is unreliable
- Need formal guarantees for confidence scores

Options considered:
1. **Logit-based methods**: Requires model access (unavailable)
2. **Self-consistency**: Multiple samples, expensive
3. **Conformal prediction**: Distribution-free, formal guarantees

## Decision

Use MAPIE library for conformal prediction to provide coverage guarantees on confidence intervals.

## Consequences

### Positive

- **Formal guarantees**: Coverage probability is calibrated
- **Distribution-free**: No assumptions about underlying distribution
- **API-compatible**: Works without logit access
- **Interpretable**: "This prediction set covers the true value with 95% probability"

### Negative

- **Requires calibration set**: Need labeled examples for calibration
- **Set predictions**: Returns prediction sets, not point estimates
- **Computational cost**: Requires multiple predictions for calibration

### Implementation Plan

1. Build calibration dataset (~100 manually verified attributions)
2. Use MAPIE's `MapieClassifier` or `MapieRegressor`
3. Report prediction sets with coverage guarantee
4. Evaluate with ECE (Expected Calibration Error)

### References

- [MAPIE Documentation](https://mapie.readthedocs.io/)
- [smoothECE implementation](https://github.com/apple/ml-calibration) for calibration evaluation
- PLAN.md Section 7.3 for detailed UQ strategy
