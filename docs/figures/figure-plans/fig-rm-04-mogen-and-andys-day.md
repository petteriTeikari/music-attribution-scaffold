# fig-rm-04: Mogen & Andy's Day

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-rm-04 |
| **Title** | Mogen & Andy's Day |
| **Location** | README.md |
| **Style Guide** | STYLE-GUIDE-v2.md (Unified Risograph/Zine) |

---

## Content Specification

### Title
MOGEN & ANDY'S DAY

### Subtitle
A Day in the Life with the system

### Main Visual Elements
- Three horizontal panels showing a user journey (Morning → Afternoon → Evening)
- Mogen character (blonde ponytail, dark glasses, black clothing) as protagonist
- Andy character (bald, round glasses, beard stubble, dark clothing) in evening panel
- Simple icons/badges for dashboard, verification, and permission actions

### Layout Pattern
Pattern E: User Journey (vertical stack of steps)

```
┌─────────────────────────────────────────────────────┐
│  MORNING                                            │
│  [Mogen icon] checks dashboard                      │
│  🔔 "Your credit on 'Tiny Human' needs review"     │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│  AFTERNOON                                          │
│  [Mogen icon] fixes a credit                        │
│  BEFORE: Producer [???] → AFTER: Producer ✓ Mogen  │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│  EVENING                                            │
│  [Andy icon] reviews AI request                     │
│  "JenMusic AI wants to use 'Hide and Seek'"        │
│  [✓ APPROVE]  [✗ DENY]                             │
└─────────────────────────────────────────────────────┘
```

### Labels & Text

**Panel 1 - Morning:**
- "MORNING"
- "Mogen checks her dashboard"
- "🔔 Your credit on 'Tiny Human' needs review"

**Panel 2 - Afternoon:**
- "AFTERNOON"
- "Mogen fixes a credit"
- "BEFORE: Producer [???]"
- "AFTER: Producer ✓ Imogen Heap"
- "Confidence: 0.32 → 0.98"

**Panel 3 - Evening:**
- "EVENING"
- "Andy reviews AI request"
- "JenMusic AI wants to use 'Hide and Seek'"
- "APPROVE" / "DENY" buttons

**Bottom quote:**
- "Check. Fix. Decide. That's it."

### Character Descriptions (from STYLE-GUIDE-v2)

**Mogen:** Woman with light blonde hair in ponytail, rectangular dark-framed glasses, black clothing

**Andy:** Bald man with gray beard stubble, round black-framed glasses, dark clothing

### Key Semantic Roles

| Element | Role | Color Treatment |
|---------|------|-----------------|
| Mogen figure | Primary persona | Pink accents |
| Andy figure | Secondary persona | Teal accents |
| Panel borders | Structure | Black, hand-drawn |
| Notification badge | Alert | Pink fill |
| Before/After | Transformation | Pink (before) → Teal (after) |
| Approve button | Positive action | Teal |
| Deny button | Negative action | Pink outline |

---

## Gemini Prompt

```json
{
  "prompt": "A risograph-style zine page printed on a very light, off-white (#fcfbf4) paper with a subtle textured finish. The image shows three horizontal panels stacked vertically representing a user journey through a day. PANEL 1 (MORNING): Shows a stylized female figure with blonde hair in a ponytail and rectangular dark glasses (labeled 'Mogen') looking at a notification that says 'Your credit needs review'. PANEL 2 (AFTERNOON): Shows the same Mogen figure with a before/after comparison - 'Producer: ???' transforms to 'Producer: Imogen Heap ✓' with confidence score increasing. PANEL 3 (EVENING): Shows a stylized bald male figure with round glasses and beard stubble (labeled 'Andy') looking at an AI permission request with APPROVE and DENY buttons. Hand-drawn arrows connect the panels. The title 'MOGEN & ANDY'S DAY' is at the top in a bold, black, hand-printed font, with the subtitle 'A Day in the Life with the system' below it. At the bottom is the quote 'Check. Fix. Decide. That's it.' The overall aesthetic is a DIY, imperfect, indie-zine look with visible misregistration of fluorescent pink, teal, and black inks. The background is a clean, bright off-white, making the colored elements pop."
}
```

---

## Why Should I Care?

> "This is what using the system actually feels like."

## Explain It to a Label Exec

> "Here's a typical day: check your dashboard, fix a wrong credit in two clicks, decide whether an AI company can use your music. That's the whole product."

---

## Alt Text

Risograph-style zine page showing three stacked panels representing a day with the system. Morning panel shows Mogen (blonde woman with glasses) checking a notification. Afternoon panel shows her fixing a producer credit from unknown to verified. Evening panel shows Andy (bald man with round glasses) reviewing an AI permission request with approve/deny buttons. Title reads "MOGEN & ANDY'S DAY."

---

## Status

- [x] Content specification complete
- [x] Generated via Gemini
- [x] Reviewed for clarity
- [x] Embedded in README.md
