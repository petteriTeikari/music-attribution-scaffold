# fig-tech-02: MCP Server Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-tech-02 |
| **Title** | Three-Tier MCP Server Architecture |
| **Audience** | Technical (developers) |
| **Complexity** | L3 (detailed implementation) |
| **Location** | docs/prd/mcp-server-prd.md, docs/architecture/README.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |

## Purpose

Show the three-tier trust model for MCP server access, including OAuth flow, rate limits, and tool exposure per tier.

## Key Message

"Three access tiers (Internal, Verified, Public) with progressively restricted permissions ensure trusted collaboration while protecting artist data."

## Visual Concept

Layered tier diagram with client types on left, MCP server in center, and tools/permissions on right.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  THREE-TIER MCP SERVER ARCHITECTURE                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   CLIENTS                    MCP SERVER                    TOOLS            │
│   ───────                    ──────────                    ─────            │
│                                                                             │
│   ┌─────────────┐                                                           │
│   │  the system   │           ┌────────────────────┐        ┌─────────────┐  │
│   │    Apps     │──────────▶│                    │───────▶│ Full CRUD   │  │
│   │  (Internal) │   TIER 1  │                    │        │ No limits   │  │
│   └─────────────┘   Blue    │                    │        └─────────────┘  │
│                             │                    │                         │
│   ┌─────────────┐           │    OAuth 2.0 +    │        ┌─────────────┐  │
│   │   Mogen &   │──────────▶│    RFC 8707      │───────▶│ Read + Edit │  │
│   │  Partners   │   TIER 2  │   Resource       │        │ 1000/min    │  │
│   │ (Verified)  │   Gold    │   Indicators     │        └─────────────┘  │
│   └─────────────┘           │                    │                         │
│                             │                    │        ┌─────────────┐  │
│   ┌─────────────┐           │                    │───────▶│ Read-only   │  │
│   │  Unknown    │──────────▶│                    │        │ 100/min     │  │
│   │     AI      │   TIER 3  │                    │        │ Anonymized  │  │
│   │  (Public)   │   Gray    └────────────────────┘        └─────────────┘  │
│   └─────────────┘                                                           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  MCP TOOLS: get_artist_attribution | search_songs | verify_credit |         │
│             check_ai_permission | report_usage                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| System Apps | `tier_internal` | Internal clients, full access |
| Mogen & Partners | `tier_verified` | Verified partners, trusted |
| Unknown AI | `tier_public` | Public clients, restricted |
| MCP Server | `api_endpoint` | Central server with OAuth |
| Full CRUD | `confidence_high` | Green, no restrictions |
| Read + Edit | `confidence_medium` | Amber, rate limited |
| Read-only | `confidence_low` | Gray, heavily restricted |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| System Apps | MCP Server | Arrow | "TIER 1" |
| Mogen & Partners | MCP Server | Arrow | "TIER 2" |
| Unknown AI | MCP Server | Arrow | "TIER 3" |
| MCP Server | Full CRUD | Arrow | "internal" |
| MCP Server | Read + Edit | Arrow | "verified" |
| MCP Server | Read-only | Arrow | "public" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "MCP TOOLS" | get_artist_attribution, search_songs, verify_credit, check_ai_permission, report_usage | Bottom |

## Text Content

### Labels (Max 30 chars each)

- "System Apps"
- "Mogen & Partners"
- "Unknown AI Platforms"
- "OAuth 2.0 + RFC 8707"
- "Resource Indicators"
- "Full CRUD, No limits"
- "Read + Edit, 1000/min"
- "Read-only, 100/min"
- "Anonymized responses"

### Caption (for embedding)

Three-tier MCP server architecture: Internal (system apps) gets full CRUD access, Verified partners (Mogen) get read + scoped edit with 1000 req/min, Public (unknown AI) gets read-only anonymized data at 100 req/min. OAuth 2.0 with RFC 8707 Resource Indicators for fine-grained permissions.

## Prompts for Nano Banana Pro

### Style Prompt

Professional architecture diagram on warm off-white background (#F8F6F0).
Elegant scientific visualization style, clean sans-serif typography.
Three distinct tier levels shown as horizontal bands or stacked sections.
Deep blue for internal tier, warm gold for verified tier, gray for public tier.
Central MCP server box with OAuth badge. Organic flowing arrows.
Matte finish, subtle shadows, no glowing effects.

### Content Prompt

Create a three-tier access control diagram:
- LEFT COLUMN: Three client types stacked
  - Top: "System Apps" (deep blue box) - TIER 1
  - Middle: "Mogen & Partners" (gold box) - TIER 2
  - Bottom: "Unknown AI" (gray box) - TIER 3
- CENTER: MCP Server box
  - Shows "OAuth 2.0" and "RFC 8707 Resource Indicators"
- RIGHT COLUMN: Permission levels matching tiers
  - Top: "Full CRUD, No limits" (green)
  - Middle: "Read + Edit, 1000/min" (amber)
  - Bottom: "Read-only, 100/min, Anonymized" (gray)
- BOTTOM: Tool list callout

### Refinement Notes

- Tier colors should be clearly distinct (blue/gold/gray)
- Arrows from clients to server should show authentication flow
- Rate limits should be prominently displayed
- Tool names in monospace or code-style font

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "tech-02",
    "title": "Three-Tier MCP Server Architecture",
    "audience": "technical"
  },
  "content_architecture": {
    "primary_message": "Three access tiers with progressively restricted permissions",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "System Apps",
        "role": "tier_internal",
        "is_highlighted": true,
        "labels": ["Internal", "TIER 1"]
      },
      {
        "name": "Mogen & Partners",
        "role": "tier_verified",
        "is_highlighted": false,
        "labels": ["Verified", "TIER 2"]
      },
      {
        "name": "Unknown AI",
        "role": "tier_public",
        "is_highlighted": false,
        "labels": ["Public", "TIER 3"]
      },
      {
        "name": "MCP Server",
        "role": "api_endpoint",
        "is_highlighted": true,
        "labels": ["OAuth 2.0", "RFC 8707"]
      },
      {
        "name": "Full CRUD",
        "role": "confidence_high",
        "is_highlighted": false,
        "labels": ["No rate limit"]
      },
      {
        "name": "Read + Edit",
        "role": "confidence_medium",
        "is_highlighted": false,
        "labels": ["1000 req/min"]
      },
      {
        "name": "Read-only",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["100 req/min", "Anonymized"]
      }
    ],
    "relationships": [
      {"from": "System Apps", "to": "MCP Server", "type": "arrow", "label": "TIER 1"},
      {"from": "Mogen & Partners", "to": "MCP Server", "type": "arrow", "label": "TIER 2"},
      {"from": "Unknown AI", "to": "MCP Server", "type": "arrow", "label": "TIER 3"},
      {"from": "MCP Server", "to": "Full CRUD", "type": "arrow", "label": "internal"},
      {"from": "MCP Server", "to": "Read + Edit", "type": "arrow", "label": "verified"},
      {"from": "MCP Server", "to": "Read-only", "type": "arrow", "label": "public"}
    ],
    "callout_boxes": [
      {
        "heading": "MCP TOOLS",
        "body_text": "get_artist_attribution | search_songs | verify_credit | check_ai_permission | report_usage",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Alt Text

Three-tier MCP architecture: Internal tier (system apps) with full CRUD, Verified tier (Mogen partners) with read/edit at 1000/min, Public tier (unknown AI) with read-only at 100/min. OAuth 2.0 with RFC 8707 Resource Indicators.

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Embedded in documentation
