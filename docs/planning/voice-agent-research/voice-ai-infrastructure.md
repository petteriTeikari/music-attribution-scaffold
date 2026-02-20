# Voice AI Infrastructure: Production Stack Assessment (Jan 2025 -- Feb 2026)

**Last Updated:** 2026-02-20
**Audience:** L3--L4 Engineers
**Companion to:** Teikari, P. (2026). *Music Attribution with Transparent Confidence*. SSRN No. 6109087.

---

This document surveys the production voice AI landscape as of February 2026, covering frameworks, speech-to-text, text-to-speech, turn-taking, end-to-end speech models, multimodal agents, transport, and edge deployment. The assessment is oriented toward engineering teams evaluating stack choices for real-time voice agent systems, with particular attention to the music attribution domain where conversational voice interfaces serve as a premium feature for artist-facing workflows.

The field has undergone a phase transition since early 2025. Open-source TTS now rivals commercial offerings in naturalness, semantic turn detection has largely replaced VAD-only approaches, and end-to-end speech LLMs have moved from research curiosity to production-viable. The cost structure has also shifted: on-device STT+TTS can reduce per-minute API costs to near-zero, collapsing the economics to LLM inference alone.

---

## 1. Framework Layer

The framework layer orchestrates the full voice pipeline: audio capture, speech-to-text, language model inference, text-to-speech, and audio playback. The two dominant open-source options -- Pipecat and LiveKit Agents -- have converged on similar architectures but differ in transport philosophy and ecosystem positioning.

### 1.1 Pipecat (Daily.co)

[Pipecat](https://github.com/pipecat-ai/pipecat) is a Python-first, open-source (BSD-licensed) framework for building real-time voice and multimodal AI agents. It is the most widely adopted framework in the space as of early 2026.

**Architecture:**

- Modular pipeline model: STT --> LLM --> TTS with parallel processing stages
- Each stage runs as an independent processor, enabling hot-swap of providers
- Frame-based data flow allows mixing audio, text, images, and control signals

**Transport and Audio:**

- Supports both WebSocket and WebRTC transports
- Built-in echo cancellation and noise reduction via Daily.co infrastructure
- Cross-platform client SDKs: Python, JavaScript, React, iOS, Android, C++

**Ecosystem:**

- 40+ AI service plugins covering all major STT, LLM, and TTS providers
- NVIDIA NIM integration for GPU-accelerated on-premises deployment
- Smart Turn: a fully open-source semantic turn detection model (see Section 4.2)
- Active community with 8K+ GitHub stars as of Feb 2026

**Strengths:** Python-native (natural fit for ML teams), largest plugin ecosystem, BSD license allows unrestricted commercial use, strong Daily.co backing for managed transport.

**Weaknesses:** Daily.co transport layer adds a commercial dependency for WebRTC; self-hosting WebRTC without Daily requires additional infrastructure work. The Python-only server runtime limits deployment in Node.js-heavy stacks.

**Key Source:** [github.com/pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat)

### 1.2 LiveKit Agents

[LiveKit Agents](https://docs.livekit.io/agents/) is an open-source framework built on the LiveKit WebRTC platform, backed by a $45M Series B (April 2025).

**Architecture (Agents 1.0):**

- Full STT-LLM-TTS pipeline runs as a WebRTC participant in a LiveKit room
- The agent joins as a peer, enabling natural multi-party conversations
- Worker-based scaling: agents are dispatched to rooms on demand

**Turn Detection:**

- Semantic turn detection via a purpose-built transformer model
- <25ms CPU inference latency (no GPU required)
- Supports 13 languages out of the box
- Represents a significant advance over pure VAD-based approaches

**Telephony:**

- Telephony 1.0: native SIP trunking, HD audio, DTMF support
- Cold and warm call transfers for contact center integration
- Direct integration with Twilio, Telnyx, and other SIP carriers

**Runtimes and Deployment:**

- Python and Node.js server runtimes (broader language coverage than Pipecat)
- Fully self-hostable with open-source LiveKit Server
- Managed Cloud Agents option for teams that prefer not to run infrastructure

**Strengths:** Self-hostable WebRTC server (no third-party transport dependency), semantic turn detection is best-in-class, telephony support enables PSTN integration, dual Python/Node.js runtimes.

**Weaknesses:** Smaller plugin ecosystem than Pipecat, tighter coupling to LiveKit infrastructure conventions, steeper learning curve for teams unfamiliar with WebRTC room semantics.

**Key Source:** [docs.livekit.io/agents](https://docs.livekit.io/agents/)

### 1.3 Managed Voice Agent Platforms

For teams that prefer a fully managed API over framework-level control, three platforms dominate.

| Platform | Price (per min) | Strengths | Limitations |
|----------|----------------|-----------|-------------|
| **Retell AI** | $0.07 all-in | Transparent pricing, simple API | Less granular component control |
| **Vapi** | $0.144 | Granular per-component control, flexible | 2x cost vs Retell at scale |
| **Bland AI** | $0.09+ | 20K+ calls/hour capacity, enterprise scale | Variable pricing, less transparent |

**Cost at Scale (20K minutes/month):**

| Platform | Monthly Cost |
|----------|-------------|
| Retell AI | ~$1,400 |
| Vapi | ~$2,880 |
| Bland AI | Variable (volume-dependent) |

**Assessment:** Managed platforms are appropriate for rapid prototyping and low-volume production (< 5K min/month). At scale, self-hosted frameworks (Pipecat or LiveKit) with direct STT/TTS provider contracts offer 3--5x cost savings. For the music attribution use case, where voice is a Pro-tier upsell with initially modest volume, a managed platform may be appropriate for MVP before migrating to self-hosted infrastructure.

### 1.4 Framework Comparison Summary

| Dimension | Pipecat | LiveKit Agents | Managed (Retell/Vapi) |
|-----------|---------|----------------|----------------------|
| **License** | BSD | Apache 2.0 | Proprietary |
| **Transport** | WebRTC (Daily), WebSocket | WebRTC (self-hosted) | Abstracted |
| **Server Runtimes** | Python | Python, Node.js | N/A (API) |
| **Turn Detection** | Smart Turn (open-source) | Semantic (transformer, <25ms) | Provider-dependent |
| **Telephony** | Via integrations | Native SIP/PSTN | Built-in |
| **Plugin Ecosystem** | 40+ providers | Growing | N/A |
| **Self-Hosting** | Partial (transport via Daily) | Full | No |
| **Ideal For** | ML teams, Python shops | Infrastructure teams, telephony | Rapid MVP, low volume |

---

## 2. Speech-to-Text (STT)

The STT landscape has bifurcated into two tiers: commercial APIs optimized for latency and accuracy on streaming audio, and open-source Whisper variants optimized for cost and deployment flexibility.

### 2.1 Deepgram Nova-3 and Flux

[Deepgram](https://deepgram.com/learn/introducing-nova-3-speech-to-text-api) remains the leading commercial STT provider for real-time voice agents, with two critical product lines.

**Nova-3 (General STT):**

- Streaming WER: 6.84%
- Batch WER: 5.26%
- 54.2% word error rate reduction vs nearest competitor (per Deepgram benchmarks)
- Multi-language support with accent robustness

**Flux (Conversational Speech Recognition):**

- Purpose-built for voice agent use cases
- First model marketed as "Conversational Speech Recognition" -- fuses acoustic and semantic signals
- End-of-turn detection in approximately 260ms
- Reduces false interruptions by approximately 30% compared to VAD-only approaches (see Section 4.2)

**Pricing:**

| Tier | Price per Minute |
|------|-----------------|
| Pay-as-you-go | $0.0077 |
| Growth | $0.0065 |
| Enterprise | Custom |

**Assessment:** Deepgram Flux is the current best-in-class for streaming conversational STT when latency and turn-detection accuracy are the primary constraints. The pricing is competitive but adds up at scale -- 100K minutes/month at Growth tier is $650/month for STT alone.

**Key Source:** [deepgram.com/learn/introducing-nova-3-speech-to-text-api](https://deepgram.com/learn/introducing-nova-3-speech-to-text-api)

### 2.2 Whisper Variants for Production

OpenAI's Whisper remains the foundation of open-source STT, but the base model is too slow for real-time use. Several production-optimized variants have emerged.

| Variant | Speedup vs Whisper | Accuracy Impact | Optimization Strategy | Best For |
|---------|-------------------|-----------------|----------------------|----------|
| **Distil-Whisper** | 6x faster | Within 1% WER of original | Knowledge distillation | Speed-critical, GPU available |
| **Faster-Whisper** | 4x faster | Identical (same weights) | CTranslate2 + INT8 quantization | General production default |
| **Whisper.cpp** | Varies | Identical (same weights) | CPU-optimized, GGML format | No-GPU environments, Apple Silicon |
| **Large V3 Turbo** | 6x faster | 1--2% accuracy tradeoff | Architecture pruning | Balanced speed/accuracy |

**Deployment Recommendations:**

- **Default production:** Faster-Whisper -- best balance of speed, accuracy, and GPU utilization
- **No-GPU / edge:** Whisper.cpp with GGML quantization, particularly strong on Apple Silicon
- **Maximum throughput:** Distil-Whisper when sub-1% accuracy loss is acceptable
- **Balanced:** Large V3 Turbo for teams wanting a single-model solution

**Cost Advantage:** Self-hosted Whisper variants on a dedicated A10G instance (~$0.75/hr on AWS) can process concurrent streams at a marginal cost of approximately $0.001--0.003/min, a 2--7x reduction vs Deepgram. The tradeoff is operational complexity and the absence of Deepgram's semantic turn detection.

### 2.3 Speechmatics

[Speechmatics](https://www.speechmatics.com/) occupies a niche between Deepgram and open-source, with particular strength in regulated industries.

**Real-Time Performance:**

- Partial transcripts delivered in <250ms
- End-of-speech detection in approximately 400ms
- Strong performance in noisy environments

**Flow API (Voice Agent Optimized):**

- Purpose-built for voice agent pipelines
- $0.03/min usage-based pricing
- Includes built-in turn management

**Specialized Capabilities:**

- Medical STT: 93% accuracy, 96% keyword recall on clinical terminology
- On-device model achieves within 10% of server-side accuracy
- Strong in European languages and accents

**Assessment:** Speechmatics is the strongest choice for healthcare, legal, and other regulated domains where domain-specific vocabulary accuracy is critical. The $0.03/min price point is significantly higher than Deepgram ($0.0065--0.0077/min), justified primarily by domain specialization and on-premises deployment options.

### 2.4 Emerging: Mistral Voxtral Mini 4B

Released February 2026 under Apache 2.0, [Voxtral Mini 4B](https://mistral.ai/) represents a new class of compact, open-source STT models.

**Performance Claims:**

- 480ms end-to-end delay
- Outperforms Whisper large-v3, GPT-4o mini Transcribe, and Gemini 2.5 Flash on standard benchmarks
- 4B parameters -- small enough for single-GPU deployment

**Significance:** This is the first open-source model to claim parity with commercial STT APIs on accuracy while remaining small enough for cost-effective self-hosting. If the benchmarks hold under independent evaluation, Voxtral Mini could become the default self-hosted STT choice, replacing Whisper variants for teams willing to run a 4B model.

---

## 3. Text-to-Speech (TTS)

TTS has undergone the most dramatic transformation in the voice AI stack. In early 2025, ElevenLabs was the unchallenged leader in naturalness. By February 2026, open-source models (Chatterbox, Orpheus, Kokoro) match or exceed commercial offerings in blind evaluations, fundamentally altering the cost calculus.

### 3.1 ElevenLabs

[ElevenLabs](https://elevenlabs.io/) remains the market leader in commercial TTS, with the broadest feature set.

**Models:**

| Model | Latency | Use Case |
|-------|---------|----------|
| **Eleven v3** | Standard | Highest expressiveness, 70+ languages, audio tags for emotion control |
| **Flash v2.5** | ~75ms | Agent-optimized, low latency |

**Conversational AI Pricing:**

| Tier | Price per Minute |
|------|-----------------|
| Creator / Pro | $0.10 |
| Business (annual) | $0.08 |

**Voice Cloning:**

- Instant cloning available at Starter tier (few seconds of reference audio)
- Professional cloning at Creator tier (higher fidelity, more reference data)

**Assessment:** ElevenLabs offers the most complete commercial package: high quality, low latency, broad language support, and mature voice cloning. The $0.08--0.10/min cost is the primary drawback -- at 50K min/month, TTS alone costs $4K--5K. This is the component most vulnerable to open-source displacement.

### 3.2 Cartesia Sonic

[Cartesia](https://cartesia.ai/) has carved a latency-leadership position through a novel architecture.

**Models:**

| Model | Time-to-First-Audio (TTFA) | Notes |
|-------|---------------------------|-------|
| **Sonic 3** | 90ms | Production-grade |
| **Sonic Turbo** | 40ms | Industry-leading latency |

**Architecture Differentiation:**

- State Space Model (SSM) architecture, not Transformer-based
- SSMs offer constant-time inference per token regardless of context length
- This architectural choice directly enables the sub-50ms TTFA

**Additional Products:**

- **Ink STT:** A Whisper variant with dynamic chunking, priced at $0.13/hr
- **On-device:** SSM-based on-device TTS in private beta -- SSM architecture is particularly well-suited to resource-constrained environments

**Assessment:** Cartesia Sonic Turbo at 40ms TTFA is the clear choice when minimizing perceived latency is the top priority. The SSM architecture is a genuine technical differentiator, not marketing. For voice agents where responsiveness directly impacts user experience, the 35ms advantage over ElevenLabs Flash (75ms) is perceptible.

### 3.3 Open-Source TTS Revolution (2025--2026)

The most consequential development in voice AI during this period is the emergence of open-source TTS models that rival or exceed commercial offerings in naturalness.

| Model | Size | License | Key Capability | Latency |
|-------|------|---------|---------------|---------|
| **Chatterbox** (Resemble AI) | 350M | MIT | #1 on HuggingFace, outperforms ElevenLabs in blind evals | Streaming-capable |
| **Orpheus TTS** | 3B | Apache 2.0 | Emotional tags (`<laugh>`, `<sigh>`), highly expressive | ~200ms streaming |
| **Kokoro-82M** | 82M | Apache 2.0 | Ultra-efficient: <0.3s inference, <1GB VRAM | <300ms |
| **CosyVoice 2/3** (Alibaba) | Varies | Apache 2.0 | 150ms streaming, strong multilingual | 150ms |
| **Fish Speech v1.5** | Varies | Open | DualAR architecture, 300K+ hours training data | Streaming-capable |

**Chatterbox** deserves particular attention. Released by Resemble AI under MIT license, it achieved the #1 position on HuggingFace's TTS leaderboard and outperformed ElevenLabs in multiple blind evaluations. At 350M parameters, it runs comfortably on consumer GPUs.

**Orpheus TTS** at 3B parameters offers the richest expressiveness among open-source options, with audio emotion tags that enable fine-grained control over delivery style -- a feature previously exclusive to ElevenLabs v3.

**Kokoro-82M** is notable for extreme efficiency: at 82M parameters, it runs on <1GB VRAM with inference under 0.3 seconds, making it viable for edge deployment on mobile devices. Estimated cost at scale: approximately $0.06/hr.

**Cost Implications:**

| Approach | Cost per Minute | Notes |
|----------|----------------|-------|
| ElevenLabs (Business) | $0.08 | Managed API |
| Cartesia Sonic | Comparable | Managed API |
| Self-hosted Orpheus (A10G) | ~$0.005--0.01 | Requires GPU infrastructure |
| Self-hosted Kokoro (CPU) | ~$0.001--0.003 | Runs without GPU |
| Self-hosted Chatterbox (T4) | ~$0.003--0.008 | Consumer GPU viable |

The 10--80x cost reduction from self-hosted open-source TTS is the single largest cost lever in the voice agent stack.

### 3.4 Inworld AI

[Inworld AI](https://inworld.ai/) focuses on gaming and interactive entertainment, with a distinctive real-time architecture.

**Performance:**

- 200ms end-to-end response time (vs 1--2s industry standard for gaming NPCs)
- Character-consistent voice across sessions
- Emotion and personality modeling integrated into TTS

**Pricing:**

- TTS from $5 per 1M characters
- Gaming-optimized: "Death by AI" hit 1M users within 2 weeks of launch

**Assessment:** Inworld's gaming-optimized architecture is not directly applicable to the music attribution use case, but their latency achievements demonstrate what is possible with purpose-built infrastructure. Their character consistency technology is relevant for the "digital twin" voice persona concept.

### 3.5 Other Notable TTS Providers

| Provider | Key Differentiator | Pricing | Notes |
|----------|-------------------|---------|-------|
| **PlayHT** | PlayDialog for multi-turn dialogue TTS | Variable | Dialogue-aware prosody |
| **Rime AI** | Sub-200ms, no concurrency limits | $20--30 per 1M chars | Strong for high-concurrency |
| **MARS5** (CAMB.AI) | 1.2B params, 140+ languages, 2--3s reference cloning | Variable | Broadest language coverage |

---

## 4. Voice Activity Detection (VAD) and Turn-Taking

Turn-taking is arguably the most impactful component in voice agent UX. Poor turn detection creates either (a) the agent cutting off users mid-sentence, or (b) uncomfortable silences while the system waits for certainty that the user has finished. The field has undergone a paradigm shift from acoustic-only VAD to semantic turn detection.

### 4.1 VAD Engines (Acoustic Only)

Traditional VAD models detect whether audio contains speech based purely on acoustic features.

| Engine | Architecture | True Positive Rate | False Positive Rate | Real-Time Factor | Notes |
|--------|-------------|-------------------|--------------------|--------------------|-------|
| **Silero VAD** | Deep learning (LSTM) | 87.7% | 5% | 0.004 | Best open-source, widely used |
| **Picovoice Cobra** | Proprietary DNN | Highest AUC | Lowest | Very low | Cross-platform, commercial |
| **WebRTC VAD** | Legacy GMM | ~50% | Very low | Lowest | Fastest but poor accuracy |

**Silero VAD** is the de facto standard for open-source voice agents. At an RTF of 0.004 (250x faster than real-time), it adds negligible compute overhead. However, acoustic-only VAD cannot distinguish between a user pausing to think ("I want to attribute this to... hmm... let me think...") and a completed utterance, leading to premature interruptions.

**Picovoice Cobra** achieves the highest area under ROC curve in published benchmarks but is commercial and proprietary.

**WebRTC VAD** is included for completeness but is a legacy approach with unacceptable accuracy for modern voice agents.

### 4.2 Semantic Turn Detection (The Paradigm Shift)

Semantic turn detection fuses acoustic signals (silence, prosody, energy) with linguistic signals (sentence completeness, question patterns, discourse markers) to determine whether a user has finished their turn. This is the single most impactful UX improvement in voice agents since 2024.

| System | Approach | Latency | Key Metric | Availability |
|--------|----------|---------|------------|-------------|
| **Deepgram Flux** | Fused acoustic + semantic in STT model | ~260ms end-of-turn | ~30% fewer false interruptions | Commercial API |
| **LiveKit Semantic Turn** | Transformer model | <25ms CPU inference | 13 languages | Open-source |
| **Pipecat Smart Turn** | Open-source model | Varies | Community-validated | Fully open-source |
| **Krisp v1/v2** | Audio-only DNN | Low | 6M params, CPU-deployable | Commercial |
| **OpenAI Semantic VAD** | Context-aware | N/A | Integrated with Realtime API | API-only |

**Deepgram Flux** integrates turn detection directly into the STT model, eliminating the need for a separate VAD component. The approximately 30% reduction in false interruptions is measured against acoustic-only VAD baselines.

**LiveKit's semantic turn detector** is particularly notable: at <25ms CPU inference, it adds virtually no latency, supports 13 languages, and is open-source. This is a strong reason to consider the LiveKit ecosystem.

**Pipecat Smart Turn** is the first fully open-source semantic turn model, enabling complete self-hosting without commercial dependencies.

**Architectural Recommendation:** Semantic turn detection should be considered mandatory for any production voice agent deployed in 2026. The UX difference between acoustic-only VAD and semantic turn detection is immediately perceptible to users. For the music attribution domain, where users may pause to recall collaborator names or think through attribution details, semantic understanding of turn completion is especially critical.

---

## 5. End-to-End Speech Models

End-to-end speech models bypass the traditional STT --> LLM --> TTS pipeline entirely, processing audio input and producing audio output within a single model. This eliminates two latency-inducing serialization boundaries and enables capabilities impossible in pipeline architectures (e.g., true full-duplex conversation, audio-native reasoning).

### 5.1 Ultravox v0.7

[Ultravox](https://ultravox.ai/) is a speech-native LLM that processes raw audio directly without an intermediate ASR (automatic speech recognition) stage.

**Architecture:**

- Audio encoder fused with an LLM decoder
- Processes audio tokens alongside text tokens in a unified sequence
- No separate STT module -- the model "understands" speech natively

**Performance:**

| Metric | Ultravox v0.7 | GPT-4o Realtime | Gemini Live |
|--------|--------------|-----------------|-------------|
| aiewf-eval pass rate | 97.7% | 86.7% | 86.0% |
| Time to first token | ~150ms | ~300ms | ~200ms |
| Throughput (A100) | 50--100 tok/s | N/A (API) | N/A (API) |

**Deployment:**

- Open-source, self-hostable
- Multiple model sizes including 1B variant for edge deployment
- Compatible with standard LLM serving infrastructure (vLLM, TGI)

**Assessment:** Ultravox's 97.7% pass rate on aiewf-eval is remarkable -- 11 percentage points above GPT-4o Realtime. The ~150ms TTFT enables genuinely responsive conversation. The open-source availability and 1B edge variant make this a compelling option for teams willing to run their own infrastructure. The primary limitation is that it produces text output (requiring a separate TTS stage) rather than direct audio output.

### 5.2 Moshi (Kyutai Labs)

[Moshi](https://github.com/kyutai-labs/moshi) is the first real-time full-duplex spoken LLM, enabling truly simultaneous speech -- both parties can speak and listen at the same time, like a natural phone conversation.

**Architecture:**

- 7B parameters
- Dual-stream architecture: one stream for the user's speech, one for the model's speech
- "Inner Monologue" method: the model generates text tokens internally that align with its audio output, improving coherence
- Audio codec tokenizer for both input and output

**Latency:**

- 160ms theoretical latency
- 200ms practical end-to-end latency
- Full-duplex: the model listens while speaking, enabling natural backchanneling

**Significance:** Moshi represents a fundamentally different interaction paradigm from turn-based voice agents. Traditional agents follow a strict listen --> think --> speak cycle; Moshi can process incoming speech while generating output. This enables natural conversational behaviors like "uh-huh" backchanneling, interruption handling, and overlapping speech -- features that are extremely difficult to achieve in pipeline architectures.

**Limitations:** The 7B model requires significant compute (A100-class GPU). Audio output quality lags behind dedicated TTS models. The model's reasoning capability is limited compared to frontier LLMs.

### 5.3 Other Notable End-to-End Models

| Model | Key Innovation | Status |
|-------|---------------|--------|
| **GLM-4-Voice** (Zhipu AI) | End-to-end spoken chatbot, Chinese-first | Research release |
| **LLaMA-Omni 2** | Open-source streaming speech synthesis built on LLaMA | Research release |
| **SALMONN-omni** | Codec-free full-duplex -- no audio tokenizer needed | Research |
| **PersonaPlex** (NVIDIA) | Voice cloning + role/persona control, accepted at ICASSP 2026 | Pre-production |
| **Sesame CSM-1B** | Evaluators show no preference vs human speech in blind tests | Research release |

**Sesame CSM-1B** deserves a highlight: if human-indistinguishable speech synthesis holds up under broader evaluation, it represents a threshold crossing for voice agent naturalness.

### 5.4 End-to-End vs Pipeline: Current Assessment

| Dimension | Pipeline (STT+LLM+TTS) | End-to-End |
|-----------|------------------------|------------|
| **Latency** | 300--800ms cumulative | 150--200ms |
| **Audio Quality** | Best-in-class (ElevenLabs, Cartesia) | Good but not leading |
| **Reasoning** | Frontier LLMs (Claude, GPT-4o) | Limited to model capacity |
| **Flexibility** | Swap any component | Monolithic |
| **Full-Duplex** | Difficult to implement | Native (Moshi) |
| **Production Maturity** | High | Early |
| **Cost Control** | Granular per-component | Single model cost |

**Recommendation for 2026:** Pipeline architecture remains the correct choice for production voice agents that require frontier reasoning (e.g., music attribution analysis). End-to-end models should be tracked closely -- Ultravox is the nearest to production-readiness. The convergence point (where end-to-end models match both reasoning and audio quality) is likely 12--18 months away.

---

## 6. Multimodal Voice Agents

Multimodal voice agents combine speech with visual output (video avatars, lip-synced faces), creating a richer interaction surface.

### 6.1 Tavus Phoenix-4 (Feb 2026)

[Tavus](https://tavus.io/) released Phoenix-4 in February 2026, representing the state of the art in real-time video avatar generation for conversational AI.

**Architecture (Three-Model System):**

| Model | Function |
|-------|----------|
| **Raven-1** | Perception -- understands user's visual and audio input |
| **Sparrow-1** | Timing -- manages conversational rhythm and turn-taking |
| **Phoenix-4** | Synthesis -- generates photorealistic video output |

**Performance:**

- Gaussian-Diffusion model for video synthesis
- Sub-600ms end-to-end latency
- 40fps at 1080p resolution
- Emotion Control API for programmatic facial expression management

**Assessment:** Tavus Phoenix-4 is relevant for the "digital twin" persona concept described in the music attribution PRD. An artist's visual likeness combined with voice creates a compelling identity verification surface. However, the compute cost and complexity of video generation make this a post-MVP consideration.

### 6.2 OpenAI Realtime API

The [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime) provides GPT-4o with native audio input/output capabilities.

**Transport:**

- Supports both WebRTC (lower latency) and WebSocket (simpler integration)
- Native browser integration via WebRTC

**Pricing:**

| Direction | Price per 1M Tokens | Approximate per Minute |
|-----------|--------------------|-----------------------|
| Audio Input | $32 | ~$0.06 |
| Audio Output | $64 | ~$0.24 |

**Features:**

- Semantic VAD for turn detection
- Tool/function calling support
- 32K token context window
- Audio input/output processed natively by GPT-4o (no separate STT/TTS)

**Assessment:** At approximately $0.30/min total, OpenAI Realtime is the most expensive option in this survey. It is best suited for prototyping and use cases where GPT-4o's reasoning capability must be tightly coupled with audio understanding. For production voice agents at scale, the pipeline approach with separate STT+LLM+TTS is 3--6x cheaper.

---

## 7. Transport Layer

The transport layer determines how audio moves between client and server. The choice between WebRTC and WebSocket has significant implications for latency, reliability, and implementation complexity.

### 7.1 WebRTC

**Characteristics:**

- Sub-30ms transport latency (UDP-based, no head-of-line blocking)
- Native browser support in all modern browsers
- Built-in echo cancellation, noise suppression, and automatic gain control
- Peer-to-peer capable (though server-mediated is standard for voice agents)

**Framework Support:**

- LiveKit: native WebRTC (self-hosted or cloud)
- Pipecat: WebRTC via Daily.co transport
- OpenAI Realtime: WebRTC option

**When to Use:** Any application where perceived latency is critical and the client is a web browser or mobile app. WebRTC is the correct default for voice agents.

### 7.2 WebSocket

**Characteristics:**

- Higher latency than WebRTC (TCP-based, subject to head-of-line blocking)
- Simpler to implement -- standard HTTP upgrade, no ICE/STUN/TURN negotiation
- Better suited for server-to-server communication
- No built-in echo cancellation (must be handled at application layer)

**Framework Support:**

- Pipecat: WebSocket transport option
- OpenAI Realtime: WebSocket option
- Most STT/TTS APIs: WebSocket streaming

**When to Use:** Server-to-server pipelines, environments where WebRTC infrastructure (TURN servers) is impractical, or when simplicity outweighs latency requirements.

### 7.3 Transport Comparison

| Dimension | WebRTC | WebSocket |
|-----------|--------|-----------|
| **Transport Latency** | <30ms | 50--150ms |
| **Protocol** | UDP (SRTP) | TCP (WSS) |
| **Echo Cancellation** | Built-in | Manual |
| **Browser Support** | Native | Native |
| **Implementation Complexity** | High (ICE, STUN, TURN) | Low |
| **Server-to-Server** | Possible but unusual | Natural fit |
| **Firewall Traversal** | Requires TURN fallback | Standard HTTPS ports |

---

## 8. On-Device / Edge Deployment

On-device deployment eliminates per-minute API costs for STT and TTS, collapsing the voice agent cost structure to LLM inference alone. This is the most significant cost optimization available in the voice agent stack.

### 8.1 STT on Device

| Model | Size | Latency | Accuracy | Platform |
|-------|------|---------|----------|----------|
| **Moonshine** | 27M--400MB | 5--15x faster than Whisper | Matches or beats Whisper | Cross-platform |
| **WhisperKit** | 1B | 0.46s | 2.2% WER | Apple Neural Engine |
| **Whisper.cpp** | Varies | Platform-dependent | Same as Whisper | CPU (Apple Silicon optimized) |

**Moonshine** is particularly notable at 27M parameters -- small enough for mobile deployment while maintaining competitive accuracy. The 5--15x speedup over base Whisper makes real-time on-device STT practical on modern smartphones.

**WhisperKit** achieves 2.2% WER on Apple Silicon by leveraging the Neural Engine, outperforming many cloud APIs on accuracy while running entirely on-device.

### 8.2 TTS on Device

| Model | Size | Latency | Requirements | License |
|-------|------|---------|-------------|---------|
| **Kokoro-82M** | 82M | <0.3s | <1GB VRAM | Apache 2.0 |
| **Cartesia Sonic On-Device** | N/A | Low | SSM-optimized | Private beta |
| **Smallest.ai Lightning** | Small | RTF 0.01 | CPU | Commercial |
| **Orpheus 150M** | 150M | 100--200ms streaming | Modest GPU | Apache 2.0 |

**Kokoro-82M** at <1GB VRAM is the standout for edge TTS. It runs on virtually any modern device and produces quality competitive with commercial APIs. The Apache 2.0 license enables unrestricted commercial use.

**Smallest.ai Lightning** at RTF 0.01 (100x real-time) supports 16 languages and runs on CPU, making it viable for server-side deployment without GPU infrastructure.

### 8.3 Cost Impact Analysis

The financial case for on-device STT+TTS is compelling.

| Configuration | Cost per Minute | Components |
|---------------|----------------|------------|
| **Full cloud** (Deepgram + ElevenLabs + LLM) | $0.05--0.15 | STT API + TTS API + LLM API |
| **Self-hosted STT+TTS** (Whisper + Kokoro + LLM API) | $0.01--0.03 | GPU amortized + LLM API |
| **On-device STT+TTS** (Moonshine + Kokoro + LLM API) | ~LLM cost only | LLM API only |
| **Fully on-device** (all local) | Near-zero marginal | Hardware amortized |

**At 100K minutes/month:**

| Configuration | Monthly Cost |
|---------------|-------------|
| Full cloud | $5,000--15,000 |
| Self-hosted STT+TTS | $1,000--3,000 |
| On-device STT+TTS + cloud LLM | $500--2,000 (LLM only) |

The transition from full-cloud to self-hosted STT+TTS reduces costs by 3--5x. Adding on-device processing for STT+TTS further reduces costs to LLM inference alone. For the music attribution use case, where voice is a Pro-tier feature with initially modest volume, the cloud approach is appropriate for MVP, with a migration path to self-hosted as volume grows.

### 8.4 Edge Deployment Considerations

| Factor | Consideration |
|--------|-------------|
| **Model Updates** | On-device models require OTA update mechanisms |
| **Quality Variance** | Device hardware varies; quality must be tested across targets |
| **Privacy** | On-device processing keeps audio data local -- significant for GDPR |
| **Offline Capability** | STT+TTS work offline; LLM requires connectivity (unless fully local) |
| **Battery Impact** | Continuous STT is power-intensive; VAD-gated processing is essential |

---

## 9. Cross-Cutting Concerns

### 9.1 Latency Budget

A well-designed voice agent targets <500ms total response latency (user stops speaking to first audio output). Here is a representative latency budget.

| Stage | Target | Best Available |
|-------|--------|---------------|
| End-of-turn detection | <100ms | LiveKit: <25ms |
| STT finalization | <200ms | Deepgram Flux: ~260ms total |
| LLM first token | <200ms | Ultravox: ~150ms |
| TTS first audio | <100ms | Cartesia Turbo: 40ms |
| Transport | <30ms | WebRTC: <30ms |
| **Total** | **<500ms** | **~350--500ms achievable** |

### 9.2 Language and Accent Coverage

| Provider | Languages | Accent Robustness |
|----------|-----------|-------------------|
| Deepgram Nova-3 | 36+ | Strong |
| Speechmatics | 50+ | Very strong (European) |
| ElevenLabs v3 | 70+ | Strong |
| CosyVoice 3 | 10+ | Strong (CJK) |
| LiveKit Turn Detection | 13 | Moderate |

### 9.3 Security and Privacy

| Concern | Mitigation |
|---------|-----------|
| Audio data in transit | WebRTC SRTP (encrypted by default), WSS for WebSocket |
| Audio data at rest | Ephemeral processing; do not persist raw audio unless consented |
| Voice cloning abuse | Consent verification, watermarking (ElevenLabs, Resemble) |
| Model extraction | On-device models require obfuscation/encryption |
| GDPR/CCPA | On-device processing avoids data transfer; cloud requires DPA |

---

## 10. Summary: Technology Maturity Matrix

| Component | Mature (Production) | Emerging (Early Production) | Research (Track) |
|-----------|--------------------|-----------------------------|-----------------|
| **Framework** | Pipecat, LiveKit Agents | Managed platforms at scale | -- |
| **STT** | Deepgram Nova-3/Flux, Faster-Whisper | Voxtral Mini 4B | -- |
| **TTS** | ElevenLabs, Cartesia Sonic | Chatterbox, Orpheus, Kokoro | Fish Speech |
| **VAD** | Silero VAD | -- | -- |
| **Turn Detection** | LiveKit semantic, Deepgram Flux | Pipecat Smart Turn | -- |
| **End-to-End** | -- | Ultravox v0.7 | Moshi, Sesame CSM-1B |
| **Multimodal** | -- | OpenAI Realtime | Tavus Phoenix-4 |
| **On-Device STT** | Whisper.cpp | Moonshine, WhisperKit | -- |
| **On-Device TTS** | -- | Kokoro-82M | Cartesia On-Device |
| **Transport** | WebRTC, WebSocket | -- | -- |

---

## References

- Pipecat. (2024--2026). *Open-source framework for voice and multimodal conversational AI.* [github.com/pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat)
- LiveKit. (2024--2026). *LiveKit Agents documentation.* [docs.livekit.io/agents](https://docs.livekit.io/agents/)
- Deepgram. (2025). *Introducing Nova-3.* [deepgram.com/learn/introducing-nova-3-speech-to-text-api](https://deepgram.com/learn/introducing-nova-3-speech-to-text-api)
- Deepgram. (2025). *Flux: Conversational Speech Recognition.* [deepgram.com](https://deepgram.com)
- ElevenLabs. (2025--2026). *Eleven v3 and Conversational AI.* [elevenlabs.io](https://elevenlabs.io)
- Cartesia. (2025--2026). *Sonic TTS.* [cartesia.ai](https://cartesia.ai)
- Resemble AI. (2025). *Chatterbox: Open-source TTS.* [github.com/resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox)
- Kyutai Labs. (2024--2025). *Moshi: Real-time full-duplex spoken LLM.* [github.com/kyutai-labs/moshi](https://github.com/kyutai-labs/moshi)
- Fixie.ai. (2025--2026). *Ultravox v0.7.* [ultravox.ai](https://ultravox.ai)
- Tavus. (2026). *Phoenix-4 conversational video.* [tavus.io](https://tavus.io)
- OpenAI. (2025). *Realtime API.* [platform.openai.com/docs/guides/realtime](https://platform.openai.com/docs/guides/realtime)
- Speechmatics. (2025--2026). *Flow API.* [speechmatics.com](https://www.speechmatics.com/)
- Mistral AI. (2026). *Voxtral Mini 4B.* [mistral.ai](https://mistral.ai)
- Silero. (2024--2025). *Silero VAD.* [github.com/snakers4/silero-vad](https://github.com/snakers4/silero-vad)
- Inworld AI. (2025--2026). *Real-time character AI.* [inworld.ai](https://inworld.ai)
- Sesame. (2026). *CSM-1B.* [sesame.com](https://www.sesame.com)
