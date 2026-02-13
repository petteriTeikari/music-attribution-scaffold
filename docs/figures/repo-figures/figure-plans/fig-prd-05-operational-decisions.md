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

Maps the L4 deployment and L5 operations layers, showing how compute platform choice cascades into hosting, CI/CD, observability, and scaling. Highlights the volatility classification -- 12 stable, 12 shifting, 6 volatile decisions. Shows that operational decisions are where archetype differences become most dramatic (Render vs AWS ECS vs Railway).

The key message is: "Deployment and operations decisions are the most archetype-sensitive -- the same scaffold deploys on Render (musician), AWS ECS (enterprise), or Railway (solo) depending on team constraints."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  OPERATIONAL DECISIONS                                         |
|  ■ L4 Deployment + L5 Operations                               |
+---------------------------------------------------------------+
|                                                                |
|  L4: DEPLOYMENT ───────────────────────────────────────        |
|                                                                |
|  ┌──────────────┐    ┌──────────────┐    ┌───────────┐        |
|  │  COMPUTE     │───>│ DB HOSTING   │    │  CI/CD    │        |
|  │  PLATFORM    │    │              │    │  PIPELINE │        |
|  │  ──────────  │    │  ──────────  │    │  ──────── │        |
|  │  Render      │    │  Neon        │    │  GitHub   │        |
|  │  AWS ECS     │    │  Supabase    │    │  Actions  │        |
|  │  Railway     │    │  AWS RDS     │    │  Auto-Dpl │        |
|  └──────┬───────┘    └──────────────┘    └───────────┘        |
|         │                                                      |
|  ┌──────┴──────────┐    ┌───────────────┐                     |
|  │  IaC TOOLING    │    │  CONTAINER    │                     |
|  │  ────────────   │    │  STRATEGY     │                     |
|  │  Terraform      │    │  ──────────   │                     |
|  │  None (PaaS)    │    │  Docker       │                     |
|  │  Platform Native│    │  Compose      │                     |
|  └─────────────────┘    └───────────────┘                     |
|         │                                                      |
|  L5: OPERATIONS ───────────────────────────────────────        |
|                                                                |
|  ┌──────────┐ ┌────────┐ ┌────────┐ ┌───────┐ ┌───────┐     |
|  │Observ-   │ │Scaling │ │Backup/ │ │Secrets│ │Schema │     |
|  │ability   │ │Strategy│ │DR      │ │Mgmt   │ │Govern.│     |
|  │──────    │ │──────  │ │──────  │ │────── │ │────── │     |
|  │PostHog + │ │Vertical│ │Managed │ │Env    │ │DVC +  │     |
|  │Sentry    │ │        │ │Provider│ │Vars   │ │JSON   │     |
|  └──────────┘ └────────┘ └────────┘ └───────┘ └───────┘     |
|                                                                |
+---------------------------------------------------------------+
|  VOLATILITY: 12 stable | 12 shifting | 6 volatile             |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "OPERATIONAL DECISIONS" with coral accent square |
| L4 Deployment nodes (5) | `decision_point` | Compute Platform, DB Hosting, CI/CD, IaC, Container Strategy |
| L5 Operations nodes (5) | `decision_point` | Observability, Scaling, Backup/DR, Secrets, Schema Governance |
| Level banners | `label_editorial` | L4 and L5 horizontal section headers |
| Option lists per node | `branching_path` | Top candidate options listed inside each node |
| Cascade arrows | `data_flow` | Compute Platform to DB Hosting, to Observability, to Scaling |
| Volatility footer | `callout_bar` | Stability classification summary: 12/12/6 |

## Anti-Hallucination Rules

1. L4 has 5 nodes in REPORT.md: Compute Platform, DB Hosting, CI/CD Pipeline, IaC Tooling, Container Strategy. The _network.yaml adds Orchestrator Choice and CD Strategy in v1.9+.
2. L5 has 5 nodes in REPORT.md: Observability, Scaling, Backup/DR, Secrets, Schema Governance. The _network.yaml adds ML Monitoring, Documentation Tooling, Policy-as-Code, FinOps, Ethics Governance in v1.9-v2.0.
3. Volatility counts from REPORT.md: 12 stable, 12 shifting, 6 volatile.
4. Compute Platform archetype options: Render (Musician-First), AWS ECS (Engineer/Well-Funded), Railway (Solo) -- per REPORT.md cross-archetype table.
5. Observability options per REPORT.md: Grafana (Engineer), Minimal (Musician/Solo), Datadog (Well-Funded). PostHog + Sentry is the scaffold's reference choice.
6. Do NOT show pricing -- this is an architectural overview.
7. Background must be warm cream (#f6f3e6).

## Alt Text

Two-tier layout showing L4 deployment decisions flowing into L5 operations decisions, with candidate options listed in each node and volatility classification footer.
