# fig-repo-22: MCP-Guard Three-Stage Defense Pipeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-22 |
| **Title** | MCP-Guard Three-Stage Defense Pipeline |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/mcp-security-production-research.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Show engineers the MCP-Guard three-stage defense pipeline architecture — how requests flow through static scanning (<2ms), neural classification (<50ms, 96.01% accuracy), and LLM arbiter (~500ms, 89.07% F1) — with the key insight that 95% of requests never reach Stage 3.

## Key Message

MCP-Guard's cascading architecture handles 95% of requests in under 50ms while achieving 96.01% detection accuracy — security without latency sacrifice.

## Visual Concept

Split-panel layout with a vertical pipeline flow on the left showing three cascading stages with latency and accuracy metrics, and block/pass routing at each stage. A callout bar at the bottom highlights the 12x speedup over LLM-only approaches.

```
+-----------------------------------------------------------------------+
|  MCP-GUARD THREE-STAGE DEFENSE                                         |
|  ■ Cascading Security Pipeline                                         |
+-----------------------------------------------------------------------+
|                                                                        |
|  INCOMING REQUEST                                                      |
|       │                                                                |
|       ▼                                                                |
|  ┌─────────────────┐                                                   |
|  │ STAGE 1: STATIC │  < 2ms latency                                   |
|  │ Pattern matching │  95% of attacks caught                           |
|  │ SQL/cmd inject   │                                                   |
|  └────────┬────────┘                                                   |
|           │ PASS                     ╳ BLOCK                           |
|           ▼                                                            |
|  ┌─────────────────┐                                                   |
|  │ STAGE 2: NEURAL │  < 50ms latency                                  |
|  │ Transformer clf  │  96.01% accuracy                                 |
|  │ Novel patterns   │  3.2% false positive                             |
|  └────────┬────────┘                                                   |
|           │ AMBIGUOUS (~5%)          ╳ BLOCK                           |
|           ▼                                                            |
|  ┌─────────────────┐                                                   |
|  │ STAGE 3: LLM    │  ~500ms latency                                  |
|  │ Semantic analysis │  89.07% F1                                      |
|  │ Full evaluation  │  Only 5% of reqs                                 |
|  └────────┬────────┘                                                   |
|           │ PASS                     ╳ BLOCK                           |
|           ▼                                                            |
|  ┌─────────────────┐                                                   |
|  │ TOOL EXECUTION  │                                                   |
|  └─────────────────┘                                                   |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  12× faster than LLM-only approaches (Shan et al. 2025)       │   |
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
    content: "MCP-GUARD THREE-STAGE DEFENSE"
    role: title

  - id: pipeline_zone
    bounds: [80, 140, 1760, 760]
    role: pipeline_flow

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    role: callout_box

anchors:
  - id: incoming_request
    position: [480, 150]
    size: [960, 40]
    role: data_flow
    label: "INCOMING REQUEST"

  - id: stage_1_static
    position: [480, 220]
    size: [560, 140]
    role: processing_stage
    label: "STAGE 1: STATIC"

  - id: stage_1_metrics
    position: [1100, 220]
    size: [400, 140]
    role: data_flow
    label: "< 2ms, 95% caught"

  - id: stage_1_block
    position: [1100, 280]
    size: [200, 40]
    role: security_layer
    label: "BLOCK"

  - id: flow_1_to_2
    from: stage_1_static
    to: stage_2_neural
    type: arrow
    label: "PASS"

  - id: stage_2_neural
    position: [480, 400]
    size: [560, 140]
    role: processing_stage
    label: "STAGE 2: NEURAL"

  - id: stage_2_metrics
    position: [1100, 400]
    size: [400, 140]
    role: data_flow
    label: "< 50ms, 96.01% accuracy, 3.2% FP"

  - id: stage_2_block
    position: [1100, 460]
    size: [200, 40]
    role: security_layer
    label: "BLOCK"

  - id: flow_2_to_3
    from: stage_2_neural
    to: stage_3_llm
    type: arrow
    label: "AMBIGUOUS (~5%)"

  - id: stage_3_llm
    position: [480, 580]
    size: [560, 140]
    role: processing_stage
    label: "STAGE 3: LLM"

  - id: stage_3_metrics
    position: [1100, 580]
    size: [400, 140]
    role: data_flow
    label: "~500ms, 89.07% F1, 5% of reqs"

  - id: stage_3_block
    position: [1100, 640]
    size: [200, 40]
    role: security_layer
    label: "BLOCK"

  - id: flow_3_to_exec
    from: stage_3_llm
    to: tool_execution
    type: arrow
    label: "PASS"

  - id: tool_execution
    position: [480, 780]
    size: [560, 80]
    role: processing_stage
    label: "TOOL EXECUTION"

  - id: callout_bar
    position: [80, 940]
    size: [1760, 100]
    role: callout_box
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Incoming Request | `data_flow` | Entry point for all MCP tool calls |
| Stage 1: Static Scanner | `processing_stage` | Pattern matching for SQL/command injection, <2ms |
| Stage 2: Neural Classifier | `processing_stage` | Transformer-based classification, 96.01% accuracy, <50ms |
| Stage 3: LLM Arbiter | `processing_stage` | Full semantic analysis, 89.07% F1, ~500ms |
| Tool Execution | `processing_stage` | Approved request reaches actual tool |
| Block actions | `security_layer` | Rejected requests at each stage |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Incoming Request | Stage 1 | arrow | "all requests" |
| Stage 1 | Stage 2 | arrow | "PASS" |
| Stage 1 | Block | arrow | "BLOCK" |
| Stage 2 | Stage 3 | arrow | "AMBIGUOUS (~5%)" |
| Stage 2 | Block | arrow | "BLOCK" |
| Stage 3 | Tool Execution | arrow | "PASS" |
| Stage 3 | Block | arrow | "BLOCK" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PERFORMANCE" | 12x faster than LLM-only approaches (Shan et al. 2025) | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "INCOMING REQUEST"
- Label 2: "STAGE 1: STATIC"
- Label 3: "STAGE 2: NEURAL"
- Label 4: "STAGE 3: LLM"
- Label 5: "TOOL EXECUTION"
- Label 6: "< 2ms latency"
- Label 7: "< 50ms latency"
- Label 8: "~500ms latency"
- Label 9: "96.01% accuracy"
- Label 10: "89.07% F1"
- Label 11: "3.2% false positive"
- Label 12: "Only 5% of requests"
- Label 13: "PASS"
- Label 14: "BLOCK"

### Caption (for embedding in documentation)

MCP-Guard three-stage cascading defense pipeline achieving 96.01% detection accuracy with 95% of requests resolved in under 50ms, 12x faster than LLM-only approaches.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color.
5. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 22." or any numbered academic caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. Stage 2 accuracy is 96.01% — from MCP-Guard (Shan et al. 2025). Do NOT round to 96%.
9. Stage 3 F1 score is 89.07%. Do NOT confuse with accuracy.
10. 12x speedup is vs LLM-only approaches, NOT vs no validation.
11. The "5% reach Stage 3" is from the MCP-Guard paper. Do NOT fabricate other percentage breakdowns.
12. False positive rate is 3.2% for Stage 2.

## Alt Text

MCP-Guard three-stage defense pipeline: Stage 1 static scanner under 2ms, Stage 2 neural classifier at 96.01 percent accuracy under 50ms, Stage 3 LLM arbiter at 89.07 percent F1 for the 5 percent of ambiguous requests, achieving 12x speedup over LLM-only approaches.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![MCP-Guard three-stage defense pipeline with cascading latency and accuracy metrics.](docs/figures/repo-figures/assets/fig-repo-22-mcp-guard-three-stage.jpg)

*Figure 22. MCP-Guard three-stage cascading defense pipeline from Shan et al. 2025, achieving 96.01% accuracy with 12x speedup.*

### From this figure plan (relative)

![MCP-Guard three-stage defense](../assets/fig-repo-22-mcp-guard-three-stage.jpg)

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
