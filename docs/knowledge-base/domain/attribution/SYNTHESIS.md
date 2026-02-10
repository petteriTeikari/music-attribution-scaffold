# Attribution Knowledge Synthesis

Key insights from music attribution domain research.

## Core Insight

> Attribution verification faces fundamental epistemic limits. No external oracle can verify ALL claims, so systems must embrace and communicate uncertainty.

## A0-A3 Framework Summary

Four assurance levels map confidence to human understanding:

| Level | Meaning | Score Range | Action |
|-------|---------|-------------|--------|
| A3 | Verified (artist confirmed) | 0.85+ | Trust |
| A2 | Corroborated (sources agree) | 0.70-0.85 | Display with indicator |
| A1 | Claimed (single source) | 0.40-0.70 | Seek confirmation |
| A0 | Unknown (no data) | 0.00-0.40 | Request input |

**Key insight**: A3 is rarely achievable due to the oracle problem.

See: [a0-a3-framework.md](a0-a3-framework.md)

## Oracle Problem Summary

Why 100% accuracy is impossible:

1. **No universal authority** exists for music credits
2. **Historical records** are incomplete
3. **Memory is fallible** - even artists misremember
4. **Legitimate disputes** exist between collaborators

**Implication**: The system must be transparent about uncertainty, not hide it.

See: [oracle-problem.md](oracle-problem.md)

## Cross-Domain Connection

The attribution challenge connects directly to technical UQ approaches:

```
Attribution Problem          →    Technical Solution
─────────────────────              ──────────────────
No oracle exists            →    Multi-source aggregation
Sources disagree            →    Weighted voting + confidence
Historical gaps             →    Explicit A0/A1 levels
Artist memory limits        →    Confirmation, not assumption
```

## Implications for the system

1. **Design for uncertainty**: Every UI element should communicate confidence level
2. **Source transparency**: Show which databases support each claim
3. **Human-in-the-loop**: Chat interface for artist confirmation
4. **Confidence caps**: Never display 100%, even for A3

## Open Questions

- How to handle disputed credits between collaborators?
- What's the minimum corroboration for A2?
- Should confidence decay over time (stale data)?

## Related Knowledge

- [../../technical/uncertainty/](../../technical/uncertainty/) - UQ methods
- [../../../prd/attribution-engine-prd.md](../../../prd/attribution-engine-prd.md) - Implementation
