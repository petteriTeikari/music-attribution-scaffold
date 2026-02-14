# fig-prd-09: PRD Versioning Timeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-09 |
| **Title** | PRD Versioning Timeline -- v1.0 to v2.0 Evolution |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (structural overview) |
| **Location** | docs/prd/decisions/REPORT.md |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Traces the evolution of the PRD decision network from initial version through v2.0.0. Shows which nodes were added at each version, demonstrating that the network grows incrementally as new decisions become relevant. This validates the probabilistic approach -- new decisions can be added without disrupting existing ones.

The key message is: "The decision network has grown from an initial core to 40+ nodes across 7 major versions, each adding decisions as the scaffold's scope expanded."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  PRD VERSIONING TIMELINE                                       |
|  ■ Network Growth: v1.0 to v2.0                                |
+---------------------------------------------------------------+
|                                                                |
|  v1.0 ──■── Core Foundation                                   |
|  │       L1-L3 core decisions (business, architecture, DB)     |
|  │       ~15 initial nodes                                     |
|  │                                                             |
|  v1.5 ──■── Architecture Expansion                             |
|  │       + Artifact Decoupling Strategy                        |
|  │       + Data Quality Strategy                               |
|  │       + Schema Governance                                   |
|  │                                                             |
|  v1.6 ──■── Agentic UI + Voice + Graph RAG                    |
|  │       + UI Adaptation Strategy                              |
|  │       + Agentic UI Framework (CopilotKit)                   |
|  │       + Voice Agent Stack                                   |
|  │       + Graph RAG Engine                                    |
|  │       30 nodes total                                        |
|  │                                                             |
|  v1.7 ──■── LLM + Audio Metadata                              |
|  │       + LLM Routing Strategy                                |
|  │       + Audio Metadata Library (tinytag)                    |
|  │       31 nodes total                                        |
|  │                                                             |
|  v1.8 ──■── Commercial Landscape                               |
|  │       + Training Attribution Integration                    |
|  │       + Rights Management Scope                             |
|  │       + Provenance Verification                             |
|  │       + External Registry Integration                       |
|  │                                                             |
|  v1.9 ──■── xOps Expansion                                    |
|  │       + Orchestrator Choice                                 |
|  │       + CD Strategy                                         |
|  │       + ML Monitoring                                       |
|  │       + Documentation Tooling                               |
|  │       + Policy-as-Code, FinOps, Ethics Governance           |
|  │                                                             |
|  v2.0 ──■── Regulatory Compliance                              |
|          + Provenance & Citation Strategy                       |
|          + Compliance Framework Mapping                        |
|          + TDM Rights Reservation                              |
|          40+ nodes total                                       |
|                                                                |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "PRD VERSIONING TIMELINE" with coral accent square |
| Version milestones | `decision_point` | Vertical timeline with version markers |
| Version labels | `label_editorial` | v1.0 through v2.0 with descriptive names |
| Added nodes per version | `branching_path` | List of new decision nodes added at each version |
| Node count markers | `data_mono` | Running totals at key milestones |
| Timeline line | `accent_line_v` | Vertical coral accent line connecting versions |

## Anti-Hallucination Rules

1. The _network.yaml version is 2.0.0 as of 2026-02-13.
2. The REPORT.md references 30 nodes in its overview. The _network.yaml has grown to 40+ with v1.8-v2.0 additions.
3. Key v1.6 additions: UI Adaptation Strategy, Agentic UI Framework, Voice Agent Stack, Graph RAG Engine -- explicitly documented in REPORT.md.
4. Key v1.7 additions: LLM Routing Strategy, Audio Metadata Library -- per _network.yaml file comments.
5. Key v1.8 additions (commercial landscape): Training Attribution Integration, Rights Management Scope, Provenance Verification, External Registry Integration -- per _network.yaml L3-components section.
6. Key v1.9 additions (xOps): Orchestrator Choice, CD Strategy, ML Monitoring, Documentation Tooling, Policy-as-Code, FinOps Strategy, Ethics Governance -- per _network.yaml edge comments "v1.9.0".
7. Key v2.0 additions (regulatory): Provenance & Citation Strategy, Compliance Framework Mapping, TDM Rights Reservation -- per _network.yaml edge comments "v2.0.0".
8. The exact version numbers and node assignments are reconstructed from the _network.yaml structure. Some assignments may differ from actual git history.
9. Background must be warm cream (#f6f3e6).

## Alt Text

Timeline visualization: evolution of the music attribution scaffold probabilistic PRD from v1.0 core foundation through v2.0 regulatory compliance, showing incremental growth from 15 to 40-plus decision nodes across seven versions -- demonstrating how open-source music metadata architecture decisions expand without disrupting existing Bayesian confidence scoring structures.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Timeline visualization: evolution of the music attribution scaffold probabilistic PRD from v1.0 core foundation through v2.0 regulatory compliance, showing incremental growth from 15 to 40-plus decision nodes across seven versions -- demonstrating how open-source music metadata architecture decisions expand without disrupting existing Bayesian confidence scoring structures.](docs/figures/repo-figures/assets/fig-prd-09-versioning-timeline.jpg)

*Figure 9. The probabilistic PRD has grown incrementally from 15 initial nodes (v1.0) to 40-plus nodes (v2.0), adding agentic UI, LLM routing, commercial landscape, xOps, and regulatory compliance decisions -- each version extending the network without breaking prior conditional probability structures.*

### From this figure plan (relative)

![Timeline visualization: evolution of the music attribution scaffold probabilistic PRD from v1.0 core foundation through v2.0 regulatory compliance, showing incremental growth from 15 to 40-plus decision nodes across seven versions -- demonstrating how open-source music metadata architecture decisions expand without disrupting existing Bayesian confidence scoring structures.](../assets/fig-prd-09-versioning-timeline.jpg)
