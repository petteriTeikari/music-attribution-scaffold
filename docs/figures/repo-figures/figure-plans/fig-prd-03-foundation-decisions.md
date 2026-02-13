# fig-prd-03: Level 0-1 Foundation Decisions

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-03 |
| **Title** | Level 0-1: Foundation Decisions -- Language, Framework, DB, Package Manager |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/REPORT.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Details the foundational L1 business decisions and how they cascade into core technology choices. Shows the four L1 nodes (Build vs Buy, Target Market, Revenue Model, Regulatory Posture) and their direct influence on L2 architecture nodes. This is where the "DNA" of every instantiation is set.

The key message is: "Four business decisions at L1 determine the probability landscape for all 26+ downstream technology choices."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  FOUNDATION DECISIONS                                          |
|  ■ L1 Business Layer Sets the Probability Landscape            |
+---------------------------------------------------------------+
|                                                                |
|  ┌─────────────────┐        ┌─────────────────────┐           |
|  │ BUILD VS BUY    │        │ TARGET MARKET        │           |
|  │ ■ Custom Build  │───────>│ ■ Indie Creators     │           |
|  │ ■ Managed Svc   │        │ ■ Mid-tier Labels    │           |
|  │ ■ SaaS Max      │        │ ■ Enterprise Rights  │           |
|  └────────┬────────┘        └──────┬───────────────┘           |
|           │                        │                            |
|   ┌───────┼────────────────────────┼──────────┐                |
|   │       ▼                        ▼          │                |
|   │  ┌──────────┐  ┌──────────┐  ┌────────┐  │                |
|   │  │Data Model│  │ Service  │  │  API   │  │  L2            |
|   │  │Complexity│  │  Decomp  │  │Protocol│  │                |
|   │  └──────────┘  └──────────┘  └────────┘  │                |
|   └──────────────────────────────────────────-┘                |
|                                                                |
|  ┌─────────────────┐        ┌─────────────────────┐           |
|  │ REVENUE MODEL   │        │ REGULATORY POSTURE   │           |
|  │ ■ Open Core     │        │ ■ Best Effort        │           |
|  │ ■ Freemium SaaS │        │ ■ Compliance Aware   │           |
|  │ ■ Enterprise Lic│        │ ■ Compliance First   │           |
|  └─────────────────┘        └─────────────────────┘           |
|                                                                |
+---------------------------------------------------------------+
|  SKIP CONNECTIONS: Build vs Buy reaches L3 (DB), L4 (Compute) |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "FOUNDATION DECISIONS" with coral accent square |
| Build vs Buy node | `decision_point` | Three options: Custom Build, Managed Services, SaaS Maximalist |
| Target Market node | `decision_point` | Three options: Indie Creators, Mid-tier Labels, Enterprise Rights Orgs |
| Revenue Model node | `decision_point` | Three options: Open Core, Freemium SaaS, Enterprise Licensing |
| Regulatory Posture node | `decision_point` | Three options: Best Effort, Compliance Aware, Compliance First |
| L2 destination nodes | `processing_stage` | Data Model Complexity, Service Decomposition, API Protocol |
| Cascade arrows | `data_flow` | Arrows from L1 nodes to L2 nodes showing influence |
| Skip connection callout | `callout_bar` | Note about L1-to-L3 and L1-to-L4 skip connections |

## Anti-Hallucination Rules

1. Build vs Buy has THREE options: Custom Build, Managed Services, SaaS Maximalist -- not two.
2. Target Market options are: Independent Creators, Mid-tier Labels, Enterprise Rights Organizations -- per the REPORT.md cross-archetype tables.
3. Revenue Model options are: Open Core, Freemium SaaS, Enterprise Licensing -- per REPORT.md.
4. Regulatory Posture options are: Best Effort, Compliance Aware, Compliance First -- per REPORT.md.
5. Skip connections are a key feature -- Build vs Buy directly influences L3 Primary Database and L4 Compute Platform.
6. Do NOT show Python or FastAPI as "Level 0" decisions -- the PRD network starts at L1 Business.
7. Background must be warm cream (#f6f3e6).

## Alt Text

Four L1 business decision nodes with their options, showing cascade arrows into L2 architecture decisions and callout about skip connections to L3 and L4.
