---
id: observability/toc-observability
title: Observability - Table of Contents
status: active
version: 0.1.0
last_updated: 2026-02-04
priority: medium

requires:
  - vision-v1.md#executive-summary
  - llm-context.md

cross_refs:
  - attribution-engine/confidence-scoring.md
  - chat-interface/toc-chat-interface.md
  - voice-agent/toc-voice-agent.md
  - uncertainty/toc-uncertainty.md

tags:
  - observability
  - langfuse
  - monitoring
  - cross-cutting

changelog:
  - version: "0.1.0"
    date: 2026-02-04
    changes: "Initial structure for observability infrastructure"
---

# Observability

**Purpose**: Comprehensive monitoring of LLM interactions, confidence calibration, and system health

**Primary Tool**: Langfuse for LLM observability

**Cross-Cutting**: This domain provides monitoring for all other domains

---

## Overview

Observability in the system focuses on:
1. **LLM Interactions**: Track chat/voice conversations, prompts, responses
2. **Confidence Calibration**: Verify "90% confident" actually means 90% accurate
3. **System Health**: Standard application monitoring
4. **Business Metrics**: Gap-fill rates, artist engagement, MCP usage

## Core Capabilities

| Capability | Description | PRD |
|------------|-------------|-----|
| **Langfuse Integration** | Core LLM observability | [langfuse.md](langfuse.md) |
| **Confidence Monitoring** | Track calibration metrics | [confidence-monitoring.md](confidence-monitoring.md) |
| **Conversation Tracking** | Chat and voice session logs | [conversation-tracking.md](conversation-tracking.md) |
| **Business Metrics** | KPIs and dashboards | [business-metrics.md](business-metrics.md) |
| **Alerting** | Threshold-based alerts | [alerting.md](alerting.md) |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      OBSERVABILITY                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Data Sources                    Langfuse                       │
│  ────────────                    ────────                       │
│                                                                 │
│  ┌─────────────┐                 ┌─────────────────────────┐   │
│  │    Chat     │────traces──────►│                         │   │
│  │  Interface  │                 │      Langfuse           │   │
│  └─────────────┘                 │                         │   │
│                                  │  • Traces               │   │
│  ┌─────────────┐                 │  • Spans                │   │
│  │   Voice     │────traces──────►│  • Scores               │   │
│  │   Agent     │                 │  • Sessions             │   │
│  └─────────────┘                 │                         │   │
│                                  │  Custom Scores:         │   │
│  ┌─────────────┐                 │  • confidence_calibration│  │
│  │ Attribution │────scores──────►│  • gap_fill_rate        │   │
│  │   Engine    │                 │  • source_agreement     │   │
│  └─────────────┘                 │                         │   │
│                                  └───────────┬─────────────┘   │
│  ┌─────────────┐                             │                  │
│  │    MCP      │────metrics─────►            │                  │
│  │   Server    │                             │                  │
│  └─────────────┘                             ▼                  │
│                                  ┌─────────────────────────┐   │
│                                  │      Dashboards         │   │
│                                  │  • Calibration          │   │
│                                  │  • Conversation Quality │   │
│                                  │  • System Health        │   │
│                                  └─────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Key Metrics

### Confidence Calibration (Critical)

Per Imogen's "90-100% confident" requirement:

| Metric | Target | Description |
|--------|--------|-------------|
| `coverage_at_90` | ≥90% | % of HIGH confidence fields confirmed correct |
| `expected_calibration_error` | <0.05 | Difference between predicted and actual accuracy |
| `auto_fill_rate` | >60% | % of fields auto-filled (HIGH confidence) |
| `gap_rate` | <20% | % of fields with NO_DATA |

### Conversation Quality

| Metric | Target | Description |
|--------|--------|-------------|
| `gap_fill_success_rate` | >70% | % of prompted gaps successfully filled |
| `conversation_length` | <5 turns | Average turns to fill a gap |
| `abandonment_rate` | <15% | % of conversations abandoned mid-gap |

### System Health

| Metric | Target | Description |
|--------|--------|-------------|
| `source_api_latency` | <2s | p95 latency for external source APIs |
| `aggregation_latency` | <5s | p95 time to aggregate all sources |
| `mcp_request_latency` | <500ms | p95 MCP response time |

## Langfuse Integration

```python
from langfuse import Langfuse
from langfuse.decorators import observe, langfuse_context

langfuse = Langfuse()

@observe(as_type="generation")
async def generate_gap_prompt(field: str, sources: list[str]) -> str:
    """Generate a chat prompt for gap-filling."""
    # LLM call is automatically traced
    ...

# Custom confidence score
langfuse_context.score_current_trace(
    name="confidence_calibration",
    value=0.92,
    comment="Expected: 0.90, Actual: 0.92"
)
```

## Implementation Priority

1. **langfuse.md** - Core integration
2. **confidence-monitoring.md** - Calibration tracking (critical for "90%" claim)
3. **conversation-tracking.md** - Chat/voice session logs
4. **business-metrics.md** - KPI dashboards
5. **alerting.md** - Threshold alerts

## Cross-Cutting Dependencies

Every domain integrates with observability:

| Domain | Observability Integration |
|--------|---------------------------|
| Attribution Engine | Confidence scores, source latency |
| Chat Interface | Conversation traces, gap-fill rates |
| Voice Agent | Session quality, latency |
| MCP Server | Request logs, permission checks |
| Data Layer | Query performance |

## Related Documents

- [uncertainty/conformal-prediction.md](../uncertainty/conformal-prediction.md) - What we're monitoring
- [attribution-engine/confidence-scoring.md](../attribution-engine/confidence-scoring.md) - Confidence metrics source
- [defaults.yaml](../defaults.yaml) - Langfuse configuration

---

## Cross-Domain Impact Diagram

Observability is the nervous system of the system - every domain emits telemetry, and observability provides the feedback loop.

```mermaid
flowchart TB
    subgraph Observability["Observability Layer"]
        LF[Langfuse<br/>LLM Traces]
        CM[Confidence Monitoring<br/>Calibration Metrics]
        CT[Conversation Tracking<br/>Session Logs]
        BM[Business Metrics<br/>KPI Dashboards]
        AL[Alerting<br/>Threshold Triggers]
    end

    subgraph DataSources["Data-Producing Domains"]
        AE[Attribution Engine]
        CI[Chat Interface]
        VA[Voice Agent]
        MCP[MCP Server]
        DL[Data Layer]
    end

    subgraph CrossCutting["Cross-Cutting Concerns"]
        SEC[Security]
        UQ[Uncertainty<br/>Quantification]
        IP[Identity &<br/>Permissions]
        INF[Infrastructure]
    end

    subgraph Outputs["Observability Outputs"]
        DASH[Dashboards]
        ALERTS[Alert Notifications]
        REPORTS[Calibration Reports]
        AUDIT[Audit Logs]
    end

    AE -->|"Confidence scores"| LF
    AE -->|"Source latency"| CM
    CI -->|"Conversation traces"| CT
    CI -->|"Gap-fill rates"| BM
    VA -->|"Session quality"| CT
    VA -->|"Latency metrics"| LF
    MCP -->|"Request logs"| LF
    MCP -->|"Permission checks"| BM
    DL -->|"Query performance"| LF

    SEC -->|"Auth events"| AUDIT
    UQ -->|"Calibration data"| CM
    IP -->|"Verification events"| BM
    INF -->|"System health"| AL

    LF --> DASH
    CM --> REPORTS
    CT --> DASH
    BM --> DASH
    AL --> ALERTS

    style Observability fill:#e8f5e9,stroke:#2e7d32
    style LF fill:#fff9c4,stroke:#f57f17
    style CM fill:#fff9c4,stroke:#f57f17
```

### Domain-by-Domain Telemetry

| Domain | Metrics Emitted | Why It Matters |
|--------|-----------------|----------------|
| **Attribution Engine** | Confidence scores, source latency, aggregation time | Core product quality - is the data accurate? |
| **Chat Interface** | Conversation length, gap-fill success, abandonment | User engagement - are artists completing profiles? |
| **Voice Agent** | Latency, session duration, transcription quality | UX quality - is voice natural and responsive? |
| **MCP Server** | Request volume, permission check results, latency | API adoption - are AI platforms using us? |
| **Data Layer** | Query latency, connection pool usage, error rates | System health - is the database performing? |
| **Uncertainty** | ECE, calibration drift, coverage metrics | Trust metric - does "90% confident" mean 90%? |
| **Security** | Auth failures, suspicious patterns, audit events | Security posture - are we protected? |
| **Infrastructure** | CPU, memory, request counts, error rates | Operational health - is the system up? |

---

## For Domain Experts (Imogen/Andy)

### Business Impact Summary

**Why This Matters for Artist Relations (Imogen):**
- Observability is how we prove the "90% confident" claim is real, not marketing
- Gap-fill metrics show which parts of the artist experience need improvement
- Conversation tracking identifies where artists struggle or abandon the process
- Business metrics dashboards can show artist engagement and data completeness

**Why This Matters for Strategy (Andy):**
- Calibration reports are audit-ready proof of accuracy for enterprise deals
- MCP usage metrics demonstrate AI platform adoption for investor conversations
- Alerting catches problems before they become customer complaints
- Business dashboards provide the KPIs needed for board reporting

### Key Business Metrics

| Metric | What It Tells Us | Target |
|--------|------------------|--------|
| **coverage_at_90** | Are HIGH confidence fields actually 90%+ accurate? | >= 90% |
| **gap_fill_success_rate** | Are artists successfully completing their profiles? | >= 70% |
| **mcp_daily_requests** | How much are AI platforms using our data? | Growth metric |
| **artist_onboarding_completion** | What % of artists complete verification? | >= 80% |
| **abandonment_rate** | Where do artists give up? | < 15% |

### The "90% Confidence" Promise

Imogen's requirement that the system only auto-fills data when "90-100% confident" is enforced through observability:

```mermaid
flowchart LR
    subgraph Promise["The Promise"]
        P1[/"90% confident<br/>means 90% accurate"/]
    end

    subgraph Measurement["How We Measure"]
        M1[Langfuse scores]
        M2[Calibration pipeline]
        M3[ECE calculation]
    end

    subgraph Proof["How We Prove"]
        PR1[Calibration dashboards]
        PR2[Historical accuracy reports]
        PR3[Per-field breakdowns]
    end

    P1 --> M1 --> PR1
    P1 --> M2 --> PR2
    P1 --> M3 --> PR3

    style Promise fill:#e3f2fd,stroke:#1565c0
    style Measurement fill:#fff3e0,stroke:#ef6c00
    style Proof fill:#e8f5e9,stroke:#2e7d32
```

---

## Known Unknowns

These are identified gaps requiring research or executive decisions:

| Unknown | Impact | Research Needed |
|---------|--------|-----------------|
| **Langfuse cost at scale** | Per-trace pricing may become significant at high volume | Model costs at 10K, 100K, 1M daily traces |
| **PII in traces** | Conversation content may contain sensitive data | Data retention and anonymization policies |
| **Real-time vs. batch calibration** | How often must we recalculate ECE? | Performance vs. accuracy trade-off analysis |
| **Alert fatigue thresholds** | Too many alerts = ignored alerts | Establish baseline, tune over time |
| **Cross-tenant metrics** | Can we aggregate metrics without revealing per-tenant data? | Privacy-preserving aggregation methods |
| **Calibration ground truth** | Need artist confirmations to calculate accuracy | Incentive design for artist feedback |

---

## Executive Decision Impact

Observability choices affect what we can measure, prove, and promise.

```mermaid
flowchart LR
    subgraph Tech["Technical Decisions"]
        T1[Observability Platform<br/>Langfuse vs. LangSmith vs. DIY]
        T2[Trace Retention<br/>7d vs. 30d vs. 90d]
        T3[Alerting Channels<br/>Slack vs. PagerDuty vs. Email]
        T4[Dashboard Access<br/>Internal vs. Customer-facing]
    end

    subgraph Biz["Business Impact"]
        B1[Monthly Cost<br/>$100-$2000+]
        B2[Compliance<br/>Audit readiness]
        B3[Incident Response<br/>MTTR speed]
        B4[Customer Trust<br/>Transparency]
    end

    subgraph Strategy["Strategic Implications"]
        S1[Margin Pressure]
        S2[Enterprise Sales]
        S3[SLA Commitments]
        S4[Product Differentiation]
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
| **Observability platform** | Langfuse, LangSmith, Helicone, DIY | Cost vs. features vs. integration effort |
| **Trace retention** | 7/30/90 days | Storage cost vs. historical analysis depth |
| **Calibration frequency** | Real-time / hourly / daily | Compute cost vs. accuracy freshness |
| **Dashboard scope** | Internal only / customer-facing | Development effort vs. customer trust |
| **Alert severity levels** | 2-tier / 3-tier / custom | Simplicity vs. nuanced response |

### Recommendations for Executive Review

1. **Langfuse for MVP** - best LLM observability features, reasonable cost, can migrate later if needed
2. **30-day trace retention** - balances cost with ability to investigate issues and prove calibration
3. **Daily calibration recalculation** - hourly is overkill, weekly misses drift
4. **Customer-facing accuracy dashboard** (Phase 2) - major trust differentiator, shows confidence in our own claims
5. **Slack + email alerts initially** - PagerDuty when we have 24/7 on-call
