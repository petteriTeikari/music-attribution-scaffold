# The Oracle Problem in Music Attribution

Why no external source can verify ALL attribution claims.

## The Core Problem

> There is no omniscient oracle that can definitively verify every music credit claim.

Unlike structured domains (e.g., "Is this a valid ISBN?"), music attribution faces fundamental epistemic limits.

## Why This Matters for the system

The system cannot promise 100% accuracy because:

1. **Historical records are incomplete**: Session musicians from the 1960s-80s often went uncredited
2. **Sources disagree**: Legitimate conflicts exist between databases
3. **Memory is fallible**: Even artists misremember their own credits
4. **Ghostwriting exists**: Some credits are intentionally hidden

## The Verification Hierarchy

```
                    ┌─────────────────┐
                    │   Artist says   │  Most authoritative
                    │   "I did this"  │  but still fallible
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Legal documents │  Contracts, registrations
                    │  (if available)  │  but often private
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Multiple sources │  Cross-reference
                    │     agree        │  (the system approach)
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Single source   │  May be wrong
                    │    claims        │
                    └─────────────────┘
```

## Implications for Confidence Scoring

Because there's no oracle, The system must:

1. **Embrace uncertainty**: Confidence scores are estimates, not guarantees
2. **Be transparent**: Show which sources support each claim
3. **Allow disputes**: Artists can challenge incorrect data
4. **Cap confidence**: Never show 100%, even with artist verification (they might be wrong)

## The A3 Challenge

The A3 (Verified) level requires artist confirmation, but even this has limits:

| Scenario | True A3? |
|----------|----------|
| Artist confirms their own composition | Yes |
| Artist confirms session musician worked on track | Maybe (memory) |
| Artist confirms co-writer (disputed by co-writer) | No (conflict) |
| Estate confirms credits for deceased artist | Probably (but hearsay) |

## Practical Approach

Given the oracle problem, the system takes a **probabilistic stance**:

1. **Aggregate multiple sources** to increase confidence
2. **Weight sources by authority** (artist > database > automated)
3. **Display uncertainty explicitly** to users
4. **Enable human correction** via chat interface
5. **Track provenance** so claims can be audited

## Philosophical Background

This echoes broader epistemological challenges:

- **Gettier problems**: Justified true belief isn't sufficient for knowledge
- **Testimony-based knowledge**: How much do we trust what others tell us?
- **Documentary evidence**: Records can be forged, incomplete, or misinterpreted

## Cross-References

- [a0-a3-framework.md](a0-a3-framework.md) - Assurance levels
- [../../technical/uncertainty/](../../technical/uncertainty/) - UQ approaches
- [../../../prd/attribution-engine-prd.md](../../../prd/attribution-engine-prd.md) - How we handle this
