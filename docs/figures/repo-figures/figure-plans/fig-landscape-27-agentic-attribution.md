# fig-landscape-27: Agentic Music Attribution: When AI Agents Query & Pay

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-27 |
| **Title** | Agentic Music Attribution: When AI Agents Query & Pay |
| **Audience** | L3 (Engineer) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

This figure shows how machine-to-machine consent infrastructure will automate music attribution -- from an AI agent's intent to use music, through permission queries, agent coordination, royalty negotiation, to automatic payment. It connects the manuscript's protocol analysis (MCP/A2A/ACP) to a concrete music attribution workflow and illustrates the "bowling-shoe vs BYO" agent archetype distinction.

## Key Message

MCP permission queries + A2A agent coordination + ACP royalty negotiation = machine-to-machine consent infrastructure where AI agents autonomously query, license, and pay for music usage.

## Visual Concept

A left-to-right flowchart showing the agentic attribution pipeline. An AI agent on the far left initiates the flow. Three protocol layers (MCP, A2A, ACP) are stacked vertically in the center, each handling a different aspect of the transaction. The flow converges to automatic payment on the right. Above the main flow, a "bowling-shoe vs BYO" archetype comparison shows two agent models. Below, a timeline showing when this becomes reality.

```
+---------------------------------------------------------------+
|  AGENTIC MUSIC ATTRIBUTION                                     |
|  ■ When AI Agents Query, License, and Pay Autonomously         |
+---------------------------------------------------------------+
|                                                                |
|  AGENT ARCHETYPES                                              |
|  ┌──────────────┐        ┌──────────────┐                      |
|  │ BOWLING-SHOE │        │ BYO (BRING   │                      |
|  │ Platform owns │        │ YOUR OWN)    │                      |
|  │ the agent     │        │ User owns    │                      |
|  │ (Spotify, YT) │        │ the agent    │                      |
|  └──────────────┘        └──────────────┘                      |
|         ■                                                      |
|  ATTRIBUTION FLOW                                              |
|                                                                |
|  ┌────────┐    ┌──────────────────────────────┐   ┌────────┐  |
|  │  AI    │    │  THREE PROTOCOL LAYERS        │   │ AUTO   │  |
|  │ AGENT  │    │                                │   │ PAY-   │  |
|  │        │    │  MCP ─── Permission/Consent    │   │ MENT   │  |
|  │ Intent:│───▶│  "Can I use this track for X?" │──▶│        │  |
|  │ "Use   │    │                                │   │ Micro- │  |
|  │ track  │    │  A2A ─── Agent Coordination    │   │ payment│  |
|  │ for X" │    │  Rights holder's agent agrees   │   │ to     │  |
|  │        │    │                                │   │ rights │  |
|  │        │    │  ACP ─── Commerce/Payment      │   │ holder │  |
|  │        │    │  Negotiates royalty terms       │   │        │  |
|  └────────┘    └──────────────────────────────┘   └────────┘  |
|                                                                |
|  PERMISSION SERVER                                             |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │ Checks: A0-A3 assurance │ Licensing terms │ Usage scope  │   |
|  └─────────────────────────────────────────────────────────┘   |
|                                                                |
|  ■ THE FUTURE: Attribution is AUTOMATED, not manual            |
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
      text: "AGENTIC MUSIC ATTRIBUTION"
    - type: label_editorial
      text: "When AI Agents Query, License, and Pay Autonomously"

archetype_section:
  position: [60, 140]
  width: 1800
  height: 160
  elements:
    - type: label_editorial
      text: "AGENT ARCHETYPES"

archetype_bowling:
  position: [60, 180]
  width: 400
  height: 100
  label: "BOWLING-SHOE"
  elements:
    - { type: data_mono, text: "Platform owns the agent" }
    - { type: data_mono, text: "Spotify, YouTube Music, Apple Music" }
    - { type: label_editorial, text: "Constrained permissions, platform-scoped" }

archetype_byo:
  position: [520, 180]
  width: 400
  height: 100
  label: "BYO (BRING YOUR OWN)"
  elements:
    - { type: data_mono, text: "User owns the agent" }
    - { type: data_mono, text: "Personal AI assistant, custom agent" }
    - { type: label_editorial, text: "Broad permissions, user-scoped" }

flow_agent:
  position: [60, 340]
  width: 300
  height: 340
  label: "AI AGENT"
  elements:
    - { type: heading_display, text: "Intent" }
    - { type: data_mono, text: "Use track for purpose X" }
    - { type: data_mono, text: "Context: platform, audience, duration" }

flow_protocols:
  position: [420, 340]
  width: 1000
  height: 340
  label: "THREE PROTOCOL LAYERS"
  elements:
    - type: processing_stage
      text: "MCP — Permission/Consent"
      detail: "Machine-readable permission query: Can I use this track for X?"
      y_offset: 0
    - type: processing_stage
      text: "A2A — Agent Coordination"
      detail: "Rights holder's agent reviews, negotiates, agrees/declines"
      y_offset: 120
    - type: processing_stage
      text: "ACP — Commerce/Payment"
      detail: "Negotiates royalty terms: rate, duration, territory, exclusivity"
      y_offset: 240

flow_payment:
  position: [1480, 340]
  width: 300
  height: 340
  label: "AUTOMATIC PAYMENT"
  elements:
    - { type: heading_display, text: "Micro-payment" }
    - { type: data_mono, text: "To rights holder(s)" }
    - { type: data_mono, text: "Proportional split via Shapley" }
    - { type: data_mono, text: "Logged to provenance chain" }

permission_server:
  position: [60, 720]
  width: 1800
  height: 80
  label: "PERMISSION SERVER"
  elements:
    - { type: data_mono, text: "Checks: A0-A3 assurance level" }
    - { type: data_mono, text: "Licensing terms: CC, commercial, sync" }
    - { type: data_mono, text: "Usage scope: territory, duration, medium" }

insight_callout:
  position: [60, 830]
  width: 1800
  height: 50
  elements:
    - type: callout_bar
      text: "THE FUTURE: Attribution is AUTOMATED, not manual -- agents handle consent, licensing, and payment"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "AGENTIC MUSIC ATTRIBUTION" with coral accent square |
| Subtitle | `label_editorial` | "When AI Agents Query, License, and Pay Autonomously" |
| Bowling-shoe archetype | `archetype_overlay` | Platform-owned agent model (Spotify, YouTube) |
| BYO archetype | `archetype_overlay` | User-owned agent model (personal AI assistant) |
| AI agent node | `stakeholder_platform` | Initiating agent with usage intent |
| MCP protocol layer | `api_endpoint` | Permission/consent query protocol |
| A2A protocol layer | `api_endpoint` | Agent-to-agent coordination protocol |
| ACP protocol layer | `api_endpoint` | Commerce/payment negotiation protocol |
| Payment node | `data_flow` | Automatic micro-payment to rights holders |
| Permission server | `security_layer` | Checks assurance level, licensing, usage scope |
| Insight callout | `callout_bar` | "Attribution is AUTOMATED, not manual" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| AI Agent | MCP layer | request | "Permission query" |
| MCP layer | Permission server | validation | "Check assurance + terms" |
| Permission server | A2A layer | response | "Permission granted/denied" |
| A2A layer | ACP layer | handoff | "Agent agreement → negotiate terms" |
| ACP layer | Payment | execution | "Terms agreed → auto-pay" |
| Payment | Provenance chain | logging | "Transaction logged" |
| Bowling-shoe | Constrained flow | archetype | "Platform-scoped permissions" |
| BYO | Full flow | archetype | "User-scoped permissions" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Protocol Stack | "MCP (consent) + A2A (coordination) + ACP (commerce) = full attribution automation" | Center, above protocol layers |
| Archetype Distinction | "Bowling-shoe: platform decides; BYO: user decides -- same protocols, different trust models" | Top right |
| Oracle Problem | "Digital permission does not guarantee physical reality -- design for deterrence, not detection" | Bottom right |

## Text Content

### Labels (Max 30 chars each)

- AI Agent
- Permission Query
- MCP Permission/Consent
- A2A Agent Coordination
- ACP Commerce/Payment
- Automatic Payment
- Bowling-Shoe Archetype
- BYO (Bring Your Own)
- Permission Server
- A0-A3 Assurance Check
- Licensing Terms
- Usage Scope
- Micro-payment
- Rights Holder
- Provenance Chain

### Caption (for embedding in documentation)

Agentic music attribution automates the full consent-license-pay cycle through three protocol layers: MCP handles machine-readable permission queries ("Can I use this track for X?"), A2A coordinates between the requesting agent and the rights holder's agent, and ACP negotiates royalty terms and triggers automatic micro-payment. Two agent archetypes -- bowling-shoe (platform-owned) and BYO (user-owned) -- traverse the same protocol stack with different trust models.

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

1. MCP, A2A, and ACP are SPECIFIC protocols -- do NOT generalize to "APIs" or "web services."
2. The flow is LEFT-TO-RIGHT, not circular -- it shows a single transaction, not a feedback loop.
3. Bowling-shoe and BYO are MANUSCRIPT-DEFINED archetypes -- do NOT invent other archetype names.
4. The permission server checks A0-A3 assurance levels -- do NOT simplify to "checks permissions."
5. Payment is AUTOMATIC micro-payment -- do NOT show manual invoicing or batch settlement.
6. Do NOT imply this system exists today -- it is a FUTURE architecture based on emerging protocols.
7. Do NOT show blockchain as a required component -- the provenance chain is protocol-agnostic.
8. Do NOT conflate A2A with MCP -- they serve different functions (coordination vs. consent).

## Alt Text

Agentic attribution flowchart: AI agent queries MCP, coordinates via A2A, pays via ACP automatically.

## JSON Export Block

```json
{
  "id": "fig-landscape-27",
  "title": "Agentic Music Attribution: When AI Agents Query & Pay",
  "audience": "L3",
  "priority": "P1",
  "layout": "C",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Speculate",
  "novelty": 4,
  "protocols": [
    {
      "name": "MCP",
      "function": "Permission/Consent",
      "query": "Can I use this track for X purpose?",
      "manuscript_ref": "Music Attribution primary"
    },
    {
      "name": "A2A",
      "function": "Agent-to-Agent Coordination",
      "query": "Rights holder's agent reviews and agrees",
      "manuscript_ref": "AI Passport v1"
    },
    {
      "name": "ACP",
      "function": "Commerce/Payment",
      "query": "Negotiate royalty terms and trigger payment",
      "manuscript_ref": "AI Passport v1"
    }
  ],
  "archetypes": [
    { "name": "Bowling-Shoe", "owner": "Platform", "examples": ["Spotify", "YouTube Music"] },
    { "name": "BYO", "owner": "User", "examples": ["Personal AI assistant", "Custom agent"] }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "archetype_overlay", "stakeholder_platform",
    "api_endpoint", "data_flow", "security_layer", "callout_bar", "processing_stage"
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
