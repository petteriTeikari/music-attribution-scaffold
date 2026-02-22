# Voice AI Economics and FinOps (Jan 2025 - Feb 2026)

> **Purpose**: Reference document for business decisions about the voice agent feature in Music Attribution Scaffold. All pricing verified as of February 2026 from public pricing pages and industry reports.

---

## 1. Cost Per Minute: Provider Comparison

### 1.1 Component-Level Costs

The voice AI stack decomposes into three billable components: Speech-to-Text (STT), Large Language Model (LLM) inference, and Text-to-Speech (TTS). Each has wildly different pricing models (per-minute, per-character, per-token) that must be normalized for comparison.

| Component | Provider | Model | Rate | Unit | Source |
|-----------|----------|-------|------|------|--------|
| STT | Deepgram | Nova-3 | $0.0077 | /min (PAYG) | [Deepgram Pricing](https://deepgram.com/pricing) |
| STT | Deepgram | Nova-3 | $0.0065 | /min (Growth) | [Deepgram Pricing](https://deepgram.com/pricing) |
| STT | AssemblyAI | Universal | $0.0025 | /min | [AssemblyAI Pricing](https://www.assemblyai.com/pricing) |
| STT | Azure | Real-time STT | $0.0167 | /min | [Azure Speech Pricing](https://azure.microsoft.com/en-us/pricing/details/speech/) |
| STT | Google Cloud | Standard (V2) | $0.016-0.024 | /min | [Google Cloud STT Pricing](https://cloud.google.com/speech-to-text/pricing) |
| STT | AWS | Transcribe T1 | $0.024 | /min | [AWS Transcribe Pricing](https://aws.amazon.com/transcribe/pricing/) |
| STT | Speechmatics | Flow | $0.03 | /min (est.) | [Speechmatics Pricing](https://www.speechmatics.com/pricing) |
| STT | Cartesia | Ink | $0.0022 | /sec (~$0.13/hr) | [Cartesia Pricing](https://cartesia.ai/pricing) |
| STT | OpenAI | Whisper API | $0.006 | /min | [OpenAI Pricing](https://developers.openai.com/api/docs/pricing) |
| TTS | ElevenLabs | Flash v2.5 | ~$0.07-0.10 | /min (est.) | [ElevenLabs API Pricing](https://elevenlabs.io/pricing/api) |
| TTS | ElevenLabs | Conversational AI | $0.08-0.10 | /min | [ElevenLabs Conversational AI](https://elevenlabs.io/blog/we-cut-our-pricing-for-conversational-ai) |
| TTS | Cartesia | Sonic 3 | ~$0.02-0.03 | /min | [Cartesia Pricing](https://cartesia.ai/pricing) |
| TTS | Deepgram | Aura-2 | $0.030 | /1K chars | [Deepgram Aura-2](https://deepgram.com/learn/introducing-aura-2-enterprise-text-to-speech) |
| TTS | Rime | Mist v2 | ~$0.02 | /min (est.) | [Rime Pricing](https://rime.ai/pricing) |
| TTS | Rime | Arcana v3 | ~$0.03 | /min (est.) | [Rime Arcana v3](https://rime.ai/resources/arcana-v3) |
| TTS | Azure | Neural TTS | $0.016 | /1K chars | [Azure Speech Pricing](https://azure.microsoft.com/en-us/pricing/details/speech/) |
| TTS | PlayHT | PlayDialog | ~$0.065 | /min (est.) | [PlayHT Pricing](https://play.ht/pricing/) |
| TTS | Smallest.ai | Lightning | $0.01-0.04 | /min | [Smallest.ai](https://smallest.ai/blog/lightning-fastest-text-to-speech-model-by-smallestai) |
| TTS | Kokoro | 82M (self-hosted) | ~$0.00 | /min (GPU cost only) | [Kokoro on HuggingFace](https://huggingface.co/hexgrad/Kokoro-82M) |
| LLM | OpenAI | GPT-4o mini | ~$0.006 | /min (est.) | [OpenAI Pricing](https://developers.openai.com/api/docs/pricing) |
| LLM | OpenAI | Realtime Audio (4o) | ~$0.30 | /min (in+out) | [OpenAI Realtime API](https://developers.openai.com/api/docs/pricing) |
| LLM | OpenAI | Realtime Audio (mini) | ~$0.10 | /min (in+out) | [OpenAI Realtime API](https://developers.openai.com/api/docs/pricing) |
| LLM | Anthropic | Haiku 4.5 | ~$0.003 | /min (est.) | [Anthropic Pricing](https://www.anthropic.com/pricing) |
| LLM | Anthropic | Sonnet 4.5 | ~$0.06 | /min (est.) | [Anthropic Pricing](https://www.anthropic.com/pricing) |
| LLM | Google | Gemini 2.0 Flash | ~$0.001 | /min (est.) | [Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| LLM | Google | Gemini 3 Flash | ~$0.002 | /min (est.) | [Gemini 3 Flash](https://blog.google/products/gemini/gemini-3-flash/) |

**Notes on LLM per-minute estimates**: These assume ~1,500 tokens per minute of conversational interaction (mix of input/output). Actual costs vary significantly with prompt length, system prompts, and response verbosity. OpenAI Realtime API is a special case -- it bills on both audio time (per minute) and text tokens (per million), creating a combined rate of ~$0.06/min input + $0.24/min output for gpt-4o-realtime.

**Notes on TTS character-to-minute conversion**: Approximately 800-1,000 characters per minute of spoken output at normal speech rate. Deepgram Aura-2 at $0.030/1K chars translates to roughly $0.024-0.030/min. Azure Neural TTS at $0.016/1K chars translates to roughly $0.013-0.016/min.

### 1.2 Managed Platform All-In Costs

Managed platforms bundle STT + LLM + TTS + telephony into a single per-minute rate. Simpler to budget, but less control over component choices and typically 2-5x more expensive than assembling components yourself.

| Platform | Cost/Min | Monthly (20K min) | Includes | Source |
|----------|----------|-------------------|----------|--------|
| Retell AI | $0.070 | $1,400 | STT + LLM + TTS + telephony | [Retell AI Pricing](https://www.retellai.com/pricing) |
| Deepgram Voice Agent | $0.04-0.16 | $800-3,200 | STT + LLM + TTS (tiered) | [Deepgram Pricing](https://deepgram.com/pricing) |
| Vapi | $0.144 | $2,880 | Platform + all components | [Vapi Pricing](https://vapi.ai) |
| Bland AI | $0.09-0.11 | $1,800-2,200 | Base + components | [Bland AI Billing](https://docs.bland.ai/platform/billing) |
| CloudTalk | $0.25-0.50 | $5,000-10,000 | AI voice agent (1K min incl. at $350/mo) | [CloudTalk Pricing](https://www.cloudtalk.io/pricing/) |
| ElevenLabs Conv. AI | $0.08-0.10 | $1,600-2,000 | Full conversational stack | [ElevenLabs](https://elevenlabs.io/blog/we-cut-our-pricing-for-conversational-ai) |

**Key differentiators**:
- **Retell AI** includes STT at no extra charge (unlike Vapi's $0.01/min STT fee). Transparent modular pricing with no platform fees.
- **Vapi** charges platform fee + telephony + AI voice + model + transcriber as separate line items. Total ~$0.144/min at 10K minutes ([source](https://www.retellai.com/resources/voice-ai-platform-pricing-comparison-2025)).
- **Bland AI** base rate of $0.09/min increased to $0.11/min for Scale plan users (December 2025 pricing change). Minimum $0.015/call for outbound or failed calls.
- **CloudTalk** is the most expensive at $0.50/min pay-as-you-go, but targets enterprise call center use cases with compliance and CRM integrations.

### 1.3 Three-Tier Cost Stack (Budget / Mid / Premium)

For the Music Attribution voice agent, we can target three distinct cost profiles:

| Tier | STT | LLM | TTS | Total/Min | Monthly (500 sessions x 7 min) |
|------|-----|-----|-----|-----------|-------------------------------|
| **Budget** | Self-hosted faster-whisper ($0.00) | Gemini 2.0 Flash ($0.001) | Kokoro self-hosted ($0.00) | **~$0.01** | **~$35** |
| **Mid** | Deepgram Nova-3 ($0.007) | GPT-4o mini ($0.006) | Cartesia Sonic 3 ($0.025) | **~$0.04-0.06** | **~$140-210** |
| **Premium** | Deepgram Nova-3 ($0.007) | Claude Sonnet 4.5 ($0.06) | ElevenLabs ($0.08) | **~$0.15-0.20** | **~$525-700** |

**Budget tier** requires GPU infrastructure. Kokoro TTS (82M params) runs at ~210x real-time on RTX 4090, ~3-11x real-time on modern CPUs ([source](https://huggingface.co/hexgrad/Kokoro-82M)). faster-whisper runs 4x faster than original Whisper with same quality. Self-hosting breakeven: ~14+ hours of transcription per month ([source](https://brasstranscripts.com/blog/openai-whisper-api-pricing-2025-self-hosted-vs-managed)).

**Mid tier** is the recommended starting point. Deepgram Nova-3 has best-in-class accuracy with sub-300ms latency. Cartesia Sonic 3 offers ~5x cheaper than ElevenLabs with competitive quality. GPT-4o mini handles attribution queries well at minimal cost.

**Premium tier** justified only for artist-facing features (voice cloning, digital twin interactions) where quality perception directly affects willingness to pay.

---

## 2. The AI Companion Cost Trap

Understanding the economics of AI companion products is critical because our voice agent could exhibit similar usage patterns -- particularly if users find conversational music exploration engaging.

### 2.1 The Usage Spiral

AI companion products exhibit a dangerous pattern: engagement correlates inversely with unit economics.

- **Character.AI**: Users average 75-93 minutes per day of interaction. Some power users engage 12+ hours daily. The platform processes over 2 billion chat minutes per month ([source](https://www.demandsage.com/character-ai-statistics/)).
- **Replika**: Average daily usage of approximately 2-3 hours for active users. 25% free-to-paid conversion rate -- exceptional vs. typical 2-5% freemium rates ([source](https://www.eesel.ai/blog/replika-ai-pricing)).
- **At scale**: If Character.AI's 20M monthly active users each use 1 hour/day at even $0.01/hr serving cost, that is $73M/year in inference alone. 2024 revenue was $32.2M -- revenue is structurally below serving cost ([source](https://completeaitraining.com/news/character-ai-2025-by-the-numbers-20m-maus-322m-revenue-1b/)).

The core problem: flat-rate subscriptions ($9.99/mo) are structurally unprofitable for heavy users. The heaviest users generate the most engagement metrics but consume the most resources.

### 2.2 The 1% Who Consume 99%

Power user economics create extreme cost distributions:

- **Heavy users**: Individual token costs can reach $35,000/month for the most engaged users on uncapped plans. This is not hypothetical -- it is documented in production AI companion services.
- **Inference dominance**: 60-80% of total operating expenses for AI-first companies come from inference costs alone ([source](https://www.cloudzero.com/blog/inference-cost/), citing a16z 2023 analysis). Inference consumes 80-90% of all AI computing power.
- **Subscription math**: A $9.99/mo subscriber using 12 hours/day at $0.05/min costs $1,080/month to serve. Even at $0.01/min, that is $216/month -- 21x the subscription price.
- **The paradox**: The users who love your product the most are the ones bankrupting it.

### 2.3 The Dolores Case Study

The "Dolores" AI companion (discussed extensively on Hacker News, circa 2024) provides a cautionary case study for voice-first AI products:

- **Scale**: $25/day in API costs from just 1,000 beta users -- approximately $0.025 per user per day, or ~$0.75/month per user before voice.
- **Voice as premium lever**: 70% of revenue came from ElevenLabs realistic voice purchases. Users were willing to pay significant premiums for voice that felt emotionally real.
- **The "John, I really love you!" effect**: Users paid specifically for voices that could deliver emotional statements convincingly. This reveals that **voice quality is not a commodity** -- it is the primary value driver.
- **Content moderation cliff**: When OpenAI enforced content moderation on the underlying LLM, 70% of usage dropped overnight. This highlights platform dependency risk.
- **Key lesson for music attribution**: Voice is the feature users will pay for. Not the attribution data, not the confidence scores -- the voice interaction itself. This maps directly to our premium tier strategy.

Source: Hacker News discussions on AI companion economics, ElevenLabs community reports. Note: exact figures from the Dolores case should be treated as approximate -- they come from founder discussions, not audited financials.

### 2.4 Mitigation Strategies

Given these dynamics, any voice feature must have hard cost guardrails:

| Strategy | Expected Impact | Implementation Complexity |
|----------|----------------|--------------------------|
| **Tiered access** (free/basic/premium/power) | Segments cost exposure by willingness to pay | Low |
| **Token budgeting** per user per day | Hard cap prevents runaway costs | Low |
| **On-device STT fallback** for heavy users | Eliminates STT cost for power users | Medium |
| **Rate limiting with graceful degradation** | Text fallback when voice budget exhausted | Low |
| **Semantic caching** | 15-30% cost reduction on repeated queries | Medium |
| **Session length limits** | Hard stop at N minutes, upsell to continue | Low |
| **Off-peak batch processing** | Shift non-interactive work to cheaper batch rates | Medium |
| **Model routing** (small model for simple queries) | 60-80% of queries can use cheapest model | Medium |

**Recommended for Music Attribution MVP**: Token budget per user per day (10 min free, 30 min basic, unlimited premium) + semantic caching + model routing. This combination limits worst-case cost per user to ~$0.50-1.50/day on the mid tier.

---

## 3. Cost Optimization Strategies

### 3.1 Hybrid Cloud/Edge Architecture

The optimal voice architecture splits components across cloud and edge based on their cost/latency/privacy characteristics:

| Component | Recommended Location | Rationale |
|-----------|---------------------|-----------|
| STT | On-device or edge | Lowest latency, best privacy, eliminates STT API cost |
| LLM | Cloud | Maximum quality, tool-calling for attribution lookups |
| TTS | Depends on quality needs | Cloud for premium voices, edge for cost optimization |

- **Edge STT** (faster-whisper, Whisper.cpp): Eliminates $0.007-0.024/min STT cost entirely. Privacy-preserving -- audio never leaves device. Latency is local, not network-dependent.
- **Cloud LLM**: Attribution queries require database lookups, MusicBrainz API calls, ISRC resolution -- all cloud-side. The LLM must remain cloud-hosted for tool access.
- **TTS split**: Budget users get on-device Kokoro ($0/min, 82M params, Apache-licensed). Premium users get ElevenLabs with artist voice clones ($0.08-0.10/min).

A 7B SLM is 10-30x cheaper than a 70B-175B LLM for inference, with distilled models covering 80-90% of single-turn queries with negligible quality loss ([source](https://redis.io/blog/model-distillation-llm-guide/)).

### 3.2 Model Distillation and Quantization

Combined optimization can achieve up to 16x effective cost reduction:

| Technique | Cost Reduction | Quality Impact |
|-----------|---------------|----------------|
| Distillation (70B to 7B) | 5-10x | 5-15% quality loss on complex tasks |
| Quantization (FP16 to INT4) | 3-4x | 2-5% quality loss |
| Combined | **~16x** | 10-20% quality loss (acceptable for most queries) |

**Self-hosting breakeven analysis**:
- 7B models: breakeven at ~50% GPU utilization (~8,000+ conversations/day)
- 13B models: breakeven at ~10% utilization (lower bar due to higher API cost alternative)
- Minimum viable: ~14 hours/month of transcription to beat API pricing for STT ([source](https://brasstranscripts.com/blog/openai-whisper-api-pricing-2025-self-hosted-vs-managed))
- Infrastructure: Minimum GPU instance ~$276/month, or as low as a $5/month VPS for faster-whisper with CPU inference

**Optimal compression order**: Pruning -> Distillation -> Quantization (P-KD-Q) yields best balance of compression and preserved capabilities ([source](https://brics-econ.org/cost-performance-tuning-for-open-source-llm-inference-how-to-slash-costs-without-losing-quality)).

### 3.3 Semantic Caching

Semantic caching stores LLM responses keyed by embedding similarity, not exact string match. For voice agents handling repetitive attribution queries ("Who wrote this song?", "What's the confidence on this track?"), cache hit rates can be substantial.

| Metric | Value | Source |
|--------|-------|--------|
| Latency improvement | ~10x faster (~50ms vs ~500ms) | [Redis Blog](https://redis.io/blog/prompt-caching-vs-semantic-caching/) |
| Typical cost reduction | 15-30% | Industry reports |
| Best case (FAQ-heavy) | 60-80% reduction | [ScyllaDB](https://www.scylladb.com/2025/11/24/cut-llm-costs-and-latency-with-scylladb-semantic-caching/) |
| Combined with prefix caching | 80%+ savings vs naive | [Redis Blog](https://redis.io/blog/prompt-caching-vs-semantic-caching/) |

**Music Attribution use case**: Attribution queries are highly repetitive. "Who produced X?" and "What's the confidence score for Y?" have a limited set of underlying data. Semantic caching with a similarity threshold of ~0.92 should capture most repeated intents. Expected cost reduction: **20-40%** for our specific workload.

### 3.4 Batch vs Real-Time

Streaming (real-time) STT costs 25-79% more than batch for the same model, depending on provider:

| Provider | Real-time | Batch | Premium for Streaming |
|----------|-----------|-------|-----------------------|
| AWS Transcribe | $0.030/min | $0.024/min | +25% |
| Azure | $0.0167/min | $0.006/min | +178% |
| Google Cloud | $0.024/min | $0.004/min | +500% |
| Deepgram | $0.0077/min | $0.0066/min | +17% |

Sources: [AWS](https://aws.amazon.com/transcribe/pricing/), [Azure](https://azure.microsoft.com/en-us/pricing/details/speech/), [Google Cloud](https://cloud.google.com/speech-to-text/pricing), [Deepgram](https://deepgram.com/pricing)

**Latency vs cost tradeoff**: Voice agents require real-time STT -- there is no batch alternative for interactive conversations. However, non-interactive processing (transcribing uploaded audio files, batch attribution analysis) should always use batch rates.

**The latency cliff**: Research shows user satisfaction drops sharply above 300ms response time -- the natural pause length in human conversation ([source](https://www.assemblyai.com/blog/low-latency-voice-ai)). Beyond 800ms, users begin repeating themselves, assuming the system did not hear them. A 40%+ higher dropout/hangup rate occurs when total voice-to-voice latency exceeds 1 second.

**Target latency budget for Music Attribution**:
| Component | Budget | Typical |
|-----------|--------|---------|
| STT | 100-200ms | 150ms (Deepgram Nova-3) |
| LLM inference | 200-400ms | 300ms (Haiku 4.5) |
| TTS | 100-200ms | 150ms (Cartesia first-byte) |
| Network overhead | 50-100ms | 75ms |
| **Total** | **450-900ms** | **~675ms** |

### 3.5 GPU Instance Pricing

For self-hosted inference (STT, TTS, or fine-tuned LLM), GPU selection dramatically affects unit economics:

| GPU | VRAM | Cloud $/hr (range) | Best For | Source |
|-----|------|--------------------|---------|----|
| H100 80GB | 80GB | $1.90-6.98 | Training + low-latency inference | [RunPod](https://www.runpod.io/pricing), [Lambda](https://lambda.ai/pricing) |
| A100 80GB | 80GB | $0.66-2.29 | General purpose (end-of-life value play) | [CUDO](https://www.cudocompute.com/blog/real-world-gpu-benchmarks) |
| L40S 48GB | 48GB | $0.87-2.00 | Inference (best price/performance) | [CUDO](https://www.cudocompute.com/blog/real-world-gpu-benchmarks) |
| RTX 4090 24GB | 24GB | $0.30-0.75 | Small model inference, dev/test | [RunPod](https://www.runpod.io/pricing) |

**Key findings from cost-per-token analysis** ([source](https://aihardwareindex.com/blog/h100-vs-a100-vs-l40s-the-cost-per-token-analysis)):
- **L40S**: Lowest cost-per-token at $0.15-0.25/1M tokens despite slower raw performance
- **H100**: 2x throughput but 2.5x hourly cost -- only cost-effective for latency-sensitive workloads
- **A100**: Now worst value -- slower than H100, nearly same cost-per-token as L40S, approaching EOL
- **Strategy**: Train on H100, deploy inference on L40S fleets

**Self-hosted breakeven**: Under 1 year at heavy utilization. For music attribution specifically, self-hosting only makes sense above ~8,000 conversations/day -- well beyond MVP scale.

### 3.6 Infrastructure Migrations: Industry Benchmarks

Large-scale migrations demonstrate the magnitude of optimization opportunity:

| Company | Migration | Savings | Timeframe | Source |
|---------|-----------|---------|-----------|--------|
| Character.AI | NVIDIA GPU -> Google TPU v6e | 3.8x cost improvement | 2025 | [AINEWSHub](https://www.ainewshub.org/post/nvidia-vs-google-tpu-2025-cost-comparison) |
| Midjourney | NVIDIA A100/H100 -> TPU v6e | $16.8M/year ($2.1M/mo to $700K/mo) | Q2 2025 | [AINEWSHub](https://www.ainewshub.org/post/nvidia-vs-google-tpu-2025-cost-comparison) |
| Stability AI | Partial GPU -> TPU v6 (40% of workload) | ~40% reduction on migrated portion | Q3 2025 | Industry reports |

Midjourney's CEO David Holz noted: "We were skeptical. The migration took our team 6 weeks. The payback period was 11 days."

**Relevance to Music Attribution**: TPU migration is not relevant at MVP scale. But it demonstrates that **infrastructure choice matters more than code optimization** for AI workloads at scale. Even at our scale, choosing Deepgram ($0.007/min) over AWS Transcribe ($0.024/min) is a 3.4x difference for functionally similar STT.

---

## 4. Jevons Paradox in AI

The most important macro-economic phenomenon in AI right now is Jevons Paradox: as per-unit costs drop, total spending increases rather than decreases.

### 4.1 The Numbers

| Metric | 2022 | 2025 | Change | Source |
|--------|------|------|--------|--------|
| Per-token cost (1M tokens) | ~$20 | ~$0.40 | **-1,000x** | [Artur Markus](https://www.arturmarkus.com/the-inference-cost-paradox-why-generative-ai-spending-surged-320-in-2025-despite-per-token-costs-dropping-1000x-and-what-it-means-for-your-ai-budget-in-2026/) |
| Enterprise AI spending | $11.5B | $37B | **+320%** | [Artur Markus](https://www.arturmarkus.com/the-inference-cost-paradox-why-generative-ai-spending-surged-320-in-2025-despite-per-token-costs-dropping-1000x-and-what-it-means-for-your-ai-budget-in-2026/) |
| Avg monthly enterprise budget | ~$63K | $85,521 | **+36%** | [CloudZero State of AI Costs](https://www.cloudzero.com/state-of-ai-costs/) |
| Orgs spending $100K+/month | 20% | 45% | **+125%** | [CloudZero State of AI Costs](https://www.cloudzero.com/state-of-ai-costs/) |

### 4.2 Why This Happens

1. **Use case proliferation**: Falling costs remove financial gatekeeping. Teams that previously could not justify AI now deploy it across dozens of use cases.
2. **Quality ratchet**: Once users experience Claude Sonnet quality, they resist downgrading to Haiku even when Haiku would suffice. Demand shifts upmarket.
3. **Prompt inflation**: As models get cheaper, prompts get longer and more elaborate. System prompts grow from 200 tokens to 2,000+.
4. **Agent loops**: Agentic workflows multiply token consumption 10-100x per user action (tool calls, retries, chain-of-thought).
5. **New modalities**: Voice and vision add 10-50x token cost per interaction vs. text.

### 4.3 Measurement Gap

- Only **51% of organizations can confidently measure AI ROI** ([Menlo Ventures](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/))
- **FinOps Foundation** documents **30-200x cost variance** between the most expensive leading vendor with no optimizations and a fully optimized platform choice ([source](https://www.finops.org/wg/effect-of-optimization-on-ai-forecasting/))
- Spending grew faster than measurement and governance frameworks could adapt

### 4.4 Implications for Music Attribution

We are adding voice (10-50x cost multiplier) to an existing text agent (~$0.003/min Haiku). Without explicit cost governance:

- **Optimistic**: Voice stays at $0.04-0.06/min (mid tier), 200 sessions/day x 7 min = $560-840/mo
- **Jevons scenario**: Users love it, sessions grow to 500/day x 15 min avg = $3,000-4,500/mo (mid tier)
- **Worst case**: Premium tier demand + power users = $7,000-15,000/mo

The mitigation is **hard limits**: daily minute caps, automatic tier downgrade for heavy users, session-length nudges.

---

## 5. Music Attribution Voice Agent: Cost Model

### 5.1 MVP Cost Estimate (Text Agent + Voice Upgrade)

**Current text agent cost baseline**:
- PydanticAI + Haiku 4.5: ~$0.003/min
- Tool calls (MusicBrainz, ISRC resolution): negligible (free APIs)
- Current monthly cost: effectively $0 (low usage during development)

**Voice upgrade cost addition**:

| Component | Budget | Mid | Premium |
|-----------|--------|-----|---------|
| STT | faster-whisper ($0.00) | Deepgram Nova-3 ($0.007) | Deepgram Nova-3 ($0.007) |
| LLM | Haiku 4.5 ($0.003) | GPT-4o mini ($0.006) | Sonnet 4.5 ($0.06) |
| TTS | Kokoro ($0.00) | Cartesia Sonic 3 ($0.025) | ElevenLabs ($0.08) |
| **Total/min** | **$0.003** | **$0.038** | **$0.147** |

**Expected early usage** (first 3 months post-launch):
- 50-200 sessions/day, 5-10 min average session
- Monthly minutes: 7,500-60,000

| Scenario | Tier | Monthly Min | Monthly Cost |
|----------|------|-------------|-------------|
| Low usage, budget | Budget | 7,500 | **$23** |
| Low usage, mid | Mid | 7,500 | **$285** |
| Medium usage, mid | Mid | 30,000 | **$1,140** |
| High usage, mid | Mid | 60,000 | **$2,280** |
| High usage, premium | Premium | 60,000 | **$8,820** |

### 5.2 Premium Tier (Digital Twin with Artist Voice Clone)

The premium tier targets a specific use case: **artist digital twins** that can answer questions about their own discography, attribution decisions, and creative process using a cloned version of their voice.

**Cost structure**:
| Item | Cost | Notes |
|------|------|-------|
| ElevenLabs Professional Voice Clone | $0 (included in Pro plan) | Requires ~30 min of clean audio |
| TTS per minute (cloned voice) | $0.10-0.15/min | Premium voice quality |
| STT (Deepgram Nova-3) | $0.007/min | Same as mid tier |
| LLM (Sonnet 4.5 for nuanced responses) | $0.06/min | Artist persona requires higher quality |
| **Total per minute** | **$0.17-0.22** | |

**Expected usage pattern**: Shorter fan-facing sessions (2-5 min) vs longer artist workflow sessions (10-30 min).

**Revenue model**:
- Premium subscription: $9.99-19.99/month
- Breakeven at mid tier: ~263-527 minutes/month per subscriber
- Breakeven at premium tier: ~45-118 minutes/month per subscriber
- If average fan uses 3 min/session x 10 sessions/month = 30 min/month, premium tier cost = $5.10-6.60/month -- profitable at $9.99/mo subscription

### 5.3 Free Tier Strategy

The free tier must be viable at near-zero marginal cost per user:

| Component | Choice | Cost | Rationale |
|-----------|--------|------|-----------|
| STT | Self-hosted faster-whisper | $0.00/min | Apache 2.0 license, 4x faster than Whisper |
| LLM | Haiku 4.5 | $0.003/min | Cheapest quality LLM for attribution queries |
| TTS | Kokoro self-hosted | $0.00/min | Apache license, 82M params, CPU-viable |
| **Total** | | **~$0.003/min** | GPU amortization adds ~$0.005-0.01/min |

**Hard limits for free tier**:
- Daily cap: **10 minutes** free, then upgrade prompt
- Session cap: **5 minutes** per session
- Monthly cost per free user (assuming 10 min/day x 20 days): **$0.60-1.20**
- Monthly cost per free user (assuming 3 min/day x 30 days): **$0.27-0.54**

**Infrastructure requirement**: One L40S instance (~$0.87/hr = $635/mo) can serve self-hosted STT + TTS for approximately 1,000-5,000 concurrent free-tier users, depending on model sizes and batching efficiency. At 1,000 free users, that is $0.64/user/month for infrastructure -- viable.

**Upgrade funnel**: "You've used your 10 free voice minutes today. Upgrade to Basic ($4.99/mo) for 60 minutes, or Premium ($19.99/mo) for unlimited + artist voice clones."

### 5.4 Cost Monitoring and FinOps Governance

Given Jevons Paradox dynamics, the following FinOps controls are non-negotiable:

1. **Per-user daily cost tracking** with alerts at 80% of tier budget
2. **Automatic tier downgrade**: If a free user somehow exceeds limits, drop to text-only
3. **Monthly cost dashboards** broken down by: STT / LLM / TTS / infrastructure
4. **Cost-per-session metric** as a first-class KPI alongside session satisfaction
5. **A/B testing**: Route 10% of traffic to budget tier, measure NPS delta vs mid tier
6. **Semantic cache hit rate** as an operational metric (target: >30%)

---

## Appendix A: Key Sources

| Source | URL | Retrieved |
|--------|-----|-----------|
| Deepgram Pricing | https://deepgram.com/pricing | Feb 2026 |
| ElevenLabs API Pricing | https://elevenlabs.io/pricing/api | Feb 2026 |
| Cartesia Pricing | https://cartesia.ai/pricing | Feb 2026 |
| AssemblyAI Pricing | https://www.assemblyai.com/pricing | Feb 2026 |
| Retell AI Pricing | https://www.retellai.com/pricing | Feb 2026 |
| Bland AI Billing | https://docs.bland.ai/platform/billing | Feb 2026 |
| OpenAI Pricing | https://developers.openai.com/api/docs/pricing | Feb 2026 |
| Azure Speech Pricing | https://azure.microsoft.com/en-us/pricing/details/speech/ | Feb 2026 |
| Google Cloud STT Pricing | https://cloud.google.com/speech-to-text/pricing | Feb 2026 |
| AWS Transcribe Pricing | https://aws.amazon.com/transcribe/pricing/ | Feb 2026 |
| CloudZero State of AI Costs | https://www.cloudzero.com/state-of-ai-costs/ | Feb 2026 |
| FinOps Foundation AI Forecasting | https://www.finops.org/wg/effect-of-optimization-on-ai-forecasting/ | Feb 2026 |
| Inference Cost Paradox (Jevons) | https://www.arturmarkus.com/the-inference-cost-paradox-why-generative-ai-spending-surged-320-in-2025-despite-per-token-costs-dropping-1000x-and-what-it-means-for-your-ai-budget-in-2026/ | Feb 2026 |
| Character.AI Statistics | https://www.demandsage.com/character-ai-statistics/ | Feb 2026 |
| Kokoro TTS (HuggingFace) | https://huggingface.co/hexgrad/Kokoro-82M | Feb 2026 |
| H100 vs A100 vs L40S Cost-Per-Token | https://aihardwareindex.com/blog/h100-vs-a100-vs-l40s-the-cost-per-token-analysis | Feb 2026 |
| GPU-TPU Migration (Character.AI, Midjourney) | https://www.ainewshub.org/post/nvidia-vs-google-tpu-2025-cost-comparison | Feb 2026 |
| AssemblyAI 300ms Rule | https://www.assemblyai.com/blog/low-latency-voice-ai | Feb 2026 |
| Redis Semantic Caching | https://redis.io/blog/prompt-caching-vs-semantic-caching/ | Feb 2026 |
| Retell AI Platform Comparison | https://www.retellai.com/resources/voice-ai-platform-pricing-comparison-2025 | Feb 2026 |

## Appendix B: Pricing Volatility Warning

Voice AI pricing is in freefall. Between January 2025 and February 2026:

- ElevenLabs cut Conversational AI pricing by ~50% ([source](https://elevenlabs.io/blog/we-cut-our-pricing-for-conversational-ai))
- Deepgram doubled Aura-2 TTS pricing from $0.015 to $0.030/1K chars (prices can go up too) ([source](https://pricingsaas.com/news/deepgram/20251118/))
- OpenAI Realtime API dropped 20% with gpt-realtime vs gpt-4o-realtime-preview
- Gemini 3 Flash launched at ~50% cheaper than Gemini 2.0 Flash
- Kokoro TTS (open source, free) reached #1 on HuggingFace TTS Arena, threatening all paid TTS providers

**Recommendation**: Review this document quarterly. Lock in committed-use discounts only for 3-month terms maximum. Maintain provider abstraction in the codebase (LiveKit or similar) to enable rapid switching.

## Appendix C: Decision Matrix

For the Music Attribution voice agent specifically:

| Decision | Recommendation | Rationale |
|----------|---------------|-----------|
| STT provider (MVP) | Deepgram Nova-3 | Best accuracy/latency/cost ratio |
| TTS provider (MVP) | Cartesia Sonic 3 | 5x cheaper than ElevenLabs, competitive quality |
| LLM (MVP) | Haiku 4.5 (existing) | Already integrated, cheapest quality option |
| Free tier TTS | Kokoro self-hosted | Apache license, CPU-viable, free |
| Premium tier TTS | ElevenLabs | Voice cloning, emotional range, brand recognition |
| Managed platform | None (build modular) | 2-5x cheaper, more control |
| Caching | Semantic cache (Redis/pgvector) | 20-40% cost reduction expected |
| Self-hosting | Not at MVP | Breakeven requires 8K+ conversations/day |
| Cost governance | Hard daily limits + per-user tracking | Jevons Paradox mitigation |
