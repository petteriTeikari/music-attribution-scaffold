# fig-domain-04: Trust Tiers Explained

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-domain-04 |
| **Title** | Three-Tier Trust Model for Music Attribution |
| **Audience** | Domain (music industry decision-makers) |
| **Complexity** | L1 (concept explanation) |
| **Location** | docs/prd/mcp-server-prd.md, docs/knowledge-base/domain/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |

## Purpose

Explain the three-tier access model in business terms: who gets access to what, and why this protects artist data while enabling collaboration.

## Key Message

"Three trust tiers ensure your data is protected: Internal (system apps), Verified (trusted partners like Mogen), and Public (unknown AI with limited access)."

## Visual Concept

Pyramid or layered diagram showing three tiers with business-friendly descriptions.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  THREE-TIER TRUST MODEL                                                      │
│  Protecting Artist Data While Enabling Collaboration                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                        ┌─────────────────────────┐                          │
│                        │      TIER 1: INTERNAL   │                          │
│                        │         (Blue)          │                          │
│                        │                         │                          │
│                        │  System Apps          │                          │
│                        │  • Full access          │                          │
│                        │  • Read + Write + Admin │                          │
│                        │  • No rate limits       │                          │
│                        └───────────┬─────────────┘                          │
│                                    │                                        │
│                    ┌───────────────┴───────────────┐                        │
│                    │      TIER 2: VERIFIED         │                        │
│                    │          (Gold)               │                        │
│                    │                               │                        │
│                    │  Trusted Partners (Mogen)     │                        │
│                    │  • Read + Edit own data       │                        │
│                    │  • 1000 requests/minute       │                        │
│                    │  • Audit trail required       │                        │
│                    └───────────────┬───────────────┘                        │
│                                    │                                        │
│        ┌───────────────────────────┴───────────────────────────┐            │
│        │                  TIER 3: PUBLIC                        │            │
│        │                    (Gray)                              │            │
│        │                                                        │            │
│        │  Unknown AI Platforms & Third Parties                  │            │
│        │  • Read-only access                                    │            │
│        │  • 100 requests/minute                                 │            │
│        │  • Anonymized data (protects artist identity)          │            │
│        │  • No write access                                     │            │
│        └────────────────────────────────────────────────────────┘            │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  WHY THIS MATTERS: Your data stays protected. Partners you trust get more   │
│  access. Unknown AI gets just enough to be useful—nothing more.             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Tier 1: Internal | `tier_internal` | Full access, system apps |
| Tier 2: Verified | `tier_verified` | Trusted partners, scoped access |
| Tier 3: Public | `tier_public` | Unknown clients, restricted |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Internal | Verified | Contains | "more restricted" |
| Verified | Public | Contains | "most restricted" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "WHY THIS MATTERS" | Your data stays protected. Partners get access. Unknown AI gets just enough. | Bottom |

## Text Content

### Labels (Max 30 chars each)

- "TIER 1: INTERNAL"
- "System Apps"
- "Full access, no limits"
- "TIER 2: VERIFIED"
- "Trusted Partners (Mogen)"
- "Read + Edit, 1000 req/min"
- "TIER 3: PUBLIC"
- "Unknown AI Platforms"
- "Read-only, 100 req/min"
- "Anonymized data"

### Caption (for embedding)

Three-tier trust model: Internal (system apps) gets full access, Verified partners (Mogen) get read + scoped edit with audit trails, Public (unknown AI) gets read-only anonymized data with strict rate limits. Your data is protected while enabling collaboration with trusted partners.

## Prompts for Nano Banana Pro

### Style Prompt

Trust tier pyramid diagram on warm off-white background (#F8F6F0).
Three stacked layers, narrowest at top (Internal), widest at bottom (Public).
Deep blue for Internal tier, warm gold for Verified tier, gray for Public tier.
Clean sans-serif typography, business-friendly tone.
Each tier shows: who, what access, limits.
Professional, reassuring aesthetic—this protects your data.

### Content Prompt

Create a three-tier trust pyramid:
- TOP (smallest): TIER 1 INTERNAL (deep blue)
  - "System Apps"
  - Bullet: Full access, Read + Write + Admin, No rate limits
- MIDDLE: TIER 2 VERIFIED (warm gold)
  - "Trusted Partners (Mogen)"
  - Bullet: Read + Edit own data, 1000 req/min, Audit trail required
- BOTTOM (widest): TIER 3 PUBLIC (gray)
  - "Unknown AI Platforms & Third Parties"
  - Bullet: Read-only, 100 req/min, Anonymized data, No write access
- FOOTER: "Why This Matters" callout with reassuring message

### Refinement Notes

- Pyramid should feel stable and protective
- Blue/gold/gray colors clearly distinguish tiers
- Business-friendly language (not technical jargon)
- Emphasize protection while enabling collaboration

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "domain-04",
    "title": "Three-Tier Trust Model for Music Attribution",
    "audience": "domain"
  },
  "content_architecture": {
    "primary_message": "Three trust tiers protect your data while enabling collaboration",
    "layout_flow": "pyramid-top-to-bottom",
    "key_structures": [
      {
        "name": "Tier 1: Internal",
        "role": "tier_internal",
        "is_highlighted": true,
        "labels": ["System Apps", "Full access", "No limits"]
      },
      {
        "name": "Tier 2: Verified",
        "role": "tier_verified",
        "is_highlighted": true,
        "labels": ["Trusted Partners", "Read + Edit", "1000 req/min"]
      },
      {
        "name": "Tier 3: Public",
        "role": "tier_public",
        "is_highlighted": false,
        "labels": ["Unknown AI", "Read-only", "100 req/min", "Anonymized"]
      }
    ],
    "callout_boxes": [
      {
        "heading": "WHY THIS MATTERS",
        "body_text": "Your data stays protected. Partners you trust get more access. Unknown AI gets just enough—nothing more.",
        "position": "bottom-full-width"
      }
    ]
  }
}
```

## Alt Text

Three-tier trust pyramid: Tier 1 Internal (blue, top) for the system apps with full access. Tier 2 Verified (gold, middle) for trusted partners with read/edit and rate limits. Tier 3 Public (gray, bottom) for unknown AI with read-only anonymized access.

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Embedded in documentation
