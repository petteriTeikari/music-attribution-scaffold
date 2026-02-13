# STYLE GUIDE -- Repository Documentation Figures

**Version:** 1.0.0
**Scope:** Repository explanation figures -- architecture, workflows, decision trees, module maps
**Target:** Warp Records editorial aesthetic meets constructivist data visualization
**Generator:** Gemini (Nano Banana Pro)

---

## DESIGN AESTHETIC

### Target Style

- **40%** Warp Records artwork -- abstract data visualization, Roman numerals, pale warm backgrounds
- **30%** Constructivist graphic design -- geometric compositions, bold red/navy/cream, asymmetric grids
- **20%** Scandinavian editorial -- dramatic whitespace, Bauhaus-inspired shapes, typographic hierarchy
- **10%** Vintage recording studio diagrams -- signal chains, patch bay schematics, mixing desk layouts

### Visual Identity

Repository figures communicate **architectural clarity, probabilistic confidence, and scaffold flexibility**:

- **Clarity**: Clean pipeline flows, unambiguous module boundaries
- **Confidence**: Green/amber/red confidence tiers are first-class visual citizens
- **Scaffold**: Branching paths, dashed alternatives, archetype overlays show that this is a framework, not a monolith

### CRITICAL: NO AI SLOP

**BANNED:**

- Generic stock art or clip art
- Corporate SaaS gradients
- Sci-fi neon/glow/holographic effects
- Symmetric, predictable compositions
- Rounded-everything pill aesthetics
- Dark-mode-first design (pure black backgrounds)
- PowerPoint/Lucidchart/Miro default styling
- Drop shadows on boxes
- Glossy or 3D-rendered finishes
- Literal screenshots of code or UI

**REQUIRED:**

- Abstract, editorial interpretations of technical concepts
- Bold geometric compositions with intentional asymmetry
- Warm cream (#f6f3e6) as primary background
- Coral red (#E84C4F) as primary graphic accent
- Grain or halftone textures where appropriate
- Matte finishes on all elements
- At least 30% negative space

---

## COLOR PALETTE

### Background (MANDATORY)

| Element | Hex | RGB | Usage |
|---------|-----|-----|-------|
| **Primary Background** | `#f6f3e6` | 246, 243, 230 | Main figure background -- exact match to frontend surface |
| Secondary Background | `#eeeadb` | 238, 234, 219 | Panel/zone backgrounds |
| Elevated Surface | `#FFFFFF` | 255, 255, 255 | Callout boxes, emphasis panels |

### Brand Accent Colors

| Element | Hex | RGB | Usage |
|---------|-----|-----|-------|
| **Coral Red** | `#E84C4F` | 232, 76, 79 | Primary graphic accent -- lines, squares, stage markers, emphasis |
| **Deep Navy** | `#1E3A5F` | 30, 58, 95 | Secondary accent -- module boundaries, text overlays, pipeline paths |
| **Teal** | `#2E7D7B` | 46, 125, 123 | Technology/innovation accent -- feedback loops, API endpoints |
| **Artist Gold** | `#D4A03C` | 212, 160, 60 | Artist-related elements, human-in-the-loop stages |

### Confidence Tier Colors (Critical -- used in every scoring figure)

| Semantic Tag | Hex | Visual | Threshold | Usage |
|--------------|-----|--------|-----------|-------|
| `confidence_high` | `#4A7C59` | Green | >= 0.85 | Verified, high-trust elements |
| `confidence_medium` | `#E09F3E` | Amber | 0.50 -- 0.84 | Partial corroboration |
| `confidence_low` | `#C44536` | Red | < 0.50 | Uncorroborated, flagged elements |

### Assurance Level Colors (A0 -- A3)

| Semantic Tag | Hex | Visual | Level | Meaning |
|--------------|-----|--------|-------|---------|
| `assurance_a3` | `#4A7C59` | Green | A3 | Artist-verified |
| `assurance_a2` | `#5B9BD5` | Blue | A2 | Multiple sources agree |
| `assurance_a1` | `#E09F3E` | Amber | A1 | Single source only |
| `assurance_a0` | `#9E9E9E` | Gray | A0 | No data |

### Data Source Colors

| Semantic Tag | Hex | Visual | Source |
|--------------|-----|--------|--------|
| `source_musicbrainz` | `#BA478F` | Purple | MusicBrainz open database |
| `source_discogs` | `#333333` | Dark gray | Discogs catalog |
| `source_acoustid` | `#2E7D7B` | Teal | AcoustID fingerprint |
| `source_file` | `#8B7E6A` | Warm gray | File metadata (ID3/Vorbis) |
| `source_artist` | `#D4A03C` | Gold | Artist direct input (highest authority) |

### Pipeline Stage Colors

| Stage | Primary Color | Secondary | Description |
|-------|---------------|-----------|-------------|
| ETL/Extract | Deep navy | Coral accent | Data ingestion and normalization |
| Entity Resolution | Deep navy | Teal accent | Matching, merging, deduplication |
| Source Corroboration | Deep navy | Green/amber/red | Multi-source agreement scoring |
| Final Score | Deep navy | Gold accent | Calibrated confidence output |

### Typography Colors

| Element | Hex | Usage |
|---------|-----|-------|
| Main headings | `#1A1A1A` | Near-black, bold display |
| Subheadings | `#333333` | Dark charcoal |
| Labels | `#4A4A4A` | Medium gray |
| Captions/Annotations | `#666666` | Light gray |

---

## TYPOGRAPHY IN FIGURES

| Role | Font | Style | Usage |
|------|------|-------|-------|
| **Display** | Instrument Serif | Regular/Italic, 48-96px | Figure titles, section headings |
| **Labels** | Plus Jakarta Sans | ALL-CAPS, 0.15em tracking, 500 weight | Section markers, data labels, stage names |
| **Data** | IBM Plex Mono | Regular 400, tabular-nums | Numbers, percentages, confidence scores, code identifiers |

### Editorial Typography Rules

1. **ALL-CAPS with tracking** for section labels and stage markers
2. **Roman numerals** (I, II, III, IV, V) for sequential pipeline stages or numbered elements
3. **Display type as hero element** -- the figure title IS the primary visual, not decoration
4. **Max 30 characters** per label to prevent wrapping
5. **No body paragraphs** -- figures communicate through visual hierarchy, not prose

---

## COMPOSITION RULES

1. **Asymmetric grids** -- never perfectly centered or symmetrical
2. **Accent squares** -- 28px solid coral squares as graphic punctuation at stage boundaries
3. **Thin accent lines** -- 1px coral horizontal rules as section dividers
4. **Roman numerals** -- I, II, III... for sequential elements (Warp Records homage)
5. **Negative space** -- at least 30% of canvas must be empty
6. **Overlapping elements** -- text can overlap into graphic space
7. **No drop shadows** -- flat, matte finishes only
8. **No rounded corners** -- sharp geometric edges (except data source dots)
9. **Dashed lines for alternatives** -- scaffold branching paths shown as dashed, not solid
10. **Signal-flow metaphor** -- pipelines flow left-to-right or top-to-bottom, never both simultaneously
11. **Layered depth** -- use opacity (20-80%) for background zones, full opacity for foreground elements

---

## POWER KEYWORDS FOR NANO BANANA PRO

### Positive (Include in every prompt)

```
Warp Records aesthetic, constructivist data visualization, editorial art direction,
Bauhaus bold shapes, geometric data art, mid-century modernism, Scandinavian minimalism,
typographic hierarchy, warm cream background #f6f3e6, coral red accent #E84C4F,
matte finish, halftone texture, grain overlay, asymmetric composition,
signal chain diagram, mixing desk schematic, abstract pipeline flow,
accent squares, thin accent lines, Roman numerals, ALL-CAPS labels,
generous negative space, flat matte surfaces, sharp geometric edges
```

### Negative (Exclude in every prompt)

```
--no stock photography, generic AI art, corporate gradient, neon glow,
sci-fi futuristic, dark background, symmetric layout, rounded pill shapes,
glossy finish, 3D render, photorealistic, detailed faces, text-heavy,
PowerPoint style, flowchart software, Lucidchart, Miro, drop shadows,
thick block arrows, centered composition, dense dashboard, clip art,
holographic, plasma effects, oversaturated colors, pure white background,
visible hex codes, semantic tag names as text, prompt keywords visible
```

---

## QUALITY CHECKLIST (17/20 Pass Threshold)

Score each item 1 (pass) or 0 (fail). Accept the figure only if score >= 17/20.

### Palette (5 items)

- [ ] 1. Background is warm cream (#f6f3e6), not white, gray, or yellow
- [ ] 2. Coral red (#E84C4F) is present as primary graphic accent
- [ ] 3. Deep navy (#1E3A5F) is present as secondary structural color
- [ ] 4. No unauthorized colors appear (no neon, no pure black backgrounds)
- [ ] 5. Confidence tiers use correct green/amber/red if shown

### Typography (4 items)

- [ ] 6. Display headings use serif font (Instrument Serif style)
- [ ] 7. Labels use ALL-CAPS sans-serif with visible letter-spacing
- [ ] 8. No garbled, illegible, or pseudo-text anywhere
- [ ] 9. All text is crisp and readable at 50% zoom

### Composition (5 items)

- [ ] 10. Layout is asymmetric (not centered or symmetrical)
- [ ] 11. At least 30% negative space
- [ ] 12. No drop shadows or glossy effects anywhere
- [ ] 13. Matte, flat finish on all surfaces
- [ ] 14. Information hierarchy is clear (title > sections > labels > annotations)

### Domain (4 items)

- [ ] 15. Technical content is accurate (pipeline stages in correct order)
- [ ] 16. No internal terms rendered as visible text (no semantic tags, no hex codes)
- [ ] 17. Would look at home in a Warp Records catalog or studio wall poster
- [ ] 18. Would be understood by the target audience (see complexity level)

### Production (2 items)

- [ ] 19. Aspect ratio matches specification (16:9, 16:10, or 3:4 portrait)
- [ ] 20. Resolution sufficient for GitHub rendering (minimum 1200px wide)

---

## LAYOUT TEMPLATES

### Template A: Hero Overview

Best for: README banners, landing page figures, high-level system introductions.

```
+-------------------------------------------------------------------+
|                                                                   |
|       FIGURE TITLE                                                |
|       in Instrument Serif, 72px                                   |
|                                                                   |
|  +--------+                                                       |
|  | coral  |    Subtitle in Plus Jakarta Sans ALL-CAPS             |
|  | square |                                                       |
|  +--------+                                                       |
|                                                                   |
|   [   Large central visual element   ]                            |
|   [   (abstract pipeline, signal     ]                            |
|   [   chain, waveform composition)   ]                            |
|                                                                   |
|                                                                   |
|                                  KEY MESSAGE in editorial caps    |
|                                  thin coral accent line below     |
|                                                                   |
+-------------------------------------------------------------------+
```

### Template B: Multi-Panel Architecture

Best for: Pipeline overviews, module maps, system decomposition.

```
+-------------------------------------------------------------------+
|  TITLE                                                  [coral sq] |
|  Subtitle                                                         |
+--------+-----------+-----------+-----------+----------------------+
|        |           |           |           |                      |
|  I     |    II     |   III     |    IV     |     V                |
| Stage  |  Stage    |  Stage    |  Stage    |   Output             |
|        |           |           |           |                      |
|        |           |           |           |                      |
|  ----> |  ----->   |  ----->   |  ----->   |                      |
|        |           |           |           |                      |
+--------+-----------+-----------+-----------+----------------------+
|                                                                   |
|  KEY INSIGHT callout                            [accent line]     |
|                                                                   |
+-------------------------------------------------------------------+
```

### Template C: Flowchart / Decision Tree

Best for: PRD decision nodes, archetype selection, configuration choices.

```
+-------------------------------------------------------------------+
|  TITLE                                                            |
|  Subtitle                                                  [sq]   |
|                                                                   |
|              +-------------+                                      |
|              | Decision    |                                      |
|              | Node        |                                      |
|              +------+------+                                      |
|                     |                                             |
|            +--------+--------+                                    |
|            |                 |                                    |
|     +------v------+  +------v------+                              |
|     | Option A    |  | Option B    |                              |
|     | (dashed if  |  | (solid if   |                              |
|     |  unchosen)  |  |  selected)  |                              |
|     +-------------+  +-------------+                              |
|                                                                   |
|  [coral accent line]                                              |
|  KEY: Solid = selected path, Dashed = alternative                 |
+-------------------------------------------------------------------+
```

### Template D: Split-Panel Comparison

Best for: Before/after, problem/solution, old vs. new workflow.

```
+-------------------------------------------------------------------+
|  TITLE                                                            |
+-------------------------------+-----------------------------------+
|                               |                                   |
|   LEFT PANEL                  |   RIGHT PANEL                     |
|   (problem / before / old)    |   (solution / after / new)        |
|                               |                                   |
|   Muted colors                |   Full palette                    |
|   (gray, faded coral)         |   (coral, navy, teal, green)      |
|                               |                                   |
|   x  Issue 1                  |   +  Solution 1                   |
|   x  Issue 2                  |   +  Solution 2                   |
|   x  Issue 3                  |   +  Solution 3                   |
|                               |                                   |
+-------------------------------+-----------------------------------+
|                                                                   |
|  KEY MESSAGE spanning full width            [accent line]         |
+-------------------------------------------------------------------+
```

### Template E: How-To Steps (Vertical Signal Chain)

Best for: Workflow guides, setup instructions, pipeline walkthroughs.

```
+---------------------------------------------+
|                                             |
|  TITLE in Instrument Serif                  |
|  [coral sq] Subtitle                        |
|                                             |
|  o  o  o  o  o   (source inputs at top)     |
|  |  |  |  |  |                              |
|  +--+--+--+--+                              |
|        |                                    |
|  +-----------+                              |
|  | I  STAGE  | [coral sq]                   |
|  | [details] |                              |
|  +-----+-----+                              |
|        |                                    |
|  +-----------+                              |
|  | II STAGE  | [coral sq]                   |
|  | [details] |                              |
|  +-----+-----+                              |
|        |                                    |
|  +-----------+                              |
|  | III STAGE | [coral sq]                   |
|  | [details] |                              |
|  +-----+-----+                              |
|        |                                    |
|  +-----------+                              |
|  | IV STAGE  | [coral sq]                   |
|  | [details] |                              |
|  +-----+-----+                              |
|        |                                    |
|    [OUTPUT]                                 |
|        |                                    |
|    feedback arc (teal, right edge)          |
|                                             |
+---------------------------------------------+
```

---

## FILE NAMING CONVENTION

```
fig-repo-{NN}-{short-description}.{ext}
```

Examples:

- `fig-repo-01-pipeline-overview.png` -- Full pipeline architecture
- `fig-repo-02-prd-decision-tree.png` -- PRD decision network visualization
- `fig-repo-03-confidence-calibration.png` -- Confidence scoring walkthrough
- `fig-repo-04-archetype-comparison.png` -- Team archetype split-panel

Output directories:

- `docs/figures/repo-figures/assets/` -- Web-optimized JPEGs (tracked in git)
- `docs/figures/repo-figures/generated/` -- Raw Nano Banana Pro PNGs (gitignored)

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-14 | Initial repo-figures style guide adapted from frontend-figures |

---

*Music Attribution Scaffold -- Repository Documentation Figure Style Guide v1.0.0*
