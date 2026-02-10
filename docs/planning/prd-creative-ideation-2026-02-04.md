# PRD: Creative Ideation & Diversity Enhancement

**Date**: 2026-02-04
**Status**: Draft
**Author**: AI-assisted

## Overview

This PRD explores techniques for enhancing creative diversity and idea generation quality in LLM-powered systems, with application to the attribution engine and voice agent capabilities.

## Problem Statement

Large Language Models exhibit a tendency toward creative homogenization—generating outputs that converge on similar patterns, reducing diversity in brainstorming, problem-solving, and creative tasks. This affects:

1. **Attribution Engine**: Generating diverse hypotheses for uncertain metadata
2. **Voice Agent Digital Twin**: Creative responses that feel authentic and varied
3. **Gap Analysis**: Identifying non-obvious connections in music metadata

## Literature Foundation

### Core Paper

- **meincke-2024-prompting-diverse-ideas-ai-variance-cot.md** - Primary inspiration examining prompting strategies for diverse idea generation with Chain-of-Thought variance techniques

### Supporting Research

The following papers provide additional context on LLM creativity limitations and enhancement strategies:

| Paper | Focus Area |
|-------|------------|
| meincke-2024-prompting-diverse-ideas-ai-variance.md | Base variance prompting techniques |
| boussioux-2023-crowdless-future-generative-ai-problem-solving.md | AI replacing crowd-sourced problem solving |
| haase-2025-llm-creativity-peaked.md | Limitations of LLM creative capacity |
| ito-2024-collaborative-brainstorming-ibis-ai.md | IBIS-based collaborative AI brainstorming |
| keon-2025-galton-law-mediocrity-llm-creativity.md | Statistical regression to mean in LLM outputs |
| maiden-2025-computational-model-novel-innovation.md | Computational models for novel idea generation |
| moon-2025-homogenizing-effect-llm-creative-diversity.md | Homogenization effects in creative tasks |
| wenger-2025-creative-homogeneity-across-llms.md | Cross-model homogeneity patterns |
| yu-2025-think-llm-think-aloud.md | Think-aloud protocols for LLM reasoning |

## Proposed Solutions

### 1. Variance-Enhanced Prompting

Implement CoT-variance techniques to increase output diversity:

```yaml
strategies:
  - explicit_diversity_instructions: true
  - temperature_scheduling: [0.7, 0.9, 1.1]
  - persona_rotation: true
  - constraint_randomization: true
```

### 2. Multi-Perspective Generation

Generate ideas from multiple simulated viewpoints:
- Genre-specific personas (jazz historian, rock critic, electronic producer)
- Temporal perspectives (1970s context, contemporary, futurist)
- Cultural lenses (regional, global, subculture-specific)

### 3. Divergence Scoring

Measure and optimize for output diversity:
- Semantic distance between generated hypotheses
- Lexical diversity metrics
- Structural variation analysis

### 4. IBIS-Inspired Structuring

Apply Issue-Based Information System patterns:
- Issue → Position → Argument hierarchies
- Explicit pro/con generation
- Forced alternative enumeration

## Integration Points

### Attribution Engine

```
cross_refs:
  - attribution-engine/confidence-scoring.md
  - attribution-engine/multi-source-aggregation.md
```

When confidence is LOW, use diversity-enhanced generation to:
- Propose multiple attribution hypotheses
- Generate alternative metadata interpretations
- Identify potential gaps in source coverage

### Voice Agent Digital Twin

```
cross_refs:
  - voice-agent/toc-voice-agent.md
```

Apply variance techniques to:
- Response generation for creative queries
- Storytelling and anecdote variation
- Authentic personality expression

### Uncertainty Handling

```
cross_refs:
  - uncertainty/toc-uncertainty.md
```

Diversity enhancement supports uncertainty communication by:
- Generating multiple plausible explanations
- Avoiding false confidence in creative domains
- Supporting "I don't know but here are possibilities" patterns

## Success Metrics

| Metric | Target |
|--------|--------|
| Semantic diversity score | >0.7 (normalized) |
| User-perceived novelty | >4/5 rating |
| Hypothesis coverage | >3 distinct alternatives per query |
| Homogenization index | <0.3 (lower is better) |

## Implementation Phases

### Phase 1: Research Synthesis
- Deep analysis of all cited papers
- Extract actionable prompting patterns
- Document homogenization risks

### Phase 2: Prototype Development
- Implement variance-enhanced prompt templates
- Build diversity scoring module
- Create A/B testing framework

### Phase 3: Integration
- Connect to attribution engine confidence triage
- Implement in voice agent response generation
- Add observability for diversity metrics

## References

All source materials located in `docs/knowledge-base/sources/`:

1. meincke-2024-prompting-diverse-ideas-ai-variance-cot.md
2. meincke-2024-prompting-diverse-ideas-ai-variance.md
3. boussioux-2023-crowdless-future-generative-ai-problem-solving.md
4. haase-2025-llm-creativity-peaked.md
5. ito-2024-collaborative-brainstorming-ibis-ai.md
6. keon-2025-galton-law-mediocrity-llm-creativity.md
7. maiden-2025-computational-model-novel-innovation.md
8. moon-2025-homogenizing-effect-llm-creative-diversity.md
9. wenger-2025-creative-homogeneity-across-llms.md
10. yu-2025-think-llm-think-aloud.md

---

## Iterated Divergent LLM Council

### Verbatim User Prompt (2026-02-04)

> So the /home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/planning/prd-creative-ideation-2026-02-04.md plan was meant as an inspiration for a divergent creative "Iterated LLM Council" (/home/petteri/Dropbox/github-personal/sci-llm-writer/.claude/skills/iterated-llm-council), with the Ralph Wiggum loop now optimizing for creative, divergent, orthogonal ideas and improvements for our open-ended PRD ideation so that we a lot of options in our multi-hypothesis planning so that we can be flexible, lean and agile (the buzzwords for quick reactions to the changing world). Add this as verbatim to the plan, and let's plan how to actually run this iterated divergent ideation plan with reviewer agents then optimizing the actionable exeution plan! We are running out of token so let's not yet run this plan, and after the planning let's create a Github Issue that has full context in the .md and a plan that can be run with cold-start (full context) for some future PR then!

### Concept: Ralph Wiggum for Divergent PRD Ideation

The original Iterated LLM Council is designed for **convergent refinement** (manuscript → publication quality). We invert this for **divergent ideation**:

| Original Council | Divergent Ideation Council |
|------------------|---------------------------|
| Converge to consensus | Maximize divergence |
| Reduce issues to zero | Generate maximum orthogonal ideas |
| Quality target: ACCEPT | Quality target: MAXIMUM_OPTIONS |
| Stop when: issues = 0 | Stop when: diminishing novelty |
| Reviewers find problems | Ideators generate possibilities |

### Adapted Workflow

```
Iteration N:
  1. D3: Spawn DIVERGENT ideator agents    → See "Ideator Personas" below
  2. D2: Synthesize ALL ideas (no filtering)
  3. D1: Score for NOVELTY + ORTHOGONALITY (not quality)
  4. D0: Generate PRD hypothesis branches
  5. CHECKPOINT: Git commit ideas
  6. CONVERGE? Check diminishing returns
     If novelty drops: DONE (we have enough options)
     If still novel: Iteration N+1
```

### Ideator Personas (D3 Agents)

Instead of domain expert reviewers, spawn **creative ideators**:

| Persona | Role | Optimization Target |
|---------|------|---------------------|
| **Contrarian** | Challenge all assumptions | Orthogonality |
| **Futurist** | 5-year horizon thinking | Long-term flexibility |
| **Minimalist** | Simplest possible approach | Lean options |
| **Maximalist** | Kitchen-sink features | Comprehensive options |
| **User Advocate** | Artist/creator perspective | UX diversity |
| **Tech Skeptic** | Question every technology choice | Alternative stacks |
| **Business Hawk** | Revenue/sustainability focus | Commercial viability |

### Novelty Scoring (D1)

Instead of publication quality, score for:

```yaml
novelty_metrics:
  semantic_distance: 0-1  # From existing PRD ideas
  orthogonality: 0-1      # Independence from other ideas
  actionability: 0-1      # Can be turned into PRD branch
  risk_profile: "safe|moderate|bold"

convergence_criteria:
  stop_when:
    - avg_novelty < 0.3 for 2 consecutive iterations
    - total_unique_ideas > 50
    - all_personas_repeat_themes: true
```

### Output: Multi-Hypothesis PRD Branches

Each iteration produces candidate PRD branches:

```
docs/prd/
├── hypotheses/
│   ├── iter-1/
│   │   ├── contrarian-no-graph-db.md
│   │   ├── futurist-decentralized-attribution.md
│   │   └── minimalist-metadata-api-only.md
│   ├── iter-2/
│   │   ├── maximalist-full-voice-platform.md
│   │   ├── tech-skeptic-sqlite-everything.md
│   │   └── business-hawk-freemium-model.md
│   └── synthesis/
│       └── final-hypothesis-matrix.md
```

### Execution Plan for Future PR

```bash
# Cold-start execution (full context provided)

# 1. Load context
cat docs/planning/prd-creative-ideation-2026-02-04.md
cat docs/planning/prd-improvement-for-hierarchical-composable-plan.md

# 2. Load source papers (for techniques)
ls docs/knowledge-base/sources/*.md

# 3. Run divergent council
# - Spawn D3 ideator agents (Task tool with different personas)
# - Each ideator reviews current PRD structure
# - Each generates 3-5 orthogonal improvement ideas
# - D2 collects ALL ideas (no filtering!)
# - D1 scores novelty/orthogonality
# - D0 generates PRD branch files

# 4. Iterate until diminishing novelty
# - Track semantic distance between iterations
# - Stop when ideas start repeating

# 5. Final synthesis
# - Create hypothesis matrix
# - Map to specification change scenarios
# - Document trade-offs for each path
```

### Expected Outputs

1. **50+ unique PRD hypothesis branches** across domains
2. **Hypothesis matrix** mapping ideas to specification changes
3. **Trade-off documentation** for lean/agile pivoting
4. **Divergence metrics** showing idea space coverage

---

## Next Steps

1. ~~Conduct detailed analysis of each paper (Phase 2)~~ → Defer to council
2. ~~Extract specific prompting techniques~~ → Let ideators discover
3. **Create GitHub Issue** with full cold-start context
4. **Run Divergent Council** in future PR with fresh context
5. **Synthesize** into actionable PRD hypothesis matrix
