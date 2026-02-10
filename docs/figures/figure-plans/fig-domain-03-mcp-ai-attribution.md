# fig-domain-03: MCP for AI Attribution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-domain-03 |
| **Title** | MCP: Ethical AI Training with Artist Consent |
| **Audience** | Domain (music industry + AI platforms) |
| **Complexity** | L2 (overview) |
| **Location** | docs/prd/mcp-server-prd.md, docs/knowledge-base/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |

## Purpose

Show how MCP enables AI platforms to train on music ethically—with artist consent, proper attribution, and transparent permissions.

## Key Message

"MCP lets AI platforms check artist permissions before training, ensuring consent and maintaining attribution throughout the AI pipeline."

## Visual Concept

Flow diagram showing artist → the system → AI platform permission flow.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MCP: ETHICAL AI TRAINING WITH ARTIST CONSENT                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ARTIST                    ATTRIBUTION                    AI PLATFORM         │
│   ──────                    ────────                    ───────────         │
│                                                                             │
│   ┌─────────────┐          ┌─────────────┐          ┌─────────────┐        │
│   │             │          │             │          │             │        │
│   │  Sets AI    │─────────▶│  Stores     │◀─────────│  Queries    │        │
│   │  Permissions│   1      │  Permissions│    2     │  Permission │        │
│   │             │          │  via MCP    │          │  via MCP    │        │
│   └─────────────┘          └──────┬──────┘          └──────┬──────┘        │
│                                   │                        │               │
│   "Allow training: yes"           │                        │               │
│   "Require attribution: yes"      │   ┌──────────────┐    │               │
│   "Commercial use: licensed"      │   │              │    │               │
│                                   └──▶│   RESPONSE   │◀───┘               │
│                                       │              │                     │
│                                       │ ✓ Allowed    │                     │
│                                       │ ✓ Must credit│                     │
│                                       │ ✓ Report use │                     │
│                                       └──────────────┘                     │
│                                                                             │
│                                              │                              │
│                                              ▼                              │
│                                   ┌──────────────────┐                     │
│                                   │   AI TRAINS      │                     │
│                                   │   WITH CONSENT   │                     │
│                                   │   + ATTRIBUTION  │                     │
│                                   └──────────────────┘                     │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  "An AI that can ask 'May I use this?' and get a real answer."              │
│                                          — The Ethical AI Vision            │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Artist | `stakeholder_artist` | Sets permissions |
| the attribution MCP | `source_system` | Stores and serves permissions |
| AI Platform | `stakeholder_platform` | Queries before training |
| Permission Response | `attribution_verified` | Consent + requirements |
| AI Training | `solution_component` | Ethical outcome |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Artist | The System | Arrow | "1. Sets permissions" |
| AI Platform | The System | Arrow | "2. Queries MCP" |
| The System | Response | Arrow | "Returns consent" |
| Response | AI Training | Arrow | "Enables ethical training" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "VISION" | An AI that can ask 'May I use this?' and get a real answer | Bottom |

## Text Content

### Labels (Max 30 chars each)

- "Sets AI Permissions"
- "Stores via MCP"
- "Queries Permission"
- "Allow training: yes"
- "Require attribution: yes"
- "Commercial use: licensed"
- "Must credit artist"
- "Report usage"
- "Ethical AI training"

### Caption (for embedding)

MCP enables ethical AI training: artists set permissions in the system (allow training, require attribution, commercial terms). AI platforms query the system via MCP before training. Response includes consent status and requirements. Result: AI trains with consent, maintains attribution, and reports usage.

## Prompts for Nano Banana Pro

### Style Prompt

Permission flow diagram on warm off-white background (#F8F6F0).
Three-column layout: Artist (left), the system (center), AI Platform (right).
Clean flowing arrows showing permission request/response cycle.
Deep blue for the system elements, gold for artist elements, gray for AI platform.
Professional, trustworthy tone. No sci-fi aesthetics.
Quote callout at bottom with ethical AI vision statement.

### Content Prompt

Create an MCP AI permission flow diagram:
- LEFT COLUMN: Artist
  - Box showing "Sets AI Permissions"
  - List: "Allow training: yes", "Require attribution: yes", "Commercial: licensed"
- CENTER COLUMN: the attribution MCP Server
  - Central hub receiving and serving permissions
  - Arrow from Artist labeled "1. Sets"
- RIGHT COLUMN: AI Platform
  - Box showing "Queries Permission"
  - Arrow to the system labeled "2. Queries MCP"
- CENTER RESPONSE BOX: Permission response
  - Checkmarks: Allowed, Must credit, Report use
- BOTTOM: "AI TRAINS WITH CONSENT + ATTRIBUTION" outcome box
- FOOTER: Ethical AI vision quote

### Refinement Notes

- Flow should be clear and simple (artist controls, AI asks, gets answer)
- Permission list should look like settings/preferences
- Outcome should feel positive and ethical
- Emphasize ethical AI and music attribution principles

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "domain-03",
    "title": "MCP: Ethical AI Training with Artist Consent",
    "audience": "domain"
  },
  "content_architecture": {
    "primary_message": "MCP lets AI platforms check artist permissions before training",
    "layout_flow": "three-column-flow",
    "key_structures": [
      {
        "name": "Artist",
        "role": "stakeholder_artist",
        "is_highlighted": true,
        "labels": ["Sets AI Permissions", "Controls consent"]
      },
      {
        "name": "the attribution MCP",
        "role": "source_system",
        "is_highlighted": true,
        "labels": ["Stores permissions", "Serves via MCP"]
      },
      {
        "name": "AI Platform",
        "role": "stakeholder_platform",
        "is_highlighted": false,
        "labels": ["Queries before training", "Respects response"]
      },
      {
        "name": "Permission Response",
        "role": "attribution_verified",
        "is_highlighted": true,
        "labels": ["Allowed", "Must credit", "Report use"]
      },
      {
        "name": "Ethical Outcome",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["AI trains with consent", "Attribution maintained"]
      }
    ],
    "relationships": [
      {"from": "Artist", "to": "the attribution MCP", "type": "arrow", "label": "1. Sets permissions"},
      {"from": "AI Platform", "to": "the attribution MCP", "type": "arrow", "label": "2. Queries MCP"},
      {"from": "the attribution MCP", "to": "Permission Response", "type": "arrow", "label": "Returns consent"},
      {"from": "Permission Response", "to": "Ethical Outcome", "type": "arrow", "label": "Enables"}
    ],
    "callout_boxes": [
      {
        "heading": "VISION",
        "body_text": "An AI that can ask 'May I use this?' and get a real answer. — The Ethical AI Vision",
        "position": "bottom-full-width"
      }
    ]
  }
}
```

## Alt Text

MCP permission flow: Artist sets AI permissions in the system (allow training, require attribution). AI platform queries the system via MCP. Response includes consent status and requirements. Outcome: AI trains with consent and maintains attribution.

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Embedded in documentation
