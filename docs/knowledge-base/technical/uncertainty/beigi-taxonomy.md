# LLM Uncertainty Taxonomy (Beigi et al. 2024)

A systematic review of uncertainty quantification methods for large language models.

## Overview

Beigi et al. (2024) categorize UQ methods for LLMs into four approaches, each with distinct trade-offs relevant to the system.

## The Four Categories

### 1. Logit-Based Methods

**How it works**: Analyze the probability distribution over vocabulary tokens.

```
P(next_token) = softmax(logits)
entropy = -Σ p(x) log p(x)
```

**Pros**:
- Computationally efficient
- Direct measure of model's internal state

**Cons**:
- **Requires logit access** (not available for Claude, GPT-4 APIs)
- Softmax probabilities are often overconfident
- Sensitive to temperature parameter

**Relevance to the system**: Not applicable - we use API-based models without logit access.

### 2. Self-Evaluation Methods

**How it works**: Ask the model to assess its own confidence.

```
Prompt: "How confident are you that Imogen Heap composed this track? (1-10)"
Response: "8/10"
```

**Pros**:
- Simple to implement
- Works with any model

**Cons**:
- **Models have poor self-awareness** (tend to be overconfident)
- Sensitive to prompt phrasing
- Can be manipulated by adversarial prompts

**Key finding**: "LLMs exhibit significant overconfidence in their self-reported certainty."

**Relevance to the system**: Use with caution. Can supplement but not replace source-based confidence.

### 3. Consistency-Based Methods

**How it works**: Sample multiple responses and measure agreement.

```python
responses = [model.generate(prompt) for _ in range(5)]
consistency = measure_agreement(responses)
```

**Pros**:
- Works without logit access
- Theoretically grounded (epistemic uncertainty)

**Cons**:
- **Expensive** (multiple API calls)
- **Challenged by paraphrasing** - semantically identical answers may look different
- Temperature-dependent results

**Relevance to the system**: Could be used for high-stakes verifications, but cost is a concern.

### 4. Internal-Based Methods

**How it works**: Analyze model's internal representations (activations, attention).

```
hidden_states → uncertainty_estimator → confidence
```

**Pros**:
- Direct access to model's reasoning
- Can identify specific uncertainty sources

**Cons**:
- **Requires model internals** (not available for API models)
- **High computational cost**
- Model-specific implementation

**Relevance to the system**: Not applicable - we use API-based models.

## Key Insight for the system

> "All methods estimate confidence, but fail to identify specific uncertainty sources."

This is why the system takes a **source-level approach**:

| Traditional UQ | System Approach |
|----------------|-------------------|
| "85% confident" | "3 sources agree: MusicBrainz, Discogs, Artist" |
| Black box | Transparent provenance |
| Single score | Per-field, per-source confidence |

## Recommended the system Strategy

Given the limitations above:

1. **Primary**: Multi-source agreement (not LLM-based)
   - Count agreeing sources
   - Weight by authority
   - Track which sources support each claim

2. **Secondary**: Consistency sampling (for LLM-assisted tasks)
   - Use when LLM extracts/interprets data
   - Keep samples low (2-3) for cost
   - Flag high variance for human review

3. **Avoid**: Self-evaluation prompts as primary confidence
   - Useful for user communication only
   - Never use as scoring input

## Bibliography

- Beigi et al. (2024) "Uncertainty Quantification for Large Language Models: A Survey"
- Liu et al. (2025) "A Comprehensive Survey of LLM Uncertainty Quantification"
- Soudani et al. (2025) "Why Uncertainty Quantification Fails in RAG"

## Cross-References

- [conformal-prediction.md](conformal-prediction.md) - Alternative approach
- [../../domain/attribution/oracle-problem.md](../../domain/attribution/oracle-problem.md) - Epistemic limits
- [../../../prd/attribution-engine-prd.md](../../../prd/attribution-engine-prd.md) - Our approach
