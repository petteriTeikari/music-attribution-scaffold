# A0-A3 Attribution Assurance Framework

A hierarchical model for classifying attribution confidence levels in music metadata.

## Overview

The A0-A3 framework provides a standardized way to communicate the reliability of attribution claims. Rather than using opaque confidence scores, it maps scores to human-understandable assurance levels.

## The Four Levels

### A0: Unknown

- **Definition**: No attribution data available from any source
- **Confidence Score**: 0.0
- **UI Treatment**: "No data found"
- **Action Required**: Full manual input needed

**Example**: A newly uploaded track with no metadata or source matches.

### A1: Claimed

- **Definition**: Single source claims the attribution, unverified
- **Confidence Score**: 0.4-0.6
- **UI Treatment**: "Claimed by [source], unverified"
- **Action Required**: Seek corroboration or artist confirmation

**Example**: Discogs lists "John Smith" as producer, no other sources found.

### A2: Corroborated

- **Definition**: Multiple independent sources agree on the attribution
- **Confidence Score**: 0.7-0.85
- **UI Treatment**: "Confirmed by [N] sources"
- **Action Required**: Display with confidence, flag edge cases

**Example**: Both MusicBrainz and Discogs list "Imogen Heap" as composer.

### A3: Verified

- **Definition**: Attribution confirmed by authoritative source (artist, rights holder)
- **Confidence Score**: 0.85-0.95 (capped to prevent overconfidence)
- **UI Treatment**: "Verified" with checkmark
- **Action Required**: None - treat as fact

**Example**: Artist confirmed credits via the system chat interface.

## Mapping to Confidence Scores

```
A3 (Verified)     ████████████████████  0.85-0.95
A2 (Corroborated) ██████████████        0.70-0.85
A1 (Claimed)      ████████              0.40-0.70
A0 (Unknown)      ██                    0.00-0.40
```

## Why A3 is Rarely Achievable

The [oracle problem](oracle-problem.md) explains why true A3 verification is rare:

1. **No universal authority**: No single entity can verify all claims
2. **Historical gaps**: Session musician credits from 1970s may never be verifiable
3. **Disputes**: Legitimate disagreements exist (co-writing credits, etc.)

## Implementation Notes

```python
def assurance_level(confidence: float, has_artist_verification: bool) -> str:
    """Map confidence score to A0-A3 level."""
    if has_artist_verification and confidence >= 0.85:
        return "A3"  # Verified
    elif confidence >= 0.70:
        return "A2"  # Corroborated
    elif confidence >= 0.40:
        return "A1"  # Claimed
    else:
        return "A0"  # Unknown
```

## User Communication

| Level | User Message | Suggested Action |
|-------|--------------|------------------|
| A3 | "This credit is verified" | Display as fact |
| A2 | "Multiple sources confirm this" | Display with indicator |
| A1 | "One source claims this" | "Can you confirm?" |
| A0 | "No data found" | "Please provide..." |

## Cross-References

- [oracle-problem.md](oracle-problem.md) - Why verification is hard
- [../../../prd/attribution-engine-prd.md](../../../prd/attribution-engine-prd.md) - Technical implementation
- [../../technical/uncertainty/](../../technical/uncertainty/) - UQ methods
