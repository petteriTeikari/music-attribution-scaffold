# fig-landscape-23: Founder's Build-vs-Buy-vs-Partner Decision Map

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-23 |
| **Title** | Founder's Build-vs-Buy-vs-Partner Decision Map |
| **Audience** | L3 (Engineer) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

This figure maps 12 infrastructure components against three team archetypes, showing how the optimal mix of build, buy, and partner changes depending on funding stage, team size, and IP strategy. It answers: "For my specific team archetype, which components should I build in-house, buy off the shelf, or partner for?"

## Key Message

12 infrastructure components map differently across 3 team archetypes -- the optimal mix of build, buy, and partner depends on funding stage and IP strategy.

## Visual Concept

Split panel. Left side lists 12 infrastructure components vertically, grouped into commodity, core, and strategic tiers. Right side shows a 12x3 grid matrix with three team archetype columns (Solo Hacker, Funded Startup, Enterprise Team). Each cell is marked Build, Buy, or Partner. A legend at the bottom explains: buy = commodity (no differentiation), build = differentiator (competitive advantage), partner = strategic (access without ownership). Based on docs/planning/music-tech-landscape/07-buy-vs-build.md.

```
+---------------------------------------------------------------+
|  FOUNDER'S DECISION MAP                                        |
|  ■ Build vs Buy vs Partner for 12 Components                   |
+---------------------------------------------------------------+
|                               |                                |
|  COMPONENTS                   |  TEAM ARCHETYPES               |
|  ──────────                   |  ────────────────              |
|                               |  Solo    Funded   Enterprise   |
|                               |  Hacker  Startup  Team         |
|  ┌─────────────────────────┐  |  ┌──────┬──────┬──────┐       |
|  │ Auth & identity         │  |  │ BUY  │ BUY  │ BUILD│       |
|  │ Database/storage        │  |  │ BUY  │ BUY  │ BUY  │       |
|  │ Hosting/infra           │  |  │ BUY  │ BUY  │ BUY  │       |
|  │ LLM provider            │  |  │ BUY  │ BUY  │ PTNR │       |
|  ├─────────────────────────┤  |  ├──────┼──────┼──────┤       |
|  │ Embeddings/vectors      │  |  │ BUY  │BUILD │ BUILD│       |
|  │ MusicBrainz integration │  |  │ BUY  │BUILD │ PTNR │       |
|  │ Audio fingerprinting    │  |  │ BUY  │ PTNR │ BUILD│       |
|  │ Entity resolution       │  |  │  --  │BUILD │ BUILD│       |
|  ├─────────────────────────┤  |  ├──────┼──────┼──────┤       |
|  │ Confidence scoring      │  |  │  --  │BUILD │ BUILD│       |
|  │ MCP server              │  |  │BUILD │BUILD │ BUILD│       |
|  │ TDA pipeline            │  |  │  --  │  --  │ BUILD│       |
|  │ Graph knowledge base    │  |  │  --  │ PTNR │ BUILD│       |
|  └─────────────────────────┘  |  └──────┴──────┴──────┘       |
|                               |                                |
+---------------------------------------------------------------+
|  ■ BUY = commodity (no differentiation)                        |
|  ■ BUILD = differentiator (competitive advantage)              |
|  ■ PARTNER = strategic (access without ownership)              |
|  ■ -- = skip at this stage                                     |
|                                                                |
|  Based on: 07-buy-vs-build.md analysis                         |
+---------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: warm_cream

title_block:
  position: [60, 40]
  width: 1800
  height: 80
  elements:
    - type: heading_display
      text: "FOUNDER'S DECISION MAP"
    - type: label_editorial
      text: "Build vs Buy vs Partner for 12 Components"

component_list:
  position: [60, 140]
  width: 800
  height: 700
  label: "COMPONENTS"
  tiers:
    commodity:
      label: "Commodity Tier"
      items:
        - "Auth & identity"
        - "Database/storage"
        - "Hosting/infra"
        - "LLM provider"
    core:
      label: "Core Tier"
      items:
        - "Embeddings/vectors"
        - "MusicBrainz integration"
        - "Audio fingerprinting"
        - "Entity resolution"
    strategic:
      label: "Strategic Tier"
      items:
        - "Confidence scoring"
        - "MCP server"
        - "TDA pipeline"
        - "Graph knowledge base"

archetype_matrix:
  position: [880, 140]
  width: 980
  height: 700
  columns:
    - { name: "Solo Hacker", funding: "Pre-seed/$0", team: "1-2 people" }
    - { name: "Funded Startup", funding: "Seed-A/$1-5M", team: "5-15 people" }
    - { name: "Enterprise Team", funding: "Series B+/$10M+", team: "30+ people" }
  cells:
    # Commodity tier
    - { component: "Auth & identity", solo: "buy", startup: "buy", enterprise: "build" }
    - { component: "Database/storage", solo: "buy", startup: "buy", enterprise: "buy" }
    - { component: "Hosting/infra", solo: "buy", startup: "buy", enterprise: "buy" }
    - { component: "LLM provider", solo: "buy", startup: "buy", enterprise: "partner" }
    # Core tier
    - { component: "Embeddings/vectors", solo: "buy", startup: "build", enterprise: "build" }
    - { component: "MusicBrainz integration", solo: "buy", startup: "build", enterprise: "partner" }
    - { component: "Audio fingerprinting", solo: "buy", startup: "partner", enterprise: "build" }
    - { component: "Entity resolution", solo: "skip", startup: "build", enterprise: "build" }
    # Strategic tier
    - { component: "Confidence scoring", solo: "skip", startup: "build", enterprise: "build" }
    - { component: "MCP server", solo: "build", startup: "build", enterprise: "build" }
    - { component: "TDA pipeline", solo: "skip", startup: "skip", enterprise: "build" }
    - { component: "Graph knowledge base", solo: "skip", startup: "partner", enterprise: "build" }

legend:
  position: [60, 870]
  width: 1800
  height: 140
  elements:
    - type: badge_label
      items:
        - { label: "BUY", meaning: "commodity — no differentiation" }
        - { label: "BUILD", meaning: "differentiator — competitive advantage" }
        - { label: "PARTNER", meaning: "strategic — access without ownership" }
        - { label: "--", meaning: "skip at this stage" }
    - type: data_mono
      text: "Based on: 07-buy-vs-build.md analysis"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "FOUNDER'S DECISION MAP" with coral accent square |
| Subtitle | `label_editorial` | "Build vs Buy vs Partner for 12 Components" |
| Component list | `solution_component` | 12 components grouped into commodity/core/strategic |
| Commodity tier | `deferred_option` | Auth, database, hosting, LLM -- typically bought |
| Core tier | `branching_path` | Embeddings, MusicBrainz, fingerprinting, entity resolution |
| Strategic tier | `selected_option` | Confidence scoring, MCP, TDA, graph KB -- differentiators |
| Solo Hacker column | `archetype_overlay` | Pre-seed, 1-2 people, maximum buy |
| Funded Startup column | `archetype_overlay` | Seed-A, 5-15 people, selective build |
| Enterprise column | `archetype_overlay` | Series B+, 30+ people, build differentiators |
| Decision cells | `badge_label` | BUY / BUILD / PARTNER / skip indicators |
| Legend | `callout_bar` | Explanation of buy/build/partner/skip semantics |
| Source reference | `data_mono` | "Based on: 07-buy-vs-build.md analysis" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Commodity tier | All archetypes | recommendation | "Almost always buy" |
| Core tier | Archetype columns | varies | "Depends on funding and IP strategy" |
| Strategic tier | Enterprise column | recommendation | "Build for differentiation" |
| Strategic tier | Solo Hacker column | recommendation | "Skip until funded" |
| Funding stage | Build/buy ratio | correlation | "More funding = more build" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Legend | BUY/BUILD/PARTNER/skip definitions | Bottom bar |
| Source | "Based on: 07-buy-vs-build.md analysis" | Bottom-right |
| MCP Insight | "MCP server is BUILD for ALL archetypes — core differentiator" | Inline with MCP row |

## Text Content

### Labels (Max 30 chars each)

- FOUNDER'S DECISION MAP
- Build vs Buy vs Partner
- COMPONENTS
- TEAM ARCHETYPES
- Commodity Tier
- Core Tier
- Strategic Tier
- Solo Hacker
- Funded Startup
- Enterprise Team
- Auth & identity
- Database/storage
- Hosting/infra
- LLM provider
- Embeddings/vectors
- MusicBrainz integration
- Audio fingerprinting
- Entity resolution
- Confidence scoring
- MCP server
- TDA pipeline
- Graph knowledge base
- BUY
- BUILD
- PARTNER

### Caption (for embedding in documentation)

Twelve infrastructure components mapped across three team archetypes (Solo Hacker, Funded Startup, Enterprise Team) with build/buy/partner recommendations for each. Commodity components (auth, database, hosting) are almost always bought; core components (embeddings, fingerprinting, entity resolution) vary by funding stage; strategic components (confidence scoring, MCP, TDA, graph KB) are built in-house when resources allow. Based on 07-buy-vs-build.md analysis.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)**.
5. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

1. There are exactly 12 components and 3 archetypes -- do NOT add or remove any.
2. Build/buy/partner assignments are RECOMMENDATIONS, not mandates -- context matters.
3. "Skip" (--) means the component is not worth investing in at that stage, not that it is unimportant.
4. MCP server is BUILD for ALL archetypes -- this is a deliberate design choice reflecting the scaffold's philosophy.
5. TDA pipeline is only BUILD for Enterprise -- do NOT recommend for smaller teams.
6. The three archetypes are ILLUSTRATIVE team profiles, not rigid categories.
7. Do NOT name specific vendor products in the matrix cells -- the focus is build/buy/partner STRATEGY.
8. Funding ranges are approximate (Pre-seed, Seed-A, Series B+) -- do NOT claim exact thresholds.
9. The 07-buy-vs-build.md source is a real document in this repo -- reference it accurately.
10. Do NOT imply that "build" is always superior to "buy" -- the point is STRATEGIC SELECTION.

## Alt Text

Decision matrix mapping 12 infrastructure components to build/buy/partner for three team archetypes.

## JSON Export Block

```json
{
  "id": "fig-landscape-23",
  "title": "Founder's Build-vs-Buy-vs-Partner Decision Map",
  "audience": "L3",
  "priority": "P1",
  "layout": "D",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Synthesize",
  "components": [
    { "name": "Auth & identity", "tier": "commodity" },
    { "name": "Database/storage", "tier": "commodity" },
    { "name": "Hosting/infra", "tier": "commodity" },
    { "name": "LLM provider", "tier": "commodity" },
    { "name": "Embeddings/vectors", "tier": "core" },
    { "name": "MusicBrainz integration", "tier": "core" },
    { "name": "Audio fingerprinting", "tier": "core" },
    { "name": "Entity resolution", "tier": "core" },
    { "name": "Confidence scoring", "tier": "strategic" },
    { "name": "MCP server", "tier": "strategic" },
    { "name": "TDA pipeline", "tier": "strategic" },
    { "name": "Graph knowledge base", "tier": "strategic" }
  ],
  "archetypes": [
    { "name": "Solo Hacker", "funding": "Pre-seed", "team_size": "1-2" },
    { "name": "Funded Startup", "funding": "Seed-A", "team_size": "5-15" },
    { "name": "Enterprise Team", "funding": "Series B+", "team_size": "30+" }
  ],
  "source": "docs/planning/music-tech-landscape/07-buy-vs-build.md",
  "semantic_tags_used": [
    "heading_display", "label_editorial", "solution_component", "archetype_overlay",
    "branching_path", "selected_option", "deferred_option", "badge_label",
    "callout_bar", "data_mono"
  ]
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L1/L2/L3/L4)
- [x] Layout template identified (A/B/C/D/E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
