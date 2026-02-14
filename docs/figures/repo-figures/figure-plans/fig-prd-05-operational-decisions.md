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

Maps the L4 deployment and L5 operations layers as updated in PRD v2.1.0, showing how compute platform choice cascades into hosting, object storage, CI/CD, observability, and FinOps strategy. Highlights the expanded decision network with Object Storage as a new L4 node, Kamal 2 as a container strategy, Pulumi as recommended IaC, and two distinct Hetzner compute paths (Ubicloud managed vs bare-metal). Shows that operational decisions are where archetype differences become most dramatic.

The key message is: "PRD v2.1.0 adds Object Storage, Kamal 2, and Ubicloud paths -- deployment decisions are the most archetype-sensitive layer, with five compute options cascading into six database hosting choices, four container strategies, and a new FinOps cost model."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  OPERATIONAL DECISIONS (v2.1.0)                                |
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
|  │  Hetzner +   │    │  Supabase    │    │  Actions  │        |
|  │    Ubicloud  │    │  Ubicloud PG │    │  Auto-Dpl │        |
|  │  Hetzner bare│    │  Self-managed│    │           │        |
|  │  Big Three   │    │  AWS RDS     │    │           │        |
|  └──────┬───────┘    └──────────────┘    └───────────┘        |
|         │                                                      |
|  ┌──────┴──────────┐  ┌───────────────┐  ┌──────────────┐    |
|  │  IaC TOOLING    │  │  CONTAINER    │  │ OBJECT       │    |
|  │  ────────────   │  │  STRATEGY     │  │ STORAGE      │    |
|  │  Pulumi (rec.)  │  │  ──────────   │  │ ──────────   │    |
|  │  Terraform      │  │  Docker Comp. │  │ Cloudflare   │    |
|  │  None (PaaS)    │  │  Kamal 2      │  │ R2 (rec.)    │    |
|  │                 │  │  Kubernetes   │  │ Hetzner Obj  │    |
|  └─────────────────┘  └───────────────┘  └──────────────┘    |
|         │                                                      |
|  L5: OPERATIONS ───────────────────────────────────────        |
|                                                                |
|  ┌──────────┐ ┌────────┐ ┌────────┐ ┌───────┐ ┌───────┐     |
|  │Observ-   │ │Scaling │ │Backup/ │ │Secrets│ │FinOps │     |
|  │ability   │ │Strategy│ │DR      │ │Mgmt   │ │Strat. │     |
|  │──────    │ │──────  │ │──────  │ │────── │ │────── │     |
|  │PostHog + │ │Vertical│ │Managed │ │Env    │ │DevOps │     |
|  │Sentry    │ │        │ │Provider│ │Vars   │ │Tax +  │     |
|  │          │ │        │ │        │ │       │ │Egress │     |
|  └──────────┘ └────────┘ └────────┘ └───────┘ └───────┘     |
|                                                                |
+---------------------------------------------------------------+
|  NEW in v2.1.0: Object Storage node, Kamal 2, Ubicloud paths  |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "OPERATIONAL DECISIONS (v2.1.0)" with coral accent square |
| L4 Deployment nodes (6) | `decision_point` | Compute Platform, DB Hosting, CI/CD, IaC, Container Strategy, Object Storage |
| L5 Operations nodes (5) | `decision_point` | Observability, Scaling, Backup/DR, Secrets, FinOps Strategy |
| Level banners | `label_editorial` | L4 and L5 horizontal section headers |
| Option lists per node | `branching_path` | Top candidate options listed inside each node |
| Cascade arrows | `data_flow` | Compute Platform to DB Hosting, to Object Storage, to FinOps |
| Version footer | `callout_bar` | PRD v2.1.0 additions: Object Storage, Kamal 2, Ubicloud paths |

## Anti-Hallucination Rules

1. L4 has 6 nodes in v2.1.0: Compute Platform (7 options), DB Hosting (6 options), CI/CD Pipeline, IaC Tooling (5 options), Container Strategy (4 options), Object Storage (6 options, NEW).
2. L5 includes FinOps Strategy (now `active` status) with DevOps tax framework, egress cost analysis, and phased cost projections.
3. Compute Platform options: Render (0.25), Hetzner+Ubicloud (0.10, managed K8s), Hetzner bare-metal (0.05, self-managed), Big Three AWS/GCP/Azure (0.20), Railway (0.15), Fly.io (0.10), Vercel+backend (0.15).
4. IaC Tooling: Pulumi is now `recommended` (0.25) over Terraform (0.15) due to BSL license after IBM acquisition. Pulumi has MCP server for Claude and native Python support.
5. Container Strategy now includes Kamal 2 (0.15) from 37signals -- Docker deployment without K8s complexity.
6. Object Storage: Cloudflare R2 recommended (0.45) -- zero egress fees save $2,700-9,000/mo at scale vs AWS S3.
7. DB Hosting now includes Ubicloud managed PG (0.10) on Hetzner -- preview Feb 2026.
8. Do NOT show pricing -- this is an architectural overview. See `docs/planning/deployement-finops-landscape.md` for costs.
9. Background must be warm cream (#f6f3e6).

## Alt Text

Decision diagram: deployment and operations layers of the music attribution scaffold PRD v2.1.0, showing six L4 deployment nodes including new Object Storage with Cloudflare R2, expanded compute platform with Hetzner Ubicloud and bare-metal paths, Kamal 2 container strategy, Pulumi as recommended IaC, and L5 operations with active FinOps strategy -- the most team-archetype-sensitive decisions in the open-source probabilistic PRD.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Decision diagram: deployment and operations layers of the music attribution scaffold PRD v2.1.0, showing six L4 deployment nodes including new Object Storage with Cloudflare R2, expanded compute platform with Hetzner Ubicloud and bare-metal paths, Kamal 2 container strategy, Pulumi as recommended IaC, and L5 operations with active FinOps strategy -- the most team-archetype-sensitive decisions in the open-source probabilistic PRD.](docs/figures/repo-figures/assets/fig-prd-05-operational-decisions.jpg)

*Figure 5. PRD v2.1.0 operational decisions with expanded deployment layer: Object Storage (Cloudflare R2), two Hetzner paths (Ubicloud managed vs bare-metal), Kamal 2 container strategy, and Pulumi as recommended IaC -- cascading into an active FinOps strategy with DevOps tax analysis.*

### From this figure plan (relative)

![Decision diagram: deployment and operations layers of the music attribution scaffold PRD v2.1.0, showing six L4 deployment nodes including new Object Storage with Cloudflare R2, expanded compute platform with Hetzner Ubicloud and bare-metal paths, Kamal 2 container strategy, Pulumi as recommended IaC, and L5 operations with active FinOps strategy -- the most team-archetype-sensitive decisions in the open-source probabilistic PRD.](../assets/fig-prd-05-operational-decisions.jpg)
