# Conformal Prediction for the system

Distribution-free uncertainty quantification with coverage guarantees.

## Why Conformal Prediction?

Traditional confidence scores (softmax probabilities) are often miscalibrated. Conformal prediction provides **formal coverage guarantees** without assuming any distribution.

**Key insight**: Instead of predicting "The composer is X with 85% confidence," conformal prediction says "The composer is in {X, Y, Z} with 95% coverage guarantee."

## Core Concept

Given:
- A calibration set of labeled examples
- A new prediction
- A desired coverage level (e.g., 95%)

Conformal prediction returns a **prediction set** that contains the true answer with the specified probability.

```
Traditional: "Composer is Imogen Heap (0.87 confidence)"
             ↳ What does 0.87 mean? Often miscalibrated.

Conformal:   "Composer is in {Imogen Heap} with 95% coverage"
             ↳ Formal guarantee: 95% of such sets contain the truth.
```

## MAPIE Library

The system uses [MAPIE](https://mapie.readthedocs.io/) for conformal prediction:

```python
from mapie.classification import MapieClassifier
from sklearn.ensemble import RandomForestClassifier

# Train base model
base_model = RandomForestClassifier()
base_model.fit(X_train, y_train)

# Wrap with MAPIE for conformal prediction
mapie = MapieClassifier(estimator=base_model, cv="prefit")
mapie.fit(X_calibration, y_calibration)

# Get prediction sets with 95% coverage
y_pred_sets = mapie.predict(X_test, alpha=0.05)  # alpha = 1 - coverage
```

## Application to Attribution

### Entity Resolution

For "John Smith" appearing in multiple sources:

```python
# Without conformal
result = {"match": "John Smith (MusicBrainz)", "confidence": 0.72}
# Is 0.72 good enough? Unclear.

# With conformal
result = {
    "prediction_set": [
        "John Smith (MusicBrainz)",
        "J. Smith (Discogs)"
    ],
    "coverage": 0.95
}
# Interpretation: 95% of the time, the true match is in this set.
```

### Credit Verification

For verifying a composer claim:

```python
# Traditional
verified = True  # Based on what threshold?

# Conformal
prediction_set = ["verified", "disputed"]  # If both in set, human review needed
coverage = 0.95
```

## When Prediction Sets Are Large

Large prediction sets indicate high uncertainty:

| Set Size | Interpretation | Action |
|----------|---------------|--------|
| 1 | High confidence | Accept |
| 2-3 | Some uncertainty | Flag for review |
| >3 | Low confidence | Request more data |

## Calibration Requirements

Conformal prediction requires a **calibration set**:

- **Minimum size**: 100+ examples (more = tighter bounds)
- **Representative**: Must reflect production distribution
- **Ground truth**: Must have verified labels

For the system MVP:
1. Manually verify 100 attributions
2. Use as calibration set
3. Report prediction set sizes alongside confidence

## Advantages Over Alternatives

| Method | Pros | Cons |
|--------|------|------|
| **Softmax** | Simple | Often miscalibrated |
| **Temperature scaling** | Easy calibration | Requires logit access |
| **Conformal** | Formal guarantees | Larger outputs (sets) |

**Why conformal for the system**: We use API-based LLMs (no logit access), and we need formal guarantees for trust.

## Evaluation Metrics

### Expected Calibration Error (ECE)

Measures how well predicted confidence matches actual accuracy:

```python
def expected_calibration_error(predictions, ground_truth, n_bins=10):
    """Compute ECE for calibration validation."""
    # Bin predictions by confidence
    # Compare average confidence vs accuracy in each bin
    # Weight by bin size
    ...
```

**Target**: ECE < 0.15 for production deployment.

### smoothECE

For small sample sizes, use smoothECE from [Apple's ml-calibration](https://github.com/apple/ml-calibration):

```python
from calibration import smooth_ece

ece = smooth_ece(predictions, ground_truth)
```

## Cross-References

- [beigi-taxonomy.md](beigi-taxonomy.md) - LLM uncertainty methods
- [MAPIE Documentation](https://mapie.readthedocs.io/)
- [Angelopoulos & Bates 2021](https://arxiv.org/abs/2107.07511) - Conformal primer
- [../../../prd/attribution-engine-prd.md](../../../prd/attribution-engine-prd.md) - Implementation
