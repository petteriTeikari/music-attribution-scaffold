# fig-theory-08: Two-Friction Taxonomy -- ELI5 (Airport Analogy)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-08 |
| **Title** | Two-Friction Taxonomy -- ELI5 (Airport Analogy) |
| **Audience** | L1 (Music Industry Professional) |
| **Complexity** | L1 (concept introduction -- no code, real-world analogy) |
| **Location** | docs/theory/two-friction-taxonomy.md, README.md theory section |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure introduces the two-friction taxonomy using everyday analogies. It answers: "Not all friction is bad -- how do we tell the difference between friction we should remove and friction we should keep?"

The key message is: "Administrative friction (paperwork, licensing forms, royalty calculations) should be automated away. Discovery friction (browsing a record store, curating a playlist) should be preserved because it creates value."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  TWO KINDS OF FRICTION                                         |
|  ■ Not All Friction Is Bad                                     |
+-------------------------------+-------------------------------+
|                               |                               |
|  I. ADMIN FRICTION            |  II. DISCOVERY FRICTION        |
|  ─────────────────            |  ──────────────────            |
|  = AUTOMATE THIS              |  = PRESERVE THIS               |
|                               |                               |
|  ┌─────────────────────┐     |  ┌─────────────────────┐      |
|  │                     │     |  │                     │      |
|  │  AIRPORT SECURITY   │     |  │  RECORD STORE       │      |
|  │  ──────────────     │     |  │  ────────────       │      |
|  │                     │     |  │                     │      |
|  │  ┌───┐ ┌───┐ ┌───┐│     |  │   ♪   ♪   ♪         │      |
|  │  │ ID│ │BAG│ │TSA││     |  │  ┌─┐ ┌─┐ ┌─┐       │      |
|  │  └───┘ └───┘ └───┘│     |  │  │ │ │ │ │ │       │      |
|  │                     │     |  │  └─┘ └─┘ └─┘       │      |
|  │  Nobody WANTS to    │     |  │                     │      |
|  │  stand in this line.│     |  │  You WANT to browse.│      |
|  │  Make it faster.    │     |  │  Keep this magic.   │      |
|  │                     │     |  │                     │      |
|  └─────────────────────┘     |  └─────────────────────┘      |
|                               |                               |
|  MUSIC EXAMPLES:              |  MUSIC EXAMPLES:              |
|                               |                               |
|  ■ Filling out licensing      |  ■ A DJ digging for vinyl     |
|    forms                      |  ■ A fan discovering a new     |
|  ■ Calculating royalty         |    artist via recommendation  |
|    splits                     |  ■ A curator building a        |
|  ■ Registering works with     |    playlist with taste         |
|    collecting societies       |  ■ An artist choosing who     |
|  ■ Filing metadata across     |    to collaborate with        |
|    20 platforms               |                               |
|                               |                               |
+-------------------------------+-------------------------------+
|  ■ This scaffold automates the LEFT and protects the RIGHT.   |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "TWO KINDS OF FRICTION" with coral accent square |
| Subtitle | `label_editorial` | "Not All Friction Is Bad" |
| Left panel header | `section_numeral` | "I. ADMIN FRICTION" with "= AUTOMATE THIS" directive |
| Right panel header | `section_numeral` | "II. DISCOVERY FRICTION" with "= PRESERVE THIS" directive |
| Airport security illustration | `problem_statement` | Security line with ID/bag/TSA checkpoints -- nobody wants this |
| Record store illustration | `solution_component` | Browsing vinyl records with music notes -- people want this |
| Left: "Nobody WANTS..." text | `problem_statement` | Emotional anchor for administrative friction |
| Right: "You WANT..." text | `solution_component` | Emotional anchor for discovery friction |
| Left: Music examples list | `problem_statement` | Four bullet points of admin friction in music |
| Right: Music examples list | `solution_component` | Four bullet points of discovery friction in music |
| Vertical divider | `accent_line_v` | Coral red vertical line between panels |
| Footer callout | `callout_box` | "This scaffold automates the LEFT and protects the RIGHT" |

## Anti-Hallucination Rules

1. There are exactly TWO types of friction: Administrative and Discovery. Do NOT add a third type.
2. Admin friction = AUTOMATE. Discovery friction = PRESERVE. Do NOT swap or blur these directives.
3. The airport analogy is for admin friction. The record store analogy is for discovery friction. Do NOT mix.
4. Music examples for admin: licensing forms, royalty splits, collecting societies, multi-platform filing.
5. Music examples for discovery: DJ digging, fan discovering artists, curator building playlists, artist choosing collaborators.
6. Do NOT use technical terms like "ETL pipeline" or "entity resolution" -- this is L1.
7. Do NOT imply that ALL friction should be removed -- the core insight is that some friction has value.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Split panel: left shows airport security as admin friction to automate, right shows record store browsing as discovery friction to preserve, with music industry examples for each.
