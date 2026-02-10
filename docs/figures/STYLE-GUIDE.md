# STYLE GUIDE - The system Documentation Infographics

**Version:** 1.0.0
**Scope:** Repository documentation figures for the system
**Target:** Elegant professional infographic / Scientific American quality

---

## DESIGN AESTHETIC

### Target Style

- **75%** Herman Miller mid-century modernism - elegant, timeless, professional
- **25%** Economist data visualization - clean, informative, grid-aligned

### Visual Identity

The system figures communicate **trust, transparency, and creative collaboration**:

- Trust: Deep blues, professional typography
- Transparency: Clear hierarchy, explicit confidence levels
- Creativity: Warm gold accents (music industry heritage)

### CRITICAL: NO SCI-FI AESTHETICS

**BANNED:**
- Glowing elements, neon highlights
- Futuristic/cyberpunk UI elements
- Holographic effects, plasma/energy effects
- Pure black backgrounds
- Matrix/digital rain aesthetics

**REQUIRED:**
- Elegant scientific illustration
- Warm, professional tones
- Matte finishes on all elements
- Natural lighting, soft shadows

---

## COLOR PALETTE

### Background (MANDATORY)

| Element | Hex | RGB | Usage |
|---------|-----|-----|-------|
| **Primary Background** | #F8F6F0 | 248, 246, 240 | Main figure background |
| Secondary Background | #F0EDE5 | 240, 237, 229 | Panel backgrounds |
| Callout Background | #FFFFFF | 255, 255, 255 | White for emphasis boxes |

### Brand Colors

| Element | Hex | RGB | Meaning |
|---------|-----|-----|---------|
| **Primary Blue** | #1E3A5F | 30, 58, 95 | Trust, authority, system brand |
| **Creative Gold** | #D4A03C | 212, 160, 60 | Music/creativity, warmth |
| Accent Teal | #2E7D7B | 46, 125, 123 | Innovation, technology |

### Attribution Level Colors

| Semantic Tag | Hex | Visual | Meaning |
|--------------|-----|--------|---------|
| `attribution_verified` | #4A7C59 | Green | A3: Verified by artist |
| `attribution_corroborated` | #5B9BD5 | Blue | A2: Multiple sources agree |
| `attribution_claimed` | #E09F3E | Amber | A1: Single source claims |
| `attribution_unknown` | #9E9E9E | Gray | A0: No data found |

### Data Source Colors

| Semantic Tag | Hex | Visual | Source |
|--------------|-----|--------|--------|
| `source_system` | #1E3A5F | Deep blue | System Own (primary) |
| `source_musicbrainz` | #BA478F | Purple | MusicBrainz |
| `source_discogs` | #333333 | Dark gray | Discogs |

### Access Tier Colors

| Semantic Tag | Hex | Visual | Tier |
|--------------|-----|--------|------|
| `tier_internal` | #1E3A5F | Deep blue | Internal (system apps) |
| `tier_verified` | #D4A03C | Gold | Verified partners (Mogen) |
| `tier_public` | #9E9E9E | Gray | Public (unknown AI) |

### Confidence Level Colors

| Semantic Tag | Hex | Visual | Range |
|--------------|-----|--------|-------|
| `confidence_high` | #4A7C59 | Green | 0.85+ |
| `confidence_medium` | #E09F3E | Amber | 0.50-0.84 |
| `confidence_low` | #C44536 | Red | <0.50 |

### Typography Colors

| Element | Hex | Usage |
|---------|-----|-------|
| Main Headings | #1A1A1A | Near-black, bold |
| Subheadings | #333333 | Dark charcoal |
| Body Text | #4A4A4A | Medium gray |
| Labels/Captions | #666666 | Light gray |

---

## SEMANTIC TAG REFERENCE

### CRITICAL: INTERNAL USE ONLY

Semantic tags are for **workflow communication between Claude Code and Gemini**.

**NEVER render tag names as visible text in images.**

When writing prompts, translate tags to natural language:
- `source_system` → "deep blue the system elements"
- `attribution_verified` → "green verified status"
- `tier_internal` → "blue internal access"

### Structure Roles

| Semantic Tag | When to Use |
|--------------|-------------|
| `primary_pathway` | Main data flows, highlighted paths |
| `secondary_pathway` | Supporting flows, background elements |
| `processing_stage` | Pipeline stages, transformations |
| `storage_layer` | Database, persistence elements |
| `api_endpoint` | External interfaces, MCP tools |
| `security_layer` | Auth, permissions, trust boundaries |

### Element Types

| Semantic Tag | When to Use |
|--------------|-------------|
| `callout_box` | Key insight boxes |
| `annotation` | Small labels |
| `title` | Figure title |
| `section_heading` | Panel headings |
| `data_flow` | Arrows showing information flow |
| `decision_point` | Branching logic |

### Domain-Specific (Music Industry)

| Semantic Tag | When to Use |
|--------------|-------------|
| `stakeholder_artist` | Artist-related elements |
| `stakeholder_platform` | Platform/label elements |
| `problem_statement` | Crisis/issue visualization |
| `solution_component` | system solution parts |
| `benefit_artist` | Artist benefits |
| `benefit_platform` | Platform benefits |

---

## TYPOGRAPHY

| Level | Font | Weight | Size | Color |
|-------|------|--------|------|-------|
| H1 - Title | Helvetica/Arial | Bold (700) | 24-32pt | #1A1A1A |
| H2 - Section | Helvetica/Arial | Semibold (600) | 18-22pt | #1A1A1A |
| H3 - Subsection | Sans-serif | Medium (500) | 14-16pt | #333333 |
| Body | Sans-serif | Regular (400) | 12-14pt | #4A4A4A |
| Labels | Sans-serif | Regular (400) | 10-12pt | #666666 |
| Code | Monospace | Regular (400) | 11pt | #333333 |

---

## FORMAT SPECIFICATIONS

### Figure Dimensions

| Spec | Value | Notes |
|------|-------|-------|
| **Aspect Ratio** | 16:9 or 16:10 | Landscape for README |
| **Resolution** | 300 DPI source | Export at high quality |
| **Width** | 1200-1920px | Good GitHub rendering |
| **Panels** | 2-6 panels | Organized layouts |
| **Max Label** | 30 characters | Prevent wrapping |

### Rendering

| Surface Type | Rendering |
|--------------|-----------|
| Containers | Rounded corners, soft shadows |
| Arrows | Organic flowing (not rigid) |
| Icons | Flat, clean, anti-aliased |
| Text | Crisp, never garbled |

### Lighting

- **Primary:** Top-left soft diffuse
- **Shadows:** Soft (10-20% opacity)
- **NO:** Harsh shadows, dramatic backlighting, glow effects

---

## POWER KEYWORDS (For Nano Banana Pro)

### Positive (Include)

```
Medical illustration quality, Elegant scientific visualization,
Economist-style infographic, Herman Miller modernism,
Soft ambient lighting, Matte professional finish,
Clean typography, Clear information hierarchy,
Warm off-white background (#F8F6F0), Sans-serif labels,
Organic flowing arrows, Rounded containers, Subtle shadows
```

### Negative (Exclude)

```
cartoon, clip art, flat illustration, minimalist, watercolor, sketch,
hand-drawn, vintage, retro, neon colors, oversaturated,
pure white background, harsh shadows, corporate generic,
glowing effects, neon glow, sci-fi aesthetic, cyberpunk, futuristic,
holographic, plasma effects, dark mode, pure black backgrounds,
garbled text, illegible glyphs, blurred characters, pseudo-text,
visible hex codes, semantic tag names as text, prompt keywords visible
```

---

## LAYOUT TEMPLATES

### Pipeline Flow (Technical)

```
┌─────────────────────────────────────────────────────────────────┐
│  FIGURE TITLE                                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────┐      ┌─────────┐      ┌─────────┐               │
│   │ Source  │  →   │ Process │  →   │ Output  │               │
│   │   A     │      │  Stage  │      │  Data   │               │
│   └─────────┘      └─────────┘      └─────────┘               │
│        ↓                                                        │
│   ┌─────────┐                                                   │
│   │ Source  │                                                   │
│   │   B     │                                                   │
│   └─────────┘                                                   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  KEY INSIGHT: Summary callout                                    │
└─────────────────────────────────────────────────────────────────┘
```

### Before/After Comparison (Domain)

```
┌─────────────────────────────────────────────────────────────────┐
│  FIGURE TITLE                                                    │
├────────────────────────────┬────────────────────────────────────┤
│                            │                                    │
│   THE PROBLEM              │   THE SOLUTION                     │
│   (Red/Gray tones)         │   (Blue/Green tones)               │
│                            │                                    │
│   - Issue 1                │   + Solution 1                     │
│   - Issue 2                │   + Solution 2                     │
│   - Issue 3                │   + Solution 3                     │
│                            │                                    │
├────────────────────────────┴────────────────────────────────────┤
│  KEY MESSAGE: What The system enables                              │
└─────────────────────────────────────────────────────────────────┘
```

### Tier/Level Diagram (Access Control)

```
┌─────────────────────────────────────────────────────────────────┐
│  THREE-TIER ACCESS MODEL                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────────────────────────────────────────────┐      │
│   │  TIER 1: INTERNAL (Blue)                             │      │
│   │  Full access, system apps                          │      │
│   ├─────────────────────────────────────────────────────┤      │
│   │  TIER 2: VERIFIED (Gold)                             │      │
│   │  Trusted partners, read + scoped write               │      │
│   ├─────────────────────────────────────────────────────┤      │
│   │  TIER 3: PUBLIC (Gray)                               │      │
│   │  Unknown clients, read-only, rate-limited            │      │
│   └─────────────────────────────────────────────────────┘      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## QUALITY CHECKLIST

### Before Generation

- [ ] Background specified as #F8F6F0
- [ ] NO glowing/sci-fi keywords in prompt
- [ ] Semantic tags used (not hex codes in content)
- [ ] Negative prompt includes anti-sci-fi terms
- [ ] Layout sketched with ASCII
- [ ] Labels under 30 characters

### After Generation

- [ ] Background IS warm off-white
- [ ] NO glowing effects anywhere
- [ ] Matte, elegant finish on all elements
- [ ] Clean typography (no garbled text)
- [ ] Clear information hierarchy
- [ ] Professional enough for investor presentation

---

*the system Style Guide v1.0.0 - For content/style decoupled figure generation*
