# fig-prd-02: Full Decision Network Overview

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-02 |
| **Title** | Full Decision Network Overview -- 30+ Nodes Across 5 Levels |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (structural overview) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Provides the complete bird's-eye view of the entire probabilistic decision network. All 30+ nodes across 5 levels, with edges showing how upstream decisions influence downstream choices. Color-coded by level. This is the "map of the territory" that researchers and policy analysts use to understand the full scope of architectural decisions.

The key message is: "The scaffold's architecture is a 5-level Bayesian decision network with 30+ nodes, 60+ edges, and conditional probabilities -- not a single fixed architecture."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  DECISION NETWORK OVERVIEW                                     |
|  ■ 30+ Nodes, 5 Levels, 60+ Conditional Edges                 |
+---------------------------------------------------------------+
|                                                                |
|  L1 BUSINESS ─────────────────────────────────────────────     |
|  ┌─────────┐ ┌──────────┐ ┌─────────┐ ┌──────────────┐       |
|  │Build vs │ │ Target   │ │Revenue  │ │ Regulatory   │       |
|  │Buy      │ │ Market   │ │Model    │ │ Posture      │       |
|  └────┬────┘ └────┬─────┘ └─────────┘ └──────────────┘       |
|       │           │                                            |
|  L2 ARCHITECTURE ──────────────────────────────────────────    |
|  ┌────┴───┐ ┌────┴───┐ ┌────────┐ ┌──────┐ ┌──────┐ ┌────┐  |
|  │Data    │ │API     │ │Service │ │AI Fwk│ │Art.  │ │UI  │  |
|  │Model   │ │Protocol│ │Decomp. │ │Strat.│ │Decpl.│ │Adpt│  |
|  └───┬────┘ └───┬────┘ └───┬────┘ └──┬───┘ └──────┘ └────┘  |
|      │          │          │         │                         |
|  L3 IMPLEMENTATION ────────────────────────────────────────    |
|  ┌────┐┌────┐┌────┐┌────┐┌────┐┌────┐┌────┐┌────┐┌────┐┌──┐ |
|  │DB  ││Grph││Vec ││LLM ││Frnt││Auth││DQ  ││AgUI││Voic││GR│ |
|  └──┬─┘└────┘└────┘└────┘└────┘└────┘└────┘└────┘└────┘└──┘ |
|     │                                                          |
|  L4 DEPLOYMENT ────────────────────────────────────────────    |
|  ┌───────┐ ┌────────┐ ┌──────┐ ┌──────┐ ┌──────────┐         |
|  │Compute│ │DB Host │ │CI/CD │ │IaC   │ │Container │         |
|  └───┬───┘ └────────┘ └──────┘ └──────┘ └──────────┘         |
|      │                                                         |
|  L5 OPERATIONS ────────────────────────────────────────────    |
|  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                |
|  │Observ│ │Scale │ │Backup│ │Secret│ │Schema│                |
|  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘                |
|                                                                |
+---------------------------------------------------------------+
|  LEGEND: ━━ same-level (15) ── adjacent (21) ╌╌ skip (24)    |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DECISION NETWORK OVERVIEW" with coral accent square |
| Subtitle | `label_editorial` | Node and edge counts |
| L1 Business nodes (4) | `decision_point` | Build vs Buy, Target Market, Revenue Model, Regulatory Posture |
| L2 Architecture nodes (6) | `decision_point` | Data Model, API Protocol, Service Decomp, AI Framework, Artifact Decoupling, UI Adaptation |
| L3 Implementation nodes (10) | `decision_point` | Database, Graph, Vector, LLM, Frontend, Auth, Data Quality, Agentic UI, Voice, Graph RAG |
| L4 Deployment nodes (5) | `decision_point` | Compute, DB Hosting, CI/CD, IaC, Container |
| L5 Operations nodes (5) | `decision_point` | Observability, Scaling, Backup/DR, Secrets, Schema Governance |
| Level labels | `label_editorial` | L1-L5 horizontal banners |
| Edge lines | `data_flow` | Same-level, adjacent-level, and skip-connection edges differentiated by line style |
| Legend bar | `callout_bar` | Edge type counts: 15 same-level, 21 adjacent, 24 skip-connections |

## Anti-Hallucination Rules

1. The network has exactly 30 nodes in the REPORT.md overview, but the _network.yaml has expanded to include additional nodes (LLM routing, audio metadata, commercial landscape stubs, xOps nodes). Refer to network version 2.0.0.
2. Level counts from REPORT.md: L1=4, L2=6, L3=10, L4=5, L5=5. The _network.yaml includes additional L3 component and L4/L5 nodes added in v1.9-v2.0.
3. Edge counts from REPORT.md: 60 total, 15 same-level, 21 adjacent, 24 skip-connections.
4. Do NOT invent node names not in the actual network.
5. Level colors should follow the mermaid chart pattern: L1 navy, L2 teal, L3 gold, L4 green, L5 red.
6. Background must be warm cream (#f6f3e6).
7. This is L2 audience -- use "assurance levels" not "trust scores", use "decision nodes" not "config options".

## Alt Text

Network visualization: complete Bayesian decision network for the music attribution scaffold with 30-plus nodes across five levels -- business, architecture, implementation, deployment, and operations -- connected by 60-plus conditional probability edges that govern transparent confidence scoring for music metadata and credits.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Network visualization: complete Bayesian decision network for the music attribution scaffold with 30-plus nodes across five levels -- business, architecture, implementation, deployment, and operations -- connected by 60-plus conditional probability edges that govern transparent confidence scoring for music metadata and credits.](docs/figures/repo-figures/assets/fig-prd-02-full-decision-network.jpg)

*Figure 2. The full probabilistic PRD decision network maps every architectural choice in the open-source music attribution scaffold, from L1 business strategy through L5 operations, revealing how upstream decisions conditionally shape downstream technology selection.*

### From this figure plan (relative)

![Network visualization: complete Bayesian decision network for the music attribution scaffold with 30-plus nodes across five levels -- business, architecture, implementation, deployment, and operations -- connected by 60-plus conditional probability edges that govern transparent confidence scoring for music metadata and credits.](../assets/fig-prd-02-full-decision-network.jpg)
