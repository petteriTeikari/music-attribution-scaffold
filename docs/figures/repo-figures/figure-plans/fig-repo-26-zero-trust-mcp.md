# fig-repo-26: Zero-Trust Architecture for MCP Deployments

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-26 |
| **Title** | Zero-Trust Architecture for MCP Deployments |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/mcp-security-production-research.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Show the zero-trust MCP architecture proposed by CSA/MIT -- contrasting the current trust-on-first-use model (left) with the target DID/VC model (right), including Agent Name Service for discovery.

## Key Message

Current MCP deployments use trust-on-first-use which enables supply chain attacks -- zero-trust with DID/VC provides cryptographic server identity but requires ecosystem maturation.

## Visual Concept

Split-panel layout: LEFT shows the current trust-on-first-use flow (client trusts server without verification, vulnerable to typosquatting). RIGHT shows the target zero-trust flow (client demands proof, Agent Name Service resolves DID, server presents Verifiable Credential). A callout bar at the bottom cites the <5% cryptographic verification statistic.

```
+-----------------------------------------------------------------------+
|  ZERO-TRUST ARCHITECTURE FOR MCP                                       |
|  ■ Current Model vs. Target Model                                      |
+-----------------------------------------------------------------------+
|                                                                        |
|  CURRENT: Trust-on-First-Use         TARGET: Zero-Trust DID/VC         |
|  ─────────────────────────           ──────────────────────            |
|                                                                        |
|  ┌─────────────────┐                ┌─────────────────┐               |
|  │ MCP Client      │                │ MCP Client      │               |
|  │ "I trust you"   │                │ "Prove identity" │               |
|  └────────┬────────┘                └────────┬────────┘               |
|           │                                  │                         |
|           v                                  v                         |
|  ┌─────────────────┐                ┌─────────────────┐               |
|  │ MCP Server      │                │ Agent Name Svc  │               |
|  │ Self-declared    │                │ DNS-like lookup  │               |
|  │ No verification  │                │ DID resolution   │               |
|  └─────────────────┘                └────────┬────────┘               |
|                                              │                         |
|  Vulnerability:                              v                         |
|  ┌─────────────────┐                ┌─────────────────┐               |
|  │ Typosquat server│                │ MCP Server      │               |
|  │ impersonates    │                │ Presents VC     │               |
|  │ legitimate one  │                │ Crypto verified  │               |
|  └─────────────────┘                └─────────────────┘               |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  <5% of servers verify identity cryptographically              │   |
|  │  (Guo et al. 2025)                                            │   |
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
    content: "ZERO-TRUST ARCHITECTURE FOR MCP"
    role: title

  - id: left_panel
    bounds: [80, 160, 840, 700]
    role: threat_panel

  - id: right_panel
    bounds: [1000, 160, 840, 700]
    role: solution_panel

  - id: callout_zone
    bounds: [80, 900, 1760, 120]
    role: callout_box

anchors:
  - id: current_client
    position: [160, 200]
    size: [680, 100]
    role: entity_box

  - id: current_server
    position: [160, 380]
    size: [680, 120]
    role: entity_box

  - id: current_vuln
    position: [160, 580]
    size: [680, 120]
    role: warning_box

  - id: target_client
    position: [1080, 200]
    size: [680, 100]
    role: entity_box

  - id: target_ans
    position: [1080, 380]
    size: [680, 120]
    role: entity_box

  - id: target_server
    position: [1080, 580]
    size: [680, 120]
    role: solution_component

  - id: flow_current_1
    from: current_client
    to: current_server
    type: arrow
    label: "trusts blindly"

  - id: flow_target_1
    from: target_client
    to: target_ans
    type: arrow
    label: "requests DID"

  - id: flow_target_2
    from: target_ans
    to: target_server
    type: arrow
    label: "resolves identity"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Current MCP Client | `entity_box` | Client that trusts server without verification |
| Current MCP Server | `entity_box` | Self-declared identity, no cryptographic proof |
| Typosquat vulnerability | `warning_box` | Attacker impersonates legitimate server |
| Target MCP Client | `entity_box` | Client demands identity proof before trust |
| Agent Name Service | `entity_box` | DNS-like lookup with DID resolution (proposed) |
| Target MCP Server | `solution_component` | Presents Verifiable Credential, cryptographically verified |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Current Client | Current Server | arrow | "trusts blindly" |
| Current Server | Typosquat vuln | dashed | "exploited by" |
| Target Client | Agent Name Svc | arrow | "requests DID" |
| Agent Name Svc | Target Server | arrow | "resolves identity" |
| Target Server | Target Client | dashed_return | "presents VC" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "VERIFICATION GAP" | Less than 5% of MCP servers verify identity cryptographically (Guo et al. 2025). Agent Name Service and MCP Server Cards are PROPOSALS, not deployed systems. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "CURRENT: Trust-on-First-Use"
- Label 2: "TARGET: Zero-Trust DID/VC"
- Label 3: "MCP Client"
- Label 4: "MCP Server"
- Label 5: "Agent Name Service"
- Label 6: "Verifiable Credential"
- Label 7: "Typosquat vulnerability"
- Label 8: "<5% crypto verification"

### Caption (for embedding in documentation)

Zero-trust MCP architecture contrasting current trust-on-first-use model with target DID/VC model, citing fewer than 5% of servers verifying identity cryptographically.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color.
5. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 26." or any numbered academic caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. DID = Decentralized Identifiers. VC = Verifiable Credentials. Both are W3C standards.
9. Agent Name Service is a PROPOSED concept, not a deployed system. Do NOT present it as existing infrastructure.
10. The <5% cryptographic verification statistic is from Guo et al. 2025. Do NOT attribute to other sources.
11. CSA = Cloud Security Alliance. The zero-trust proposal is a joint CSA/MIT effort.
12. MCP Server Cards are a MICROSOFT proposal, not part of the core MCP spec.
13. Do NOT show specific company names as vulnerable.

## Alt Text

Split-panel comparison of current trust-on-first-use MCP model versus target zero-trust architecture with Decentralized Identifiers, Verifiable Credentials, and Agent Name Service for cryptographic server identity verification, noting that fewer than 5 percent of servers currently verify identity cryptographically.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Zero-trust MCP architecture contrasting current trust-on-first-use with target DID/VC model.](docs/figures/repo-figures/assets/fig-repo-26-zero-trust-mcp.jpg)

*Figure 26. Zero-trust architecture for MCP: current trust-on-first-use model versus target DID/VC model with Agent Name Service.*

### From this figure plan (relative)

![Zero-trust MCP architecture](../assets/fig-repo-26-zero-trust-mcp.jpg)

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
