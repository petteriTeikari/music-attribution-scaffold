# fig-theory-19: MCP Consent -- ELI5 (Library Card Analogy)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-19 |
| **Title** | MCP Consent -- ELI5 (Library Card Analogy) |
| **Audience** | L1 (Music Industry Professional) |
| **Complexity** | L1 (concept introduction -- no code, everyday analogy) |
| **Location** | docs/theory/mcp-consent.md, README.md theory section |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure introduces the concept of machine-readable consent for AI training using the analogy of a library card. It answers: "How can artists control what AI systems are allowed to do with their music?"

The key message is: "A library card lets you borrow books but not photocopy the whole library -- MCP permissions work the same way: artists grant specific, limited permissions for how their music can be used by AI."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  MACHINE-READABLE CONSENT                                      |
|  ■ Like a Library Card for Your Music                          |
+-------------------------------+-------------------------------+
|                               |                               |
|  I. THE LIBRARY CARD          |  II. MCP PERMISSION            |
|  ────────────────             |  ─────────────────             |
|                               |                               |
|  ┌─────────────────────┐     |  ┌─────────────────────┐      |
|  │  LIBRARY CARD        │     |  │  MCP PERMISSION      │      |
|  │  ────────────        │     |  │  ──────────────      │      |
|  │                      │     |  │                      │      |
|  │  Name: You           │     |  │  Artist: Imogen Heap │      |
|  │  Card #: 12345       │     |  │  Work: "Hide & Seek" │      |
|  │                      │     |  │                      │      |
|  │  ✓ Borrow books      │     |  │  ✓ Streaming         │      |
|  │  ✓ Use reading room  │     |  │  ✓ Sync licensing    │      |
|  │  ✗ Photocopy entire  │     |  │  ✗ AI voice cloning  │      |
|  │    books             │     |  │  ✗ AI training data  │      |
|  │  ✗ Sell borrowed     │     |  │  ? Remix (ask first) │      |
|  │    books             │     |  │                      │      |
|  └─────────────────────┘     |  └─────────────────────┘      |
|                               |                               |
|  The library card tells the   |  The MCP permission tells AI  |
|  librarian what you CAN and   |  systems what they CAN and    |
|  CANNOT do -- automatically.  |  CANNOT do -- automatically.  |
|                               |                               |
+-------------------------------+-------------------------------+
|                                                                |
|  HOW IT WORKS                                                  |
|  ────────────                                                  |
|                                                                |
|  ┌──────┐    "Can I use this    ┌──────────┐    ┌──────┐     |
|  │  AI  │    song for training?" │Permission│    │Answer│     |
|  │System│───────────────────────►│  Server  │───►│      │     |
|  └──────┘                       └──────────┘    │ YES  │     |
|                                                  │ NO   │     |
|                                                  │ ASK  │     |
|                                                  └──────┘     |
|                                                                |
|  ■ The artist sets the rules ONCE. Machines check              |
|    automatically EVERY TIME.                                   |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "MACHINE-READABLE CONSENT" with coral accent square |
| Subtitle | `label_editorial` | "Like a Library Card for Your Music" |
| Left panel header | `section_numeral` | "I. THE LIBRARY CARD" |
| Right panel header | `section_numeral` | "II. MCP PERMISSION" |
| Library card | `stakeholder_artist` | Card with allowed actions (borrow, reading room) and denied actions (photocopy, sell) |
| MCP permission card | `solution_component` | Card with allowed (streaming, sync) and denied (voice cloning, training) actions |
| Checkmarks (allowed) | `confidence_high` | Green check marks for permitted actions |
| Cross marks (denied) | `confidence_low` | Red cross marks for denied actions |
| Question mark (conditional) | `confidence_medium` | Amber question mark for "ask first" actions |
| How-it-works flow | `data_flow` | AI System -> "Can I use?" -> Permission Server -> YES/NO/ASK |
| AI System box | `stakeholder_platform` | The requesting AI system |
| Permission Server box | `security_layer` | The MCP server that holds permissions |
| Answer box | `primary_outcome` | Three possible responses: YES, NO, ASK |
| Vertical divider | `accent_line_v` | Coral vertical line between panels |
| Footer callout | `callout_box` | "Artist sets rules ONCE. Machines check automatically EVERY TIME." |

## Anti-Hallucination Rules

1. MCP stands for Model Context Protocol -- but do NOT spell it out in this L1 figure. Just use "MCP permission."
2. The library card analogy is specific: borrow=yes, photocopy=no. Do NOT change the permissions.
3. MCP permission example: streaming=yes, sync=yes, voice cloning=no, training data=no, remix=ask. These are illustrative.
4. The artist is Imogen Heap and the work is "Hide & Seek" -- the project persona. Do NOT change.
5. Three response types: YES, NO, ASK (conditional). Do NOT add more response types.
6. Do NOT use terms like "API," "endpoint," "JSON," or "protocol spec" -- this is L1.
7. The key insight is SET ONCE, CHECK AUTOMATICALLY -- emphasize this.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Split panel comparing library card permissions (borrow yes, photocopy no) with MCP music permissions (streaming yes, AI training no), plus flow showing AI system querying permission server.
