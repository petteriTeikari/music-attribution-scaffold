# fig-topic-12: MLSecOps & Trust Centers

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-12 |
| **Title** | MLSecOps — Security Pyramid & Trust Center |
| **Audience** | Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card XII (Governance & Security group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Layered security pyramid from infrastructure up to AI governance, with a trust center dashboard. Communicates: "enterprise-grade security is built in layers, visible through real-time transparency."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│           ╱╲                         │
│          ╱  ╲  ISO 42001             │
│         ╱ AI ╲  (AI governance)      │
│        ╱──────╲                      │
│       ╱ ISO    ╲  ISO 27001          │
│      ╱ 27001    ╲ (infosec)          │
│     ╱────────────╲                   │
│    ╱   SOC2       ╲  SOC2 Type II    │
│   ╱   Type II      ╲ (operations)    │
│  ╱────────────────────╲              │
│  INFRASTRUCTURE                      │
│                                      │
│  ┌─────────────────────┐            │
│  │ TRUST CENTER        │            │
│  │ uptime: 99.97%      │            │
│  │ incidents: 0        │            │
│  │ ████████████░░ cert  │            │
│  └─────────────────────┘            │
│                                      │
│  ■ ■ ■ multi-tenant isolation       │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Infrastructure base | `region_neutral` | Grey wide base of pyramid |
| SOC2 layer | `data_warning` | Orange middle-lower layer |
| ISO 27001 layer | `data_primary` | Teal middle-upper layer |
| ISO 42001 apex | `data_primary` | Teal top of pyramid |
| Trust center | `region_secondary` | Navy rectangle with dashboard content |
| Multi-tenant bars | `data_sources` | Three separate colored columns |
| Layer labels | `label_editorial` | ALL-CAPS certification names |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "MLSECOPS", "INFRASTRUCTURE", "SOC2 TYPE II", "ISO 27001", "ISO 42001", "TRUST CENTER", "UPTIME", "INCIDENTS", "MULTI-TENANT ISOLATION".

## Alt Text

Layered security pyramid with grey infrastructure at the base, orange SOC2 Type II above, teal ISO 27001 next, and teal ISO 42001 at the apex for AI governance. A trust center dashboard shows uptime and incident metrics. Three separate colored columns illustrate multi-tenant data isolation.
