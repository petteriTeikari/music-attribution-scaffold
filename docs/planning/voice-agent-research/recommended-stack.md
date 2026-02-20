# Recommended Voice Agent Stack for Music Attribution

**Last Updated:** 2026-02-20
**Status:** Recommendation based on comprehensive research (see sibling documents)
**Context:** Extends existing MVP text agent (PydanticAI + Haiku 4.5 + CopilotKit AG-UI)

---

## Executive Summary

The music attribution scaffold already has a working text-based conversational agent (PydanticAI with 4 tools, AG-UI streaming via CopilotKit). Adding voice requires wrapping this agent in a voice pipeline. The recommended approach uses **Pipecat** as the orchestration framework, adding STT and TTS around the existing LLM agent.

**Estimated MVP cost:** $0.05-0.08/min (mid-tier), dropping to $0.01-0.02/min with self-hosted components.

---

## Recommended Stack

### Layer 1: Framework — Pipecat

| Aspect | Details |
|--------|---------|
| **Choice** | [Pipecat](https://github.com/pipecat-ai/pipecat) (Daily.co) |
| **Why** | Python-native (matches PydanticAI backend), 40+ service plugins, BSD license, most widely used open-source voice agent framework |
| **Alternative** | LiveKit Agents — stronger if WebRTC is primary transport and you need managed telephony |
| **Rejected** | Managed platforms (Retell, Vapi) — too opaque for a scaffold that needs to demonstrate internals |

**Integration path:** Pipecat's `FrameProcessor` pipeline wraps the existing PydanticAI agent as a service. The agent receives text from STT and returns text to TTS, preserving all existing tool-calling logic.

### Layer 2: Speech-to-Text — Deepgram Nova-3 / Flux

| Aspect | Details |
|--------|---------|
| **Primary** | [Deepgram Nova-3](https://deepgram.com/learn/introducing-nova-3-speech-to-text-api) for accuracy (5.26% WER batch) |
| **Upgrade** | [Deepgram Flux](https://deepgram.com/learn/introducing-flux-conversational-speech-recognition) for conversational speech recognition (260ms end-of-turn) |
| **Self-hosted fallback** | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) — 4x faster than Whisper, self-hostable, zero per-minute cost |
| **Edge future** | [Moonshine](https://github.com/moonshine-ai/moonshine) — 27M-400MB, 5-15x faster than Whisper, for mobile apps |
| **Cost** | $0.0077/min (PAYG), $0.0065/min (Growth) |

**Why Deepgram:** Best production accuracy, native Pipecat plugin, Flux CSR eliminates separate VAD+endpointing. The music domain demands accurate transcription of artist names, track titles, and ISRC codes — Deepgram's WER lead matters here.

### Layer 3: Language Model — Existing PydanticAI Agent

| Aspect | Details |
|--------|---------|
| **Primary** | Existing PydanticAI agent with `anthropic:claude-haiku-4-5` |
| **Escalation** | FallbackModel to Sonnet 4.5 for complex queries |
| **Config** | `ATTRIBUTION_AGENT_MODEL` env var (already implemented) |
| **Cost** | ~$0.003/min (Haiku), ~$0.06/min (Sonnet escalation) |

**No change needed.** The voice pipeline sends transcribed text to the same agent that handles text chat. All 4 tools (query attribution, check permissions, suggest corrections, explain confidence) work unchanged.

### Layer 4: Text-to-Speech — Cartesia Sonic + Orpheus Fallback

| Aspect | Details |
|--------|---------|
| **Primary** | [Cartesia Sonic 3](https://cartesia.ai/sonic) — 90ms TTFA, lowest latency commercial TTS |
| **Turbo option** | Cartesia Sonic Turbo — 40ms TTFA for ultra-responsive mode |
| **Self-hosted fallback** | [Orpheus TTS](https://github.com/canopyai/Orpheus-TTS) — Apache 2.0, 3B params, emotional tags, ~200ms streaming |
| **Budget fallback** | [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) — Apache 2.0, <0.3s, <1GB VRAM, ~$0.06/hr |
| **Digital twin** | [ElevenLabs Professional Voice Clone](https://elevenlabs.io/) — for artist voice replication (Phase IV) |
| **Cost** | Cartesia: ~$0.02-0.03/min, Orpheus self-hosted: ~$0.001/min |

**Why Cartesia for MVP:** Lowest latency is critical for natural conversation. The 40-90ms TTFA keeps total pipeline under 500ms. Orpheus provides the Apache 2.0 self-hosted path for cost optimization at scale.

**Why ElevenLabs for Digital Twin:** Voice cloning quality matters for artist personas. ElevenLabs Professional cloning is the industry standard. This is a Phase IV feature, not MVP.

### Layer 5: Transport — WebRTC via Daily.co

| Aspect | Details |
|--------|---------|
| **Choice** | WebRTC via [Daily.co](https://www.daily.co/) (Pipecat native) |
| **Why** | Sub-30ms transport, built-in echo cancellation and noise suppression, browser-native |
| **Alternative** | WebSocket — simpler but +50-100ms latency |

### Layer 6: Turn Detection — Pipecat Smart Turn

| Aspect | Details |
|--------|---------|
| **Choice** | [Pipecat Smart Turn](https://docs.pipecat.ai/) — open-source semantic turn detection |
| **Backup** | Silero VAD — 87.7% TPR, RTF 0.004, reliable fallback |
| **Future** | Deepgram Flux CSR — eliminates separate turn detection entirely |

### Layer 7: Voice Activity Detection — Silero VAD

| Aspect | Details |
|--------|---------|
| **Choice** | [Silero VAD](https://github.com/snakers4/silero-vad) — pre-trained, enterprise-grade, open-source |
| **Specs** | 87.7% TPR at 5% FPR, processes 1hr in 15.4s on CPU |
| **Integration** | Native Pipecat and LiveKit plugins available |

---

## Cost Model

### Standard Tier (Mid-Range)

| Component | Provider | Cost/Min |
|-----------|----------|----------|
| STT | Deepgram Nova-3 | $0.0077 |
| LLM | Haiku 4.5 | $0.003 |
| TTS | Cartesia Sonic | $0.025 |
| Transport | Daily.co | $0.004 |
| VAD + Turn | Silero + Smart Turn | $0.000 |
| **Total** | | **~$0.040/min** |

### Premium Tier (Digital Twin)

| Component | Provider | Cost/Min |
|-----------|----------|----------|
| STT | Deepgram Flux | $0.010 |
| LLM | Sonnet 4.5 (escalation) | $0.060 |
| TTS | ElevenLabs Flash v2.5 | $0.080 |
| Transport | Daily.co | $0.004 |
| **Total** | | **~$0.154/min** |

### Budget Tier (Self-Hosted)

| Component | Provider | Cost/Min |
|-----------|----------|----------|
| STT | faster-whisper (self-hosted) | ~$0.001 |
| LLM | Haiku 4.5 | $0.003 |
| TTS | Orpheus/Kokoro (self-hosted) | ~$0.001 |
| Transport | WebSocket (self-hosted) | $0.000 |
| **Total** | | **~$0.005/min** |

### Monthly Projections

| Scenario | Sessions/Day | Avg Duration | Monthly Cost (Standard) | Monthly Cost (Budget) |
|----------|-------------|-------------|------------------------|----------------------|
| Early MVP | 50 | 5 min | $300 | $38 |
| Growing | 200 | 5 min | $1,200 | $150 |
| Scale | 1,000 | 5 min | $6,000 | $750 |

---

## Implementation Phases

### Phase I: Voice Input Only (Month 1-2)

**Goal:** Artists can speak to the existing text agent. No TTS yet — responses displayed as text.

- Add Pipecat with Deepgram STT plugin
- Route transcribed text to existing PydanticAI agent
- Display agent responses in CopilotKit sidebar (text)
- **Cost:** STT only = ~$0.008/min
- **Complexity:** Low — no TTS, no turn detection needed

### Phase II: System Voice Response (Month 2-3)

**Goal:** Agent responds with synthesized speech (system voice, not artist clone).

- Add Cartesia Sonic TTS plugin to Pipecat pipeline
- Implement basic turn detection (Silero VAD)
- WebRTC transport via Daily.co
- **Cost:** STT + TTS = ~$0.035/min
- **Complexity:** Medium — need turn detection and audio streaming

### Phase III: Natural Conversation (Month 3-4)

**Goal:** Conversation feels natural — proper interruption handling, backchanneling.

- Upgrade to Pipecat Smart Turn semantic detection
- Implement interruption handling
- Add context management (conversation history)
- Optimize latency budget (<500ms target)
- **Cost:** Same as Phase II
- **Complexity:** Medium-High — turn-taking is the hardest UX problem

### Phase IV: Digital Twin (Month 4-6)

**Goal:** Artist voice clone for fan interactions and promotional experiences.

- ElevenLabs Professional Voice Cloning for artist persona
- Implement persona management (attribution agent vs digital twin)
- Voice consent framework (Level 1/2/3)
- Content safety filters for digital twin responses
- **Cost:** ~$0.10-0.15/min for digital twin sessions
- **Complexity:** High — consent framework, persona switching, safety

### Phase V: Premium Features (Month 6+)

**Goal:** Differentiated premium experience.

- Emotional TTS (Orpheus tags for confidence signaling)
- Multi-language support
- On-device STT/TTS for cost reduction at scale
- Voice verification for A3 assurance (ASVspoof-grade)
- Fan interaction analytics
- **Cost:** Variable — on-device reduces to ~$0.005/min
- **Complexity:** High — multi-language, edge deployment

---

## Architecture Decision Records

### ADR-1: Pipecat over LiveKit Agents

**Context:** Both are production-ready open-source voice agent frameworks.
**Decision:** Pipecat
**Rationale:**
1. Python-native matches existing PydanticAI/FastAPI backend
2. Service plugin architecture (40+) allows swapping STT/TTS without code changes
3. BSD license (LiveKit is Apache 2.0 — both permissive)
4. Pipecat Flows for conversation state management
5. Daily.co transport is battle-tested

**Tradeoff:** LiveKit's agent-as-participant model is arguably more elegant for WebRTC, and their managed Cloud Agents product is more mature. If telephony (PSTN/SIP) becomes important, LiveKit's Telephony 1.0 is ahead.

### ADR-2: Deepgram over Whisper for Production STT

**Context:** Self-hosted Whisper is free; Deepgram charges per minute.
**Decision:** Deepgram Nova-3 for production, faster-whisper for self-hosted fallback
**Rationale:**
1. Nova-3 achieves 5.26% WER (batch) — 36% lower than Whisper
2. Flux CSR eliminates separate VAD+endpointing (simplifies pipeline)
3. $0.0077/min is affordable for MVP volumes
4. Music domain demands highest accuracy for artist names, ISRCs
5. Self-hosted whisper available as budget fallback

**Tradeoff:** Vendor dependency on Deepgram. Mitigation: faster-whisper fallback path tested and documented.

### ADR-3: Cartesia over ElevenLabs for System Voice TTS

**Context:** ElevenLabs is the quality leader; Cartesia is the latency leader.
**Decision:** Cartesia Sonic for system voice, ElevenLabs for digital twin only
**Rationale:**
1. 40-90ms TTFA vs ElevenLabs ~75ms (Cartesia wins on P99)
2. SSM architecture provides consistent latency from SF to Tokyo
3. Lower cost (~$0.025/min vs ~$0.08/min)
4. System voice doesn't need ElevenLabs' expressiveness
5. Digital twin DOES need ElevenLabs voice cloning quality

**Tradeoff:** Cartesia has 500 char limit per request (vs ElevenLabs' 40K). For long responses, need chunking. ElevenLabs' Conversational AI 2.0 is a more complete managed solution.

### ADR-4: Orpheus as Self-Hosted TTS Fallback

**Context:** Need an open-source TTS for cost optimization.
**Decision:** Orpheus TTS (Apache 2.0) as primary self-hosted, Kokoro-82M as ultra-light option
**Rationale:**
1. Apache 2.0 license (commercial use OK)
2. Emotional tags (<laugh>, <sigh>) for confidence signaling
3. ~200ms streaming latency is production-viable
4. 3B params on Llama backbone — familiar deployment pattern
5. Kokoro-82M at 82M params runs on <1GB VRAM for budget deployments

---

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Deepgram pricing increase | Cost spike | faster-whisper fallback ready |
| Cartesia 500 char limit | Long response truncation | Response chunking in Pipecat |
| ElevenLabs voice clone quality | Artist dissatisfaction | Evaluate multiple providers before Phase IV |
| Turn detection false positives | Conversation frustration | Tune Smart Turn thresholds per persona |
| Music vocabulary STT errors | Wrong artist names | Custom vocabulary/dictionary (Deepgram feature) |
| EU AI Act compliance | Legal risk | Implement disclosure from Phase I |
| Power user cost spiral | FinOps problem | Per-user daily caps + tiered pricing |

---

## Key Sources

- [Pipecat Documentation](https://docs.pipecat.ai/)
- [Deepgram Nova-3](https://deepgram.com/learn/introducing-nova-3-speech-to-text-api)
- [Deepgram Flux](https://deepgram.com/learn/introducing-flux-conversational-speech-recognition)
- [Cartesia Sonic 3](https://cartesia.ai/sonic)
- [Orpheus TTS](https://github.com/canopyai/Orpheus-TTS)
- [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
- [ElevenLabs Conversational AI](https://elevenlabs.io/conversational-ai)
- [Daily.co Blog: Advice on Building Voice AI](https://www.daily.co/blog/advice-on-building-voice-ai-in-june-2025/)
- [aiewf-eval Benchmark](https://github.com/kwindla/aiewf-eval)
- [Pipecat Benchmarks](https://www.daily.co/blog/benchmarking-llms-for-voice-agent-use-cases/)
