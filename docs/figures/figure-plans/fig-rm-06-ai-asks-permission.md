# fig-rm-06: AI Asks Permission

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-rm-06 |
| **Title** | AI Asks Permission |
| **Location** | README.md |
| **Style Guide** | STYLE-GUIDE-v2.md (Unified Risograph/Zine) |
| **Gap Filled** | What is MCP? How does AI consent work? |

---

## Content Specification

### Title
AI ASKS PERMISSION

### Subtitle
How the MCP Protocol Protects Your Music

### Main Visual Elements
- LEFT: AI platform icon/badge asking a question
- CENTER: The system acting as gatekeeper/bouncer
- RIGHT: Mogen making the decision (YES or NO)
- Flow shows: AI asks → the system checks → Artist decides

### Layout Pattern
Pattern A: Horizontal Flow (left to right)

```
    AI PLATFORM              ATTRIBUTION              MOGEN
    ┌─────────┐            ┌─────────┐          ┌─────────┐
    │  🤖     │            │   🚪    │          │  👤     │
    │  "Can I │───────────▶│ CHECKS  │─────────▶│  YES?   │
    │  use    │            │ PERMISSION│         │  NO?    │
    │  'Hide  │            │         │          │         │
    │  and    │            └─────────┘          └────┬────┘
    │  Seek'?"│                                      │
    └─────────┘                                      ▼
                                              ┌─────────────┐
                                              │ ✓ APPROVED  │
                                              │ or          │
                                              │ ✗ DENIED    │
                                              └─────────────┘
```

### Labels & Text

**Left (AI Platform):**
- "AI PLATFORM"
- "Can I use 'Hide and Seek' for training?"

**Center (the system):**
- "ATTRIBUTION"
- "Checks your permissions"
- "MCP Protocol"

**Right (Mogen):**
- "MOGEN DECIDES"
- "✓ Yes, approved"
- "✗ No, denied"

**Bottom quote:**
- "AI can't just take your music. They have to ask—and YOU decide."

### Key Semantic Roles

| Element | Role | Color Treatment |
|---------|------|-----------------|
| AI Platform | Requester | Teal outline |
| The System gate | Gatekeeper | Black, central |
| Mogen | Decision maker | Pink accents |
| Request arrow | The ask | Teal |
| Decision | Outcome | Pink (deny) or Teal (approve) |

---

## Gemini Prompt

```json
{
  "prompt": "A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish. The image shows a horizontal flow from left to right with three main elements. LEFT: A circular badge with a robot/AI icon labeled 'AI PLATFORM' with a speech bubble asking 'Can I use Hide and Seek for training?'. CENTER: A circular badge labeled 'ATTRIBUTION' shown as a gatekeeper with 'MCP Protocol' and 'Checks your permissions' text. RIGHT: A stylized female figure with blonde ponytail and rectangular glasses (Mogen) making a decision, with 'YES ✓' and 'NO ✗' options shown. Hand-drawn arrows connect all three elements showing the flow. The title 'AI ASKS PERMISSION' is at the top in a bold, black, hand-printed font, with the subtitle 'How the MCP Protocol Protects Your Music' below it. At the bottom is the quote 'AI can't just take your music. They have to ask—and YOU decide.' The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop.",
  "negative_prompt": "garbled text, illegible glyphs, blurred characters, pseudo-text, corrupted letters, gibberish words, broken typography, visible hex codes, color codes as text, file paths visible, markdown syntax visible, citation brackets, '[cite:' text, '.md' text, internal references as text, yaml syntax, json syntax, technical markup visible, prompt instructions as labels, style keywords visible, rendering keywords as labels, aesthetic descriptors as text, parentheses with style words"
}
```

### ⚠️ Internal Reference Warning

The style guide, color codes, and file references in this document are for **workflow use only**. They must NEVER appear as visible text in the generated image. The negative prompt above helps prevent this.

---

## Why Should I Care?

> "This is how you stay in control when AI companies come knocking."

## Explain It to a Label Exec

> "MCP is like a bouncer for your music. AI platforms can't access artist data without going through the system first—and the artist has final say."

---

## Alt Text

Risograph-style zine page showing a horizontal flow: an AI platform icon asks "Can I use Hide and Seek?", the request passes through the system (shown as a gatekeeper checking permissions via MCP Protocol), and finally reaches Mogen who decides YES or NO. Title reads "AI ASKS PERMISSION."

---

## Status

- [x] Content specification complete
- [x] Generated via Gemini
- [x] Reviewed for clarity
- [x] Embedded in README.md
