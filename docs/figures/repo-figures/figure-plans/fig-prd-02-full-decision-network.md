# fig-prd-02: Full Decision Network Overview

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-02 |
| **Title** | Full Decision Network Overview -- 78 Nodes Across 5 Levels |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (structural overview) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Provides the complete bird's-eye view of the entire probabilistic decision network. All 78 nodes across 5 levels, with edges showing how upstream decisions influence downstream choices. Color-coded by level. The v3.0.0 expansion added 28 ecosystem integration nodes (partnerships, protocols, compliance), creating a dual-subgraph structure: Core Infrastructure (50 nodes) and Ecosystem Integration (28 nodes). This is the "map of the territory" that researchers and policy analysts use to understand the full scope of architectural decisions.

The key message is: "The scaffold's architecture is a 5-level Bayesian decision network with 78 nodes, ~131 edges, and conditional probabilities -- not a single fixed architecture. Core infrastructure (50 nodes) and ecosystem integration (28 nodes) form two coherent subgraphs."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  DECISION NETWORK OVERVIEW (v3.0.0)                            |
|  ■ 78 Nodes, 5 Levels, ~131 Conditional Edges                 |
+---------------------------------------------------------------+
|                                                                |
|  CORE INFRASTRUCTURE (50)     │  ECOSYSTEM INTEGRATION (28)    |
|  ─────────────────────────    │  ──────────────────────────    |
|                               │                                |
|  L1 BUSINESS ──────────────── │                                |
|  ┌───────┐┌──────┐┌────┐┌──┐ │                                |
|  │Bld/Buy││Target││Rev ││Reg│ │                                |
|  └───┬───┘└──┬───┘└────┘└──┘ │                                |
|      │       │                │                                |
|  L2 ARCHITECTURE ──────────── │  L2 ARCHITECTURE ────────────  |
|  ┌────┐┌────┐┌────┐┌──┐┌──┐  │  ┌────────┐ ┌───────────┐     |
|  │Data││API ││Svc ││AI││UI│  │  │Platform│ │Partnership│     |
|  │Mdl ││Prot││Dec ││Fw││Ad│  │  │Strategy│ │Model      │     |
|  └──┬─┘└──┬─┘└──┬─┘└──┘└──┘  │  └────┬───┘ └─────┬─────┘     |
|     │     │     │             │       │           │            |
|  L3 IMPLEMENTATION ────────── │  L3 COMPONENTS (24) ─────────  |
|  ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐   │  ┌────┐┌────┐┌────┐┌────┐     |
|  │DB││Gr││Ve││LL││Fr││Au│   │  │TDA ││CMO ││Cont││AgIn│     |
|  └──┘└──┘└──┘└──┘└──┘└──┘   │  └────┘└────┘└────┘└────┘     |
|  ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐   │  ┌────┐┌────┐┌────┐┌────┐     |
|  │DQ││Ag││Vo││GR││Rt││Au│   │  │Meta││KGrp││Edge││Eval│     |
|  └──┘└──┘└──┘└──┘└──┘└──┘   │  └────┘└────┘└────┘└────┘     |
|  + MCP sec, MCP prod, ...    │  + 6 company + 4 more nodes    |
|                               │                                |
|  L4 DEPLOYMENT (9) ────────── │  L4 DEPLOYMENT (4) ──────────  |
|  ┌──────┐┌────┐┌────┐┌────┐  │  ┌──────┐┌──────┐┌────┐┌────┐ |
|  │Comput││DBHs││CI/CD││IaC │  │  │Comply││Prove ││Gold││Edge│ |
|  └──────┘└────┘└────┘└────┘  │  └──────┘└──────┘└────┘└────┘ |
|  + Container, Orch, Obj, ... │                                |
|                               │                                |
|  L5 OPERATIONS (10) ───────── │  L5 OPERATIONS (4) ──────────  |
|  ┌────┐┌────┐┌────┐┌────┐    │  ┌──────┐┌──────┐┌────┐┌────┐ |
|  │Obs ││Scal││Back││Secr│    │  │RegMon││MktIn ││AccMo││Part│ |
|  └────┘└────┘└────┘└────┘    │  └──────┘└──────┘└────┘└────┘ |
|  + Schema, ML, Doc, ...      │                                |
|                               │                                |
+---------------------------------------------------------------+
|  LEGEND: ━━ same-level ── adjacent ╌╌ skip (~131 total edges) |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DECISION NETWORK OVERVIEW (v3.0.0)" with coral accent square |
| Subtitle | `label_editorial` | "78 Nodes, 5 Levels, ~131 Conditional Edges" |
| Dual-subgraph layout | `content_area` | Left: Core Infrastructure (50 nodes), Right: Ecosystem Integration (28 nodes) |
| L1 Business nodes (4) | `decision_point` | Build vs Buy, Target Market, Revenue Model, Regulatory Posture |
| L2 Architecture nodes (9) | `decision_point` | Core: Data Model, API Protocol, Service Decomp, AI Framework, Artifact Decoupling, UI Adaptation, Provenance. Ecosystem: Platform Strategy, Partnership Model |
| L3 Implementation nodes (14) | `decision_point` | Database, Graph, Vector, LLM, Frontend, Auth, Data Quality, Agentic UI, Voice, Graph RAG, LLM Routing, Audio Metadata, MCP Security, MCP Production |
| L3 Component nodes (24) | `decision_point` | 6 existing commercial + 12 category (TDA, CMO, Content ID, Platform Connector, Metadata Registry, Watermark, Agent Interop, Edge Inference, Eval Framework, Agent Observability, Agentic Commerce, Knowledge Graph) + 6 company (Musical AI, Sureel, STIM, SoundExchange, Fairly Trained, Suno/Udio) |
| L4 Deployment nodes (13) | `decision_point` | Core: Compute, DB Hosting, CI/CD, IaC, Container, Orchestrator, Object Storage, MCP Validation, CD Strategy. Ecosystem: Compliance Reporting, Provenance Store, Golden Dataset, Edge Target |
| L5 Operations nodes (14) | `decision_point` | Core: Observability, Scaling, Backup/DR, Secrets, Schema Governance, ML Monitoring, Documentation, Policy-as-Code, FinOps, Ethics. Ecosystem: Regulatory Monitoring, Market Intelligence, Attribution Accuracy, Partnership Health |
| Level labels | `label_editorial` | L1-L5 horizontal banners spanning both subgraphs |
| Edge lines | `data_flow` | Same-level, adjacent-level, and skip-connection edges differentiated by line style |
| Subgraph divider | `accent_line_v` | Vertical coral accent line separating core from ecosystem |
| Legend bar | `callout_bar` | ~131 total edges across both subgraphs |

## Anti-Hallucination Rules

1. The network has 78 nodes in _network.yaml v3.0.0. Level counts: L1=4, L2=9, L3=38 (14 implementation + 24 components), L4=13, L5=14.
2. Approximately 131 edges total. The v3.0.0 expansion added ~63 new edges for the 28 ecosystem nodes.
3. Dual-subgraph layout: Core Infrastructure (50 nodes, established) and Ecosystem Integration (28 nodes, v3.0.0 expansion).
4. Do NOT invent node names not in the _network.yaml v3.0.0.
5. Level colors should follow the mermaid chart pattern: L1 navy, L2 teal, L3 gold, L4 green, L5 red.
6. Background must be warm cream (#f6f3e6).
7. This is L2 audience -- use "assurance levels" not "trust scores", use "decision nodes" not "config options".
8. Ecosystem nodes have high "none" priors (0.40-0.55), reflecting strategic ambiguity -- do NOT depict them as committed decisions.

## Alt Text

Network visualization: 78-node Bayesian decision network for the music attribution scaffold across five levels with dual-subgraph layout -- 50 core infrastructure nodes and 28 ecosystem integration nodes connected by approximately 131 conditional probability edges governing transparent confidence scoring.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Network visualization: 78-node Bayesian decision network for the music attribution scaffold across five levels with dual-subgraph layout -- 50 core infrastructure nodes and 28 ecosystem integration nodes connected by approximately 131 conditional probability edges governing transparent confidence scoring.](docs/figures/repo-figures/assets/fig-prd-02-full-decision-network.jpg)

*Figure 2. The full probabilistic PRD decision network (v3.0.0) maps 78 architectural choices in the open-source music attribution scaffold across two coherent subgraphs -- core infrastructure and ecosystem integration -- from L1 business strategy through L5 operations.*

### From this figure plan (relative)

![Network visualization: 78-node Bayesian decision network for the music attribution scaffold across five levels with dual-subgraph layout -- 50 core infrastructure nodes and 28 ecosystem integration nodes connected by approximately 131 conditional probability edges governing transparent confidence scoring.](../assets/fig-prd-02-full-decision-network.jpg)
