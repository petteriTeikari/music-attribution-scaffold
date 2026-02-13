# fig-prd-07: Team Archetypes

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-07 |
| **Title** | Team Archetypes -- Four Lenses on the Same Scaffold |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (structural overview) |
| **Location** | docs/prd/archetypes/README.md, docs/prd/decisions/REPORT.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Presents the four team archetypes that modulate every decision in the network. Each archetype represents a probability lens -- a consistent set of biases reflecting team constraints. Shows the same decision (Primary Database) through all four lenses to demonstrate how archetypes shift probabilities. This is essential for understanding that the scaffold is not one-size-fits-all.

The key message is: "Four team archetypes -- Engineer-Heavy, Musician-First, Solo Hacker, Well-Funded -- produce four fundamentally different probability landscapes from the same decision network."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  TEAM ARCHETYPES                                               |
|  ■ Four Lenses on the Same Scaffold                            |
+---------------------------------------------------------------+
|                                                                |
|  ┌──────────────────────┐    ┌──────────────────────┐         |
|  │ ENGINEER-HEAVY       │    │ MUSICIAN-FIRST       │         |
|  │ ═══════════════      │    │ ═══════════════      │         |
|  │ Team: 5-15           │    │ Team: 1-3            │         |
|  │ Depth: Deep          │    │ Depth: Shallow       │         |
|  │ Budget: Moderate     │    │ Budget: Low          │         |
|  │ ──────────────────   │    │ ──────────────────   │         |
|  │ DB: PostgreSQL (60%) │    │ DB: Supabase (55%)   │         |
|  │ Build: Custom (60%)  │    │ Build: SaaS (60%)    │         |
|  │ Compute: AWS (30%)   │    │ Compute: Render (35%)│         |
|  │ IaC: Terraform (40%) │    │ IaC: None (45%)      │         |
|  └──────────────────────┘    └──────────────────────┘         |
|                                                                |
|  ┌──────────────────────┐    ┌──────────────────────┐         |
|  │ SOLO HACKER          │    │ WELL-FUNDED STARTUP  │         |
|  │ ═══════════════      │    │ ═══════════════      │         |
|  │ Team: 1              │    │ Team: 10-30+         │         |
|  │ Depth: Variable      │    │ Depth: Deep          │         |
|  │ Budget: Minimal      │    │ Budget: High         │         |
|  │ ──────────────────   │    │ ──────────────────   │         |
|  │ DB: Split 40/40      │    │ DB: PostgreSQL (45%) │         |
|  │ Build: SaaS (60%)    │    │ Build: Custom (45%)  │         |
|  │ Compute: Railway(30%)│    │ Compute: AWS (35%)   │         |
|  │ IaC: Platform (35%)  │    │ IaC: Terraform (40%) │         |
|  └──────────────────────┘    └──────────────────────┘         |
|                                                                |
+---------------------------------------------------------------+
|  "Same scaffold, four instantiations"                          |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "TEAM ARCHETYPES" with coral accent square |
| Engineer-Heavy card | `archetype_overlay` | Team size 5-15, deep tech depth, moderate budget, key probability picks |
| Musician-First card | `archetype_overlay` | Team size 1-3, shallow tech depth, low budget, key probability picks |
| Solo Hacker card | `archetype_overlay` | Team size 1, variable depth, minimal budget, key probability picks |
| Well-Funded card | `archetype_overlay` | Team size 10-30+, deep depth, high budget, key probability picks |
| Key decision samples | `data_mono` | Top probability picks for DB, Build vs Buy, Compute, IaC per archetype |
| Footer insight | `callout_bar` | "Same scaffold, four instantiations" |

## Anti-Hallucination Rules

1. Team sizes from archetypes README: Engineer-Heavy 5-15, Musician-First 1-3, Solo Hacker 1, Well-Funded 10-30+.
2. Technical depth: Engineer-Heavy = Deep, Musician-First = Shallow, Solo Hacker = Variable, Well-Funded = Deep.
3. Budget: Engineer-Heavy = Moderate, Musician-First = Low, Solo Hacker = Minimal, Well-Funded = High.
4. Database probabilities from REPORT.md: Engineer PostgreSQL 0.60, Musician Supabase 0.55, Solo Supabase/SQLite 0.40/0.40, Well-Funded PostgreSQL 0.45.
5. Build vs Buy from REPORT.md: Engineer Custom 0.60, Musician SaaS 0.60, Solo SaaS 0.60, Well-Funded Custom 0.45.
6. Compute from REPORT.md: Engineer AWS ECS 0.30, Musician Render 0.35, Solo Railway 0.30, Well-Funded AWS ECS 0.35.
7. Do NOT invent a fifth archetype.
8. Background must be warm cream (#f6f3e6).

## Alt Text

Four team archetype cards showing different probability distributions for key decisions: Engineer-Heavy favors PostgreSQL and custom build, Musician-First favors Supabase and SaaS.
