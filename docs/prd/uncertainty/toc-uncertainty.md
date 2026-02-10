---
id: uncertainty/toc-uncertainty
title: Uncertainty Quantification - Table of Contents
status: active
version: 0.1.0
last_updated: 2026-02-04
priority: high

requires:
  - vision-v1.md#executive-summary
  - llm-context.md

cross_refs:
  - attribution-engine/confidence-scoring.md
  - observability/confidence-monitoring.md
  - chat-interface/confidence-driven-prompts.md

tags:
  - uncertainty
  - conformal-prediction
  - calibration
  - cross-cutting

changelog:
  - version: "0.1.0"
    date: 2026-02-04
    changes: "Initial structure for uncertainty quantification"
---

# Uncertainty Quantification

**Purpose**: Formal methods for calibrated confidence scores across the platform

**Key Requirement**: When the system says "90% confident", it must be accurate 90% of the time

**Method**: Conformal Prediction (distribution-free, formal guarantees)

**Cross-Cutting**: Uncertainty quantification applies to all data-producing components

---

## Overview

Traditional ML confidence scores are often poorly calibrated - a model saying "90% confident" might only be correct 70% of the time. The system uses conformal prediction to provide formal guarantees that confidence scores match actual accuracy.

## Core Capabilities

| Capability | Description | PRD |
|------------|-------------|-----|
| **Conformal Prediction** | Core uncertainty method | [conformal-prediction.md](conformal-prediction.md) |
| **Calibration Pipeline** | Maintain calibrated scores | [calibration-pipeline.md](calibration-pipeline.md) |
| **Per-Field Uncertainty** | Confidence for each attribution field | [per-field-uncertainty.md](per-field-uncertainty.md) |
| **Prediction Sets** | For ambiguous fields, return sets of possibilities | [prediction-sets.md](prediction-sets.md) |

## Why Conformal Prediction?

| Property | Benefit for the system |
|----------|---------------------|
| **Formal guarantee** | Coverage ≥ 1-α (90% confident → right 90%+ of time) |
| **Distribution-free** | No assumptions about data distribution |
| **Per-field intervals** | "GLA is 2080-2120 sqft with 90% confidence" |
| **Prediction sets** | "Artist could be: John Smith OR J. Smith" |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   UNCERTAINTY QUANTIFICATION                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 Conformal Prediction                     │   │
│  │                                                         │   │
│  │  Calibration Set              Prediction                │   │
│  │  ───────────────             ──────────                 │   │
│  │                                                         │   │
│  │  Historical data     →     Nonconformity scores         │   │
│  │  (artist corrections)      (calibration thresholds)     │   │
│  │                                                         │   │
│  │                              ↓                          │   │
│  │                                                         │   │
│  │  New prediction      →     Calibrated confidence        │   │
│  │                            OR prediction set            │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │               Integration Points                         │   │
│  │                                                         │   │
│  │  Attribution Engine:  Per-field confidence scores       │   │
│  │  Chat Interface:      Trigger prompts from low scores   │   │
│  │  Voice Agent:         Verbalize uncertainty             │   │
│  │  MCP Server:          Include confidence in responses   │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Confidence Levels (System-Wide)

These levels are used consistently across all the system components:

| Level | Score | Source Requirement | UX Treatment |
|-------|-------|-------------------|--------------|
| **Verified** | ≥90% + artist confirm | Artist-confirmed | Green checkmark |
| **High** | ≥90% | Multi-source agreement | Auto-populate |
| **Medium** | 70-90% | Single source OR minor disagreement | Prompt for verification |
| **Low** | <70% | Sparse/conflicting data | Chat-driven gathering |
| **No Data** | N/A | No sources | Explicit gap marker |

## Calibration Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                     CALIBRATION LOOP                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Collect      →    2. Compute    →    3. Adjust             │
│     Feedback           ECE              Thresholds             │
│                                                                 │
│  Artist confirms      Compare           If ECE > 0.05,         │
│  or corrects          predicted vs      recalibrate using      │
│  HIGH confidence      actual accuracy   expanded validation    │
│  fields                                 set                     │
│                                                                 │
│                           ↓                                     │
│                                                                 │
│                    4. Monitor                                   │
│                       in Langfuse                               │
│                                                                 │
│                    Track:                                       │
│                    • coverage_at_90                             │
│                    • expected_calibration_error                 │
│                    • calibration_drift                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Implementation Priority

1. **conformal-prediction.md** - Core theory and implementation
2. **per-field-uncertainty.md** - Per-field scoring (used by attribution engine)
3. **calibration-pipeline.md** - Continuous calibration
4. **prediction-sets.md** - Ambiguous field handling

## Cross-Cutting Dependencies

| Domain | Uncertainty Integration |
|--------|------------------------|
| **Attribution Engine** | Primary consumer - every field gets a confidence score |
| **Chat Interface** | Low confidence triggers prompts |
| **Voice Agent** | Verbalizes uncertainty ("I'm not sure, but...") |
| **MCP Server** | Includes confidence in API responses |
| **Observability** | Tracks calibration metrics |

## Related Documents

- [attribution-engine/confidence-scoring.md](../attribution-engine/confidence-scoring.md) - Primary implementation
- [observability/confidence-monitoring.md](../observability/confidence-monitoring.md) - Calibration tracking
- [chat-interface/confidence-driven-prompts.md](../chat-interface/confidence-driven-prompts.md) - UX integration

---

## Cross-Domain Impact Diagram

Uncertainty Quantification is the mathematical foundation that makes the system's accuracy claims defensible.

```mermaid
flowchart TB
    subgraph UQ["Uncertainty Quantification"]
        CP[Conformal Prediction<br/>Core Algorithm]
        CAL[Calibration Pipeline<br/>Continuous Updates]
        PFU[Per-Field Uncertainty<br/>Field-Level Scores]
        PS[Prediction Sets<br/>Ambiguity Handling]
    end

    subgraph Consumers["Domain Consumers"]
        AE[Attribution Engine<br/>Every field scored]
        CI[Chat Interface<br/>Low conf = prompt]
        VA[Voice Agent<br/>Verbal hedging]
        MCP[MCP Server<br/>Conf in responses]
    end

    subgraph Feedback["Feedback Loop"]
        OBS[Observability<br/>Tracks ECE]
        ART[Artist Corrections<br/>Ground Truth]
        REC[Recalibration<br/>Threshold Adjustment]
    end

    subgraph Outputs["Calibrated Outputs"]
        HIGH[HIGH Confidence<br/>>=90%, auto-fill]
        MED[MEDIUM Confidence<br/>70-90%, verify]
        LOW[LOW Confidence<br/><70%, prompt]
        ND[NO DATA<br/>Explicit gap]
    end

    CP --> PFU
    CAL --> CP
    PFU --> AE
    PFU --> CI
    PFU --> VA
    PFU --> MCP
    PS --> AE

    AE --> OBS
    CI --> ART
    ART --> REC
    REC --> CAL
    OBS --> REC

    PFU --> HIGH
    PFU --> MED
    PFU --> LOW
    PFU --> ND

    style UQ fill:#fce4ec,stroke:#880e4f
    style CP fill:#fff9c4,stroke:#f57f17
    style CAL fill:#fff9c4,stroke:#f57f17
```

### Domain-by-Domain Integration

| Domain | How Uncertainty Affects It |
|--------|---------------------------|
| **Attribution Engine** | Every field gets a calibrated confidence score; aggregation weights sources by reliability |
| **Chat Interface** | Low/Medium confidence triggers conversational prompts to fill gaps |
| **Voice Agent** | Uncertainty is verbalized naturally ("I'm fairly confident...", "I'm not sure about...") |
| **MCP Server** | API responses include confidence scores so AI platforms can make informed decisions |
| **Observability** | Tracks ECE (Expected Calibration Error) to ensure scores stay calibrated |
| **Data Layer** | Confidence scores stored per-field, enabling historical accuracy analysis |

---

## For Domain Experts (Imogen/Andy)

### Business Impact Summary

**Why This Matters for Artist Relations (Imogen):**
- Uncertainty quantification is HOW we deliver on the "only auto-fill when 90%+ confident" promise
- It protects artists from incorrect data being published without their knowledge
- Explicit "NO DATA" marking is more respectful than inventing data
- Medium confidence prompts engage artists in improving their own data

**Why This Matters for Strategy (Andy):**
- Calibrated confidence is a major differentiator - most metadata systems don't quantify uncertainty at all
- Formal mathematical guarantees (conformal prediction) are defensible to enterprise customers
- This enables tiered product offerings based on data quality/confidence levels
- AI platforms can trust our confidence scores, making MCP more valuable

### The "90% Confident" Business Promise

```mermaid
flowchart LR
    subgraph Problem["Industry Problem"]
        P1[/"Metadata systems<br/>say 'probably right'<br/>but no proof"/]
    end

    subgraph Solution["Attribution Solution"]
        S1[Conformal<br/>Prediction]
        S2[Calibration<br/>Pipeline]
        S3[Continuous<br/>Monitoring]
    end

    subgraph Outcome["Business Outcome"]
        O1[/"When we say 90%<br/>we can PROVE it"/]
    end

    P1 --> S1
    S1 --> S2
    S2 --> S3
    S3 --> O1

    style Problem fill:#ffcdd2,stroke:#b71c1c
    style Solution fill:#fff9c4,stroke:#f57f17
    style Outcome fill:#c8e6c9,stroke:#2e7d32
```

### Why Conformal Prediction?

| Alternative | Why Not |
|-------------|---------|
| LLM self-reported confidence | Notoriously uncalibrated; models say "95% confident" when they're wrong 30% of time |
| Simple heuristics | "3+ sources agree = HIGH" doesn't adapt to data quality differences |
| Bayesian methods | Require assumptions about data distributions that may not hold |
| **Conformal Prediction** | **Distribution-free, formal guarantees, adapts to actual accuracy** |

---

## Known Unknowns

These are identified gaps requiring research or executive decisions:

| Unknown | Impact | Research Needed |
|---------|--------|-----------------|
| **Calibration set size** | How many artist corrections needed before calibration is reliable? | Statistical analysis - likely 100-500 per field type |
| **Field-type stratification** | Should we calibrate separately for names vs. dates vs. numbers? | Analysis of error patterns by field type |
| **Temporal drift** | Does calibration degrade over time? How fast? | Long-term monitoring once system is live |
| **Source reliability weighting** | How to weight Discogs vs. MusicBrainz vs. Spotify differently? | Source-specific accuracy analysis |
| **Prediction set presentation** | When showing multiple possibilities, how many is too many? | UX research with artists |
| **LLM confidence integration** | Can LLM self-reported confidence be calibrated post-hoc? | Experimentation with calibration techniques |

---

## Executive Decision Impact

Uncertainty quantification choices affect product quality, trust, and competitive positioning.

```mermaid
flowchart LR
    subgraph Tech["Technical Decisions"]
        T1[Confidence Threshold<br/>90% vs. 95% vs. 80%]
        T2[Calibration Frequency<br/>Real-time vs. Daily]
        T3[Prediction Set Size<br/>Max 3 vs. Max 5]
        T4[No Data Handling<br/>Explicit vs. Hidden]
    end

    subgraph Biz["Business Impact"]
        B1[Auto-fill Rate<br/>User effort]
        B2[Accuracy Claims<br/>Marketing truth]
        B3[UX Complexity<br/>Decision fatigue]
        B4[Data Completeness<br/>Catalog quality]
    end

    subgraph Strategy["Strategic Implications"]
        S1[Artist Experience]
        S2[Enterprise Trust]
        S3[Product Simplicity]
        S4[Market Positioning]
    end

    T1 --> B1 --> S1
    T2 --> B2 --> S2
    T3 --> B3 --> S3
    T4 --> B4 --> S4

    style Tech fill:#e3f2fd,stroke:#1565c0
    style Biz fill:#fff3e0,stroke:#ef6c00
    style Strategy fill:#f3e5f5,stroke:#7b1fa2
```

### Decision Matrix

| Technical Choice | Options | Business Trade-off |
|------------------|---------|-------------------|
| **High confidence threshold** | 80% / 90% / 95% | More auto-fill vs. more accuracy |
| **Medium → High transition** | Artist confirm / 3+ source / time-based | Artist effort vs. automation |
| **Prediction set max size** | 2 / 3 / 5 options | Simplicity vs. coverage |
| **No data display** | Explicit "Unknown" / Hidden / Prompt-driven | Transparency vs. perceived completeness |
| **Calibration ground truth** | Artist corrections / Expert review / Both | Cost vs. accuracy |

### Recommendations for Executive Review

1. **90% threshold for HIGH confidence** - aligns with Imogen's requirement, industry-leading accuracy
2. **Artist confirmation upgrades to VERIFIED** - creates clear path from HIGH (machine) to VERIFIED (human)
3. **Max 3 options in prediction sets** - more than 3 creates decision fatigue
4. **Explicit "Unknown" for NO DATA** - transparency builds trust, hides nothing
5. **Daily calibration recalculation** - balances compute cost with drift detection

### The Competitive Moat

Uncertainty quantification creates defensible differentiation:

| Competitor | Uncertainty Approach |
|------------|---------------------|
| MusicBrainz | None - data is "correct" or "disputed" |
| Discogs | User voting only |
| Spotify | Internal quality scores, not exposed |
| **the system** | **Formal guarantees, exposed via MCP, continuously calibrated** |
