# Knowledge Base Synthesis

Top-level synthesis connecting domain and technical knowledge for the system.

## Core Thesis

> Music attribution faces fundamental epistemic limits (oracle problem). Technical UQ approaches must embrace and communicate uncertainty rather than hide it. Source-level explainability beats black-box confidence scores.

## Domain Knowledge

Key insights from [domain/SYNTHESIS.md](domain/SYNTHESIS.md):

### Attribution Framework (A0-A3)

| Level | Meaning | Confidence |
|-------|---------|------------|
| A3 | Verified by artist | 0.85+ |
| A2 | Multiple sources agree | 0.70-0.85 |
| A1 | Single source claims | 0.40-0.70 |
| A0 | No data found | 0.00-0.40 |

**Key insight**: A3 is rarely achievable because no oracle exists.

### The Oracle Problem

No external source can verify ALL attribution claims:
- Historical records are incomplete
- Sources disagree legitimately
- Even artists misremember

**Implication**: The system must be transparent about uncertainty.

## Technical Knowledge

Key insights from [technical/SYNTHESIS.md](technical/SYNTHESIS.md):

### UQ Method Limitations (Beigi Taxonomy)

All LLM-based UQ methods have weaknesses:
- Logit-based: Requires model access (unavailable)
- Self-evaluation: Poor calibration
- Consistency: Expensive, paraphrase issues

**the system solution**: Source-level explainability over LLM confidence.

### Conformal Prediction

Provides formal coverage guarantees:
- Prediction sets instead of point estimates
- Requires 100+ calibration examples
- ECE < 0.15 for "calibrated" label

## Cross-Domain Connections

How domain challenges map to technical solutions:

```
┌────────────────────────────────────────────────────────────────┐
│               DOMAIN → TECHNICAL MAPPING                        │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  DOMAIN CHALLENGE              TECHNICAL SOLUTION              │
│  ────────────────              ──────────────────              │
│                                                                │
│  Oracle problem         →     Source-level explainability      │
│  (no universal truth)         (show which sources agree)       │
│                                                                │
│  A0-A3 levels           →     Conformal prediction sets        │
│  (assurance hierarchy)        (formal coverage guarantees)     │
│                                                                │
│  Historical gaps        →     Explicit uncertainty display     │
│  (incomplete records)         (A0/A1 indicators in UI)         │
│                                                                │
│  Artist memory limits   →     Confirmation, not assumption     │
│  (fallible recall)            (chat interface verification)    │
│                                                                │
│  Industry trust         →     Three-tier MCP access            │
│  (label vs indie)             (Internal/Verified/Public)       │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Attribution ↔ Uncertainty

The A0-A3 attribution framework maps directly to uncertainty quantification needs:

| Attribution Level | UQ Requirement | Technical Approach |
|-------------------|----------------|-------------------|
| A3 (Verified) | High confidence + formal guarantee | Artist confirmation + conformal |
| A2 (Corroborated) | Multi-source agreement | Weighted voting |
| A1 (Claimed) | Explicit uncertainty | Single-source confidence |
| A0 (Unknown) | Missing data indicator | Null handling |

### Music Industry ↔ MCP

MCP server design reflects industry trust patterns:

| Industry Pattern | MCP Tier | Access Level |
|------------------|----------|--------------|
| In-house data stewardship | Internal (Tier 1) | Full read/write |
| Established industry partners | Verified (Tier 2) | Read + scoped write |
| Unknown third parties | Public (Tier 3) | Read-only, rate-limited |

## Open Questions

1. **Calibration threshold**: Is 100 examples sufficient for production confidence?
2. **Temporal decay**: Should confidence scores decrease for stale data?
3. **Dispute resolution**: How to handle artist-vs-artist credit conflicts?
4. **Permission granularity**: Per-work vs. catalog-wide AI permissions?

## Implementation Priority

```
Phase 1 (Sprint MVP)
├── Source-level confidence (domain/attribution)
├── Authority weights (technical/uncertainty)
└── Three-tier MCP (industry/mcp)

Phase 2 (Calibration)
├── Conformal prediction (technical/uncertainty)
├── ECE validation (technical/uncertainty)
└── A3 verification flow (domain/attribution)
```

## Related PRDs

- [../prd/vision-v1.md](../prd/vision-v1.md) - Product vision
- [../prd/attribution-engine-prd.md](../prd/attribution-engine-prd.md) - Core implementation
- [../prd/SYNTHESIS.md](../prd/SYNTHESIS.md) - Cross-PRD decisions
