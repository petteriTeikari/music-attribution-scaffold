# fig-rm-01: Where Credits Go to Die

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-rm-01 |
| **Title** | Where Credits Go to Die |
| **Location** | README.md |
| **Style Guide** | STYLE-GUIDE-v2.md (Unified Risograph/Zine) |

---

## Content Specification

### Title
WHERE CREDITS GO TO DIE

### Subtitle
The Music Metadata Crisis

### Main Visual Elements
- Three circular database badges arranged horizontally, each showing conflicting data
- Hand-drawn arrows pointing DOWN to a central "chaos" zone
- Each badge represents a different source with DIFFERENT information for the same song
- Central element showing the CONFLICT/MISMATCH

### Layout Pattern
Pattern B variant: Three sources converging to problem

```
    ○ DISCOGS        ○ MUSICBRAINZ       ○ STREAMING
   "Hide & Seek"     "Hide n Seek"      "HIDE AND SEEK"
   "Imogen Heap"     "I. Heap"          "Unknown Artist"
   "2005"            "2004"             "2005"
        ╲                │                ╱
         ╲               │               ╱
          ╲              ▼              ╱
           ╲    ┌─────────────────┐   ╱
            └──▶│   ❌ NOTHING    │◀─┘
                │     MATCHES     │
                └─────────────────┘
```

### Labels & Text

**Badge 1 (Discogs):**
- "DISCOGS"
- "Hide & Seek"
- "Imogen Heap"
- "Prod: ???"

**Badge 2 (MusicBrainz):**
- "MUSICBRAINZ"
- "Hide n Seek"
- "I. Heap"
- "Prod: A. Carne"

**Badge 3 (Streaming):**
- "STREAMING"
- "HIDE AND SEEK"
- "Unknown Artist"
- "Prod: (missing)"

**Central conflict:**
- "NOTHING MATCHES"

**Bottom quote:**
- "Three databases. Three different answers. Zero certainty."

### Key Semantic Roles

| Element | Role | Color Treatment |
|---------|------|-----------------|
| Database badges | Data sources | Black outlines, teal fills |
| Conflicting text | The problem | Pink highlights on differences |
| Central conflict | Result | Pink fill, emphasis |
| Arrows | Flow/convergence | Black, hand-drawn |

---

## Gemini Prompt

```json
{
  "prompt": "A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish. The image features three circular badges arranged horizontally at the top, each representing a different music database (labeled DISCOGS, MUSICBRAINZ, STREAMING). Each badge contains slightly different metadata for the same song - different title spellings, different artist name formats, missing producer credits. Hand-drawn arrows point downward from all three badges, converging on a central element showing 'NOTHING MATCHES' with an X mark. The title 'WHERE CREDITS GO TO DIE' is at the top in a bold, black, hand-printed font, with the subtitle 'The Music Metadata Crisis' below it. At the bottom is the quote 'Three databases. Three different answers. Zero certainty.' The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop."
}
```

---

## Why Should I Care?

> "This is why you're not getting paid for some of your work."

## Explain It to a Label Exec

> "Look at this mess—three databases, three different answers about who made this song. And every one of them is incomplete."

---

## Alt Text

Risograph-style zine page showing three circular database badges (Discogs, MusicBrainz, Streaming) each containing different, conflicting metadata for the same song. Hand-drawn arrows converge from all three to a central "NOTHING MATCHES" element. Title reads "WHERE CREDITS GO TO DIE" with subtitle "The Music Metadata Crisis."

---

## Status

- [x] Content specification complete
- [ ] Generated via Gemini
- [ ] Reviewed for clarity
- [ ] Embedded in README.md
