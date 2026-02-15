# fig-repo-20: MCP Attack Surface Taxonomy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-20 |
| **Title** | MCP Attack Surface Taxonomy: Six Vectors, One Protocol |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/mcp-security-production-research.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Provide engineers with a comprehensive taxonomy of MCP attack vectors, showing the six primary attack types (tool poisoning, cross-server contamination, supply chain compromise, prompt injection via tools, rug pull attacks, path traversal) with their measured ASR ranges from research benchmarks.

## Key Message

MCP has six distinct attack vectors with ASR ranging from 16.7% to 85%+ — defense must address all six, not just the obvious ones.

## Visual Concept

Hero layout with a 2x3 grid of attack vector cards, each showing attack type, measured ASR, and source benchmark. A callout bar at the bottom reinforces the systemic nature of the threat landscape.

```
+-----------------------------------------------------------------------+
|  MCP ATTACK SURFACE TAXONOMY                                           |
|  ■ Six Vectors, One Protocol                                           |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                 |
|  │ TOOL         │  │ CROSS-SERVER │  │ SUPPLY CHAIN │                 |
|  │ POISONING    │  │ CONTAMINATE  │  │ COMPROMISE   │                 |
|  │ 72.8% ASR    │  │ 85%+ ASR     │  │ 16.7-64.7%   │                 |
|  │ MCPTox       │  │ MCPSecBench  │  │ Guo et al.   │                 |
|  └──────────────┘  └──────────────┘  └──────────────┘                 |
|                                                                        |
|  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                 |
|  │ PROMPT       │  │ RUG PULL     │  │ PATH         │                 |
|  │ INJECTION    │  │ ATTACKS      │  │ TRAVERSAL    │                 |
|  │ 40.71% avg   │  │ Variable     │  │ 22% servers  │                 |
|  │ MSB          │  │ MCPSecBench  │  │ MSB          │                 |
|  └──────────────┘  └──────────────┘  └──────────────┘                 |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  All six vectors active in production — 85% of servers lack    │   |
|  │  adequate authentication (Guo et al. 2025)                     │   |
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
    content: "MCP ATTACK SURFACE TAXONOMY"
    role: title

  - id: grid_zone
    bounds: [80, 160, 1760, 680]
    role: content_grid

  - id: callout_zone
    bounds: [80, 900, 1760, 120]
    role: callout_box

anchors:
  - id: vector_tool_poisoning
    position: [120, 200]
    size: [520, 260]
    role: security_layer

  - id: vector_cross_server
    position: [700, 200]
    size: [520, 260]
    role: security_layer

  - id: vector_supply_chain
    position: [1280, 200]
    size: [520, 260]
    role: security_layer

  - id: vector_prompt_injection
    position: [120, 520]
    size: [520, 260]
    role: security_layer

  - id: vector_rug_pull
    position: [700, 520]
    size: [520, 260]
    role: security_layer

  - id: vector_path_traversal
    position: [1280, 520]
    size: [520, 260]
    role: security_layer

  - id: callout_bar
    position: [80, 900]
    size: [1760, 120]
    role: callout_box
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Tool Poisoning | `security_layer` | Hidden instructions in tool descriptions, 72.8% ASR (MCPTox) |
| Cross-Server Contamination | `security_layer` | Multi-server context manipulation, 85%+ ASR (MCPSecBench) |
| Supply Chain Compromise | `security_layer` | Malicious tool packages, 16.7-64.7% ASR (Guo et al.) |
| Prompt Injection via Tools | `security_layer` | Adversarial instructions in tool responses, 40.71% avg (MSB) |
| Rug Pull Attacks | `security_layer` | Post-approval tool behavior changes, variable ASR (MCPSecBench) |
| Path Traversal | `security_layer` | File system access beyond allowed scope, 22% of servers (MSB) |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| All six vectors | Callout bar | grouping | "all active in production" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "SYSTEMIC RISK" | All six vectors active in production — 85% of servers lack adequate authentication (Guo et al. 2025) | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "TOOL POISONING"
- Label 2: "CROSS-SERVER CONTAMINATION"
- Label 3: "SUPPLY CHAIN COMPROMISE"
- Label 4: "PROMPT INJECTION"
- Label 5: "RUG PULL ATTACKS"
- Label 6: "PATH TRAVERSAL"
- Label 7: "72.8% ASR"
- Label 8: "85%+ ASR"
- Label 9: "16.7-64.7% ASR"
- Label 10: "40.71% avg ASR"
- Label 11: "Variable ASR"
- Label 12: "22% of servers"

### Caption (for embedding in documentation)

MCP attack surface taxonomy showing six distinct attack vectors with measured success rates from MCPTox, MCPSecBench, MSB, and Guo et al. 2025 benchmarks.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color.
5. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 20." or any numbered academic caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. Tool poisoning 72.8% ASR is from MCPTox (Zhang et al. 2025). Do NOT attribute to other benchmarks.
9. 85%+ compromise is from MCPSecBench (Cheng et al. 2025), NOT from MSB.
10. 40.71% average ASR is from MSB (Peng et al. 2025), covering 984 test cases across nine models.
11. Supply chain ASR range 16.7-64.7% is from Guo et al. 2025.
12. 22% path traversal prevalence is from MSB.
13. Do NOT show specific company or model names as targets.

## Alt Text

MCP attack surface taxonomy showing six attack vectors with measured success rates: tool poisoning at 72.8 percent, cross-server contamination at 85-plus percent, supply chain compromise at 16 to 65 percent, prompt injection at 40.71 percent average, rug pull attacks at variable rates, and path traversal affecting 22 percent of servers.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![MCP attack surface taxonomy showing six attack vectors with measured success rates from research benchmarks.](docs/figures/repo-figures/assets/fig-repo-20-mcp-attack-taxonomy.jpg)

*Figure 20. MCP attack surface taxonomy mapping six distinct vectors with ASR ranges from MCPTox, MCPSecBench, MSB, and Guo et al. 2025.*

### From this figure plan (relative)

![MCP attack surface taxonomy](../assets/fig-repo-20-mcp-attack-taxonomy.jpg)

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided
- [x] Audience level correct (L3)
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
