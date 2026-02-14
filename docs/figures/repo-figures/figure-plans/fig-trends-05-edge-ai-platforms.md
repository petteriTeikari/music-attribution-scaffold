# fig-trends-05: Edge AI Platforms for Attribution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-trends-05 |
| **Title** | Edge AI Platforms for Attribution |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/tech-trends-agentic-infrastructure-2026.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Compares three edge platforms for potential attribution workloads -- fingerprint comparison, metadata caching, and attribution lookup. All three are future options, not currently implemented. Answers: "If we move attribution closer to the edge, which platform fits which workload?"

## Key Message

Three edge platforms offer different trade-offs for attribution workloads -- Cloudflare Workers AI (100+ models, pay-per-request), Deno Deploy (V8 + KV, caching), Supabase Edge (Deno + PostgreSQL, direct DB).

## Visual Concept

Three-column layout with each platform as a panel. Each panel lists key capabilities and trade-offs. Bottom bar maps use cases to platforms. All marked as future/not implemented.

```
+-----------------------------------------------------------------------+
|  EDGE AI PLATFORMS FOR ATTRIBUTION                                     |
|  ■ Future options (not currently implemented)                          |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. CLOUDFLARE             II. DENO DEPLOY          III. SUPABASE EDGE |
|     WORKERS AI                                                         |
|  ─────────────────         ────────────────         ────────────────── |
|                                                                        |
|  ┌─────────────────┐      ┌─────────────────┐      ┌────────────────┐ |
|  │                 │      │                 │      │                │ |
|  │ 100+ models     │      │ V8 runtime      │      │ Deno-based     │ |
|  │ Edge inference  │      │ Built-in KV     │      │ Direct PG      │ |
|  │ Pay-per-request │      │ Sub-ms startup  │      │ attribution    │ |
|  │ Global PoPs     │      │ Web standard    │      │ queries        │ |
|  │                 │      │ APIs            │      │ Supabase Auth  │ |
|  │                 │      │                 │      │                │ |
|  └─────────────────┘      └─────────────────┘      └────────────────┘ |
|                                                                        |
|  USE CASE MAPPING                                                      |
|  ────────────────                                                      |
|                                                                        |
|  ┌─────────────────┐      ┌─────────────────┐      ┌────────────────┐ |
|  │ Fingerprint     │      │ Metadata        │      │ Attribution    │ |
|  │ comparison      │      │ caching         │      │ lookup         │ |
|  │ (model at edge) │      │ (KV store)      │      │ (direct DB)   │ |
|  └─────────────────┘      └─────────────────┘      └────────────────┘ |
|                                                                        |
+-----------------------------------------------------------------------+
|  PRD: edge_inference_strategy, edge_deployment_target                  |
|  Current: none_server_only (P=0.50, highest)                           |
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
    content: "EDGE AI PLATFORMS FOR ATTRIBUTION"
    role: title

  - id: panel_1
    bounds: [60, 160, 580, 380]
    content: "CLOUDFLARE WORKERS AI"
    role: content_area

  - id: panel_2
    bounds: [670, 160, 580, 380]
    content: "DENO DEPLOY"
    role: content_area

  - id: panel_3
    bounds: [1280, 160, 580, 380]
    content: "SUPABASE EDGE"
    role: content_area

  - id: usecase_zone
    bounds: [60, 580, 1800, 260]
    content: "USE CASE MAPPING"
    role: content_area

  - id: prd_bar
    bounds: [60, 900, 1800, 100]
    content: "PRD reference"
    role: callout_box

anchors:
  - id: cloudflare_block
    position: [120, 220]
    size: [460, 280]
    role: deferred_option

  - id: deno_block
    position: [730, 220]
    size: [460, 280]
    role: deferred_option

  - id: supabase_block
    position: [1340, 220]
    size: [460, 280]
    role: deferred_option

  - id: usecase_fingerprint
    position: [120, 640]
    size: [460, 140]
    role: processing_stage

  - id: usecase_caching
    position: [730, 640]
    size: [460, 140]
    role: processing_stage

  - id: usecase_lookup
    position: [1340, 640]
    size: [460, 140]
    role: processing_stage

  - id: flow_cf_to_fingerprint
    from: cloudflare_block
    to: usecase_fingerprint
    type: dashed
    label: "best fit"

  - id: flow_deno_to_caching
    from: deno_block
    to: usecase_caching
    type: dashed
    label: "best fit"

  - id: flow_supabase_to_lookup
    from: supabase_block
    to: usecase_lookup
    type: dashed
    label: "best fit"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Cloudflare Workers AI | `deferred_option` | 100+ models, edge inference, pay-per-request, global PoPs |
| Deno Deploy | `deferred_option` | V8 runtime, built-in KV, sub-ms startup, web standard APIs |
| Supabase Edge | `deferred_option` | Deno-based, direct PostgreSQL, attribution queries, Supabase Auth |
| Fingerprint comparison | `processing_stage` | Use case: run model at edge for audio fingerprint matching |
| Metadata caching | `processing_stage` | Use case: cache attribution metadata in KV store at edge |
| Attribution lookup | `processing_stage` | Use case: query attribution database directly from edge |
| PRD reference bar | `callout_box` | Current state: none_server_only (P=0.50) |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Cloudflare Workers AI | Fingerprint comparison | dashed | "best fit" |
| Deno Deploy | Metadata caching | dashed | "best fit" |
| Supabase Edge | Attribution lookup | dashed | "best fit" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PRD REFERENCE" | edge_inference_strategy, edge_deployment_target. Current: none_server_only (P=0.50, highest prior) | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "CLOUDFLARE WORKERS AI"
- Label 2: "DENO DEPLOY"
- Label 3: "SUPABASE EDGE"
- Label 4: "100+ models"
- Label 5: "Edge inference"
- Label 6: "Pay-per-request"
- Label 7: "V8 runtime"
- Label 8: "Built-in KV"
- Label 9: "Sub-ms startup"
- Label 10: "Deno-based"
- Label 11: "Direct PostgreSQL"
- Label 12: "Fingerprint comparison"
- Label 13: "Metadata caching"
- Label 14: "Attribution lookup"

### Caption (for embedding in documentation)

Three edge AI platforms compared for attribution workloads: Cloudflare Workers AI (inference), Deno Deploy (caching), Supabase Edge (database queries). All are future options -- current PRD prior favors server-only.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `deferred_option`, `processing_stage`, `callout_box` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD nodes: edge_inference_strategy, edge_deployment_target. none_server_only has P=0.50 (highest prior).
10. Cloudflare Workers AI supports inference on 100+ models -- this is their stated capability, not benchmarked.
11. Deno Deploy provides V8-based edge functions with KV storage -- it is a real, shipping product.
12. Supabase Edge Functions integrate with Supabase PostgreSQL -- they run Deno under the hood.
13. All three are FUTURE options, not currently implemented in the scaffold.
14. Do NOT claim specific performance numbers (latency, throughput) for any edge platform -- focus on capability trade-offs.
15. The use case mapping (fingerprint/caching/lookup) is suggestive, not prescriptive -- teams may map differently.

## Alt Text

Edge AI platforms: Cloudflare Workers AI, Deno Deploy, and Supabase Edge compared

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "trends-05",
    "title": "Edge AI Platforms for Attribution",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Three edge platforms offer different trade-offs for attribution workloads, all future options.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Cloudflare Workers AI",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["100+ models", "Edge inference", "Pay-per-request"]
      },
      {
        "name": "Deno Deploy",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["V8 runtime", "Built-in KV", "Sub-ms startup"]
      },
      {
        "name": "Supabase Edge",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["Deno-based", "Direct PostgreSQL", "Attribution queries"]
      },
      {
        "name": "Fingerprint Comparison",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Model at edge"]
      },
      {
        "name": "Metadata Caching",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["KV store"]
      },
      {
        "name": "Attribution Lookup",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Direct DB"]
      }
    ],
    "relationships": [
      {
        "from": "Cloudflare Workers AI",
        "to": "Fingerprint Comparison",
        "type": "dashed",
        "label": "best fit"
      },
      {
        "from": "Deno Deploy",
        "to": "Metadata Caching",
        "type": "dashed",
        "label": "best fit"
      },
      {
        "from": "Supabase Edge",
        "to": "Attribution Lookup",
        "type": "dashed",
        "label": "best fit"
      }
    ],
    "callout_boxes": [
      {
        "heading": "PRD REFERENCE",
        "body_text": "edge_inference_strategy, edge_deployment_target. Current: none_server_only (P=0.50)",
        "position": "bottom-center"
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
