# fig-choice-15: Deployment Options -- Hetzner vs Render vs AWS

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-15 |
| **Title** | Deployment Options: Hetzner vs Render vs AWS |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/L4-deployment/compute-platform.decision.yaml |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Maps the three deployment tracks for different team archetypes. The same scaffold deploys on radically different infrastructure depending on team constraints. Shows cost vs complexity trade-off: Hetzner (cheapest, most ops burden), Render (moderate cost, minimal ops), AWS ECS (highest cost, most scalable).

The key message is: "The scaffold deploys on Hetzner (cheapest), Render (simplest), or AWS ECS (most scalable) -- the same code, three different operational realities."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  DEPLOYMENT OPTIONS                                            |
|  ■ Three Tracks for Three Team Realities                       |
+---------------------------------------------------------------+
|                                                                |
|          COST                                                  |
|           ^                                                    |
|           |                                                    |
|     $500+ |                          ┌──────────┐             |
|           |                          │ AWS ECS  │             |
|           |                          │ + RDS    │             |
|           |                          │ + Secrets│             |
|           |                          │ Manager  │             |
|     $100  |          ┌──────────┐    └──────────┘             |
|           |          │ Render   │                             |
|           |          │ + Neon   │                             |
|           |          │ + Env Var│                             |
|      $20  | ┌──────────┐  └──────────┘                        |
|           | │ Hetzner  │                                      |
|           | │ + Self-  │                                      |
|           | │ managed  │                                      |
|           | │ PG       │                                      |
|           | └──────────┘                                      |
|           +────────────────────────────────────> COMPLEXITY    |
|          Low           Medium           High                   |
|                                                                |
|  ARCHETYPE MAPPING                                             |
|  ┌────────────┐ ┌──────────────┐ ┌───────────────┐           |
|  │ Hetzner    │ │ Render       │ │ AWS ECS       │           |
|  │ ──────     │ │ ──────       │ │ ───────       │           |
|  │ Solo Hacker│ │ Musician-    │ │ Engineer-Heavy│           |
|  │ Budget-    │ │ First Team   │ │ Well-Funded   │           |
|  │ conscious  │ │              │ │ Startup       │           |
|  │            │ │ Auto-deploy  │ │               │           |
|  │ Docker +   │ │ from Git     │ │ Terraform +   │           |
|  │ compose    │ │ push         │ │ IaC           │           |
|  │            │ │              │ │               │           |
|  │ IaC: None  │ │ IaC: None   │ │ IaC: Required │           |
|  │ CI: Manual │ │ CI: Auto    │ │ CI: GitHub    │           |
|  │            │ │              │ │ Actions       │           |
|  │ ~$20/mo    │ │ ~$50-100/mo │ │ ~$200-500/mo  │           |
|  └────────────┘ └──────────────┘ └───────────────┘           |
|                                                                |
+---------------------------------------------------------------+
|  Same code, same Docker image, three operational realities     |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DEPLOYMENT OPTIONS" with coral accent square |
| Cost vs complexity scatter | `branching_path` | Three deployment options on cost/complexity axes |
| Hetzner card | `archetype_overlay` | Solo Hacker, cheapest, most ops burden |
| Render card | `archetype_overlay` | Musician-First, auto-deploy, moderate cost |
| AWS ECS card | `archetype_overlay` | Engineer/Well-Funded, Terraform+IaC, highest cost |
| Archetype mapping | `archetype_overlay` | Which archetype maps to which deployment track |
| Footer insight | `callout_bar` | "Same code, same Docker image, three operational realities" |

## Anti-Hallucination Rules

1. Compute platform archetype preferences from REPORT.md: Engineer AWS ECS 0.30, Musician Render 0.35, Solo Railway 0.30, Well-Funded AWS ECS 0.35.
2. Note: the REPORT.md shows Railway for Solo, not Hetzner. Hetzner is mentioned in the design philosophy as a possible deployment target. The figure uses Hetzner as the budget option for illustrative purposes.
3. IaC preferences from REPORT.md: Engineer Terraform 0.40, Musician None 0.45, Solo Platform Native 0.35, Well-Funded Terraform 0.40.
4. The scaffold's Docker architecture is documented -- same Dockerfile deploys anywhere.
5. Render's golden path includes Neon for database hosting.
6. AWS path includes RDS for database and AWS Secrets Manager.
7. Cost estimates are approximate ranges, not exact pricing.
8. Do NOT claim one deployment option is better than others -- each serves different team constraints.
9. Background must be warm cream (#f6f3e6).

## Alt Text

Cost-versus-complexity scatter showing three deployment tracks: Hetzner budget path, Render balanced path, and AWS ECS enterprise path, mapped to team archetypes.
