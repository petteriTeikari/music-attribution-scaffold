# fig-rm-02: Sound Sources Unite

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-rm-02 |
| **Title** | Sound Sources Unite |
| **Location** | README.md |
| **Style Guide** | STYLE-GUIDE-v2.md (Unified Risograph/Zine) |

---

## Content Specification

### Title
SOUND SOURCES UNITE

### Subtitle
How the system Brings It Together

### Main Visual Elements
- Three circular source badges at top (Discogs, MusicBrainz, Artist Input)
- Hand-drawn arrows flowing DOWN into a central ATTRIBUTION badge
- Below that, a single "UNIFIED RECORD" output badge showing the resolved data
- The flow shows: chaos in → clarity out

### Layout Pattern
Pattern B: Central Hub (sources converging to solution)

```
    ○ DISCOGS      ○ MUSICBRAINZ      ○ ARTIST INPUT
         ╲              │               ╱
          ╲             │              ╱
           ╲            ▼             ╱
            └───▶ ◉ ATTRIBUTION ◀──────┘
                      │
                      ▼
              ┌──────────────┐
              │   UNIFIED    │
              │   RECORD     │
              │              │
              │ Hide and Seek│
              │ Imogen Heap  │
              │ Prod: Andy   │
              │ ✓ VERIFIED   │
              └──────────────┘
```

### Labels & Text

**Source badges:**
- "DISCOGS"
- "MUSICBRAINZ"
- "ARTIST INPUT" (with emphasis - this is key)

**Central badge:**
- "ATTRIBUTION"

**Output record:**
- "UNIFIED RECORD"
- "Hide and Seek"
- "Imogen Heap"
- "Produced by Andy Carne"
- "✓ VERIFIED"
- "Confidence: 0.94"

**Bottom quote:**
- "Multiple sources in. One verified truth out."

### Key Semantic Roles

| Element | Role | Color Treatment |
|---------|------|-----------------|
| Source badges | Input data | Black outlines, teal accents |
| ATTRIBUTION badge | The solution | Pink fill, emphasis |
| Unified Record | Output | Teal fill, success state |
| Artist Input badge | Key differentiator | Pink accent (YOUR input matters) |
| Arrows | Data flow | Black, hand-drawn |
| Checkmark | Verification | Teal |

---

## Gemini Prompt

```json
{
  "prompt": "A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish. The image features three circular badges at the top labeled DISCOGS, MUSICBRAINZ, and ARTIST INPUT, with hand-drawn arrows flowing downward into a central larger badge labeled ATTRIBUTION. Below the ATTRIBUTION badge, another arrow points down to a rectangular card showing 'UNIFIED RECORD' with clean metadata: song title, artist name, producer credit, and a checkmark with 'VERIFIED' and 'Confidence: 0.94'. The title 'SOUND SOURCES UNITE' is at the top in a bold, black, hand-printed font, with the subtitle 'How the system Brings It Together' below it. At the bottom is the quote 'Multiple sources in. One verified truth out.' The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop."
}
```

---

## Why Should I Care?

> "We check every source—including YOU—to find the truth."

## Explain It to a Label Exec

> "We don't pick one database and hope it's right. We compare them ALL, including what the artist tells us, and find where they agree."

---

## Alt Text

Risograph-style zine page showing three source badges (Discogs, MusicBrainz, Artist Input) with arrows flowing into a central ATTRIBUTION badge. Below, an arrow points to a "UNIFIED RECORD" card showing verified song metadata with a checkmark. Title reads "SOUND SOURCES UNITE" with subtitle "How the system Brings It Together."

---

## Status

- [x] Content specification complete
- [x] Generated via Gemini
- [x] Reviewed for clarity
- [x] Embedded in README.md
