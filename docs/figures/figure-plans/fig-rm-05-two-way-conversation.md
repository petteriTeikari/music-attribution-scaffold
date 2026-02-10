# fig-rm-05: Two-Way Conversation

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-rm-05 |
| **Title** | Two-Way Conversation |
| **Location** | README.md |
| **Style Guide** | STYLE-GUIDE-v2.md (Unified Risograph/Zine) |

---

## Content Specification

### Title
TWO-WAY CONVERSATION

### Subtitle
Input Your Data. Let Others Query It.

### Main Visual Elements
- Central ATTRIBUTION badge/hub
- LEFT SIDE: "INPUT" flow - Mogen adding/editing her credit data
- RIGHT SIDE: "QUERY" flow - Others asking questions about the data
- Two distinct arrows: one flowing IN (pink), one flowing OUT (teal)
- Query side shows TWO access methods: AI (via MCP) and Humans (via chat/search)

### Layout Pattern
Pattern B variant: Central hub with bidirectional flows

```
         INPUT                              QUERY
    (Add & Edit Data)              (Ask Questions)

    ┌─────────────┐                ┌─────────────┐
    │   MOGEN     │                │  AI (MCP)   │
    │  "I played  │                │  "Who wrote │
    │   piano"    │                │  this song?"│
    └──────┬──────┘                └──────┬──────┘
           │                              │
           │                              │
           ▼          ┌──────┐            ▼
    ─────────────────▶│ATTRIBUTION│◀─────────────────
                      │  DATA  │
    ─────────────────▶│  HUB   │◀─────────────────
           ▲          └──────┘            ▲
           │                              │
           │                              │
    ┌──────┴──────┐                ┌──────┴──────┐
    │   ANDY      │                │  HUMANS     │
    │  "Fix this  │                │  "Show me   │
    │   credit"   │                │  credits"   │
    └─────────────┘                └─────────────┘
```

### Labels & Text

**Title & Subtitle:**
- "TWO-WAY CONVERSATION"
- "Input Your Data. Let Others Query It."

**Left Side (INPUT):**
- "INPUT"
- "Add & Edit Data"
- "Mogen: 'I played piano on track 3'"
- "Andy: 'Fix this producer credit'"
- Arrow label: "Your words become verified credits"

**Center:**
- "ATTRIBUTION DATA HUB"

**Right Side (QUERY):**
- "QUERY"
- "Ask Questions"
- "AI (via MCP): 'Who wrote this song?'"
- "Humans (via Chat): 'Show me all credits'"
- Arrow label: "Others can ask—with your permission"

**Bottom quote:**
- "You control what goes in. You control who asks."

### Key Semantic Roles

| Element | Role | Color Treatment |
|---------|------|-----------------|
| Mogen figure | Data owner (input) | Pink accents |
| Andy figure | Data editor (input) | Pink accents |
| AI query icon | MCP access | Teal accents |
| Human query icon | Chat/search access | Teal accents |
| Input arrows | Data contribution | Pink |
| Query arrows | Data retrieval | Teal |
| Central hub | The System | Black outline, both colors |

### Character Descriptions (from STYLE-GUIDE-v2)

**Mogen:** Woman with light blonde hair in ponytail, rectangular dark-framed glasses, black clothing

**Andy:** Bald man with gray beard stubble, round black-framed glasses, dark clothing

---

## Gemini Prompt

```json
{
  "prompt": "A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish. The image shows a central circular badge labeled 'ATTRIBUTION DATA HUB' with TWO DISTINCT FLOWS on either side. LEFT SIDE labeled 'INPUT - Add & Edit Data': Shows two stylized figures - a woman with blonde ponytail and rectangular glasses (Mogen) and a bald man with round glasses and beard (Andy) - with speech bubbles showing them adding data like 'I played piano' and 'Fix this credit'. Pink arrows flow FROM them INTO the central hub. RIGHT SIDE labeled 'QUERY - Ask Questions': Shows an AI robot icon and a human figure, with speech bubbles showing queries like 'Who wrote this song?' and 'Show me credits'. Teal arrows flow FROM the central hub TO them. The title 'TWO-WAY CONVERSATION' is at the top in a bold, black, hand-printed font, with the subtitle 'Input Your Data. Let Others Query It.' below it. At the bottom is the quote 'You control what goes in. You control who asks.' The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop."
}
```

---

## Why Should I Care?

> "Your data isn't just stored—it can be searched by fans, researchers, and AI (with your permission)."

## Explain It to a Label Exec

> "The chat has two jobs: artists put data IN, and verified users can query data OUT. AI platforms use MCP, humans use chat or search. The artist controls both sides."

---

## Alt Text

Risograph-style zine page showing a central Attribution Data Hub with bidirectional flows. Left side (INPUT) shows Mogen and Andy contributing data with pink arrows flowing in. Right side (QUERY) shows AI and human icons querying data with teal arrows flowing out. Title reads "TWO-WAY CONVERSATION" with subtitle "Input Your Data. Let Others Query It."

---

## Status

- [x] Content specification complete
- [x] Generated via Gemini
- [x] Reviewed for clarity
- [x] Embedded in README.md
