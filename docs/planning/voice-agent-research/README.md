# Voice Agent Research

**Last Updated:** 2026-02-20
**Scope:** Comprehensive literature review and technology assessment for the premium voice agent feature.

## Documents

### Core Research

| Document | Focus | Audience |
|----------|-------|----------|
| [voice-ai-infrastructure.md](voice-ai-infrastructure.md) | Production voice AI stack: STT, TTS, frameworks, transport | L3-L4 Engineers |
| [academic-papers.md](academic-papers.md) | Research papers Jan 2025 - Feb 2026: architectures, evaluation, ethics | L2-L4 Researchers |
| [finops-economics.md](finops-economics.md) | Cost analysis, pricing, optimization strategies, the AI companion cost trap | L1-L3 Business/Engineering |
| [leaderboards-evaluation.md](leaderboards-evaluation.md) | Benchmarks, leaderboards, evaluation gaps, field evolution | L2-L4 Researchers/Engineers |
| [recommended-stack.md](recommended-stack.md) | Final recommendation for music attribution voice agent MVP | L3 Engineers |

### Persona Coherence (`persona-coherence/`)

| Document | Focus | Audience |
|----------|-------|----------|
| [persona-coherence-literature-review.md](persona-coherence/persona-coherence-literature-review.md) | Comprehensive survey of persona coherence research: five-dimension architecture, activation space control, multi-turn drift dynamics, evaluation frameworks | L3-L4 Engineers/Researchers |
| [commercial-tools-landscape.md](persona-coherence/commercial-tools-landscape.md) | Agent memory systems (Letta, Zep, Mem0), guardrails (NeMo), evaluation (PersonaGym, EchoMode), recommended tool stack composition | L3 Engineers |
| [drift-detection-methods.md](persona-coherence/drift-detection-methods.md) | The 8-turn drift cliff, voice-specific amplifiers, 5 detection paradigms, 4 mitigation families, bounded-equilibrium theory | L3-L4 Engineers |
| [hyperpersonalization-frameworks.md](persona-coherence/hyperpersonalization-frameworks.md) | Memory architectures, over-personalization failure modes (OP-Bench, PS-Bench), PRAC3 consent framework, power user economics trap | L2-L4 Engineers/Business |

## Recommended Hybrid Architecture

Based on the persona coherence research, the recommended phased approach is:

### Phase I-II: MVP Voice Agent
- **Stack**: PydanticAI + Pipecat + Deepgram Nova-3 + Cartesia
- **Persona**: Prompt-layered with periodic reinforcement (every 5 turns)
- **Memory**: Session-only or abstract category-level (Puda-style)
- **Voice**: System TTS voice (no cloning)
- **Monitoring**: Embedding cosine similarity (minimal overhead)
- **Cost**: ~$0.09-0.10/minute (voice), $0.001-0.01/turn (text)

### Phase III: Advanced Persona
- **Add**: Letta/MemGPT memory-anchored persona (read-only persona blocks)
- **Add**: EchoMode SyncScore drift detection (Apache 2.0, production-ready)
- **Add**: NeMo Guardrails for topic/response/safety rails
- **Memory**: Abstract memory with factual grounding gate (prevents sycophancy)
- **Key Finding**: Abstract memory retains 97.2% personalization effectiveness while reducing attack surface by up to 244% vs detailed memory (Puda/PS-Bench)

### Phase IV: Digital Twin
- **Add**: ElevenLabs Professional voice cloning (artist consent required)
- **Add**: Multi-dimensional drift monitoring (identity/facts/style/boundaries)
- **Add**: Cross-channel shared memory store
- **Consent**: NO FAKES Act compliance — 70-year post-mortem protection, DMCA takedown
- **Revenue**: Artist voice as premium tier ($49-99/mo Pro plan)

## PRD Decision Nodes

The persona coherence research produced 5 new PRD decision nodes (v3.1.0):

| Node | Level | Recommended Option | Key Trade-off |
|------|-------|-------------------|---------------|
| `persona_coherence_strategy` | L2 Architecture | Memory-Anchored (Letta) | Accessibility vs. robustness — prompt-layered simple but drifts after 8 turns |
| `user_modeling_strategy` | L3 Implementation | Abstract Memory (Puda-style) | Safety vs. fidelity — 97.2% effective at most restrictive privacy tier |
| `voice_persona_management` | L3 Implementation | System Voice Only (Phase I-III) | Quality vs. cost — voice adds 10-50x cost multiplier over text |
| `cross_channel_state_strategy` | L3 Implementation | Shared Memory Store | Coherence vs. simplicity — centralized state with channel adapters |
| `persona_drift_monitoring` | L5 Operations | EchoMode SyncScore | Observability vs. operational cost — continuous signal without model internals |

See `docs/prd/decisions/` for full decision node YAML files.

## Context

This research extends the existing PRD at `docs/prd/voice-agent/toc-voice-agent.md` with deep technical assessment. The PRD establishes the dual-purpose voice agent (attribution gathering + digital twin). This research provides the evidence base for technology selection, cost modeling, and phased implementation.

## Related

- **PRD Decision Network**: `docs/prd/decisions/` (v3.1.0 — 5 persona nodes added)
- **PRD Voice Agent**: `docs/prd/voice-agent/toc-voice-agent.md`
- **Figure Plans**: `docs/figures/repo-figures/figure-plans/fig-voice-*.md` (32 voice figures), `fig-persona-*.md` (30 persona figures)
- **Figure Assets**: `docs/figures/repo-figures/assets/` (62 optimized JPEGs)
- **Tutorial**: `docs/tutorials/voice-agent-implementation.md`
- **Manuscript**: Teikari, P. (2026). *Music Attribution with Transparent Confidence*. SSRN No. 6109087.
