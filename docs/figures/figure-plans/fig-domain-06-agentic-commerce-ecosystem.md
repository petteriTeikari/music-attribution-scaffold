# fig-domain-06: Attribution in Agentic Commerce Ecosystem

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-domain-06 |
| **Title** | Attribution in Agentic Commerce Ecosystem |
| **Audience** | Domain (music industry + AI platforms) |
| **Complexity** | L2 (overview) |
| **Location** | docs/knowledge-base/technical/mcp/SYNTHESIS.md, docs/prd/mcp-server-prd.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |

## Purpose

Position the system within the emerging agentic commerce protocol landscape, showing how MCP-based attribution data integrates with payment and verification protocols.

## Key Message

"AI agents will spend $2T by 2030—The system provides verified attribution data to prevent music rights hallucination across commerce protocols."

## Visual Concept

Protocol ecosystem with the system as verified data layer for music transactions.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ATTRIBUTION IN AGENTIC COMMERCE                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   PROTOCOL ECOSYSTEM                                                        │
│   ──────────────────                                                        │
│                                                                             │
│                    ┌─────────────────────────────────────┐                  │
│                    │         MCP FOUNDATION              │                  │
│                    │     (Model Context Protocol)        │                  │
│                    │                                     │                  │
│                    │  ┌───────────────────────────────┐  │                  │
│                    │  │    ATTRIBUTION MCP SERVER        │  │                  │
│                    │  │  • Attribution data           │  │                  │
│                    │  │  • Permission verification    │  │                  │
│                    │  │  • Provenance tracking        │  │                  │
│                    │  └───────────────────────────────┘  │                  │
│                    │                                     │                  │
│                    └────────────────┬────────────────────┘                  │
│                                     │                                       │
│          ┌──────────────────────────┼──────────────────────────┐           │
│          │                          │                          │            │
│          ▼                          ▼                          ▼            │
│   ┌─────────────┐           ┌─────────────┐           ┌─────────────┐      │
│   │    ACP      │           │    AP2      │           │    TAP      │      │
│   │  (OpenAI    │           │  (Google    │           │  (Visa      │      │
│   │  + Stripe)  │           │  Shopping)  │           │  Identity)  │      │
│   │             │           │             │           │             │      │
│   │ Payment     │           │ Commerce    │           │ Agent       │      │
│   │ orchestr.   │           │ actions     │           │ verification│      │
│   └─────────────┘           └─────────────┘           └─────────────┘      │
│          │                          │                          │            │
│          └──────────────────────────┼──────────────────────────┘           │
│                                     │                                       │
│                                     ▼                                       │
│                    ┌─────────────────────────────────────┐                  │
│                    │      AI MUSIC TRANSACTIONS          │                  │
│                    │  • License purchases                │                  │
│                    │  • Training data access             │                  │
│                    │  • Royalty distribution             │                  │
│                    └─────────────────────────────────────┘                  │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ MARKET: $2T agent commerce by 2030 (McKinsey) • 65% hallucination   │   │
│  │         rate without structured data (ACE Benchmark)                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| MCP Foundation | `protocol_layer` | Base protocol layer |
| the attribution MCP Server | `source_system` | The System integration point |
| ACP | `commerce_protocol` | OpenAI + Stripe payment |
| AP2 | `commerce_protocol` | Google shopping actions |
| TAP | `commerce_protocol` | Visa agent verification |
| AI Music Transactions | `use_case` | End applications |
| Market Context | `market_data` | $2T opportunity + hallucination risk |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| the attribution MCP Server | ACP | arrow | "attribution data" |
| the attribution MCP Server | AP2 | arrow | "permission checks" |
| the attribution MCP Server | TAP | arrow | "artist verification" |
| ACP | AI Music Transactions | arrow | "enables" |
| AP2 | AI Music Transactions | arrow | "enables" |
| TAP | AI Music Transactions | arrow | "verifies" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "MARKET CONTEXT" | $2T agent commerce by 2030; 65% hallucination rate without structured data | Bottom center |

## Text Content

### Labels (Max 30 chars each)

- "MCP Foundation"
- "the attribution MCP Server"
- "Attribution Data"
- "Permission Verification"
- "ACP (OpenAI + Stripe)"
- "AP2 (Google Shopping)"
- "TAP (Visa Identity)"
- "AI Music Transactions"
- "$2T by 2030"
- "65% Hallucination Rate"

### Caption (for embedding)

The system in agentic commerce ecosystem: MCP-based attribution data flows to commerce protocols (ACP, AP2, TAP) enabling verified AI music transactions. Market opportunity $2T by 2030; 65% hallucination rate without structured data (ACE Benchmark).

## Prompts for Nano Banana Pro

### Style Prompt

Professional ecosystem diagram on warm off-white background (#F8F6F0).
Economist-style data visualization with protocol logos/boxes.
Layered architecture showing MCP as foundation, commerce protocols above.
The system prominently positioned within MCP layer (deep blue branding).
Clean protocol boxes for ACP, AP2, TAP with provider names.
Business-focused aesthetic suitable for investor/partner presentations.

### Content Prompt

Create a protocol ecosystem diagram showing:
- TOP LAYER: Large "MCP Foundation" container
  - Inside: "the attribution MCP Server" box with bullets:
    - Attribution data
    - Permission verification
    - Provenance tracking
- MIDDLE LAYER: Three commerce protocol boxes
  - ACP (OpenAI + Stripe) - Payment orchestration
  - AP2 (Google Shopping) - Commerce actions
  - TAP (Visa Identity) - Agent verification
- BOTTOM: "AI Music Transactions" application layer
  - License purchases
  - Training data access
  - Royalty distribution
- Arrows flowing from the system down to each commerce protocol
- Arrows from commerce protocols to transactions
- CALLOUT: Market statistics ($2T, 65% hallucination)

### Refinement Notes

- The system should be visually prominent within MCP layer
- Protocol logos/names should be recognizable
- Flow should show the system as enabling layer
- Market statistics should emphasize opportunity + risk

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "domain-06",
    "title": "Attribution in Agentic Commerce Ecosystem",
    "audience": "domain"
  },
  "content_architecture": {
    "primary_message": "The system provides verified attribution data to commerce protocols, preventing hallucination in $2T market",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "MCP Foundation",
        "role": "protocol_layer",
        "is_highlighted": false,
        "labels": ["Model Context Protocol", "Foundation layer"]
      },
      {
        "name": "the attribution MCP Server",
        "role": "source_system",
        "is_highlighted": true,
        "labels": ["Attribution data", "Permission verification", "Provenance"]
      },
      {
        "name": "ACP",
        "role": "commerce_protocol",
        "is_highlighted": false,
        "labels": ["OpenAI + Stripe", "Payment orchestration"]
      },
      {
        "name": "AP2",
        "role": "commerce_protocol",
        "is_highlighted": false,
        "labels": ["Google Shopping", "Commerce actions"]
      },
      {
        "name": "TAP",
        "role": "commerce_protocol",
        "is_highlighted": false,
        "labels": ["Visa Identity", "Agent verification"]
      },
      {
        "name": "AI Music Transactions",
        "role": "use_case",
        "is_highlighted": true,
        "labels": ["License purchases", "Training data", "Royalties"]
      },
      {
        "name": "Market Context",
        "role": "market_data",
        "is_highlighted": true,
        "labels": ["$2T by 2030", "65% hallucination", "McKinsey", "ACE Benchmark"]
      }
    ],
    "relationships": [
      {"from": "the attribution MCP Server", "to": "ACP", "type": "arrow", "label": "attribution"},
      {"from": "the attribution MCP Server", "to": "AP2", "type": "arrow", "label": "permissions"},
      {"from": "the attribution MCP Server", "to": "TAP", "type": "arrow", "label": "verification"},
      {"from": "ACP", "to": "AI Music Transactions", "type": "arrow", "label": "enables"},
      {"from": "AP2", "to": "AI Music Transactions", "type": "arrow", "label": "enables"},
      {"from": "TAP", "to": "AI Music Transactions", "type": "arrow", "label": "verifies"}
    ],
    "callout_boxes": [
      {
        "heading": "MARKET CONTEXT",
        "body_text": "$2T agent commerce by 2030 (McKinsey) • 65% hallucination rate without structured data (ACE Benchmark)",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Alt Text

Protocol ecosystem: the attribution MCP Server provides attribution data to commerce protocols (ACP, AP2, TAP) enabling verified AI music transactions. $2T market by 2030.

## Research Basis

- **[McKinsey (2025)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-commerce-opportunity-how-ai-agents-are-ushering-in-a-new-era-for-consumers-and-merchants)**: Agentic commerce opportunity - $1T US / $3-5T global by 2030
- **[ACE Benchmark (2025)](https://arxiv.org/abs/2512.04921)**: AI Consumer Index - top model achieves 56.1% on shopping tasks (significant hallucination on prices/links)
- **[agentic-systems-research-2026-02-03.md](../../knowledge-base/technical/agentic-systems-research-2026-02-03.md)**: Section 5

## Status

- [x] Draft created
- [x] Content reviewed
- [x] Generated via Nano Banana Pro
- [x] Embedded in documentation
