# fig-repo-30: MCP Production Observability Stack

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-30 |
| **Title** | MCP Production Observability Stack |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/mcp-security-production-research.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Show the complete observability architecture for production MCP deployments -- structured logging, OpenTelemetry traces, metrics, and security event monitoring -- split between the data plane (what to capture) and the analysis plane (how to process).

## Key Message

Production MCP servers need three observability layers: structured logs for compliance (EU AI Act Art. 12), OTel traces for debugging, and security metrics for threat detection.

## Visual Concept

Split-panel layout with left side showing three data plane capture categories (structured logs, OTel traces, security metrics) and right side showing corresponding analysis plane outputs (compliance, debugging, threat detection), connected by horizontal flow arrows.

```
+-----------------------------------------------------------------------+
|  MCP PRODUCTION OBSERVABILITY                                          |
|  ■ Three Layers for Production Readiness                               |
+-----------------------------------------------------------------------+
|                                                                        |
|  DATA PLANE (Capture)               ANALYSIS PLANE (Process)           |
|  ────────────────────               ─────────────────────              |
|                                                                        |
|  ┌─────────────────────┐           ┌─────────────────────┐            |
|  │ STRUCTURED LOGS     │    ──▶    │ COMPLIANCE          │            |
|  │ Client identity     │           │ EU AI Act Art. 12   │            |
|  │ Tool invoked        │           │ Retention policy    │            |
|  │ Input/output hash   │           │ Audit export        │            |
|  │ Latency, status     │           │                     │            |
|  └─────────────────────┘           └─────────────────────┘            |
|                                                                        |
|  ┌─────────────────────┐           ┌─────────────────────┐            |
|  │ OTEL TRACES         │    ──▶    │ DEBUGGING           │            |
|  │ MCP semantic conv   │           │ Request waterfall   │            |
|  │ Tool span context   │           │ Latency breakdown   │            |
|  │ Error propagation   │           │ Dependency graph    │            |
|  └─────────────────────┘           └─────────────────────┘            |
|                                                                        |
|  ┌─────────────────────┐           ┌─────────────────────┐            |
|  │ SECURITY METRICS    │    ──▶    │ THREAT DETECTION    │            |
|  │ Blocked requests    │           │ Anomaly detection   │            |
|  │ Auth failures       │           │ Alert thresholds    │            |
|  │ Rate limit hits     │           │ Incident response   │            |
|  └─────────────────────┘           └─────────────────────┘            |
+-----------------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 120]
    content: "MCP PRODUCTION OBSERVABILITY"
    role: title

  - id: data_plane_zone
    bounds: [80, 160, 820, 860]
    role: capture_panel

  - id: analysis_plane_zone
    bounds: [1020, 160, 820, 860]
    role: analysis_panel

anchors:
  - id: data_plane_heading
    position: [80, 170]
    size: [820, 50]
    role: section_heading
    label: "DATA PLANE (Capture)"

  - id: analysis_plane_heading
    position: [1020, 170]
    size: [820, 50]
    role: section_heading
    label: "ANALYSIS PLANE (Process)"

  - id: structured_logs
    position: [100, 260]
    size: [760, 200]
    role: processing_stage
    label: "STRUCTURED LOGS"

  - id: logs_client_id
    position: [120, 320]
    size: [720, 30]
    role: data_flow
    label: "Client identity"

  - id: logs_tool
    position: [120, 355]
    size: [720, 30]
    role: data_flow
    label: "Tool invoked"

  - id: logs_hash
    position: [120, 390]
    size: [720, 30]
    role: data_flow
    label: "Input/output hash"

  - id: logs_latency
    position: [120, 425]
    size: [720, 30]
    role: data_flow
    label: "Latency, status"

  - id: compliance_box
    position: [1040, 260]
    size: [760, 200]
    role: processing_stage
    label: "COMPLIANCE"

  - id: compliance_euai
    position: [1060, 320]
    size: [720, 30]
    role: data_flow
    label: "EU AI Act Art. 12"

  - id: compliance_retention
    position: [1060, 355]
    size: [720, 30]
    role: data_flow
    label: "Retention policy"

  - id: compliance_audit
    position: [1060, 390]
    size: [720, 30]
    role: data_flow
    label: "Audit export"

  - id: flow_logs_compliance
    from: structured_logs
    to: compliance_box
    type: arrow
    label: ""

  - id: otel_traces
    position: [100, 510]
    size: [760, 180]
    role: processing_stage
    label: "OTEL TRACES"

  - id: otel_semantic
    position: [120, 570]
    size: [720, 30]
    role: data_flow
    label: "MCP semantic conv"

  - id: otel_span
    position: [120, 605]
    size: [720, 30]
    role: data_flow
    label: "Tool span context"

  - id: otel_error
    position: [120, 640]
    size: [720, 30]
    role: data_flow
    label: "Error propagation"

  - id: debugging_box
    position: [1040, 510]
    size: [760, 180]
    role: processing_stage
    label: "DEBUGGING"

  - id: debug_waterfall
    position: [1060, 570]
    size: [720, 30]
    role: data_flow
    label: "Request waterfall"

  - id: debug_latency
    position: [1060, 605]
    size: [720, 30]
    role: data_flow
    label: "Latency breakdown"

  - id: debug_dependency
    position: [1060, 640]
    size: [720, 30]
    role: data_flow
    label: "Dependency graph"

  - id: flow_otel_debugging
    from: otel_traces
    to: debugging_box
    type: arrow
    label: ""

  - id: security_metrics
    position: [100, 740]
    size: [760, 180]
    role: processing_stage
    label: "SECURITY METRICS"

  - id: security_blocked
    position: [120, 800]
    size: [720, 30]
    role: data_flow
    label: "Blocked requests"

  - id: security_auth
    position: [120, 835]
    size: [720, 30]
    role: data_flow
    label: "Auth failures"

  - id: security_rate
    position: [120, 870]
    size: [720, 30]
    role: data_flow
    label: "Rate limit hits"

  - id: threat_box
    position: [1040, 740]
    size: [760, 180]
    role: processing_stage
    label: "THREAT DETECTION"

  - id: threat_anomaly
    position: [1060, 800]
    size: [720, 30]
    role: data_flow
    label: "Anomaly detection"

  - id: threat_alerts
    position: [1060, 835]
    size: [720, 30]
    role: data_flow
    label: "Alert thresholds"

  - id: threat_incident
    position: [1060, 870]
    size: [720, 30]
    role: data_flow
    label: "Incident response"

  - id: flow_security_threat
    from: security_metrics
    to: threat_box
    type: arrow
    label: ""
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Structured Logs | `processing_stage` | Client identity, tool invoked, input/output hash, latency/status |
| OTel Traces | `processing_stage` | MCP semantic conventions, tool span context, error propagation |
| Security Metrics | `processing_stage` | Blocked requests, auth failures, rate limit hits |
| Compliance | `processing_stage` | EU AI Act Art. 12, retention policy, audit export |
| Debugging | `processing_stage` | Request waterfall, latency breakdown, dependency graph |
| Threat Detection | `processing_stage` | Anomaly detection, alert thresholds, incident response |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Structured Logs | Compliance | arrow | "feeds" |
| OTel Traces | Debugging | arrow | "feeds" |
| Security Metrics | Threat Detection | arrow | "feeds" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| None | Three layers follow standard observability pillar taxonomy | implicit in layout |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "DATA PLANE (Capture)"
- Label 2: "ANALYSIS PLANE (Process)"
- Label 3: "STRUCTURED LOGS"
- Label 4: "Client identity"
- Label 5: "Tool invoked"
- Label 6: "Input/output hash"
- Label 7: "Latency, status"
- Label 8: "COMPLIANCE"
- Label 9: "EU AI Act Art. 12"
- Label 10: "Retention policy"
- Label 11: "Audit export"
- Label 12: "OTEL TRACES"
- Label 13: "MCP semantic conv"
- Label 14: "Tool span context"
- Label 15: "Error propagation"
- Label 16: "DEBUGGING"
- Label 17: "Request waterfall"
- Label 18: "Latency breakdown"
- Label 19: "Dependency graph"
- Label 20: "SECURITY METRICS"
- Label 21: "Blocked requests"
- Label 22: "Auth failures"
- Label 23: "Rate limit hits"
- Label 24: "THREAT DETECTION"
- Label 25: "Anomaly detection"
- Label 26: "Alert thresholds"
- Label 27: "Incident response"

### Caption (for embedding in documentation)

MCP production observability architecture with three layers: structured logs for EU AI Act compliance, OpenTelemetry traces for debugging, and security metrics for threat detection.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color.
5. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 30." or any numbered academic caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. EU AI Act Article 12 requires logging sufficient for post-hoc compliance verification. Do NOT invent specific retention periods.
9. OpenTelemetry MCP semantic conventions are PROPOSED by Anthropic, not finalized.
10. "Input/output hash" means hashed values for privacy -- NOT raw inputs in logs.
11. Do NOT show specific tool names (Grafana, Datadog, etc.) -- keep generic.
12. The three layers (logs, traces, metrics) follow standard observability pillar taxonomy.

## Alt Text

Split-panel MCP production observability architecture showing data plane with structured logs, OpenTelemetry traces, and security metrics feeding into analysis plane with EU AI Act compliance, debugging waterfall, and threat detection dashboards.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![MCP production observability stack with three data capture layers feeding three analysis outputs.](docs/figures/repo-figures/assets/fig-repo-30-mcp-observability.jpg)

*Figure 30. MCP production observability: structured logs for compliance, OTel traces for debugging, security metrics for threat detection.*

### From this figure plan (relative)

![MCP production observability](../assets/fig-repo-30-mcp-observability.jpg)

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided
- [x] Audience level correct (L3)
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
