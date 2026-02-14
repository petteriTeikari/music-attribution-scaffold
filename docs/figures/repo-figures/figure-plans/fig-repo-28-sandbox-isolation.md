# fig-repo-28: MCP Sandbox Isolation Patterns

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-28 |
| **Title** | MCP Sandbox Isolation Patterns: Three Approaches |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/mcp-security-production-research.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Compare the three primary MCP sandbox isolation strategies -- Cloudflare Workers (V8 isolates), Docker containers, and Deno sandbox -- showing their trade-offs in latency, language support, isolation strength, and operational complexity.

## Key Message

Docker provides the strongest isolation with full language support but highest cold start latency; Workers and Deno trade language flexibility for sub-millisecond startup.

## Visual Concept

Split-panel layout with three equal columns, each presenting one isolation approach with its characteristics, trade-offs, and best-fit use cases. A recommendation callout bar at the bottom highlights the scaffold's Docker preference.

```
+-----------------------------------------------------------------------+
|  MCP SANDBOX ISOLATION PATTERNS                                        |
|  ■ Three Approaches Compared                                           |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌─────────────────────┐  ┌─────────────────────┐  ┌────────────────┐ |
|  │ CLOUDFLARE WORKERS  │  │ DOCKER ISOLATION     │  │ DENO SANDBOX   │ |
|  │ ─────────────────   │  │ ─────────────────    │  │ ─────────────  │ |
|  │                     │  │                      │  │                │ |
|  │ V8 isolates         │  │ Container per server │  │ V8 + perms    │ |
|  │ Sub-ms cold start   │  │ Seconds cold start   │  │ Sub-ms start  │ |
|  │ JS/TS only          │  │ Any language          │  │ TS/JS only    │ |
|  │ 10ms CPU limit      │  │ Configurable limits   │  │ Granular perms│ |
|  │ No persistent conn  │  │ Full networking       │  │ --allow-* flags│
|  │                     │  │                      │  │                │ |
|  │ BEST FOR:           │  │ BEST FOR:             │  │ BEST FOR:     │ |
|  │ Edge, low-latency   │  │ Full Python stack     │  │ TS projects   │ |
|  │ Simple tools        │  │ Complex attribution   │  │ Edge deploy   │ |
|  └─────────────────────┘  └─────────────────────┘  └────────────────┘ |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  SCAFFOLD RECOMMENDATION: Docker (matches existing infra)      │   |
|  └─────────────────────────────────────────────────────────────────┘   |
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
    content: "MCP SANDBOX ISOLATION PATTERNS"
    role: title

  - id: columns_zone
    bounds: [80, 160, 1760, 700]
    role: comparison_panel

  - id: callout_zone
    bounds: [80, 920, 1760, 100]
    role: callout_box

anchors:
  - id: col_workers
    position: [80, 180]
    size: [540, 680]
    role: processing_stage
    label: "CLOUDFLARE WORKERS"

  - id: col_docker
    position: [680, 180]
    size: [540, 680]
    role: processing_stage
    label: "DOCKER ISOLATION"

  - id: col_deno
    position: [1280, 180]
    size: [540, 680]
    role: processing_stage
    label: "DENO SANDBOX"

  - id: workers_tech
    position: [100, 280]
    size: [500, 60]
    role: data_flow
    label: "V8 isolates"

  - id: workers_latency
    position: [100, 350]
    size: [500, 60]
    role: data_flow
    label: "Sub-ms cold start"

  - id: workers_language
    position: [100, 420]
    size: [500, 60]
    role: data_flow
    label: "JS/TS only"

  - id: workers_limit
    position: [100, 490]
    size: [500, 60]
    role: data_flow
    label: "10ms CPU limit"

  - id: workers_network
    position: [100, 560]
    size: [500, 60]
    role: data_flow
    label: "No persistent conn"

  - id: workers_bestfor
    position: [100, 680]
    size: [500, 100]
    role: callout_box
    label: "Edge, low-latency, simple tools"

  - id: docker_tech
    position: [700, 280]
    size: [500, 60]
    role: data_flow
    label: "Container per server"

  - id: docker_latency
    position: [700, 350]
    size: [500, 60]
    role: data_flow
    label: "Seconds cold start"

  - id: docker_language
    position: [700, 420]
    size: [500, 60]
    role: data_flow
    label: "Any language"

  - id: docker_limit
    position: [700, 490]
    size: [500, 60]
    role: data_flow
    label: "Configurable limits"

  - id: docker_network
    position: [700, 560]
    size: [500, 60]
    role: data_flow
    label: "Full networking"

  - id: docker_bestfor
    position: [700, 680]
    size: [500, 100]
    role: callout_box
    label: "Full Python stack, complex attribution"

  - id: deno_tech
    position: [1300, 280]
    size: [500, 60]
    role: data_flow
    label: "V8 + perms"

  - id: deno_latency
    position: [1300, 350]
    size: [500, 60]
    role: data_flow
    label: "Sub-ms start"

  - id: deno_language
    position: [1300, 420]
    size: [500, 60]
    role: data_flow
    label: "TS/JS only"

  - id: deno_limit
    position: [1300, 490]
    size: [500, 60]
    role: data_flow
    label: "Granular perms"

  - id: deno_flags
    position: [1300, 560]
    size: [500, 60]
    role: data_flow
    label: "--allow-* flags"

  - id: deno_bestfor
    position: [1300, 680]
    size: [500, 100]
    role: callout_box
    label: "TS projects, edge deploy"

  - id: recommendation_bar
    position: [80, 920]
    size: [1760, 100]
    role: callout_box
    label: "SCAFFOLD RECOMMENDATION: Docker"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Cloudflare Workers column | `processing_stage` | V8 isolates with sub-ms cold start, JS/TS only, 10ms CPU limit |
| Docker Isolation column | `processing_stage` | Container per server, seconds cold start, any language, configurable limits |
| Deno Sandbox column | `processing_stage` | V8 engine with permission flags, sub-ms start, TS/JS only |
| Recommendation bar | `callout_box` | Docker recommended for scaffold due to existing infrastructure match |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Workers column | Recommendation | comparison | "sub-ms but JS only" |
| Docker column | Recommendation | comparison | "recommended" |
| Deno column | Recommendation | comparison | "sub-ms but TS only" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "RECOMMENDATION" | Docker matches existing scaffold infrastructure (Python stack, PostgreSQL, Docker Compose) | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "CLOUDFLARE WORKERS"
- Label 2: "DOCKER ISOLATION"
- Label 3: "DENO SANDBOX"
- Label 4: "V8 isolates"
- Label 5: "Container per server"
- Label 6: "V8 + perms"
- Label 7: "Sub-ms cold start"
- Label 8: "Seconds cold start"
- Label 9: "JS/TS only"
- Label 10: "Any language"
- Label 11: "TS/JS only"
- Label 12: "10ms CPU limit"
- Label 13: "Configurable limits"
- Label 14: "Granular perms"
- Label 15: "No persistent conn"
- Label 16: "Full networking"
- Label 17: "--allow-* flags"
- Label 18: "BEST FOR:"
- Label 19: "Edge, low-latency"
- Label 20: "Simple tools"
- Label 21: "Full Python stack"
- Label 22: "Complex attribution"
- Label 23: "TS projects"
- Label 24: "Edge deploy"
- Label 25: "SCAFFOLD RECOMMENDATION"
- Label 26: "Docker (matches infra)"

### Caption (for embedding in documentation)

Three MCP sandbox isolation patterns compared: Cloudflare Workers for edge latency, Docker containers for full language support and strongest isolation, and Deno sandbox for granular permissions, with Docker recommended for the scaffold.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color.
5. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 28." or any numbered academic caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. Cloudflare Workers has a 10ms CPU time limit per request. Do NOT confuse with wall-clock time.
9. Docker cold start is seconds, not milliseconds. Do NOT claim sub-second Docker cold starts.
10. Deno permission flags are --allow-net, --allow-read, etc. Do NOT fabricate flag names.
11. The scaffold recommendation is Docker because it matches existing infrastructure.
12. Do NOT claim any approach is "best" overall -- each has trade-offs.

## Alt Text

Three-column comparison of MCP sandbox isolation patterns: Cloudflare Workers with V8 isolates and sub-millisecond cold start but JavaScript only, Docker containers with any language support but seconds cold start, and Deno sandbox with granular permissions but TypeScript only, with Docker recommended for the scaffold.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Three MCP sandbox isolation patterns compared with Docker recommended for the scaffold.](docs/figures/repo-figures/assets/fig-repo-28-sandbox-isolation.jpg)

*Figure 28. MCP sandbox isolation patterns: Cloudflare Workers, Docker containers, and Deno sandbox compared across latency, language support, and isolation strength.*

### From this figure plan (relative)

![MCP sandbox isolation patterns](../assets/fig-repo-28-sandbox-isolation.jpg)

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided
- [x] Audience level correct (L3)
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
