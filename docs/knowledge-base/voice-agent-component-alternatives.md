# Voice Agent Component Alternatives

Comprehensive comparison of voice pipeline components for the Music Attribution Scaffold voice agent. Each component row includes the open-source default (used when no API keys are configured) and up to three alternatives spanning commercial APIs and managed services.

**Last Updated:** 2026-02-20
**Companion to:** Teikari, P. (2026). *Music Attribution with Transparent Confidence*. SSRN No. 6109087.
**Implementation:** `src/music_attribution/voice/` (config, pipeline, persona, drift, tools, server)
**PRD Node:** `docs/prd/decisions/L3-implementation/voice-agent-stack.decision.yaml`

---

## 1. Component Comparison Matrix

### 1.1 Speech-to-Text (STT)

| Dimension | **faster-whisper** (Default) | **Deepgram Nova-3** | **AssemblyAI Universal** | **Whisper.cpp** |
|-----------|------------------------------|---------------------|--------------------------|-----------------|
| **License** | MIT | Commercial (API) | Commercial (API) | MIT |
| **Cost** | $0.00/min (self-hosted) | $0.0077/min (PAYG), $0.0065/min (Growth) | $0.0025/min | $0.00/min (self-hosted) |
| **Latency** | ~200-400ms (GPU-dependent) | ~150ms streaming, ~260ms end-of-turn (Flux) | ~200-300ms streaming | ~300-600ms (CPU-dependent) |
| **Quality (WER)** | 5.26% batch (Whisper Large V3 weights) | 5.26% batch, 6.84% streaming | Competitive with Nova-3 on English | Identical to Whisper (same weights) |
| **Music Domain Vocab** | Good -- handles artist names, but no custom vocabulary | Best -- custom vocabulary/dictionary feature for ISRCs, artist names | Good -- custom vocabulary available | Good -- same as Whisper |
| **Pipecat Integration** | Native: `pipecat-ai[whisper]` | Native: `pipecat-ai[deepgram]` | Native: `pipecat-ai[assemblyai]` | Not native -- requires custom FrameProcessor |
| **Installation** | `uv sync --group voice` | `uv add pipecat-ai[deepgram]` + `VOICE_DEEPGRAM_API_KEY` | `uv add pipecat-ai[assemblyai]` + `VOICE_ASSEMBLYAI_API_KEY` | Build from source or use pre-built binaries |
| **Config Enum** | `STTProvider.WHISPER` | `STTProvider.DEEPGRAM` | `STTProvider.ASSEMBLYAI` | Not in scaffold config (manual integration) |
| **Strengths** | Zero cost, self-hostable, 4x faster than base Whisper via CTranslate2 + INT8 | Best production accuracy, Flux CSR eliminates separate VAD, custom vocabulary | Lowest commercial price, good accuracy | CPU-only (no GPU needed), Apple Silicon optimized, GGML quantization |
| **Weaknesses** | Requires GPU for real-time, no streaming turn detection | Vendor dependency, cost at scale (100K min = $650/mo) | Smaller ecosystem than Deepgram | Slower than faster-whisper, no native Pipecat plugin |
| **Self-Hosting** | Yes (GPU recommended) | No | No | Yes (CPU or GPU) |

**Emerging alternative:** Mistral Voxtral Mini 4B (Apache 2.0, February 2026) -- 4B parameters, 480ms streaming delay, matches commercial API accuracy. First open-source model to close the gap with Deepgram on real-time streaming.

### 1.2 Text-to-Speech (TTS)

| Dimension | **Piper** (Default) | **Kokoro-82M** | **ElevenLabs** | **Cartesia Sonic** |
|-----------|---------------------|----------------|----------------|-------------------|
| **License** | GPL-3.0 | Apache 2.0 | Commercial (API) | Commercial (API) |
| **Cost** | $0.00/min (self-hosted) | $0.00/min ($0.06/hr GPU amortized) | $0.08-0.10/min (Business/Creator) | $0.02-0.03/min |
| **Latency (TTFA)** | ~200-300ms | <300ms | ~75ms (Flash v2.5) | 40ms (Turbo), 90ms (Sonic 3) |
| **Quality** | Functional but robotic | Competitive with commercial -- #1 HuggingFace TTS Arena period | Industry leader in expressiveness, 70+ languages | High quality, SSM architecture provides consistent latency |
| **Music Domain Suitability** | Adequate for system prompts | Good for budget deployments | Best for artist digital twin (voice cloning) | Best for low-latency system voice |
| **Pipecat Integration** | Native: `pipecat-ai[piper]` | Not native -- falls back to Piper in scaffold | Native: `pipecat-ai[elevenlabs]` | Native: `pipecat-ai[cartesia]` |
| **Installation** | `uv sync --group voice-gpl` | Manual integration (HuggingFace download) | `uv add pipecat-ai[elevenlabs]` + `VOICE_ELEVENLABS_API_KEY` | `uv add pipecat-ai[cartesia]` + `VOICE_CARTESIA_API_KEY` |
| **Config Enum** | `TTSProvider.PIPER` | `TTSProvider.KOKORO` (falls back to Piper currently) | `TTSProvider.ELEVENLABS` | `TTSProvider.CARTESIA` |
| **Voice Cloning** | No | No | Yes -- Professional cloning (Creator+ tier) | Limited |
| **Emotional Tags** | No | No | Yes -- audio tags in v3 | No |
| **Strengths** | Zero cost, simple, well-tested | Apache 2.0, ultra-efficient (<1GB VRAM), CPU-viable | Voice cloning, emotional range, broadest language support | Lowest latency (40ms Turbo), SSM architecture, 5x cheaper than ElevenLabs |
| **Weaknesses** | GPL license (viral), robotic quality | Not yet a Pipecat native plugin | Expensive ($0.08/min), 500 char limit absent | 500 char limit per request (needs chunking for long responses) |
| **Self-Hosting** | Yes | Yes | No | No (on-device in private beta) |

**Additional open-source options:**
- **Orpheus TTS** (Apache 2.0, 3B params): Emotional tags (`<laugh>`, `<sigh>`), ~200ms streaming, best expressiveness among open-source. Good for confidence signaling in attribution responses.
- **Chatterbox** (MIT, 350M params, Resemble AI): #1 on HuggingFace TTS Arena, outperforms ElevenLabs in blind evals. Consumer GPU viable.
- **CosyVoice 2/3** (Apache 2.0, Alibaba): 150ms streaming, strong multilingual (CJK).

### 1.3 Voice Activity Detection (VAD)

| Dimension | **Silero VAD** (Default) | **WebRTC VAD** | **Deepgram Flux CSR** |
|-----------|--------------------------|----------------|----------------------|
| **License** | MIT | BSD | Commercial (bundled with Deepgram STT) |
| **Cost** | $0.00/min | $0.00/min | Included in Deepgram STT pricing |
| **Latency** | RTF 0.004 (250x real-time) | Lowest (legacy GMM) | ~260ms end-of-turn |
| **Quality (TPR/FPR)** | 87.7% TPR at 5% FPR | ~50% TPR, very low FPR | ~30% fewer false interruptions vs VAD-only |
| **Pipecat Integration** | Native: `pipecat-ai[silero]` | Via WebRTC transport | Native when using Deepgram STT |
| **Installation** | `uv sync --group voice` (included) | Built into browser/WebRTC stack | Automatic with `pipecat-ai[deepgram]` |
| **Semantic Turn Detection** | No (acoustic only) | No (acoustic only) | Yes -- fuses acoustic + semantic signals |
| **Strengths** | Best open-source VAD, enterprise-grade, processes 1hr audio in 15.4s on CPU | Zero overhead, fastest raw processing | Eliminates separate VAD, reduces interruptions |
| **Weaknesses** | Cannot distinguish pause-to-think from end-of-turn | Poor accuracy, legacy approach | Requires Deepgram subscription |

**Semantic turn detection alternatives** (complement VAD, do not replace it):
- **Pipecat Smart Turn**: Fully open-source semantic turn detection model. Community-validated.
- **LiveKit Semantic Turn**: Transformer-based, <25ms CPU inference, 13 languages. Open-source. Best-in-class.

### 1.4 Language Model (LLM)

| Dimension | **Ollama + Qwen3** (Default) | **Claude Haiku 4.5** | **GPT-4o-mini** | **Gemini Flash** |
|-----------|------------------------------|----------------------|-----------------|-----------------|
| **License** | Apache 2.0 (Qwen3) | Commercial (API) | Commercial (API) | Commercial (API) |
| **Cost** | $0.00/min (self-hosted) | ~$0.003/min (~1,500 tok/min) | ~$0.006/min | ~$0.001-0.002/min |
| **Latency (TTFB)** | ~100-300ms (GPU-dependent) | ~732ms (aiewf-eval) | ~760ms (aiewf-eval) | ~594ms (Gemini 2.5 Flash, aiewf-eval) |
| **Quality (aiewf-eval pass rate)** | N/A (not benchmarked) | 76.9% | 91.8% (4o-mini), 91.2% (4o) | 93.7% (2.5 Flash) |
| **Tool Calling** | Yes (OpenAI-compatible) | Yes (native) | Yes (native) | Yes (native) |
| **Music Domain Suitability** | Adequate for simple queries | Good -- existing PydanticAI agent uses this | Good general performance | Best cost/quality ratio |
| **Pipecat Integration** | Via OpenAI-compatible endpoint | Via OpenAI-compatible endpoint (Anthropic API) | Native: `pipecat-ai[openai]` | Native: `pipecat-ai[google]` |
| **Installation** | `ollama pull qwen3` (separate process) | `VOICE_LLM_MODEL=claude-haiku-4-5` + API key | Default in scaffold: `VOICE_LLM_MODEL=gpt-4o-mini` | `VOICE_LLM_MODEL=gemini-2.5-flash` + API key |
| **Strengths** | Zero API cost, full privacy, no vendor lock-in | Lowest cost commercial, already integrated in text agent | Best-benchmarked for voice agent tool calling | Cheapest commercial, fastest TTFB |
| **Weaknesses** | Requires GPU, lower quality than frontier models | Weaker on instruction following (76.9% aiewf-eval) | 2x cost of Haiku, moderate latency | Google ecosystem dependency |

**Escalation model:** The scaffold uses PydanticAI FallbackModel -- Haiku 4.5 for routine queries, automatic escalation to Sonnet 4.5 (~$0.06/min) for complex attribution analysis. Configured via `ATTRIBUTION_AGENT_MODEL` env var.

### 1.5 Transport

| Dimension | **SmallWebRTC** (Default) | **Daily WebRTC** | **LiveKit** | **Raw WebSocket** |
|-----------|---------------------------|------------------|-------------|-------------------|
| **License** | Non-commercial | Commercial (API) | Apache 2.0 (server), commercial (cloud) | N/A (standard protocol) |
| **Cost** | $0.00/min (dev only) | $0.004/min | Self-hosted: $0.00, Cloud: variable | $0.00/min |
| **Latency** | <30ms (WebRTC UDP) | <30ms (WebRTC UDP) | <30ms (WebRTC UDP) | 50-150ms (TCP) |
| **Echo Cancellation** | Built-in (WebRTC) | Built-in + Daily enhancement | Built-in (WebRTC) | Manual implementation required |
| **Pipecat Integration** | Native: `pipecat-ai[smallwebrtc]` | Native: Pipecat's primary transport | Via LiveKit Agents framework (not Pipecat) | Native: `pipecat-ai` base |
| **Installation** | `uv sync --group voice` (included) | `VOICE_DAILY_API_KEY` + Daily account | Separate framework (LiveKit Agents) | Base `pipecat-ai` package |
| **Config Enum** | `TransportType.SMALLWEBRTC` | `TransportType.DAILY` | Not in scaffold (separate framework) | `TransportType.WEBSOCKET` |
| **Telephony (SIP/PSTN)** | No | Via integrations | Native SIP trunking, DTMF, cold/warm transfers | No |
| **Strengths** | Free for development, peer-to-peer | Battle-tested, Pipecat-native, managed infrastructure | Self-hostable, best telephony, dual Python/Node.js | Simplest to implement, no ICE/STUN/TURN |
| **Weaknesses** | Non-commercial license (dev/test only) | Commercial dependency, cost at scale | Different framework (not Pipecat) | Higher latency, no echo cancellation, head-of-line blocking |
| **Self-Hosting** | Yes (dev only) | No (managed) | Yes (full self-host) | Yes |

### 1.6 Persona Management

| Dimension | **Prompt-Layered** (Default) | **Letta/MemGPT** | **Mem0** | **NeMo Guardrails** |
|-----------|------------------------------|-------------------|----------|---------------------|
| **License** | N/A (custom prompts) | Apache 2.0 | Apache 2.0 | Apache 2.0 |
| **Cost** | $0.00 | Self-hosted: $0.00, Platform: usage-based | Self-hosted: $0.00, Platform: usage-based | $0.00 (self-hosted) |
| **Architecture** | System prompt + periodic reinforcement | Memory-augmented LLM agent with structured memory blocks | User/session memory with semantic retrieval | Colang-based dialogue rails (programmable guardrails) |
| **Pipecat Integration** | Native (system prompt in pipeline) | Via REST API (scaffold: `letta_integration.py`) | Via REST API (scaffold: `mem0_integration.py`) | Via Python API (scaffold: `guardrails_integration.py`) |
| **Installation** | No extra dependencies | `uv sync --group voice-persona` | `uv sync --group voice-persona` | `uv sync --group voice-persona` |
| **Config** | `persona_enabled=false` (always active via system prompt) | `persona_enabled=true` + `VOICE_LETTA_BASE_URL` | `persona_enabled=true` + `VOICE_MEM0_API_KEY` | `guardrails_enabled=true` |
| **Cross-Session Memory** | No (stateless per session) | Yes -- persistent memory blocks | Yes -- semantic memory with user profiles | No (rail definitions are static) |
| **Drift Prevention** | Weak -- relies on prompt position and reinforcement interval | Medium -- memory retrieval grounds responses | Medium -- relevant memories injected per turn | Strong -- hard constraints on allowed topics/responses |
| **Music Domain Fit** | Adequate for MVP -- persona defined in `voice/persona.py` | Good for artist personas with long-term memory (discography, preferences) | Good for user preference learning (favorite artists, query patterns) | Good for enforcing attribution domain boundaries (no medical/legal advice) |
| **Strengths** | Zero complexity, zero latency overhead, zero dependencies | Richest memory model, self-hosted, structured + archival memory | Simplest memory API, fast retrieval, good for user modeling | Deterministic control, topic boundaries, compliance-friendly |
| **Weaknesses** | Drift after 8+ turns (Guo et al., 2025), no memory persistence | Complex deployment (separate server), learning curve | Less structured than Letta, platform dependency risk | Rigid, requires Colang learning, no adaptive personality |

### 1.7 Drift Detection

| Dimension | **Custom Embed+EWMA** (Default) | **Langfuse Traces** | **Arize Phoenix** | **Evidently** |
|-----------|----------------------------------|---------------------|-------------------|---------------|
| **License** | MIT (scaffold code) | Apache 2.0 (self-hosted), commercial (cloud) | Apache 2.0 | Apache 2.0 |
| **Cost** | $0.00 (self-hosted embeddings) | Self-hosted: $0.00, Cloud: usage-based | $0.00 (open-source) | $0.00 (open-source) |
| **Architecture** | Cosine similarity between response embeddings and persona reference, EWMA smoothing | LLM trace logging with evaluation functions | LLM observability with drift detection, embedding visualization | ML monitoring with data/concept drift detection |
| **Pipecat Integration** | Native: `DriftMonitorProcessor` in pipeline | Via trace logging (post-hoc analysis) | Via trace logging (post-hoc analysis) | Via batch analysis (not real-time) |
| **Installation** | Included in base scaffold (`voice/drift.py`) | `uv add langfuse` | `uv add arize-phoenix` | `uv add evidently` |
| **Real-Time Monitoring** | Yes -- inline pipeline processor, scores every response | Near-real-time (async trace upload) | Near-real-time (async) | Batch only |
| **Three-State Detection** | Yes: sync (>0.85), drift (0.70-0.85), desync (<0.70) | Custom via evaluation functions | Custom via drift detection APIs | Yes -- statistical drift tests |
| **Music Domain Fit** | Purpose-built for persona drift in attribution agent | General-purpose LLM observability, good for prompt iteration tracking | Good for embedding space visualization of persona drift | Better for tabular data drift than text persona drift |
| **Strengths** | Real-time, inline, zero external dependencies, EWMA smoothing prevents noise | Rich trace UI, prompt versioning, evaluation scoring, team collaboration | Open-source, embedding visualization, good for debugging drift patterns | Statistical rigor, well-tested drift detection algorithms |
| **Weaknesses** | Simple heuristic (Jaccard fallback without sentence-transformers), no UI | Not purpose-built for persona drift, requires custom evaluation logic | Heavier dependency, not designed for real-time inline use | Not designed for conversational AI, batch-oriented |

### 1.8 Evaluation

| Dimension | **DeepEval** (Default) | **Ragas** | **PersonaGym** | **Custom** |
|-----------|------------------------|-----------|----------------|------------|
| **License** | Apache 2.0 | Apache 2.0 | Research (MIT) | N/A |
| **Cost** | $0.00 (open-source) | $0.00 (open-source) | $0.00 (open-source) | $0.00 |
| **Architecture** | LLM-as-judge evaluation framework, 14+ metrics | RAG-focused evaluation (faithfulness, relevance, context recall) | Persona adherence benchmark with 6 axes | aiewf-eval methodology adapted for music domain |
| **Pipecat Integration** | Via test suite (scaffold: `tests/eval/voice/`) | Via test suite | Via test suite | Via test suite |
| **Installation** | `uv sync --group voice` (included) | `uv add ragas` | Manual (research code) | No extra dependencies |
| **Key Metrics** | Hallucination, answer relevancy, faithfulness, toxicity, bias | Faithfulness, answer relevancy, context precision/recall | Character adherence, toxicity, expected action, linguistic habits, persona consistency, knowledge accuracy | Task completion, TTFW, music-domain WER, tool-calling accuracy |
| **Music Domain Fit** | Good general-purpose eval, used in `tests/eval/voice/test_persona_fidelity.py` | Good for evaluating attribution RAG accuracy | Purpose-built for persona evaluation -- directly relevant to digital twin | Best for domain-specific needs (ISRC accuracy, confidence communication) |
| **Strengths** | Broadest metric coverage, active development, pytest integration | Best RAG evaluation framework, well-documented | Only framework specifically designed for persona consistency evaluation | Fully customizable, no external dependencies, domain-specific |
| **Weaknesses** | LLM-as-judge costs (API calls per evaluation), some metrics less relevant for voice | RAG-focused -- less relevant for conversational persona evaluation | Research-stage, limited community support | Requires building everything from scratch |

### 1.9 Framework (Orchestration)

| Dimension | **Pipecat** (Default) | **LiveKit Agents** | **Vapi** | **Custom** |
|-----------|----------------------|---------------------|----------|------------|
| **License** | BSD-2-Clause | Apache 2.0 | Commercial (managed) | N/A |
| **Cost** | $0.00 (framework) + transport/service costs | $0.00 (framework) + transport costs | $0.144/min all-in | Development time only |
| **Architecture** | Frame-based pipeline: processors connected in series, hot-swappable services | Agent-as-WebRTC-participant, worker-based scaling | Managed API: STT + LLM + TTS + telephony bundled | Direct API calls to STT/LLM/TTS |
| **Server Runtimes** | Python only | Python, Node.js | N/A (API) | Any |
| **Plugin Ecosystem** | 40+ service plugins (STT, TTS, LLM, transport) | Growing (fewer than Pipecat) | N/A (provider selection via API) | N/A |
| **Pipecat Integration** | N/A (is Pipecat) | N/A (different framework) | N/A (managed platform) | N/A |
| **Installation** | `uv sync --group voice` | `pip install livekit-agents` | API key only | Manual wiring |
| **Telephony** | Via integrations | Native SIP/PSTN, DTMF, cold/warm transfers | Built-in | Manual |
| **Turn Detection** | Smart Turn (open-source semantic) | Semantic transformer (<25ms, 13 languages) | Provider-dependent | Manual |
| **Self-Hosting** | Partial (transport via Daily for WebRTC) | Full (self-hosted LiveKit Server) | No | Full |
| **Strengths** | Largest plugin ecosystem, Python-native (matches PydanticAI backend), BSD license, Flows for conversation state | Self-hostable WebRTC, best turn detection, telephony, dual runtimes | Fastest to prototype, zero infrastructure | Full control, no dependencies |
| **Weaknesses** | Daily dependency for WebRTC, Python-only | Smaller plugin ecosystem, steeper learning curve | 2-5x more expensive than self-assembled, opaque | Must build everything: VAD, turn detection, interruption handling, streaming |

---

## 2. Cost Scenarios

Three reference configurations for the Music Attribution voice agent, from fully self-hosted to commercial production.

### 2.1 Scenario 1: Fully Open-Source Local ($0.00/min API cost)

All components self-hosted. Requires GPU infrastructure (amortized cost not included in per-minute figure).

| Component | Provider | Cost/Min | Notes |
|-----------|----------|----------|-------|
| STT | faster-whisper (MIT) | $0.000 | 4x faster than base Whisper, GPU recommended |
| TTS | Piper (GPL) or Kokoro (Apache 2.0) | $0.000 | Kokoro preferred (Apache 2.0, better quality) |
| VAD | Silero VAD (MIT) | $0.000 | CPU-only, negligible overhead |
| LLM | Ollama + Qwen3 (Apache 2.0) | $0.000 | Requires GPU; quality limited vs frontier models |
| Transport | WebSocket (self-hosted) | $0.000 | +50-100ms latency vs WebRTC |
| Persona | Prompt-layered (custom) | $0.000 | Drift after 8+ turns without reinforcement |
| Drift | Custom embed+EWMA (scaffold) | $0.000 | Jaccard fallback without sentence-transformers |
| Eval | DeepEval (Apache 2.0) | $0.000 | Requires LLM for judge (can use local Ollama) |
| Framework | Pipecat (BSD-2) | $0.000 | |
| **Total API cost** | | **$0.00/min** | |

**Infrastructure cost:** One L40S instance (~$0.87/hr = $635/mo) can serve STT + TTS + LLM for ~1,000-5,000 concurrent sessions. At 500 sessions/day x 5 min, amortized cost is approximately $0.008-0.02/min.

**Quality tradeoffs:** Lower STT accuracy than Deepgram (no custom vocabulary), robotic TTS (Piper) or good-but-not-premium TTS (Kokoro), weaker LLM reasoning than frontier models. Adequate for development, testing, and budget deployments.

**Installation:**

```bash
uv sync --group voice --group voice-gpl  # Piper (GPL) + Silero + Whisper
# OR for Apache-2.0-only stack:
uv sync --group voice  # Silero + Whisper (no Piper)
# Then manually integrate Kokoro from HuggingFace
```

### 2.2 Scenario 2: Open-Source + Anthropic (~$0.01-0.03/min)

Self-hosted STT and TTS with a commercial LLM for quality reasoning. The recommended starting point for the scaffold.

| Component | Provider | Cost/Min | Notes |
|-----------|----------|----------|-------|
| STT | faster-whisper (MIT) | $0.000 | Self-hosted, zero API cost |
| TTS | Kokoro (Apache 2.0) or Cartesia Sonic ($0.025) | $0.000-0.025 | Kokoro for budget, Cartesia for latency |
| VAD | Silero VAD (MIT) | $0.000 | |
| LLM | Claude Haiku 4.5 (Anthropic) | $0.003 | Existing PydanticAI agent, cheapest quality LLM |
| Transport | WebSocket or SmallWebRTC | $0.000 | SmallWebRTC for dev, WebSocket for simplest prod |
| Persona | Prompt-layered (custom) | $0.000 | |
| Drift | Custom embed+EWMA (scaffold) | $0.000 | |
| Eval | DeepEval (Apache 2.0) | $0.000 | |
| Framework | Pipecat (BSD-2) | $0.000 | |
| **Total (budget)** | | **~$0.003/min** | faster-whisper + Kokoro + Haiku |
| **Total (mid)** | | **~$0.028/min** | faster-whisper + Cartesia + Haiku |

**Monthly projections:**

| Usage | Sessions/Day | Avg Duration | Monthly Cost (budget) | Monthly Cost (mid) |
|-------|-------------|-------------|----------------------|-------------------|
| Early MVP | 50 | 5 min | $23 | $210 |
| Growing | 200 | 5 min | $90 | $840 |
| Scale | 1,000 | 5 min | $450 | $4,200 |

**Installation:**

```bash
uv sync --group voice
# Set environment variables:
# VOICE_STT_PROVIDER=whisper
# VOICE_TTS_PROVIDER=cartesia  (or kokoro for budget)
# VOICE_CARTESIA_API_KEY=your-key  (if using Cartesia)
# ATTRIBUTION_AGENT_MODEL=anthropic:claude-haiku-4-5
# ANTHROPIC_API_KEY=your-key
```

### 2.3 Scenario 3: Commercial Production (~$0.06-0.10/min)

Full commercial stack optimized for quality, latency, and artist-facing features.

| Component | Provider | Cost/Min | Notes |
|-----------|----------|----------|-------|
| STT | Deepgram Nova-3 | $0.0077 | Best accuracy, custom vocabulary for ISRCs/artist names |
| TTS | Cartesia Sonic 3 | $0.025 | 90ms TTFA, consistent global latency |
| VAD | Silero + Deepgram Flux (semantic) | $0.000 | Flux CSR included with Deepgram |
| LLM | Haiku 4.5 (routine) + Sonnet 4.5 (complex) | $0.003-0.060 | PydanticAI FallbackModel for automatic escalation |
| Transport | Daily WebRTC | $0.004 | Sub-30ms, echo cancellation, managed |
| Persona | Letta + NeMo Guardrails | $0.000 | Self-hosted, cross-session memory + topic rails |
| Drift | Custom embed+EWMA + Langfuse | $0.000 | Real-time inline + async observability |
| Eval | DeepEval + custom music-domain | $0.000 | |
| Framework | Pipecat (BSD-2) | $0.000 | |
| **Total (routine queries)** | | **~$0.040/min** | Haiku for LLM |
| **Total (complex queries)** | | **~$0.097/min** | Sonnet escalation |

**Premium tier (Digital Twin with artist voice clone):**

| Component | Provider | Cost/Min | Notes |
|-----------|----------|----------|-------|
| STT | Deepgram Nova-3 | $0.0077 | |
| TTS | ElevenLabs (cloned voice) | $0.080-0.100 | Professional voice cloning |
| LLM | Sonnet 4.5 | $0.060 | Artist persona requires nuanced responses |
| Transport | Daily WebRTC | $0.004 | |
| **Total** | | **~$0.15-0.17/min** | |

**Monthly projections (standard commercial):**

| Usage | Sessions/Day | Avg Duration | Monthly Cost (routine) | Monthly Cost (mixed) |
|-------|-------------|-------------|----------------------|---------------------|
| Early MVP | 50 | 5 min | $300 | $450 |
| Growing | 200 | 5 min | $1,200 | $1,800 |
| Scale | 1,000 | 5 min | $6,000 | $9,000 |

**Installation:**

```bash
uv sync --group voice --group voice-persona
# Set environment variables:
# VOICE_STT_PROVIDER=deepgram
# VOICE_DEEPGRAM_API_KEY=your-key
# VOICE_TTS_PROVIDER=cartesia
# VOICE_CARTESIA_API_KEY=your-key
# VOICE_TRANSPORT=daily
# VOICE_DAILY_API_KEY=your-key
# VOICE_PERSONA_ENABLED=true
# VOICE_LETTA_BASE_URL=http://localhost:8283
# VOICE_GUARDRAILS_ENABLED=true
# VOICE_DRIFT_MONITORING=true
# ATTRIBUTION_AGENT_MODEL=anthropic:claude-haiku-4-5
# ANTHROPIC_API_KEY=your-key
```

---

## 3. Decision Factors for Music Attribution

### 3.1 Music Domain Vocabulary

The music attribution domain has specialized vocabulary requirements that differentiate STT provider choice:

- **ISRC codes** (e.g., "USRC17607839") -- alphanumeric codes that standard models transcribe poorly
- **ISWC codes** (e.g., "T-345.246.800-1") -- international standard musical work codes
- **Artist names** -- global names with non-English phonetics (Bjork, Sigur Ros, Iannis Xenakis)
- **Label names** -- industry-specific (Warp Records, Hyperdub, Ninja Tune)
- **Technical terms** -- "provenance chain", "assurance level A2", "conformal prediction set"

Deepgram's custom vocabulary/dictionary feature is the primary reason it is recommended over faster-whisper for production use despite the cost premium.

### 3.2 Latency Budget

Target: <500ms voice-to-voice for natural conversation feel.

| Stage | Budget | Best Available |
|-------|--------|---------------|
| End-of-turn detection | <100ms | LiveKit semantic: <25ms |
| STT finalization | <200ms | Deepgram Nova-3: ~150ms |
| LLM first token | <200ms | Haiku 4.5: ~200ms |
| TTS first audio | <100ms | Cartesia Turbo: 40ms |
| Transport | <30ms | WebRTC: <30ms |
| **Total** | **<500ms** | **~445ms achievable** |

### 3.3 License Compatibility

The scaffold is open-source. License choices matter:

| License | Components | Commercial Use | Viral? |
|---------|-----------|----------------|--------|
| MIT | faster-whisper, Silero VAD, Whisper.cpp, Chatterbox | Yes | No |
| Apache 2.0 | Kokoro, Orpheus, LiveKit, Letta, Mem0, NeMo, DeepEval, Ragas, Qwen3 | Yes | No |
| BSD-2 | Pipecat | Yes | No |
| GPL-3.0 | Piper TTS | Yes (but derivative works must be GPL) | **Yes** |

**Recommendation:** Avoid Piper in production distributions. Use Kokoro (Apache 2.0) as the open-source TTS default. The scaffold separates Piper into the `voice-gpl` dependency group for this reason.

---

## 4. Cross-References

- [docs/planning/voice-agent-research/recommended-stack.md](../planning/voice-agent-research/recommended-stack.md) -- Recommended stack with ADRs
- [docs/planning/voice-agent-research/finops-economics.md](../planning/voice-agent-research/finops-economics.md) -- Detailed cost analysis and Jevons Paradox
- [docs/planning/voice-agent-research/voice-ai-infrastructure.md](../planning/voice-agent-research/voice-ai-infrastructure.md) -- Full infrastructure assessment
- [docs/planning/voice-agent-research/leaderboards-evaluation.md](../planning/voice-agent-research/leaderboards-evaluation.md) -- Benchmark data and evaluation gaps
- [src/music_attribution/voice/config.py](../../src/music_attribution/voice/config.py) -- VoiceConfig (single source of truth for provider enums)
- [src/music_attribution/voice/pipeline.py](../../src/music_attribution/voice/pipeline.py) -- Pipeline factory with provider instantiation
- [docs/prd/decisions/L3-implementation/voice-agent-stack.decision.yaml](../prd/decisions/L3-implementation/voice-agent-stack.decision.yaml) -- PRD decision node
