# Nano Banana Pro Figure Coverage Improvement Plan

**Version:** 2.0 (POST-REVIEW)
**Created:** 2026-02-04
**Branch:** `chore/improve-nano-banana-figure-coverage`
**Target Audience:** Music industry decision-makers (especially Mogen & Andy)

---

## Review Feedback Incorporated

This plan has been reviewed by three specialist agents:
1. **Creative Industry Authenticity Reviewer** - Identified clichéd metaphors, validated haute couture references
2. **Visual Style Diversity Reviewer** - Expanded template library, identified overlap risks
3. **Non-Technical Comprehension Reviewer** - Flagged abstract concepts, proposed narrative thread

### Key Changes from v1.0:
- Replaced "vinyl groove spiral" → "cochlear spiral" (inner ear anatomy)
- Replaced "heart/brain" metaphor → piano action mechanism or vocoder cross-section
- Added 3 new style templates (Risograph, Patent Drawing, Chronophotography)
- Created "Mogen's Song Journey" narrative thread using "Hide and Seek"
- Reduced README to 4 core figures (moved technical to architecture docs)
- Added "Why Should I Care?" callouts to each figure
- Replaced startup jargon (Hero Squad → Opening Gallery, P0/P1 → Essential/Supporting)

---

## User Prompt (Verbatim)

> could we create a new branch chore/improve-nano-banana-figure coverage, and then analyse the repo for opportunities to document this repo a lot better visually so that the high-level decision makers with not so much tech background can figure out what is happening (namely Imogen Heap who is reading this and who wrote this /home/petteri/Dropbox/github-personal/sci-llm-writer/biblio/biblio-music/heap-musicians-genai-2025.md). You can refer her as Mogen in the image, and you can also mention Andy (Andy Carne - Special Projects Lead @ Imogen Heap | Founder @ Streemliner | Founder @ playlist.plus | Creative Director @ thelongdrop - Artist ID: AURA01JE38RRG1T) also by name to make in the figures (so Mogen and Andy as user personas or co-creators of the platform basically) so they feel tailored for the audience ;) [...] so the visual aesthetics is more boring whereas the target audience for this is music industry professional, so we can be more creative and less boring with the visualization in the created individual .md files [...] no scifi glow, no tech bro graphs going to typical startups. Think of creative industry! Include musicians, experimental electronic musical instruments, DAW interfaces, audio attribution, audio watermarking, producers, DJs, musicians performing in haute couture outfits by Thierry Mugler, Iris von Herpen on stage [...] I give you now permission to creatively interpolate different styles and create mixed media collages with contrasting visual styles, e.g. vintage halftone photograph with graphics design overlays!

---

## Target Personas

### Mogen (Imogen Heap)
- Grammy-winning musician, producer, performer
- Founder of Mycelia/Creative Passport (precursor to the system)
- Pioneer: First music sale on Ethereum blockchain (2015)
- Known for: Mi.Mu gloves, experimental electronic music, tech advocacy
- Artist ID: AURA01JE38RP4ES
- Visual associations: Iris van Herpen-style sculptural costumes, modular synthesizers, wearable tech, theatrical performance

### Andy Carne
- Special Projects Lead for Imogen Heap
- Grammy-nominated Art Director with 25+ years in music visuals
- Software engineer/technologist/startup founder
- Built: Streemliner, Mupix, Playlist+ (AI music app)
- Artist ID: AURA01JE38RRG1T
- Visual associations: Album artwork, visual content creation, creative tech, studio environments

---

## Creative Direction: WILD STYLE VARIANCE

**CRITICAL: Each figure should have its OWN distinct visual style.**

This is NOT a corporate design system. We are creating a **portfolio of varied artistic approaches** that feel like they came from a gallery exhibition about music and technology.

### Banned Aesthetics
- Sci-fi glow, neon cyberpunk
- Tech bro startup graphs
- Corporate infographic templates
- Generic flowcharts
- Stock illustration
- Sterile medical/scientific (exception: anatomical surrealism)

### Encouraged Aesthetics (Mix & Match)
| Style | Visual Reference | Good For |
|-------|------------------|----------|
| **Vintage Halftone** | 1960s print advertising, Benday dots | Problem statements, "the crisis" |
| **Constructivist Collage** | Rodchenko, Soviet poster art | Systems architecture, data flows |
| **Mid-Century Modern** | Herman Miller, Eames | User journeys, personas |
| **Japanese Poster Art** | Tadanori Yokoo, Showa-era educational | Attribution levels, state machines |
| **Anatomical Surrealism** | Medical illustration meets music | Database schemas, internal structures |
| **Album Art 3D** | Contemporary vinyl covers, Beeple-lite | Hero/feature illustrations |
| **Haute Couture Sketch** | Thierry Mugler, Iris van Herpen designs | Performer/artist-centric figures |
| **Vintage Oscilloscope** | 1950s Bell Labs, waveform photography | Audio/signal processing concepts |
| **Editorial Mixed Media** | Collage + vector overlay | Complex multi-concept figures |
| **Modular Synth Documentary** | Klaus Schulze, Tangerine Dream era | Technology integration concepts |

### Color Philosophy
- **NOT** a fixed palette - each figure finds its own voice
- **General warmth**: Prefer warm off-whites, creams, aged paper tones for backgrounds
- **Accent freedom**: Each figure can use its own accent colors that fit its style
- **Music industry cues**: Gold/vinyl black for achievement, vintage analog warmth

---

## Mermaid Diagram Audit: 30 Diagrams Across Repository

### README.md (4 diagrams) → 6 NEW FIGURES

| Current Mermaid | Lines | Convert To | Priority |
|-----------------|-------|------------|----------|
| "Data Silos" Problem | 17-38 | **fig-rm-01**: Vintage halftone collage of fragmented records | P0 |
| "Our Solution" Multi-Source | 44-80 | **fig-rm-02**: Constructivist data flow poster | P0 |
| "Attribution Levels" State | 86-99 | **fig-rm-03**: Japanese poster progression A0→A3 | P0 |
| "System Architecture" | 109-148 | **fig-rm-04**: Anatomical music machine (central figure) | P0 |
| N/A (new) | - | **fig-rm-05**: "Mogen & Andy User Journey" mid-century style | P0 |
| N/A (new) | - | **fig-rm-06**: "The Vision" editorial collage with performers | P0 |

### docs/architecture/README.md (7 diagrams) → 4 NEW FIGURES

| Current Mermaid | Lines | Convert To | Priority |
|-----------------|-------|------------|----------|
| System Architecture + Security | 7-64 | **fig-arch-01**: Modular synth patch diagram style | P1 |
| Entity Resolution Flow | 111-138 | **fig-arch-02**: Vintage oscilloscope sequence | P1 |
| MCP Request Flow | 142-168 | **fig-arch-03**: Editorial mixed media (AI meets music) | P1 |
| Database ER Diagram | 176-247 | **fig-arch-04**: Anatomical surrealism (database organs) | P1 |
| Attribution State Machine | 251-276 | Covered by fig-rm-03 | - |
| Confidence Scoring | 280-307 | **fig-arch-05**: Vintage dial/meter instrumentation | P2 |

### docs/prd/vision-v1.md (4 diagrams) → 3 NEW FIGURES

| Current Mermaid | Lines | Convert To | Priority |
|-----------------|-------|------------|----------|
| Target Users | 77-108 | **fig-vis-01**: "Mogen, Andy & Friends" portrait gallery | P0 |
| System Design | 147-188 | Covered by fig-arch-01 | - |
| Data Model | 227-306 | **fig-vis-02**: Vinyl record label as ER diagram | P1 |
| AI Permissions Decision | 325-340 | **fig-vis-03**: Haute couture consent workflow | P1 |

### docs/prd/attribution-engine-prd.md (2 diagrams) → 2 NEW FIGURES

| Current Mermaid | Lines | Convert To | Priority |
|-----------------|-------|------------|----------|
| Attribution Pipeline | 57-90 | **fig-eng-01**: DAW-style signal chain | P1 |
| Data Provenance Hierarchy | 406-440 | **fig-eng-02**: Archaeological dig layers | P2 |

### docs/prd/mcp-server-prd.md (5 diagrams) → 3 NEW FIGURES

| Current Mermaid | Lines | Convert To | Priority |
|-----------------|-------|------------|----------|
| Three-Tier Trust Model | 42-73 | **fig-mcp-01**: Backstage pass/VIP access visual | P1 |
| MCP Tool Definitions | 130-160 | **fig-mcp-02**: DJ mixer interface metaphor | P2 |
| Security Architecture | 432-470 | **fig-mcp-03**: Stage security checkpoint | P2 |
| Inference-Time Attribution | 539-570 | Covered by fig-arch-03 | - |
| Deterrence Economics | 574-600 | **fig-mcp-04**: Consequences diagram (editorial) | P3 |

### docs/prd/chat-interface-prd.md (4 diagrams) → 2 NEW FIGURES

| Current Mermaid | Lines | Convert To | Priority |
|-----------------|-------|------------|----------|
| Chat Workflow State | 59-94 | **fig-chat-01**: Conversation as vinyl groove spiral | P1 |
| Conversation Flow | 98-120 | Merged into fig-chat-01 | - |
| Components | 178-215 | **fig-chat-02**: Recording studio console | P2 |
| Memory Flow | 261-295 | Merged into fig-chat-02 | - |

### Other Locations (3 diagrams) → 1 NEW FIGURE

| Current Mermaid | Location | Convert To | Priority |
|-----------------|----------|------------|----------|
| Single vs Multi-Agent | ADR-0005 | **fig-adr-01**: One conductor vs. orchestra | P2 |
| Knowledge Base Structure | KB README | Low priority for non-technical audience | P3 |
| Agentic Commerce | MCP SYNTHESIS | **fig-kb-01**: Ecosystem map (festival grounds) | P2 |

---

## Figure Summary by Location

### README.md (4 figures) - THE OPENING GALLERY

**Design Principle:** These 4 figures follow "Hide and Seek's Journey" - Mogen's song traveling through the system system.

| ID | Title | Style | Narrative Beat | "Why Should I Care?" |
|----|-------|-------|----------------|---------------------|
| fig-rm-01 | "Where Credits Go to Die" | Vintage halftone + degradation | "Hide and Seek" credits are wrong everywhere | "This is why you're not getting paid" |
| fig-rm-02 | "Sound Sources Unite" | Constructivist poster | The System aggregates from Discogs, MusicBrainz, Mogen herself | "We check every source to find YOUR truth" |
| fig-rm-03 | "From Unknown to Verified" | Risograph progression (Template G) | Credit moves from A0→A3 as sources confirm | "This is how we make sure YOUR name stays on YOUR music" |
| fig-rm-04 | "Mogen & Andy's Day" | Mid-century user journey | Full walkthrough: check credits, fix errors, approve AI request | "This is what using the system actually feels like" |

### Architecture Docs (4 figures) - THE TECHNICAL WING

| ID | Title | Style | Audience |
|----|-------|-------|----------|
| fig-arch-01 | "The Modular System" | Patent Drawing (Template H) | Developers who need architecture overview |
| fig-arch-02 | "Entity Resolution as Piano Action" | Instrument Anatomy (Template D) | Understanding how matching works |
| fig-arch-03 | "MCP: The Bouncer Protocol" | Editorial Mixed Media (Template E2) | How AI platforms request access |
| fig-arch-04 | "The Master Tape Vault" | Vintage Oscilloscope (Template F) | Database schema as archival storage |

### PRD Figures (8 figures) - THE CONTEXTUAL GALLERIES

| ID | Location | Title | Style |
|----|----------|-------|-------|
| fig-vis-01 | Vision PRD | "Mogen, Andy & Friends" | Fashion Sketch (Template E1) |
| fig-vis-02 | Vision PRD | "The Record Label as Data Model" | Patent Drawing (Template H) |
| fig-vis-03 | Vision PRD | "Consent: Yes or No" | Risograph (Template G) |
| fig-eng-01 | Attribution Engine PRD | "The Signal Chain" | Chronophotography (Template I) |
| fig-eng-02 | Attribution Engine PRD | "Layers of Provenance" | Japanese Poster (Template C) |
| fig-mcp-01 | MCP Server PRD | "Backstage, VIP, General" | Fashion Photography Collage (Template E2) |
| fig-mcp-02 | MCP Server PRD | "The Permission Check" | Risograph (Template G) |
| fig-chat-01 | Chat Interface PRD | "Conversation as Cochlea" | Anatomical + Audio hybrid |

### Supporting Figures (2 figures) - THE ARCHIVE

| ID | Location | Title | Style |
|----|----------|-------|-------|
| fig-adr-01 | ADR-0005 | "One Conductor, Not an Orchestra" | Constructivist (Template B) |
| fig-kb-01 | Knowledge Base | "The Festival Grounds" (now: specific venue layout) | Japanese Poster (Template C) |

**Total: 18 new figure specifications**

---

## Creative Brief Templates (Expanded v2.0)

### Template A: Vintage Halftone
```
STYLE: 1960s print advertising meets music journalism
- Benday dots texture
- Limited color palette (2-3 colors + black)
- Bold sans-serif headlines
- Cut-out photo elements with dot overlay
- Newspaper/magazine collage feel
TEXTURE: Halftone dots (Benday)
```

### Template B: Constructivist
```
STYLE: Rodchenko/Soviet poster meets album art
- Bold geometric shapes
- Diagonal compositions
- Red/black/cream color schemes
- Sans-serif industrial typography
- Strong visual hierarchy
TEXTURE: Clean vector (no texture)
```

### Template C: Japanese Poster
```
STYLE: Tadanori Yokoo / Showa-era educational
- Vibrant but harmonious colors
- Symbolic/metaphorical imagery
- Grid-breaking compositions
- Mix of traditional and modern elements
- Strong graphic design principles
TEXTURE: Paper fiber texture (washi)
```

### Template D: Instrument Anatomy (Revised from "Anatomical Surrealism")
```
STYLE: Musical instrument cross-sections and mechanism diagrams
- Piano action mechanism, vocoder architecture, modular synth internals
- Cross-section views with labeled components
- Warm parchment backgrounds
- Precise linework with watercolor fills
- Instrument metaphors for system components (NOT organs)
TEXTURE: Watercolor paper, warm parchment
```

### Template E1: Fashion Sketch (Editorial)
```
STYLE: Haute couture illustration - sketch approach
- Pencil/ink sketch aesthetic
- Elongated proportions
- Gestural, incomplete lines
- Watercolor washes
- Iris van Herpen / Hussein Chalayan aesthetic
TEXTURE: Bristol board, pencil grain
```

### Template E2: Fashion Photography Collage
```
STYLE: Haute couture illustration - collage approach
- Cut-out runway/performance photos
- Magazine tear sheet aesthetic
- Bold typography overlay
- High contrast B&W with color accents
TEXTURE: Magazine paper, glossy/matte mix
```

### Template F: Vintage Oscilloscope
```
STYLE: 1950s Bell Labs documentation
- Phosphorescent green on dark (ONLY exception to warm backgrounds)
- Waveform photography
- Technical annotation style
- Scientific instrument aesthetic
- Authentic period typography
TEXTURE: Phosphorescent glow
```

### Template G: Risograph/Zine (NEW)
```
STYLE: DIY indie music scene, limited-run prints
- 2-3 spot color misregistration
- Paper texture prominent
- Hand-drawn or lo-fi scanned elements
- Imperfect, human, authentic
- Grassroots movement feel
TEXTURE: Risograph ink spread, newsprint
```

### Template H: Technical Patent Drawing (NEW)
```
STYLE: 19th-century engineering documentation
- Isometric exploded views
- Fine cross-hatching
- Numbered callouts with leader lines
- Cream/sepia parchment background
- Elegant hand-lettered labels
TEXTURE: Aged parchment, ink stipple
```

### Template I: Chronophotography/Motion Study (NEW)
```
STYLE: Muybridge sequential photography
- Multiple exposure layering
- Grid composition
- Scientific measurement overlays
- Movement through time/states
- Perfect for state transitions and workflows
TEXTURE: Grain/noise film texture
```

---

## Curation Sequence

### Gallery 1: The Opening (4 figures) - ESSENTIAL
The README figures that every visitor sees first.
- fig-rm-01: "Where Credits Go to Die"
- fig-rm-02: "Sound Sources Unite"
- fig-rm-03: "From Unknown to Verified"
- fig-rm-04: "Mogen & Andy's Day"

### Gallery 2: The Context (8 figures) - SUPPORTING
PRD figures for those who want to understand the product deeper.
- Vision: fig-vis-01, fig-vis-02, fig-vis-03
- Attribution Engine: fig-eng-01, fig-eng-02
- MCP Server: fig-mcp-01, fig-mcp-02
- Chat: fig-chat-01

### Gallery 3: The Technical Wing (4 figures) - CONTEXTUAL
Architecture figures for developers and technical partners.
- fig-arch-01 through fig-arch-04

### Gallery 4: The Archive (2 figures) - REFERENCE
Supporting materials for deep research.
- fig-adr-01, fig-kb-01

---

## Individual Figure Plan Requirements

Each figure plan in `/docs/figures/figure-plans/` MUST include:

1. **Metadata**: ID, title, audience, location, gallery assignment
2. **Unique Style Declaration**: Which template (A-I) and texture treatment
3. **Narrative Beat**: Where does this figure fit in "Hide and Seek's Journey"?
4. **"Why Should I Care?"**: One sentence explaining relevance to artists
5. **"Explain It to a Label Exec"**: One sentence Mogen could say pointing at this figure
6. **Mogen/Andy Personalization**: How they appear or are referenced (or explicit reason if absent)
7. **Visual Concept**: ASCII layout + narrative description
8. **Content Elements**: Structured list with semantic meaning
9. **Text Content**: All labels (max 30 chars), callouts, captions
10. **Style-Specific Prompt**: Tailored for Nano Banana Pro
11. **Negative Prompt**: Style-specific exclusions + banned aesthetics
12. **Alt Text**: Accessibility description
13. **Musical/Industry References**: Specific instruments, venues, artists to evoke

### Visual Diversity Matrix Check

Before finalizing, each figure must be checked against neighbors:

| Check | Rule |
|-------|------|
| Primary Color | No two adjacent figures share same dominant color |
| Era Reference | No two adjacent figures reference same decade |
| Texture | No two adjacent figures use same texture treatment |
| Human Figures | Vary presence of people across the gallery |

---

## Curatorial Questions

Before hanging each piece in the gallery:

1. **The Mogen Test**: Can Mogen explain this to a label executive in one sentence while pointing at this image?
2. **The Gallery Walk**: When viewed in sequence, do the figures tell the story of "Hide and Seek's Journey"?
3. **The Authenticity Check**: Would Andy, with 25+ years of album art direction, consider this exhibition-worthy?
4. **The Anti-Tech-Bro Check**: Would this look at home in a music industry trade publication, NOT a startup pitch deck?
5. **The Style Variety Check**: Could this gallery be mistaken for a single-artist show, or does it celebrate diverse visual voices?
6. **The Accessibility Check**: Can someone who has never seen a database schema understand why this matters to artists?

---

## From Blueprint to Gallery

1. **COMPLETED**: Reviewer feedback incorporated (v2.0)
2. **IN PROGRESS**: Create individual figure plan .md files
3. **NEXT**: Generate figures via Nano Banana Pro
4. **FINAL**: Integrate into documentation

---

*This plan celebrates the creative industry audience by treating documentation as exhibition-worthy art, not corporate obligation. Each figure should feel like it belongs in a gallery about the future of music attribution—curated by artists, for artists.*
