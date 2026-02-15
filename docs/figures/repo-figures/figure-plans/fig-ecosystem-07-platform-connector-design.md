# fig-ecosystem-07: AI Music Platform Connector Design

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-07 |
| **Title** | AI Music Platform Connector Design |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows how platform connectors normalize Suno/Udio metadata against the NormalizedRecord schema. Answers: "How does proprietary AI platform metadata get ingested into the attribution pipeline?"

## Key Message

Platform connectors ingest proprietary metadata formats from AI music platforms, map fields to the NormalizedRecord Pydantic schema, and feed the attribution pipeline with platform-specific confidence adjustments.

## Visual Concept

Top-to-bottom flow. Top tier shows platform APIs (Suno, Udio, future platforms). Middle tier shows the connector layer performing field mapping, schema normalization, and confidence adjustment. Bottom tier shows the NormalizedRecord schema entering the ETL pipeline. Side annotation connects to the suno_udio_licensing PRD node.

```
+-----------------------------------------------------------------------+
|  AI MUSIC PLATFORM CONNECTOR                                           |
|  ■ Proprietary Metadata to NormalizedRecord                            |
+-----------------------------------------------------------------------+
|                                                                        |
|  PLATFORM APIs                                                         |
|  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                 |
|  │ Suno API     │  │ Udio API     │  │ Future       │                 |
|  │              │  │              │  │ Platforms    │                 |
|  │ $250M raised │  │ Copyright    │  │              │                 |
|  │ $2.45B val.  │  │ suits        │  │ (extensible) │                 |
|  │              │  │ settled      │  │              │                 |
|  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                 |
|         │                 │                 │                          |
|         │  proprietary    │  proprietary    │  TBD                     |
|         │  metadata       │  metadata       │  format                  |
|         │                 │                 │                          |
|         └────────────┬────┴─────────────────┘                          |
|                      ▼                                                 |
|  ┌───────────────────────────────────────────────────────────────┐    |
|  │  CONNECTOR LAYER                                               │    |
|  │  ═══════════════                                               │    |
|  │                                                                │    |
|  │  ┌──────────────┐  ┌──────────────────┐  ┌─────────────────┐  │    |
|  │  │ Field        │  │ Schema           │  │ Confidence      │  │    |
|  │  │ Mapping      │  │ Normalization    │  │ Adjustment      │  │    |
|  │  │ ──────────   │  │ ────────────     │  │ ──────────────  │  │    |
|  │  │ Platform-    │  │ Validate         │  │ Platform-       │  │    |
|  │  │ specific     │  │ against          │  │ specific        │  │    |
|  │  │ field names  │  │ NormalizedRecord │  │ authority       │  │    |
|  │  │ to canonical │  │ Pydantic schema  │  │ weights         │  │    |
|  │  └──────┬───────┘  └────────┬─────────┘  └───────┬─────────┘  │    |
|  │         └──────────────┬────┴─────────────────────┘            │    |
|  └────────────────────────┼───────────────────────────────────────┘    |
|                           ▼                                            |
|  ┌───────────────────────────────────────────────────────────────┐    |
|  │  NormalizedRecord (Pydantic)                                   │    |
|  │  ═══════════════════════════                                   │    |
|  │  title, artist_name, isrc, source, confidence_score, ...       │    |
|  └──────────────────────────┬────────────────────────────────────┘    |
|                              │                                         |
|                              ▼                                         |
|                     ┌────────────────┐                                 |
|  PRD NODE:          │  ETL Pipeline  │                                 |
|  ai_music_platform  │  (Stage I)     │                                 |
|  _connector         └────────────────┘                                 |
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
    content: "AI MUSIC PLATFORM CONNECTOR"
    role: title

  - id: platforms_zone
    bounds: [200, 140, 1520, 200]
    role: content_area
    label: "Platform APIs"

  - id: connector_zone
    bounds: [120, 400, 1680, 280]
    role: content_area_highlighted
    label: "Connector Layer"

  - id: schema_zone
    bounds: [200, 740, 1520, 120]
    role: content_area
    label: "NormalizedRecord output"

  - id: pipeline_zone
    bounds: [700, 900, 520, 100]
    role: content_area
    label: "ETL Pipeline"

anchors:
  - id: suno_api
    position: [300, 180]
    size: [360, 120]
    role: stakeholder_platform
    label: "Suno API"

  - id: udio_api
    position: [780, 180]
    size: [360, 120]
    role: stakeholder_platform
    label: "Udio API"

  - id: future_api
    position: [1260, 180]
    size: [360, 120]
    role: stakeholder_platform
    label: "Future Platforms"

  - id: field_mapping
    position: [200, 440]
    size: [440, 180]
    role: processing_stage
    label: "Field Mapping"

  - id: schema_normalization
    position: [720, 440]
    size: [440, 180]
    role: processing_stage
    label: "Schema Normalization"

  - id: confidence_adjustment
    position: [1240, 440]
    size: [440, 180]
    role: processing_stage
    label: "Confidence Adjustment"

  - id: normalized_record
    position: [300, 760]
    size: [1320, 80]
    role: etl_extract
    label: "NormalizedRecord (Pydantic)"

  - id: etl_pipeline
    position: [780, 920]
    size: [360, 60]
    role: processing_stage
    label: "ETL Pipeline (Stage I)"

  - id: platforms_to_connector
    from: suno_api
    to: field_mapping
    type: arrow
    label: "proprietary metadata"

  - id: connector_to_schema
    from: confidence_adjustment
    to: normalized_record
    type: arrow
    label: "validated output"

  - id: schema_to_etl
    from: normalized_record
    to: etl_pipeline
    type: arrow
    label: "feeds pipeline"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Suno API | `stakeholder_platform` | Suno platform API ($250M raised, $2.45B valuation) |
| Udio API | `stakeholder_platform` | Udio platform API (copyright suits settled) |
| Future Platforms | `stakeholder_platform` | Extensible connector architecture for new platforms |
| Field Mapping | `processing_stage` | Platform-specific field names mapped to canonical names |
| Schema Normalization | `processing_stage` | Validation against NormalizedRecord Pydantic schema |
| Confidence Adjustment | `processing_stage` | Platform-specific authority weights applied |
| NormalizedRecord | `etl_extract` | Pydantic boundary object at ETL output |
| ETL Pipeline | `processing_stage` | Stage I of the five-pipeline architecture |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Suno API | Field Mapping | arrow | "proprietary metadata" |
| Udio API | Field Mapping | arrow | "proprietary metadata" |
| Future Platforms | Field Mapping | dashed | "TBD format" |
| Field Mapping | Schema Normalization | arrow | "canonical fields" |
| Schema Normalization | Confidence Adjustment | arrow | "validated schema" |
| Confidence Adjustment | NormalizedRecord | arrow | "confidence-annotated" |
| NormalizedRecord | ETL Pipeline | arrow | "feeds attribution pipeline" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PRD NODE" | ai_music_platform_connector: parents platform_strategy (moderate), api_protocol (moderate); child suno_udio_licensing (strong) | left-margin |
| "NO ATTRIBUTION APIs YET" | These platforms do not currently provide attribution-specific APIs -- connectors would need to work with available metadata endpoints | bottom-right |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Suno API"
- Label 2: "Udio API"
- Label 3: "Future Platforms"
- Label 4: "Field Mapping"
- Label 5: "Schema Normalization"
- Label 6: "Confidence Adjustment"
- Label 7: "NormalizedRecord (Pydantic)"
- Label 8: "ETL Pipeline (Stage I)"

### Caption (for embedding in documentation)

Platform connectors ingest proprietary metadata from AI music platforms (Suno, Udio), map fields to the NormalizedRecord Pydantic schema, apply platform-specific confidence adjustments, and feed normalized records into the ETL pipeline.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `stakeholder_platform`, `processing_stage`, `etl_extract` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "NormalizedRecord" may appear as this is L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD node: ai_music_platform_connector. Parents: platform_strategy (moderate), api_protocol (moderate). Child: suno_udio_licensing (strong).
10. NormalizedRecord is the Pydantic boundary object at ETL output -- this is a real class in the codebase.
11. Suno raised $250M at $2.45B valuation; Udio settled copyright suits. These are factual context markers.
12. Do NOT claim these platforms currently provide attribution APIs -- connectors would work with available metadata endpoints.
13. The connector architecture is extensible to future platforms -- show this with a dashed "Future Platforms" box.

## Alt Text

Platform connector design normalizing AI music platform metadata to NormalizedRecord

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-07",
    "title": "AI Music Platform Connector Design",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Platform connectors normalize proprietary AI music metadata to NormalizedRecord schema with confidence adjustments.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Suno API",
        "role": "stakeholder_platform",
        "is_highlighted": false,
        "labels": ["Suno API", "$250M / $2.45B"]
      },
      {
        "name": "Udio API",
        "role": "stakeholder_platform",
        "is_highlighted": false,
        "labels": ["Udio API", "Suits settled"]
      },
      {
        "name": "Connector Layer",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Field Mapping", "Schema Normalization", "Confidence Adjustment"]
      },
      {
        "name": "NormalizedRecord",
        "role": "etl_extract",
        "is_highlighted": true,
        "labels": ["NormalizedRecord", "Pydantic boundary object"]
      },
      {
        "name": "ETL Pipeline",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["ETL Pipeline", "Stage I"]
      }
    ],
    "relationships": [
      {
        "from": "Platform APIs",
        "to": "Connector Layer",
        "type": "arrow",
        "label": "proprietary metadata"
      },
      {
        "from": "Connector Layer",
        "to": "NormalizedRecord",
        "type": "arrow",
        "label": "confidence-annotated output"
      },
      {
        "from": "NormalizedRecord",
        "to": "ETL Pipeline",
        "type": "arrow",
        "label": "feeds attribution pipeline"
      }
    ],
    "callout_boxes": [
      {
        "heading": "PRD NODE",
        "body_text": "ai_music_platform_connector: platform_strategy + api_protocol -> suno_udio_licensing",
        "position": "left-margin"
      },
      {
        "heading": "NO ATTRIBUTION APIs YET",
        "body_text": "Platforms do not currently provide attribution-specific APIs",
        "position": "bottom-right"
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
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
