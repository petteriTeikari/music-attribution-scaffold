# fig-ecosystem-13: Edge Inference Strategy Decision

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-13 |
| **Title** | Edge Inference Strategy Decision |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Compares server-only inference (MVP default) against edge deployment for latency-sensitive fingerprint comparison workloads. Answers: "When does the complexity cost of edge deployment justify the latency reduction for audio fingerprinting?"

## Key Message

Server-only inference (P=0.50) is the MVP default; edge deployment reduces fingerprint comparison latency from ~200ms to ~20ms but adds operational complexity across Cloudflare Workers AI, Deno Deploy, or Supabase Edge.

## Visual Concept

Split-panel with server-only on the left (current MVP, simpler) and edge deployment on the right (future, faster but complex). A horizontal axis at the bottom shows the latency vs. complexity trade-off continuum. The left panel is visually heavier (selected/current), the right is lighter (aspirational).

```
+---------------------------------------------------------------+
|  EDGE INFERENCE STRATEGY DECISION                              |
|  -- Latency vs Operational Complexity                          |
+-------------------------------+-------------------------------+
|                               |                               |
|  SERVER-ONLY (current MVP)    |  EDGE DEPLOYMENT (future)     |
|  ─────────────────────        |  ────────────────────         |
|                               |                               |
|  ┌─────────────────────────┐ |  ┌─────────────────────────┐  |
|  │  Single Region Server    │ |  │  Multi-Region Edge      │  |
|  │                          │ |  │                          │  |
|  │  Fingerprint comparison  │ |  │  Fingerprint comparison  │  |
|  │  ~200ms latency          │ |  │  ~20ms latency           │  |
|  │                          │ |  │                          │  |
|  │  Simple ops              │ |  │  Platform options:       │  |
|  │  Single deployment       │ |  │  - Cloudflare Workers AI │  |
|  │  Standard monitoring     │ |  │  - Deno Deploy           │  |
|  │                          │ |  │  - Supabase Edge Fn      │  |
|  │  P = 0.50               │ |  │                          │  |
|  └─────────────────────────┘ |  │  Added complexity:       │  |
|                               |  │  - Multi-region state    │  |
|                               |  │  - Edge cache coherence  │  |
|                               |  │  - Cold start management │  |
|                               |  │                          │  |
|                               |  └─────────────────────────┘  |
|                               |                               |
+-------------------------------+-------------------------------+
|                                                                |
|  LATENCY ◄───────────────────────────────► COMPLEXITY          |
|  ~20ms (edge)         ~200ms (server)        ops burden        |
|                                                                |
+---------------------------------------------------------------+
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
    content: "EDGE INFERENCE STRATEGY DECISION"
    role: title

  - id: left_panel
    bounds: [60, 150, 880, 680]
    role: content_area

  - id: right_panel
    bounds: [980, 150, 880, 680]
    role: content_area

  - id: divider
    bounds: [950, 150, 4, 680]
    role: accent_line_v

  - id: tradeoff_zone
    bounds: [60, 870, 1800, 140]
    role: callout_box

anchors:
  - id: server_panel
    position: [500, 490]
    size: [780, 580]
    role: selected_option
    label: "Server-Only"

  - id: edge_panel
    position: [1420, 490]
    size: [780, 580]
    role: deferred_option
    label: "Edge Deployment"

  - id: tradeoff_axis
    position: [960, 940]
    size: [1700, 80]
    role: data_flow
    label: "latency vs complexity"

  - id: cloudflare_option
    position: [1300, 520]
    size: [200, 60]
    role: branching_path
    label: "Cloudflare Workers AI"

  - id: deno_option
    position: [1300, 600]
    size: [200, 60]
    role: branching_path
    label: "Deno Deploy"

  - id: supabase_option
    position: [1300, 680]
    size: [200, 60]
    role: branching_path
    label: "Supabase Edge Functions"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "EDGE INFERENCE STRATEGY DECISION" with coral accent square |
| Server-Only panel | `selected_option` | Current MVP, single region, ~200ms latency, simple ops, P=0.50 |
| Edge Deployment panel | `deferred_option` | Future option, multi-region, ~20ms latency, complex ops |
| Cloudflare Workers AI | `branching_path` | Edge platform option within edge deployment |
| Deno Deploy | `branching_path` | Edge platform option within edge deployment |
| Supabase Edge Functions | `branching_path` | Edge platform option within edge deployment |
| Trade-off axis | `data_flow` | Horizontal axis showing latency vs complexity continuum |
| Center divider | `accent_line_v` | Coral vertical separator between panels |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| service_decomposition (parent) | edge_inference_strategy | dashed | "moderate influence" |
| build_vs_buy_posture (parent) | edge_inference_strategy | dashed | "moderate influence" |
| edge_inference_strategy | edge_deployment_target | arrow | "if edge selected, choose platform" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "MVP DEFAULT" | Server-only is the starting point -- edge is a future optimization | left-margin |
| "LATENCY NUMBERS" | ~200ms and ~20ms are approximate/illustrative, not benchmarked | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "SERVER-ONLY"
- Label 2: "EDGE DEPLOYMENT"
- Label 3: "~200ms latency"
- Label 4: "~20ms latency"
- Label 5: "Simple ops"
- Label 6: "Multi-region state"
- Label 7: "P = 0.50"
- Label 8: "Cloudflare Workers AI"
- Label 9: "Deno Deploy"
- Label 10: "Supabase Edge Functions"

### Caption (for embedding in documentation)

Edge inference strategy decision -- server-only (P=0.50) is the MVP default with ~200ms fingerprint comparison latency and simple operations; edge deployment reduces latency to ~20ms but adds operational complexity across Cloudflare Workers AI, Deno Deploy, or Supabase Edge Functions.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `deferred_option`, `branching_path` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD nodes: `edge_inference_strategy` (L3_components), `edge_deployment_target` (L4_deployment).
10. Parent nodes: `service_decomposition` (moderate), `build_vs_buy_posture` (moderate).
11. `none_server_only` has P=0.50 -- this is the highest-probability option (MVP default).
12. Edge platforms are Cloudflare Workers AI, Deno Deploy, and Supabase Edge Functions -- these are the specific options in the PRD node.
13. Latency numbers (~200ms server, ~20ms edge) are approximate/illustrative, NOT benchmarked measurements.
14. Do NOT claim edge deployment is currently implemented -- it is a future option only.
15. The "fingerprint comparison" workload is the primary latency-sensitive use case driving this decision.
16. Cold start management is a real operational concern for edge functions -- do NOT minimize it.

## Alt Text

Edge inference decision: server-only MVP default vs edge deployment for latency

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-13",
    "title": "Edge Inference Strategy Decision",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Server-only inference (P=0.50) is the MVP default; edge deployment reduces fingerprint comparison latency from ~200ms to ~20ms but adds operational complexity.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Server-Only Panel",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["SERVER-ONLY", "~200ms latency", "P = 0.50"]
      },
      {
        "name": "Edge Deployment Panel",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["EDGE DEPLOYMENT", "~20ms latency"]
      },
      {
        "name": "Cloudflare Workers AI",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["Cloudflare Workers AI"]
      },
      {
        "name": "Deno Deploy",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["Deno Deploy"]
      },
      {
        "name": "Supabase Edge Functions",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["Supabase Edge Functions"]
      }
    ],
    "relationships": [
      {
        "from": "service_decomposition",
        "to": "edge_inference_strategy",
        "type": "dashed",
        "label": "moderate influence"
      },
      {
        "from": "edge_inference_strategy",
        "to": "edge_deployment_target",
        "type": "arrow",
        "label": "if edge selected, choose platform"
      }
    ],
    "callout_boxes": [
      {
        "heading": "MVP DEFAULT",
        "body_text": "Server-only is the starting point -- edge is a future optimization",
        "position": "left-margin"
      },
      {
        "heading": "LATENCY NUMBERS",
        "body_text": "~200ms and ~20ms are approximate/illustrative, not benchmarked",
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
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
