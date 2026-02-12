# fig-topic-08: Drift Detection & Monitoring

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-08 |
| **Title** | Drift Detection — Stability Timeline with Alert Threshold |
| **Audience** | Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card VIII (Governance & Security group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Timeline showing a stable period followed by a drift event crossing an alert threshold. Communicates: "we continuously monitor for degradation and catch it before users notice."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ALERT THRESHOLD │
│                        /──╲          │
│                       /    ╲──       │
│  ──────────────── ──/        drift   │
│    stable period                     │
│                                      │
│  ■ DATA DRIFT                        │
│  ■ CONCEPT DRIFT                     │
│  ■ PREDICTION DRIFT                  │
│                                      │
│  ┌─────────────────────┐            │
│  │ GRAFANA DASHBOARD   │            │
│  │ ▁▃▅▇▅▃▁▃▅▇█▇▅      │            │
│  └─────────────────────┘            │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Stable line | `data_primary` | Teal flat line, left portion |
| Drift divergence | `data_warning` | Orange rising line, right portion |
| Alert threshold | `line_warning` | Red dashed horizontal line |
| Dashboard mockup | `region_secondary` | Small navy rectangle, sparkline bars inside |
| Drift type labels | `label_editorial` | ALL-CAPS with colored squares |
| Timeline axis | `line_subtle` | Thin grey with time labels |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "DRIFT DETECTION", "ALERT THRESHOLD", "DATA DRIFT", "CONCEPT DRIFT", "PREDICTION DRIFT", "STABLE", time markers.

## Alt Text

Timeline chart showing a stable teal line on the left that begins diverging upward in orange on the right, crossing a red dashed alert threshold. A small Grafana dashboard mockup with sparkline bars appears in the corner. Legend identifies three drift types.
