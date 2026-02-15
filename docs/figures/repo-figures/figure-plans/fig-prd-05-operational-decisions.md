# fig-prd-05: Level 3-4 Operational Decisions

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-05 |
| **Title** | Level 3-4: Operational & Deployment Decisions |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/REPORT.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Maps the L4 deployment and L5 operations layers as updated through PRD v3.0.0, showing how compute platform choice cascades into hosting, object storage, CI/CD, observability, and FinOps strategy. Includes the v3.0.0 ecosystem expansion: 4 new L4 nodes (compliance_reporting_pipeline, training_data_provenance_store, golden_dataset_management, edge_deployment_target) and 4 new L5 nodes (regulatory_monitoring, market_intelligence, attribution_accuracy_monitoring, partnership_health_metrics) with cascade arrows from upstream ecosystem nodes. Shows that operational decisions are where archetype differences become most dramatic.

The key message is: "PRD v3.0.0 expands deployment to 13 L4 nodes and operations to 14 L5 nodes -- 4 new ecosystem L4 nodes (compliance reporting, provenance store, golden datasets, edge deployment) cascade from ecosystem integration decisions into 4 new L5 monitoring nodes."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  OPERATIONAL DECISIONS (v3.0.0)                                |
|  ■ L4 Deployment (13) + L5 Operations (14)                    |
+---------------------------------------------------------------+
|                                                                |
|  L4: CORE DEPLOYMENT (9) ─────────────────────────────────    |
|                                                                |
|  ┌──────────┐  ┌────────┐  ┌──────┐  ┌──────┐  ┌────────┐   |
|  │Compute   │─>│DB Host │  │CI/CD │  │IaC   │  │Containr│   |
|  │Platform  │  │        │  │Pipeln│  │Toolng│  │Strategy│   |
|  └──────┬───┘  └────────┘  └──────┘  └──────┘  └────────┘   |
|         │                                                      |
|  ┌──────┴───┐  ┌────────┐  ┌────────┐  ┌──────────┐          |
|  │Orchestrtr│  │Obj Stor│  │MCP Val │  │CD Strat  │          |
|  └──────────┘  └────────┘  └────────┘  └──────────┘          |
|                                                                |
|  L4: ECOSYSTEM DEPLOYMENT (4, NEW v3.0.0) ────────────────    |
|                                                                |
|  ┌──────────────┐  ┌──────────────┐  ┌─────────┐  ┌────────┐ |
|  │  COMPLIANCE   │  │  PROVENANCE  │  │ GOLDEN  │  │  EDGE  │ |
|  │  REPORTING    │  │  STORE       │  │ DATASET │  │  DEPLOY│ |
|  │  PIPELINE     │  │              │  │ MGMT    │  │  TARGET│ |
|  │  ──────────   │  │  ──────────  │  │ ─────── │  │ ────── │ |
|  │  ← compliance │  │  ← primary_db│  │ ← eval  │  │ ← edge │ |
|  │    framework  │  │  ← provenance│  │   fwk   │  │   infer│ |
|  └──────────────┘  └──────────────┘  └─────────┘  └────────┘ |
|                                                                |
|  L5: CORE OPERATIONS (10) ────────────────────────────────    |
|                                                                |
|  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐               |
|  │Observ│ │Scale │ │Backup│ │Secret│ │Schema│               |
|  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘               |
|  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐               |
|  │ML Mon│ │Doc   │ │Policy│ │FinOps│ │Ethics│               |
|  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘               |
|                                                                |
|  L5: ECOSYSTEM OPERATIONS (4, NEW v3.0.0) ────────────────    |
|                                                                |
|  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐     |
|  │REGULATORY │ │MARKET     │ │ATTRIBUTION│ │PARTNERSHIP│     |
|  │MONITORING │ │INTELLIGNCE│ │ACCURACY   │ │HEALTH     │     |
|  │← reg_post │ │← platform │ │← eval_fwk │ │← partner  │     |
|  │← comply   │ │← partner  │ │← ml_mon   │ │← observ   │     |
|  └───────────┘ └───────────┘ └───────────┘ └───────────┘     |
|                                                                |
+---------------------------------------------------------------+
|  v3.0.0: +4 L4 ecosystem nodes, +4 L5 ecosystem nodes         |
|  Cascade: ecosystem L3 → new L4 → new L5 monitoring           |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "OPERATIONAL DECISIONS (v3.0.0)" with coral accent square |
| L4 Core Deployment nodes (9) | `decision_point` | Compute, DB Hosting, CI/CD, IaC, Container, Orchestrator, Object Storage, MCP Validation, CD Strategy |
| L4 Ecosystem Deployment nodes (4) | `decision_point` | Compliance Reporting Pipeline, Training Data Provenance Store, Golden Dataset Management, Edge Deployment Target |
| L5 Core Operations nodes (10) | `decision_point` | Observability, Scaling, Backup/DR, Secrets, Schema Governance, ML Monitoring, Documentation, Policy-as-Code, FinOps, Ethics Governance |
| L5 Ecosystem Operations nodes (4) | `decision_point` | Regulatory Monitoring, Market Intelligence, Attribution Accuracy Monitoring, Partnership Health Metrics |
| Level banners | `label_editorial` | L4 Core, L4 Ecosystem, L5 Core, L5 Ecosystem section headers |
| Cascade arrows (core) | `data_flow` | Compute Platform to DB Hosting, to Object Storage, to FinOps |
| Cascade arrows (ecosystem) | `data_flow` | Ecosystem L3 nodes → new L4 → new L5 (e.g., compliance_framework → compliance_reporting → regulatory_monitoring) |
| Version footer | `callout_bar` | v3.0.0: +4 L4 ecosystem nodes, +4 L5 ecosystem nodes |

## Anti-Hallucination Rules

1. L4 has 13 nodes in v3.0.0: 9 core (Compute Platform, DB Hosting, CI/CD, IaC, Container, Orchestrator, Object Storage, MCP Validation, CD Strategy) + 4 ecosystem (Compliance Reporting Pipeline, Training Data Provenance Store, Golden Dataset Management, Edge Deployment Target).
2. L5 has 14 nodes in v3.0.0: 10 core (Observability, Scaling, Backup/DR, Secrets, Schema Governance, ML Monitoring, Documentation, Policy-as-Code, FinOps, Ethics) + 4 ecosystem (Regulatory Monitoring, Market Intelligence, Attribution Accuracy Monitoring, Partnership Health Metrics).
3. New L4 ecosystem cascade: compliance_framework_mapping → compliance_reporting_pipeline (strong), edge_inference_strategy → edge_deployment_target (strong), attribution_eval_framework → golden_dataset_management (strong), provenance_strategy → training_data_provenance_store (strong).
4. New L5 ecosystem cascade: attribution_eval_framework → attribution_accuracy_monitoring (strong), platform_strategy → market_intelligence (strong), partnership_model → partnership_health_metrics (strong), regulatory_posture → regulatory_monitoring (strong).
5. Core L4/L5 details unchanged from v2.1.0 (Render, Pulumi, Kamal 2, R2, etc.).
6. Do NOT show pricing -- this is an architectural overview.
7. Background must be warm cream (#f6f3e6).
8. Ecosystem L4/L5 nodes have high "none" priors -- they activate conditionally based on ecosystem L3 decisions.

## Alt Text

Decision diagram: deployment and operations layers of the music attribution scaffold PRD v3.0.0, showing 13 L4 deployment nodes (9 core plus 4 ecosystem: compliance reporting, provenance store, golden datasets, edge deployment) and 14 L5 operations nodes (10 core plus 4 ecosystem: regulatory monitoring, market intelligence, attribution accuracy, partnership health) -- ecosystem nodes cascade from upstream integration decisions.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Decision diagram: deployment and operations layers of the music attribution scaffold PRD v3.0.0, showing 13 L4 deployment nodes and 14 L5 operations nodes including ecosystem integration cascades for compliance reporting, attribution accuracy monitoring, and partnership health metrics.](docs/figures/repo-figures/assets/fig-prd-05-operational-decisions.jpg)

*Figure 5. PRD v3.0.0 operational decisions: 13 L4 deployment nodes and 14 L5 operations nodes spanning core infrastructure and ecosystem integration, with new cascade paths from compliance frameworks to regulatory monitoring and from evaluation frameworks to attribution accuracy tracking.*

### From this figure plan (relative)

![Decision diagram: deployment and operations layers of the music attribution scaffold PRD v3.0.0, showing 13 L4 deployment nodes and 14 L5 operations nodes including ecosystem integration cascades for compliance reporting, attribution accuracy monitoring, and partnership health metrics.](../assets/fig-prd-05-operational-decisions.jpg)
