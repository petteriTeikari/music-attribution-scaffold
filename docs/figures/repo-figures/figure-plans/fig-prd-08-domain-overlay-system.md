# fig-prd-08: Domain Overlay System

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-08 |
| **Title** | Domain Overlay System -- Music Attribution vs DPP Traceability |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/domains/README.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Shows how the scaffold's decision network is domain-agnostic, with domain overlays customizing vocabulary, entities, compliance requirements, and probability priors. The core pipeline (Sources -> Entity Resolution -> Unified Record + Confidence -> Permissioned API -> Consumers) is isomorphic across music attribution and DPP traceability. Domain overlays only change the domain-specific details, not the architecture.

The key message is: "The same scaffold architecture applies isomorphically to music attribution (A0-A3 assurance) and supply chain traceability (T0-T3 assurance) -- only the vocabulary and entities change."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  DOMAIN OVERLAY SYSTEM                                         |
|  ■ One Scaffold, Multiple Domains                              |
+---------------------------------------------------------------+
|                                                                |
|  SHARED CORE PIPELINE (domain-agnostic)                        |
|  ═══════════════════════════════════════                        |
|  Sources → Entity Resolution → Unified Record → API → Agents  |
|                                                                |
|  ┌──────────────────────────┐ ┌──────────────────────────┐    |
|  │ MUSIC ATTRIBUTION        │ │ DPP TRACEABILITY         │    |
|  │ ■ Active                 │ │ ■ Active                 │    |
|  │                          │ │                          │    |
|  │ Sources:                 │ │ Sources:                 │    |
|  │  Discogs, MusicBrainz,  │ │  GS1, EPCIS, Supplier   │    |
|  │  Artist Input            │ │  Declarations            │    |
|  │                          │ │                          │    |
|  │ Entities:                │ │ Entities:                │    |
|  │  Artist, Track, Release  │ │  Product, Component,    │    |
|  │                          │ │  Material               │    |
|  │ Assurance: A0-A3         │ │ Assurance: T0-T3        │    |
|  │  A0: Unknown             │ │  T0: Unknown            │    |
|  │  A1: Claimed             │ │  T1: Declared           │    |
|  │  A2: Corroborated        │ │  T2: Audited            │    |
|  │  A3: Verified            │ │  T3: Certified          │    |
|  │                          │ │                          │    |
|  │ API: MCP (consent)       │ │ API: Digital Link       │    |
|  │ Consumers: AI platforms  │ │ Consumers: Regulators   │    |
|  │                          │ │                          │    |
|  │ Regulation: Voluntary    │ │ Regulation: EU ESPR     │    |
|  └──────────────────────────┘ └──────────────────────────┘    |
|                                                                |
|  ┌──────────────────────────────────────────────────────┐     |
|  │ PLANNED: Generic Graph RAG (backbone defaults only)  │     |
|  └──────────────────────────────────────────────────────┘     |
|                                                                |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DOMAIN OVERLAY SYSTEM" with coral accent square |
| Core pipeline banner | `processing_stage` | Shared 5-stage pipeline across all domains |
| Music Attribution overlay | `decision_point` | Sources, entities, A0-A3 assurance, MCP API, AI platform consumers |
| DPP Traceability overlay | `decision_point` | Sources, entities, T0-T3 assurance, Digital Link API, regulator consumers |
| Planned domain stub | `deferred_option` | Generic Graph RAG (planned, not active) |
| Assurance level mappings | `assurance_a0` through `assurance_a3` | Parallel A0-A3 and T0-T3 definitions |

## Anti-Hallucination Rules

1. The isomorphic pipeline is: Fragmented Sources -> Entity Resolution -> Unified Record + Confidence -> Permissioned API -> Agentic Consumers. This is from the domains README.
2. Music Attribution assurance levels: A0 (Unknown), A1 (Claimed), A2 (Corroborated), A3 (Verified).
3. DPP Traceability assurance levels: T0-T3. The exact T-level definitions should be T0 (Unknown), T1 (Declared), T2 (Audited), T3 (Certified) -- from the overlay.
4. Domain registry has 2 active domains + 1 planned (Generic Graph RAG).
5. Music sources: Discogs, MusicBrainz, Artist Input. DPP sources: GS1, EPCIS, Supplier Declarations. These are from the domains README.
6. Music API: MCP for AI training consent. DPP API: Digital Link for supply chain queries.
7. DPP regulation: EU ESPR mandates audit trails. Music regulation is currently voluntary.
8. Background must be warm cream (#f6f3e6).

## Alt Text

Architecture overview: domain overlay system showing how the music attribution scaffold and Digital Product Passport traceability share an isomorphic core pipeline -- sources, entity resolution, unified record with confidence scoring, permissioned API, and agentic consumers -- while differing in music metadata sources, assurance levels (A0-A3 versus T0-T3), and regulatory requirements.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture overview: domain overlay system showing how the music attribution scaffold and Digital Product Passport traceability share an isomorphic core pipeline -- sources, entity resolution, unified record with confidence scoring, permissioned API, and agentic consumers -- while differing in music metadata sources, assurance levels (A0-A3 versus T0-T3), and regulatory requirements.](docs/figures/repo-figures/assets/fig-prd-08-domain-overlay-system.jpg)

*Figure 8. The domain overlay system demonstrates the scaffold's generalizability: music attribution (A0-A3 assurance, MCP consent API) and supply chain traceability (T0-T3 assurance, Digital Link API) are isomorphic instantiations of the same open-source pipeline architecture.*

### From this figure plan (relative)

![Architecture overview: domain overlay system showing how the music attribution scaffold and Digital Product Passport traceability share an isomorphic core pipeline -- sources, entity resolution, unified record with confidence scoring, permissioned API, and agentic consumers -- while differing in music metadata sources, assurance levels (A0-A3 versus T0-T3), and regulatory requirements.](../assets/fig-prd-08-domain-overlay-system.jpg)
