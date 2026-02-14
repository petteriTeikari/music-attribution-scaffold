# fig-ecosystem-08: Metadata Registry Integration Map

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-08 |
| **Title** | Metadata Registry Integration Map |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Shows multi-registry integration: MusicBrainz (MBID), Discogs (release), SoundExchange (126M+ ISRCs), DDEX (industry standard). Answers: "How do four metadata registries feed into unified entity resolution?"

## Key Message

Four metadata registries provide complementary identifiers -- MusicBrainz (open, MBID), Discogs (vinyl, release), SoundExchange (126M+ ISRCs, authoritative US), DDEX (industry messaging) -- entity resolution unifies them.

## Visual Concept

Four panels in the top row, each registry showing identifier type, coverage scope, and authority weight. Bottom section shows the entity resolution layer connecting all four to a unified record. Connector lines from each registry flow down to the resolution layer, illustrating the multi-registry entity resolution flow.

```
+-----------------------------------------------------------------------+
|  METADATA REGISTRY INTEGRATION MAP                                     |
|  ■ Four Registries, Unified Resolution                                 |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ |
|  │ MUSICBRAINZ  │ │ DISCOGS      │ │ SOUNDEXCHANGE│ │ DDEX         │ |
|  │ ════════════ │ │ ════════════ │ │ ════════════ │ │ ════════════ │ |
|  │              │ │              │ │              │ │              │ |
|  │ IDENTIFIER   │ │ IDENTIFIER   │ │ IDENTIFIER   │ │ STANDARD     │ |
|  │ MBID (UUID)  │ │ Release ID   │ │ ISRC         │ │ DDEX XML     │ |
|  │              │ │              │ │              │ │              │ |
|  │ COVERAGE     │ │ COVERAGE     │ │ COVERAGE     │ │ COVERAGE     │ |
|  │ Global, open │ │ Physical     │ │ 126M+ ISRCs  │ │ Industry     │ |
|  │ community-   │ │ releases,    │ │ Authoritative│ │ messaging    │ |
|  │ curated      │ │ vinyl focus  │ │ US registry  │ │ standard     │ |
|  │              │ │              │ │              │ │              │ |
|  │ AUTHORITY    │ │ AUTHORITY    │ │ AUTHORITY    │ │ AUTHORITY    │ |
|  │ Medium       │ │ Medium       │ │ High (US)    │ │ Standard     │ |
|  │              │ │              │ │              │ │ (protocol)   │ |
|  │ STATUS       │ │ STATUS       │ │ STATUS       │ │ STATUS       │ |
|  │ ■ Integrated │ │ ■ Integrated │ │ □ Expansion  │ │ □ Expansion  │ |
|  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘ └──────┬───────┘ |
|         │                │                │                │          |
|         └────────────┬───┴────────────────┴────────┬───────┘          |
|                      ▼                             ▼                  |
|  ┌───────────────────────────────────────────────────────────────┐    |
|  │  ENTITY RESOLUTION LAYER                                       │    |
|  │  ═══════════════════════                                       │    |
|  │                                                                │    |
|  │  ┌──────────┐  ┌──────────────┐  ┌───────────────────────┐    │    |
|  │  │ Cross-   │  │ Identifier   │  │ Unified Record        │    │    |
|  │  │ Registry │  │ Reconcil-    │  │ ─────────────────     │    │    |
|  │  │ Matching │  │ iation       │  │ MBID + Release ID +   │    │    |
|  │  │          │──►│              │──►│ ISRC + DDEX mapped   │    │    |
|  │  │ Fuzzy +  │  │ MBID ↔ ISRC │  │ to ResolvedEntity    │    │    |
|  │  │ exact    │  │ Release ↔    │  │                       │    │    |
|  │  │ match    │  │ MBID         │  │                       │    │    |
|  │  └──────────┘  └──────────────┘  └───────────────────────┘    │    |
|  └───────────────────────────────────────────────────────────────┘    |
|                                                                        |
+-----------------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 120]
    content: "METADATA REGISTRY INTEGRATION MAP"
    role: title

  - id: registries_zone
    bounds: [60, 140, 1800, 440]
    role: content_area
    label: "Four registry panels"

  - id: resolution_zone
    bounds: [60, 640, 1800, 360]
    role: content_area_highlighted
    label: "Entity resolution layer"

anchors:
  - id: musicbrainz_panel
    position: [80, 160]
    size: [420, 400]
    role: source_musicbrainz
    label: "MusicBrainz"

  - id: discogs_panel
    position: [540, 160]
    size: [420, 400]
    role: source_discogs
    label: "Discogs"

  - id: soundexchange_panel
    position: [1000, 160]
    size: [420, 400]
    role: decision_point
    label: "SoundExchange"

  - id: ddex_panel
    position: [1460, 160]
    size: [420, 400]
    role: decision_point
    label: "DDEX"

  - id: cross_registry_matching
    position: [160, 680]
    size: [480, 260]
    role: entity_resolve
    label: "Cross-Registry Matching"

  - id: identifier_reconciliation
    position: [720, 680]
    size: [480, 260]
    role: entity_resolve
    label: "Identifier Reconciliation"

  - id: unified_record
    position: [1280, 680]
    size: [480, 260]
    role: final_score
    label: "Unified Record"

  - id: mb_to_resolution
    from: musicbrainz_panel
    to: cross_registry_matching
    type: arrow
    label: "MBIDs"

  - id: discogs_to_resolution
    from: discogs_panel
    to: cross_registry_matching
    type: arrow
    label: "Release IDs"

  - id: sx_to_resolution
    from: soundexchange_panel
    to: identifier_reconciliation
    type: dashed
    label: "ISRCs (expansion)"

  - id: ddex_to_resolution
    from: ddex_panel
    to: identifier_reconciliation
    type: dashed
    label: "DDEX XML (expansion)"

  - id: matching_to_reconciliation
    from: cross_registry_matching
    to: identifier_reconciliation
    type: arrow
    label: "candidate pairs"

  - id: reconciliation_to_unified
    from: identifier_reconciliation
    to: unified_record
    type: arrow
    label: "reconciled identifiers"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| MusicBrainz panel | `source_musicbrainz` | Open, community-curated, MBID (UUID), global coverage, currently integrated |
| Discogs panel | `source_discogs` | Physical releases, vinyl focus, release IDs, currently integrated |
| SoundExchange panel | `decision_point` | 126M+ ISRCs, authoritative US registry, expansion node |
| DDEX panel | `decision_point` | Industry messaging standard, XML protocol, expansion node |
| Cross-Registry Matching | `entity_resolve` | Fuzzy and exact matching across registry identifiers |
| Identifier Reconciliation | `entity_resolve` | MBID-to-ISRC, Release-to-MBID cross-mapping |
| Unified Record | `final_score` | All identifiers mapped to ResolvedEntity |
| Integration status indicators | `data_mono` | Integrated (filled) vs Expansion (open) markers |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| MusicBrainz | Cross-Registry Matching | arrow | "MBIDs" |
| Discogs | Cross-Registry Matching | arrow | "Release IDs" |
| SoundExchange | Identifier Reconciliation | dashed | "ISRCs (expansion)" |
| DDEX | Identifier Reconciliation | dashed | "DDEX XML (expansion)" |
| Cross-Registry Matching | Identifier Reconciliation | arrow | "candidate pairs" |
| Identifier Reconciliation | Unified Record | arrow | "reconciled identifiers" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CURRENTLY INTEGRATED" | MusicBrainz and Discogs are integrated in the scaffold today; SoundExchange and DDEX are expansion nodes | top-right |
| "126M+ ISRCs" | SoundExchange manages the definitive US recording registry with over 126 million ISRCs | inset in SoundExchange panel |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "MusicBrainz (MBID)"
- Label 2: "Discogs (Release ID)"
- Label 3: "SoundExchange (126M+ ISRCs)"
- Label 4: "DDEX (Industry Standard)"
- Label 5: "Cross-Registry Matching"
- Label 6: "Identifier Reconciliation"
- Label 7: "Unified Record"
- Label 8: "Currently Integrated"
- Label 9: "Expansion Node"

### Caption (for embedding in documentation)

Four metadata registries provide complementary identifiers that the entity resolution layer unifies: MusicBrainz (MBID) and Discogs (release IDs) are currently integrated, while SoundExchange (126M+ ISRCs) and DDEX (industry messaging) are expansion nodes awaiting integration.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `source_musicbrainz`, `source_discogs`, `entity_resolve` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "ResolvedEntity", "Splink" may appear as this is L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD nodes: metadata_registry_integration, external_registry_integration -> metadata_registry_integration (strong), soundexchange_registry.
10. SoundExchange manages 126M+ ISRCs. Do NOT fabricate a different number.
11. MusicBrainz uses MBIDs (UUIDs). Discogs uses release IDs. DDEX is industry messaging standard (XML). These identifier types are factual.
12. The scaffold currently integrates MusicBrainz and Discogs; SoundExchange and DDEX are expansion nodes. Visually distinguish integrated (solid) from expansion (dashed/open).
13. Do NOT add registries not mentioned (no Spotify, no Apple Music, no YouTube Content ID in this figure).

## Alt Text

Metadata registry map: MusicBrainz, Discogs, SoundExchange, DDEX unified by resolution

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-08",
    "title": "Metadata Registry Integration Map",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Four metadata registries provide complementary identifiers unified by entity resolution.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "MusicBrainz",
        "role": "source_musicbrainz",
        "is_highlighted": true,
        "labels": ["MusicBrainz", "MBID (UUID)", "Integrated"]
      },
      {
        "name": "Discogs",
        "role": "source_discogs",
        "is_highlighted": true,
        "labels": ["Discogs", "Release ID", "Integrated"]
      },
      {
        "name": "SoundExchange",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["SoundExchange", "126M+ ISRCs", "Expansion"]
      },
      {
        "name": "DDEX",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["DDEX", "Industry Standard", "Expansion"]
      },
      {
        "name": "Entity Resolution Layer",
        "role": "entity_resolve",
        "is_highlighted": true,
        "labels": ["Cross-Registry Matching", "Identifier Reconciliation", "Unified Record"]
      }
    ],
    "relationships": [
      {
        "from": "MusicBrainz",
        "to": "Cross-Registry Matching",
        "type": "arrow",
        "label": "MBIDs"
      },
      {
        "from": "Discogs",
        "to": "Cross-Registry Matching",
        "type": "arrow",
        "label": "Release IDs"
      },
      {
        "from": "SoundExchange",
        "to": "Identifier Reconciliation",
        "type": "dashed",
        "label": "ISRCs (expansion)"
      },
      {
        "from": "DDEX",
        "to": "Identifier Reconciliation",
        "type": "dashed",
        "label": "DDEX XML (expansion)"
      },
      {
        "from": "Cross-Registry Matching",
        "to": "Identifier Reconciliation",
        "type": "arrow",
        "label": "candidate pairs"
      },
      {
        "from": "Identifier Reconciliation",
        "to": "Unified Record",
        "type": "arrow",
        "label": "reconciled identifiers"
      }
    ],
    "callout_boxes": [
      {
        "heading": "CURRENTLY INTEGRATED",
        "body_text": "MusicBrainz and Discogs today; SoundExchange and DDEX are expansion nodes",
        "position": "top-right"
      },
      {
        "heading": "126M+ ISRCs",
        "body_text": "SoundExchange manages the definitive US recording registry",
        "position": "right-margin"
      }
    ]
  }
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
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
