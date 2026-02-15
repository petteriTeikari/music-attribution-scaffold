# fig-choice-15: Deployment Options — Cost vs Complexity Landscape

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-15 |
| **Title** | Deployment Options: Cost vs Complexity Landscape |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/L4-deployment/compute-platform.decision.yaml |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Maps five deployment paths on a corrected cost-vs-complexity scatter plot. The v1.0 figure incorrectly placed Hetzner at "low complexity" — in reality, Render is the simplest path and Hetzner bare-metal is the most complex. The updated figure shows two distinct Hetzner paths (managed via Ubicloud vs self-managed K8s) and includes all Big Three hyperscalers.

The key message is: "Start where complexity is lowest (Render), migrate when savings justify the ops burden (Hetzner) — same Docker image, five operational realities."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  DEPLOYMENT OPTIONS                                            |
|  ■ Cost vs Complexity — Corrected Landscape (2026)             |
+---------------------------------------------------------------+
|                                                                |
|          MONTHLY COST                                          |
|           ^                                                    |
|           |                                                    |
|     €500+ |                              ┌──────────────┐     |
|           |                              │ Big Three    │     |
|           |                              │ AWS/GCP/Azure│     |
|           |                              │ Full managed │     |
|     €100  |                              └──────────────┘     |
|           |                                                    |
|      €50  | ┌──────────┐    ┌──────────────┐                  |
|           | │ Render   │    │ Hetzner +    │                  |
|           | │ + Neon   │    │ Ubicloud K8s │                  |
|      €20  | └──────────┘    └──────────────┘                  |
|           |                                                    |
|           |                                    ┌──────────────┐|
|       €7  |                                    │ Hetzner bare ││
|           |                                    │ metal + K8s  ││
|           |                                    └──────────────┘|
|           +────────────────────────────────────> COMPLEXITY    |
|          Minimal        Moderate        Expert                 |
|          (git push)     (Kamal/Pulumi)  (Talos/K3s)           |
|                                                                |
|  ARCHETYPE MAPPING                                             |
|  ┌────────────┐ ┌──────────────┐ ┌───────────┐ ┌───────────┐ |
|  │ Render     │ │ Hetzner +    │ │ Big Three │ │ Hetzner   │ |
|  │ ──────     │ │ Ubicloud     │ │ ─────────│ │ bare metal│ |
|  │ Musician-  │ │ ────────     │ │ Well-     │ │ ──────── │ |
|  │ First Team │ │ Budget-      │ │ Funded /  │ │ Solo K8s │ |
|  │            │ │ Conscious    │ │ Enterprise│ │ Expert   │ |
|  │ git push   │ │ Startup      │ │           │ │          │ |
|  │ deploy     │ │              │ │ Pulumi /  │ │ Talos +  │ |
|  │            │ │ Docker +     │ │ Terraform │ │ CNPG +   │ |
|  │ IaC: None  │ │ Kamal / K8s │ │           │ │ self-mgd │ |
|  │ CI: Auto   │ │              │ │ IaC: Req  │ │          │ |
|  │            │ │ IaC: Optional│ │ CI: GH    │ │ IaC: Opt │ |
|  │ ~€20-35/mo │ │ ~€20-60/mo  │ │ Actions   │ │ CI: Self │ |
|  │            │ │              │ │           │ │          │ |
|  │ DevOps: 0  │ │ DevOps: Low │ │ ~€200+/mo │ │ ~€7-30/mo│ |
|  │            │ │              │ │           │ │          │ |
|  └────────────┘ └──────────────┘ │ DevOps: M │ │ DevOps: H│ |
|                                  └───────────┘ └───────────┘ |
|                                                                |
|     ──────────────────────────────────────────────────────>    |
|     RECOMMENDED MIGRATION PATH:  Render → Hetzner+Ubicloud    |
|     (Start simple, migrate when savings justify ops burden)    |
|                                                                |
+---------------------------------------------------------------+
|  Same code, same Docker image, five operational realities      |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DEPLOYMENT OPTIONS" with coral accent square |
| Cost vs complexity scatter | `branching_path` | Five deployment options on cost/complexity axes |
| Render card | `archetype_overlay` | Musician-First, lowest complexity, auto-deploy, ~€20-35/mo |
| Hetzner+Ubicloud card | `archetype_overlay` | Budget-Conscious Startup, managed K8s on Hetzner, ~€20-60/mo |
| Big Three card | `archetype_overlay` | Well-Funded/Enterprise, AWS/GCP/Azure managed, ~€200+/mo |
| Hetzner bare-metal card | `archetype_overlay` | Solo K8s Expert, cheapest but highest complexity, ~€7-30/mo |
| Migration arrow | `callout_bar` | Recommended path: Render → Hetzner+Ubicloud |
| Footer insight | `callout_bar` | "Same code, same Docker image, five operational realities" |

## Anti-Hallucination Rules

1. **CRITICAL CORRECTION**: Hetzner bare-metal is NOT "low complexity." It requires self-managed K8s (Talos/K3s), CloudNativePG, cert-manager, Ingress NGINX, and ExternalDNS. The Digital Society case study team had 10 years K8s experience.
2. Render IS the lowest-complexity option (git push deploy, managed everything).
3. There are TWO Hetzner paths: managed (via Ubicloud) and bare-metal (self-hosted K8s). These have very different complexity profiles.
4. "Big Three" includes AWS, GCP, AND Azure — not just AWS. All have similar pricing (~€200-500/mo).
5. Compute platform archetype preferences from REPORT.md: Engineer AWS ECS 0.30, Musician Render 0.35, Solo Railway 0.30, Well-Funded AWS ECS 0.35.
6. IaC preferences from REPORT.md: Engineer Terraform 0.40, Musician None 0.45, Solo Platform Native 0.35, Well-Funded Terraform 0.40. Updated: Pulumi preferred over Terraform (BSL license concern after IBM acquisition).
7. Ubicloud provides managed K8s + PostgreSQL on Hetzner Cloud (preview, Germany + Virginia as of Feb 2026).
8. Cost estimates are approximate ranges, not exact pricing. See `docs/planning/deployement-finops-landscape.md` for detailed pricing tables.
9. Do NOT claim one deployment option is universally better — each serves different team constraints and phases.
10. Background must be warm cream (#f6f3e6).

## Alt Text

Corrected cost versus complexity scatter plot showing five deployment paths for the music attribution scaffold: Render (lowest complexity, moderate cost), Hetzner with Ubicloud managed Kubernetes (moderate complexity, low cost), Big Three hyperscalers AWS GCP Azure (moderate complexity, highest cost), and Hetzner bare-metal with self-managed Kubernetes (highest complexity, lowest cost), with a recommended migration arrow from Render to Hetzner plus Ubicloud.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Corrected cost versus complexity scatter plot showing five deployment paths for the music attribution scaffold: Render (lowest complexity, moderate cost), Hetzner with Ubicloud managed Kubernetes (moderate complexity, low cost), Big Three hyperscalers AWS GCP Azure (moderate complexity, highest cost), and Hetzner bare-metal with self-managed Kubernetes (highest complexity, lowest cost), with a recommended migration arrow from Render to Hetzner plus Ubicloud.](docs/figures/repo-figures/assets/fig-choice-15-deployment-options.jpg)

*The music attribution scaffold deploys on Render (~€20--35/mo, git push), Hetzner+Ubicloud (~€20--60/mo, managed K8s), Big Three (~€200+/mo, full managed), or Hetzner bare-metal (~€7--30/mo, expert ops) — same Docker image, different operational realities. Recommended path: start on Render, migrate to Hetzner when savings justify the ops burden.*

### From this figure plan (relative)

![Corrected cost versus complexity scatter plot showing five deployment paths for the music attribution scaffold: Render (lowest complexity, moderate cost), Hetzner with Ubicloud managed Kubernetes (moderate complexity, low cost), Big Three hyperscalers AWS GCP Azure (moderate complexity, highest cost), and Hetzner bare-metal with self-managed Kubernetes (highest complexity, lowest cost), with a recommended migration arrow from Render to Hetzner plus Ubicloud.](../assets/fig-choice-15-deployment-options.jpg)
