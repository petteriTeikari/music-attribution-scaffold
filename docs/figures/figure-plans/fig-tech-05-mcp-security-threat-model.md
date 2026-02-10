# fig-tech-05: MCP Security Threat Model

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-tech-05 |
| **Title** | MCP Security Threat Model |
| **Audience** | Technical (developers) |
| **Complexity** | L3 (detailed implementation) |
| **Location** | docs/prd/mcp-server-prd.md, docs/knowledge-base/technical/mcp/SYNTHESIS.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |

## Purpose

Visualize the four attack surfaces in MCP implementations and the system's defense-in-depth mitigation strategy, communicating the 40.71% attack success rate context.

## Key Message

"MCP implementations face 40.71% attack success rate across four attack surfaces—the system implements four-layer defense: authentication, validation, sandbox, audit."

## Visual Concept

Left-to-right flow showing attack surfaces being mitigated by defense layers.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MCP SECURITY THREAT MODEL                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ATTACK SURFACES                    DEFENSE LAYERS                          │
│   ──────────────                     ──────────────                          │
│                                                                             │
│   ┌────────────────┐                ┌────────────────┐                      │
│   │ Tool Manifest  │──┬─────────────▶│ Authentication │                      │
│   │ Prompt inject  │  │             │ OAuth 2.0      │                      │
│   └────────────────┘  │             └───────┬────────┘                      │
│                       │                     │                               │
│   ┌────────────────┐  │             ┌───────▼────────┐                      │
│   │ Communication  │──┼─────────────▶│ Input Valid.  │                      │
│   │ MITM, reg.     │  │             │ 3-stage detect │                      │
│   └────────────────┘  │             └───────┬────────┘                      │
│                       │                     │                               │
│   ┌────────────────┐  │             ┌───────▼────────┐                      │
│   │ Resource Access│──┼─────────────▶│ Capability    │                      │
│   │ Path traversal │  │             │ Sandbox        │                      │
│   └────────────────┘  │             └───────┬────────┘                      │
│                       │                     │                               │
│   ┌────────────────┐  │             ┌───────▼────────┐    ┌─────────────┐  │
│   │ Execution Env  │──┘             │ Audit Trail   │────▶│ Compliant   │  │
│   │ Code injection │                │ EU AI Act     │    │ Operation   │  │
│   └────────────────┘                └────────────────┘    └─────────────┘  │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ THREAT CONTEXT: 40.71% average attack success (MCPSecBench 2025)    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Tool Manifest Attack | `threat_surface` | Prompt injection via tool metadata |
| Communication Attack | `threat_surface` | MITM, unauthorized registration |
| Resource Access Attack | `threat_surface` | Path traversal, credential theft |
| Execution Env Attack | `threat_surface` | Code injection, escalation |
| Authentication Layer | `security_layer` | OAuth 2.0 + RFC 8707 |
| Validation Layer | `security_layer` | Three-stage detection pipeline |
| Sandbox Layer | `security_layer` | Capability-based permissions |
| Audit Layer | `security_layer` | EU AI Act compliance logging |
| Compliant Operation | `primary_pathway` | Secure request completion |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Tool Manifest | Authentication | dashed arrow | "blocked by" |
| Communication | Validation | dashed arrow | "blocked by" |
| Resource Access | Sandbox | dashed arrow | "blocked by" |
| Execution Env | Audit | dashed arrow | "blocked by" |
| Authentication | Validation | arrow | "passes to" |
| Validation | Sandbox | arrow | "passes to" |
| Sandbox | Audit | arrow | "passes to" |
| Audit | Compliant Operation | arrow | "completes" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THREAT CONTEXT" | 40.71% average attack success rate (MCPSecBench 2025) | Bottom center |

## Text Content

### Labels (Max 30 chars each)

- "Tool Manifest Injection"
- "Communication MITM"
- "Resource Path Traversal"
- "Execution Code Injection"
- "OAuth 2.0 + RFC 8707"
- "3-Stage Detection"
- "Capability Sandbox"
- "EU AI Act Audit Trail"
- "40.71% Attack Success Rate"

### Caption (for embedding)

MCP security threat model showing four attack surfaces (tool manifest, communication, resource access, execution) defended by four-layer architecture (authentication, validation, sandbox, audit). Based on MCPSecBench 2025 finding 40.71% average attack success rate.

## Prompts for Nano Banana Pro

### Style Prompt

Elegant security architecture diagram on warm off-white background (#F8F6F0).
Medical illustration quality, Economist-style data visualization.
Clean sans-serif typography with alert/warning accents for threat surfaces.
Left side shows red-tinted attack vectors, right side shows green-tinted defense layers.
Clear left-to-right flow from threats to mitigations to safe operation.
Professional security documentation aesthetic, not alarming.

### Content Prompt

Create a security threat model diagram showing:
- LEFT: Four attack surface boxes stacked vertically (red-tinted)
  - Tool Manifest (prompt injection)
  - Communication (MITM)
  - Resource Access (path traversal)
  - Execution Environment (code injection)
- CENTER: Four defense layer boxes (green-tinted, connected vertically)
  - Authentication (OAuth 2.0)
  - Input Validation (3-stage)
  - Capability Sandbox
  - Audit Trail (EU AI Act)
- RIGHT: "Compliant Operation" success state
- Dashed arrows from attacks to defense layers showing mitigation
- Solid arrows between defense layers showing request flow
- BOTTOM: Alert callout with "40.71% attack success rate" statistic

### Refinement Notes

- Attack surfaces should feel threatening but professional (not cartoon-scary)
- Defense layers should convey strength and completeness
- The 40.71% statistic should be prominent but not alarmist
- Flow should clearly show defense-in-depth concept

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "tech-05",
    "title": "MCP Security Threat Model",
    "audience": "technical"
  },
  "content_architecture": {
    "primary_message": "Four attack surfaces mitigated by four-layer defense, addressing 40.71% industry attack rate",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Tool Manifest Attack",
        "role": "threat_surface",
        "is_highlighted": false,
        "labels": ["Prompt Injection", "Metadata abuse"]
      },
      {
        "name": "Communication Attack",
        "role": "threat_surface",
        "is_highlighted": false,
        "labels": ["MITM", "Unauthorized registration"]
      },
      {
        "name": "Resource Access Attack",
        "role": "threat_surface",
        "is_highlighted": false,
        "labels": ["Path traversal", "Credential theft"]
      },
      {
        "name": "Execution Env Attack",
        "role": "threat_surface",
        "is_highlighted": false,
        "labels": ["Code injection", "Privilege escalation"]
      },
      {
        "name": "Authentication Layer",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["OAuth 2.0", "RFC 8707"]
      },
      {
        "name": "Validation Layer",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["Static scanner", "Neural detector", "LLM arbiter"]
      },
      {
        "name": "Sandbox Layer",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["Capability grants", "Time-limited"]
      },
      {
        "name": "Audit Layer",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["EU AI Act Art. 12", "Artist access"]
      },
      {
        "name": "Compliant Operation",
        "role": "primary_pathway",
        "is_highlighted": true,
        "labels": ["Secure", "Auditable"]
      }
    ],
    "relationships": [
      {"from": "Tool Manifest", "to": "Authentication", "type": "dashed", "label": "blocked by"},
      {"from": "Communication", "to": "Validation", "type": "dashed", "label": "blocked by"},
      {"from": "Resource Access", "to": "Sandbox", "type": "dashed", "label": "blocked by"},
      {"from": "Execution Env", "to": "Audit", "type": "dashed", "label": "blocked by"},
      {"from": "Authentication", "to": "Validation", "type": "arrow", "label": "passes"},
      {"from": "Validation", "to": "Sandbox", "type": "arrow", "label": "passes"},
      {"from": "Sandbox", "to": "Audit", "type": "arrow", "label": "passes"},
      {"from": "Audit", "to": "Compliant Operation", "type": "arrow", "label": "completes"}
    ],
    "callout_boxes": [
      {
        "heading": "THREAT CONTEXT",
        "body_text": "40.71% average attack success rate across MCP implementations (MCPSecBench 2025)",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Alt Text

Security diagram: Four MCP attack surfaces (tool manifest, communication, resource, execution) blocked by four defense layers (authentication, validation, sandbox, audit) producing compliant operation.

## Research Basis

- **[MCP Security Bench (MSB)](https://arxiv.org/abs/2510.15994)**: 40.71% average attack success rate across nine evaluated models
- **[MCPSecBench](https://arxiv.org/abs/2508.13220)**: 85%+ attacks compromise at least one platform; four attack surface taxonomy
- **[agentic-systems-research-2026-02-03.md](../../knowledge-base/technical/agentic-systems-research-2026-02-03.md)**: Section 2.1

## Status

- [x] Draft created
- [x] Content reviewed
- [x] Generated via Nano Banana Pro
- [x] Embedded in documentation
