# Voice AI Leaderboards, Benchmarks, and Evaluation Gaps (Jan 2025 -- Feb 2026)

> **Last updated**: 2026-02-20
> **Context**: Research reference for evaluation strategy decisions in the Music Attribution Scaffold voice agent.
> **Companion to**: [voice-ai-infrastructure.md](voice-ai-infrastructure.md)

---

## 1. The Fragmented Leaderboard Landscape

As of February 2026, there is NO unified voice agent leaderboard. The ecosystem is fragmented across component-level benchmarks (STT, TTS), end-to-end voice agent evaluations, and domain-specific challenges. Each measures a different slice of what matters for production voice agents, and none captures the full picture.

### 1.1 STT Leaderboards

**HuggingFace Open ASR Leaderboard**

- Maintained by [hf-audio](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard), 60+ models, 11 datasets, 6 languages (English, German, French, Italian, Spanish, Portuguese)
- Three tracks: English, multilingual, long-form
- Companion paper: [arXiv:2510.06961](https://arxiv.org/abs/2510.06961) -- "Open ASR Leaderboard: Towards Reproducible and Transparent Multilingual and Long-Form Speech Recognition Evaluation"
- Standardized evaluation protocol enabling fair comparison across open-source and proprietary models

Top models (Feb 2026):

| Rank | Model | WER (avg) | RTFx | Params | Architecture | License |
|------|-------|-----------|------|--------|-------------|---------|
| 1 | NVIDIA Canary-Qwen-2.5B | 5.63% | 418x | 2.5B | SALM (FastConformer + Qwen3-1.7B) | CC-BY |
| 2 | IBM Granite Speech 3.3 8B | 5.85% | ~31x | 8B | Speech-augmented LLM | Apache 2.0 |
| 3 | Microsoft Phi-4-Multimodal | ~6.14% | -- | 5.6B | Multimodal SLM | MIT |
| 4 | Whisper Large V3 Turbo | ~10-12% | ~216x | 809M | Encoder-decoder (pruned) | MIT |
| ~23 | NVIDIA Parakeet TDT 1.1B | ~8% | 1,213x | 1.1B | FastConformer TDT | CC-BY |

**Key architectural insight**: The top four models all use a Conformer encoder paired with an LLM-based decoder. This architecture delivers the best accuracy but at significantly higher computational cost. Models using TDT or CTC decoders (e.g., Parakeet TDT 1.1B) sacrifice 2-3% WER for 3-6x faster inference -- a tradeoff that matters enormously for production voice agents where latency budgets are tight.

**NVIDIA Canary-Qwen-2.5B** ([HuggingFace](https://huggingface.co/nvidia/canary-qwen-2.5b)): A Speech-Augmented Language Model (SALM) combining a FastConformer encoder with an unmodified Qwen3-1.7B LLM decoder via linear projection and LoRA. Trained on 234K hours of publicly available speech data. Per-benchmark WER: 1.6% (LibriSpeech Clean), 3.1% (LibriSpeech Other), 5.6% (VoxPopuli). Released July 2025 under CC-BY license.

**IBM Granite Speech 3.3 8B** ([HuggingFace](https://huggingface.co/ibm-granite/granite-speech-3.3-8b), [arXiv:2505.08699](https://arxiv.org/abs/2505.08699)): Speech-aware LLM with strong English ASR capabilities. WER: 1.5% (LibriSpeech Clean), 7.0% (CommonVoice). BLEU on speech translation within 5 points of state-of-the-art specialist models. Apache 2.0 licensed.

**Notable new entrant**: **Mistral Voxtral Mini 4B** (February 2026) -- [Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602). Apache 2.0 licensed, natively streaming architecture with a custom causal audio encoder. At 480ms configurable delay, it matches leading offline open-source transcription models. Supports 13 languages. Among the first open-source models to achieve commercial-API-competitive accuracy in realtime streaming. This is significant because it collapses the gap between open-source and proprietary realtime ASR.

### 1.2 TTS Leaderboards

**TTS Arena V2** ([HuggingFace](https://huggingface.co/spaces/TTS-AGI/TTS-Arena-V2)) -- Elo-based blind human preference voting, analogous to Chatbot Arena for text LLMs.

| Rank | Model | Elo | Win Rate | Votes |
|------|-------|-----|----------|-------|
| 1 | Vocu V3.0 | 1613 | 57% | 1,168 |
| 2 | Inworld TTS | 1578 | 59% | 1,794 |
| 3 | CastleFlow v1.0 | 1575 | 60% | 1,637 |
| 4 | Inworld TTS MAX | 1572 | 62% | 1,279 |
| 5 | Papla P1 | 1563 | 57% | 3,132 |
| 6 | Hume Octave | 1559 | 64% | 3,263 |
| 7 | ElevenLabs Flash v2.5 | 1547 | 56% | 3,252 |
| 8 | ElevenLabs Turbo v2.5 | 1545 | 58% | 3,252 |
| 9 | MiniMax Speech-02-HD | 1543 | 57% | 2,663 |
| 10 | MiniMax Speech-02-Turbo | 1538 | 52% | 2,728 |
| 11 | ElevenLabs Multilingual v2 | 1518 | 57% | 3,328 |
| 12 | Parmesan | 1515 | 51% | 1,153 |

**Artificial Analysis Speech Arena** ([Leaderboard](https://artificialanalysis.ai/text-to-speech/arena)) -- Separate blind preference leaderboard. Inworld TTS-1.5-Max claimed #1 with sub-250ms latency at $10/million characters, 52 Elo points above ElevenLabs. Announced January 2026.

**Critical observation**: The TTS Arena rankings shift rapidly. Between January and February 2026, Vocu V3.0 overtook Inworld on TTS Arena V2, while Inworld leads on Artificial Analysis. This divergence reflects different user populations and evaluation methodologies -- a fundamental issue in preference-based benchmarking.

### 1.3 End-to-End Voice Agent Benchmarks

**aiewf-eval** ([GitHub](https://github.com/kwindla/aiewf-eval)) -- Created by Kwindla Hultman Kramer (co-founder of Daily, creator of Pipecat).

- 30-turn conversations simulating realistic voice agent scenarios
- Evaluates tool calling, instruction following, knowledge base grounding
- Claude as judge, scoring three dimensions per turn
- System prompt with few-thousand-token knowledge context plus ~12 tools
- Results aggregated across 10 runs per model

Speech-to-speech model results:

| Model | Tool Use | Instruction | KB Ground | Turn Ok | Pass Rate | V2V Latency (med) | V2V Latency (max) |
|-------|----------|-------------|-----------|---------|-----------|--------------------|--------------------|
| Ultravox v0.7 | 293/300 | 294/300 | 298/300 | 300/300 | **97.7%** | 864ms | 1,888ms |
| GPT Realtime | 271/300 | 260/300 | 300/300 | 296/300 | 86.7% | 1,536ms | 4,672ms |
| Gemini Live | 258/300 | 261/300 | 293/300 | 278/300 | 86.0% | 2,624ms | 30,000ms |
| Nova 2 Sonic | 278/300 | 265/300 | 296/300 | * | * | 1,280ms | 3,232ms |
| Grok Realtime | 267/300 | 275/300 | 295/300 | * | * | 1,184ms | 2,016ms |

Text-mode LLMs (cascaded pipeline, for reference):

| Model | Tool Use | Instruction | KB Ground | Pass Rate | TTFB (med) |
|-------|----------|-------------|-----------|-----------|------------|
| GPT-5.1 | 300/300 | 300/300 | 300/300 | **100.0%** | 916ms |
| Gemini 3 Flash Preview | 300/300 | 300/300 | 300/300 | **100.0%** | 1,193ms |
| Claude Sonnet 4.5 | 300/300 | 300/300 | 300/300 | **100.0%** | 2,234ms |
| GPT-4.1 | 283/300 | 273/300 | 298/300 | 94.9% | 683ms |
| Gemini 2.5 Flash | 275/300 | 268/300 | 300/300 | 93.7% | 594ms |
| Nova 2 Pro Preview | 288/300 | 278/300 | 289/300 | 92.7% | 686ms |
| GPT-5-mini | 271/300 | 272/300 | 289/300 | 92.4% | 6,339ms |
| GPT-4o-mini | 271/300 | 262/300 | 293/300 | 91.8% | 760ms |
| GPT-4o | 278/300 | 249/300 | 294/300 | 91.2% | 625ms |
| Nemotron 3 Nano 30B | 282/300 | 280/300 | 293/300 | 91.0% | 171ms |
| GPT-OSS-120B (Groq) | 272/300 | 270/300 | 298/300 | 89.3% | 98ms |
| GPT-5.2 | 224/300 | 228/300 | 250/300 | 78.0% | 819ms |
| Claude Haiku 4.5 | 221/300 | 172/300 | 299/300 | 76.9% | 732ms |

**Milestone**: Ultravox v0.7 is the FIRST speech-to-speech model to surpass text-mode frontier LLMs on a production-realistic benchmark. At 97.7% pass rate, it exceeds GPT-4.1 (94.9%) and matches the frontier text models (100%) within margin, while delivering 864ms median voice-to-voice latency. This is a paradigm shift -- speech-native models are no longer inherently worse at reasoning.

**Caveat**: The asterisks on Nova 2 Sonic and Grok Realtime indicate incomplete Turn Ok data, making direct comparison incomplete. And the benchmark was created by the Pipecat team (Daily), who partner with Ultravox -- though the code and methodology are fully open-source.

### 1.4 Voice Cloning Leaderboard

**ClonEval** ([arXiv:2504.20581](https://arxiv.org/abs/2504.20581)) -- First standardized benchmark for voice cloning TTS models.

- Evaluation protocol based on cosine similarity between speaker embeddings of reference and generated samples
- Open-source library and [HuggingFace leaderboard](https://huggingface.co/spaces)
- Beyond overall similarity, analyzes emotion transfer quality per model
- XTTS-v2 tops most datasets; SpeechT5 excels on LibriSpeech test-clean and TESS

**Relevance to music attribution**: Voice cloning quality directly affects the viability of artist digital twins. If a rights holder wants an AI agent that "sounds like them" for attribution queries, ClonEval-style metrics become relevant for quality assurance.

---

## 2. What Leaderboards Miss: The Evaluation Gap

### 2.1 Synthetic Speech Bias

The most pervasive problem across current benchmarks: most test audio is TTS-generated, not human-recorded.

- VoiceAgentBench generates speaker diversity via TTS voice conversion with speaker embedding sampling
- VCB Bench ([arXiv:2510.11098](https://arxiv.org/abs/2510.11098)) is explicitly built on authentic (non-synthetic) human speech -- making it an exception that highlights the rule
- Audio MultiChallenge ([arXiv:2512.14865](https://arxiv.org/abs/2512.14865)) curates 452 conversations from 47 real speakers with natural disfluencies
- SD-Eval ([NeurIPS 2024](https://github.com/amphionspace/SD-Eval)) includes real recordings with paralinguistic variations

**Why this matters**: Models optimized for clean, synthetic speech may fail on real human input with hesitations, overlapping speech, background noise, and accent variation. Production voice agents encounter human speech, not TTS output.

### 2.2 English-Centric Evaluation

- Most benchmarks are English-only or English-first
- VoiceAgentBench adds 6 Indic languages -- and reveals sharp performance degradation (SpeechLMs drop significantly on non-English agentic tasks)
- VCB Bench covers Chinese with real human speech
- VocalBench includes both English and Mandarin
- Voxtral Mini 4B supports 13 languages, but most benchmarks cannot evaluate this capability

**Scale of the gap**: There are 7,000+ spoken languages worldwide. Even "multilingual" benchmarks cover fewer than 20. For music attribution, this is a critical gap -- the global music industry spans every language community.

### 2.3 Single-Turn Bias

Traditional speech benchmarks evaluate single utterances or short exchanges:

- aiewf-eval was explicitly created because "voice conversations are fundamentally long, multi-turn" -- its 30-turn design is an outlier
- Audio MultiChallenge shows that even frontier models degrade on Self Coherence with longer audio context
- MTR-DuplexBench ([arXiv:2511.10262](https://arxiv.org/abs/2511.10262)) reveals that full-duplex models "face difficulties maintaining consistent performance across multiple rounds"
- Training data massively underrepresents multi-turn voice interaction compared to single-turn

**Implication**: A voice agent that handles the first 3 turns well may fail catastrophically at turn 15. Current benchmarks mostly cannot detect this.

### 2.4 Accent and Dialect Bias

ASR systems consistently perform worse for non-native speakers, and this bias is well-documented but poorly benchmarked:

- **ACM FAccT 2025**: ["It's not a representation of me": Examining Accent Bias and Digital Exclusion in Synthetic AI Voice Services](https://dl.acm.org/doi/10.1145/3715275.3732018) -- documents practical barriers and psychological impacts of accent-based discrimination in voice AI
- **ACM FAccT 2024**: ["Speaking of accent: A content analysis of accent misconceptions in ASR research"](https://dl.acm.org/doi/10.1145/3630106.3658969) -- reveals systematic misconceptions about accent in the ASR research community itself
- American/British English accents dominate commercial systems and training data
- SD-Eval includes accent as one of four evaluation dimensions but with limited diversity
- VoiceBench ([arXiv:2410.17196](https://arxiv.org/abs/2410.17196)) generates accent-varied test cases via voice cloning, but this is synthetic accent simulation, not real accented speech

**No leaderboard shows per-accent performance breakdowns.** This is a significant equity gap for any system serving a global user base.

### 2.5 Missing Dimensions in ALL Current Leaderboards

The following capabilities are either untested or minimally tested across all existing benchmarks:

1. **Barge-in / interruption handling** -- Only [Full-Duplex-Bench](https://arxiv.org/abs/2503.04721) and [HumDial Track II](https://arxiv.org/abs/2601.05564) evaluate this. Full-Duplex-Bench measures Latency After Interruption and distinguishes pause handling, backchanneling, smooth turn-taking, and user interruption management. HumDial found that Rejection (maintaining silence when appropriate) scores were consistently lower than Interruption handling across all submissions.

2. **Emotional appropriateness** -- Only [MULTI-Bench](https://arxiv.org/abs/2511.00850) and HumDial Track I dedicate evaluation to emotional intelligence. MULTI-Bench reveals that while SDMs handle basic emotion understanding, they struggle with advanced multi-turn reasoning about emotions.

3. **Background noise robustness** -- SD-Eval includes environmental noise as one dimension. VocalBench tests white noise, background noise, reverberation, far-field, packet loss, and clipping distortion. Most other benchmarks use clean audio only.

4. **Turn-taking quality** -- aiewf-eval begins to measure this via "Turn Ok" scoring. Full-Duplex-Bench and MTR-DuplexBench provide dedicated evaluation. Most benchmarks ignore it entirely.

5. **Hallucination under noise** -- Largely untested. When ASR produces garbled transcriptions due to noise, how do downstream LLMs respond? Do they hallucinate plausible but wrong information, or do they acknowledge uncertainty?

6. **Cross-session consistency** -- No benchmark tests whether a voice agent gives the same answer to the same question across separate sessions. For attribution queries where accuracy matters legally, this is a critical gap.

7. **Safety under adversarial audio** -- Recent research reveals alarming vulnerabilities:
   - [Gemini 2.0 Flash](https://quantumzeitgeist.com/98-26-percent-reveal-success-rate-audio-attacks/): 98.26% jailbreak success rate via audio attacks
   - Qwen2-Audio-7B-Instruct: 76-82% attack success rate with gradient-based audio perturbations
   - LLaMA-Omni: 89-93% attack success rate
   - Best-of-N Jailbreaking: >60% ASR across all tested models with 7,000 augmentations
   - Average audio-modality attack success rate (21.5%) exceeds text-modality (17.0%)
   - Defense: post-hoc activation patching can harden models at inference time without retraining ([MBZUAI](https://mbzuai.ac.ae/news/your-voice-can-jailbreak-a-speech-model-heres-how-to-stop-it-without-retraining/))

8. **Cost-quality tradeoffs** -- No leaderboard incorporates pricing. A model that scores 2% higher but costs 10x more per query may be the wrong choice for production. Hamming AI's framework acknowledges this but does not publish comparative data.

9. **Graceful error recovery** -- Only Audio MultiChallenge's Voice Editing axis tests robustness to mid-utterance speech repairs and backtracking. Production conversations are full of self-corrections that most benchmarks ignore.

10. **Multi-speaker / multi-party** -- No benchmark tests handoffs between speakers, conference-call scenarios, or distinguishing multiple simultaneous speakers in a voice agent context.

### 2.6 The Intelligence-Latency Tradeoff

This is the defining constraint of 2026 voice AI deployment.

**The data from aiewf-eval makes it stark**:

| Model | Pass Rate | Median Latency | Viable for Production? |
|-------|-----------|----------------|----------------------|
| GPT-5.1 (text) | 100.0% | 916ms TTFB | Marginal (needs TTS on top) |
| Claude Sonnet 4.5 (text) | 100.0% | 2,234ms TTFB | Too slow for voice |
| Gemini 2.5 Flash (text) | 93.7% | 594ms TTFB | Fast but imperfect |
| GPT-4o (text) | 91.2% | 625ms TTFB | Workhorse, not frontier |
| Nemotron 3 Nano (text) | 91.0% | 171ms TTFB | Fastest, good enough? |
| Ultravox v0.7 (S2S) | 97.7% | 864ms V2V | Best S2S by far |
| GPT Realtime (S2S) | 86.7% | 1,536ms V2V | Acceptable, expensive |
| Gemini Live (S2S) | 86.0% | 2,624ms V2V | Too slow, inconsistent |

Natural conversation requires voice-to-voice response times under 1,500ms ([Daily blog](https://www.daily.co/blog/benchmarking-llms-for-voice-agent-use-cases/)). The human neurological response window is 200-300ms. The industry median latency is 1.4-1.7s -- 5x slower than human expectation ([Hamming AI](https://hamming.ai/resources/voice-agent-evaluation-metrics-guide)).

**Production reality**: Most production voice agent systems run 12-18-month-old models because "switching is expensive and evaluation is hard" ([Coval/Pipecat/Ultravox conversation](https://www.coval.dev/blog/the-state-of-voice-ai-instruction-following-in-2026-a-conversation-with-kwindla-from-pipecat-and-zach-from-ultravox)). GPT-4.1's latency quickly deteriorates with long inputs (~1,300ms), making it unsuitable for realtime voice despite strong benchmark scores. Companies that build interfaces on top of third-party models "can make demos work, but at production scale, they struggle."

### 2.7 Benchmark vs Production Reality

**"Testing the Testers"** ([arXiv:2511.04133](https://arxiv.org/abs/2511.04133)) -- The first systematic meta-evaluation of voice AI testing platforms.

- Framework combining psychometric techniques (pairwise comparisons, Elo ratings, bootstrap confidence intervals, permutation tests)
- Evaluated three commercial platforms across two dimensions: simulation quality and evaluation quality
- 21,600 human judgments across 45 simulations and ground truth validation on 60 conversations

Results:

| Platform | Evaluation F1 | Evaluation Accuracy | Simulation Score |
|----------|--------------|--------------------|-----------------|
| Evalion | 0.919 | 86.7% | 61.0 |
| Cekura | 0.842 | 75.7% | 43.0 |
| Coval | 0.728 | 62.7% | 48.9 |

**Key finding**: Generating realistic test conversations (simulation quality) is significantly harder than evaluating responses (evaluation quality). The best platform (Evalion) achieves 0.92 F1 for evaluation but the simulation scores are much lower across all platforms. Traditional text metrics miss tone, hesitation, sighs, and frustration -- paralinguistic cues that are central to voice interaction quality.

---

## 3. Academic Evaluation Papers (Oct 2025 -- Feb 2026)

### 3.1 Benchmark Papers (Timeline)

| Paper | Date | arXiv | Key Contribution |
|-------|------|-------|-----------------|
| **VoiceBench** | Oct 2024 | [2410.17196](https://arxiv.org/abs/2410.17196) | Noise/accent perturbations for LLM-based voice assistants |
| **SD-Eval** | Jun 2024 (NeurIPS) | [2406.13340](https://arxiv.org/abs/2406.13340) | Paralinguistic variables (emotion, accent, age, environment) |
| **Full-Duplex-Bench** | Mar 2025 | [2503.04721](https://arxiv.org/abs/2503.04721) | Turn-taking and interruption evaluation for full-duplex SDMs |
| **VocalBench** | May 2025 | [2505.15727](https://arxiv.org/abs/2505.15727) | 27 models, 14 capabilities, speech-instruction format |
| **VoiceAgentBench** | Oct 2025 | [2510.07978](https://arxiv.org/abs/2510.07978) | 6K+ queries, 7 languages, tool-calling; ASR-LLM > SpeechLMs |
| **VCB Bench** | Oct 2025 | [2510.11098](https://arxiv.org/abs/2510.11098) | Real human speech (Chinese), robustness testing across 3 dimensions |
| **VoiceAgentEval** | Oct 2025 | [2510.21244](https://arxiv.org/abs/2510.21244) | Expert outbound calling, 6 domains, 30 sub-scenarios, 12 LLMs |
| **MULTI-Bench** | Nov 2025 | [2511.00850](https://arxiv.org/abs/2511.00850) | Emotional intelligence in spoken dialogue, 5 tasks, 3.2K samples |
| **MTR-DuplexBench** | Nov 2025 | [2511.10262](https://arxiv.org/abs/2511.10262) | Multi-round full-duplex evaluation, turn segmentation via clustering |
| **Testing the Testers** | Nov 2025 | [2511.04133](https://arxiv.org/abs/2511.04133) | Meta-evaluation of testing platforms, simulation vs evaluation quality |
| **Audio MultiChallenge** | Dec 2025 | [2512.14865](https://arxiv.org/abs/2512.14865) | Multi-turn, Voice Editing axis; best model (Gemini 3 Pro) 54.65% |
| **ICASSP 2026 HumDial** | Jan 2026 | [2601.05564](https://arxiv.org/abs/2601.05564) | Emotion + full-duplex, 100+ teams, 15 valid submissions |
| **TRACE** | Jan 2026 | [2601.13742](https://arxiv.org/abs/2601.13742) | Dimension-first S2S evaluation, LLM judges with audio blueprints |
| **LALM-as-a-Judge** | Feb 2026 | [2602.04796](https://arxiv.org/abs/2602.04796) | Safety in multi-turn spoken dialogues, 24K synthetic dialogues |
| **ClonEval** | Apr 2025 | [2504.20581](https://arxiv.org/abs/2504.20581) | Voice cloning benchmark, speaker embedding similarity |

### 3.2 Selected Paper Summaries

**VoiceAgentBench** ([arXiv:2510.07978](https://arxiv.org/abs/2510.07978)): The first benchmark specifically evaluating agentic tool-use in speech. 6,000+ synthetic spoken queries spanning single-tool invocations, multi-tool workflows, multi-turn dialogue, and safety evaluations across English and six Indic languages. Key finding: ASR-LLM cascaded pipelines outperform end-to-end SpeechLMs, achieving up to 60.6% parameter-filling accuracy on English. All models struggle in sequential workflows and safety evaluations. Publicly available on HuggingFace.

**VCB Bench** ([arXiv:2510.11098](https://arxiv.org/abs/2510.11098)): First comprehensive Chinese voice conversation benchmark built entirely on authentic (non-synthetic) speech. Evaluates across three dimensions: Instruction Following (including speech-level control like volume, speed, emotion), Knowledge (12 subjects, math/logic, dialogue comprehension), and Robustness (mispronunciations, grammatical errors, street noise, TV noise, age variation, accents). Notable for using re-recordings by the same speaker to introduce controlled perturbations.

**VoiceAgentEval** ([arXiv:2510.21244](https://arxiv.org/abs/2510.21244)): Benchmark for expert-level intelligent outbound calling. Six major business domains, 30 representative sub-scenarios with scenario-specific process decomposition and weighted scoring. Includes a large-model-driven User Simulator generating diverse persona-rich virtual users with realistic emotional variability. Dynamic evaluation adapts to task variations with automated and human-in-the-loop assessment.

**Audio MultiChallenge** ([arXiv:2512.14865](https://arxiv.org/abs/2512.14865)): Built on the text-based MultiChallenge framework. Extends evaluation to audio with four axes: Inference Memory (including Audio-Cue challenges requiring recall of ambient sounds and paralinguistic signals), Instruction Retention, Self Coherence, and the novel Voice Editing axis (mid-utterance speech repairs, backtracking). Dataset: 452 conversations from 47 speakers with 1,712 instance-specific rubrics. **Even frontier models struggle**: Gemini 3 Pro Preview (Thinking) achieves only 54.65%. Self Coherence degrades with longer audio context.

**ICASSP 2026 HumDial Challenge** ([arXiv:2601.05564](https://arxiv.org/abs/2601.05564)): Two tracks -- Track I (Emotional Intelligence): multi-turn emotional trajectory tracking, causal reasoning, empathetic response generation. Track II (Full-Duplex Interaction): real-time decision-making under "listening-while-speaking" conditions. 100+ registered teams, 15 valid submissions. Key finding: LLMs excel at analyzing emotional logic but generating empathetic vocal responses remains difficult. Silence maintenance (Rejection) scores are consistently lower than Interruption handling -- distinguishing valid user turns from background noise is the primary hurdle.

### 3.3 LLM-as-Judge for Voice (The Revolution)

Three landmark papers establish LLM-based evaluation as a viable paradigm for voice:

**1. SpeechLLM-as-Judges** ([arXiv:2510.14664](https://arxiv.org/abs/2510.14664), October 2025)

- Introduces SpeechEval: 32,207 multilingual speech clips, 128,754 annotations
- Four evaluation tasks: quality assessment, pairwise comparison, improvement suggestion, deepfake detection
- Develops SQ-LLM: speech-quality-aware LLM trained with chain-of-thought reasoning and reward optimization
- Achieves MOS prediction MSE of 0.17 and A/B test accuracy of 98.6%
- Generated explanations achieve BLEU scores of 25.8 and 30.2, surpassing task-specific models

**2. TRACE** ([arXiv:2601.13742](https://arxiv.org/abs/2601.13742), January 2026)

- Problem: LLM judges have strong reasoning but are limited to text; Audio Language Model (ALM) judges are opaque and expensive
- Solution: Extract audio cues (ASR transcription, MOS scores, prosody/affect/energy metrics) into a structured textual "blueprint"
- Feed blueprint to LLM judge for dimension-wise evaluation: Content (C), Voice Quality (VQ), Paralinguistics (P)
- Introduces Human Chain-of-Thought (HCoT) annotation protocol
- **Result**: Higher agreement with human raters than both ALMs and transcript-only LLM judges, at significantly lower cost

**3. LALM-as-a-Judge** ([arXiv:2602.04796](https://arxiv.org/abs/2602.04796), February 2026)

- First controlled benchmark for Large Audio-Language Models (LALMs) as safety judges
- 24,000 unsafe synthetic spoken dialogues (English), 3-10 turns each
- 8 harmful categories, 5 severity grades (very mild to severe)
- Benchmarks Qwen2-Audio, Audio Flamingo 3, MERaLiON as zero-shot judges across audio-only, transcription-only, and multimodal inputs
- Key finding: architecture- and modality-dependent tradeoffs -- the most sensitive judge is also the least stable across turns. Transcription quality (Whisper-Large) is a key bottleneck.

**Additionally**: ICLR 2025 published ["Audio Large Language Models Can Be Descriptive Speech Quality Evaluators"](https://arxiv.org/abs/2501.17202) -- introducing the first natural-language speech evaluation corpus from authentic human ratings with an alignment approach (ALLD) achieving 0.17 MSE and 98.6% A/B accuracy.

**Why this matters**: The shift from scalar metrics (WER, MOS) to LLM-as-Judge with chain-of-thought reasoning enables evaluation of subjective qualities -- empathy, naturalness, appropriateness -- that define production voice agent quality. TRACE's approach of extracting audio features into text blueprints is particularly elegant: it allows leveraging powerful text LLMs for audio evaluation without requiring expensive audio-native models.

---

## 4. Evolution of Voice Agent Evaluation (2024 --> 2026)

### 4.1 Timeline

**2024: Component-level metrics in isolation**
- WER for STT, MOS for TTS -- measured independently
- SD-Eval ([NeurIPS 2024](https://arxiv.org/abs/2406.13340)) begins incorporating paralinguistic variables (emotion, accent, age, environment) -- 7,303 utterances, 8.76 hours
- VoiceBench ([arXiv:2410.17196](https://arxiv.org/abs/2410.17196)) introduces noise/accent perturbations via TTS-generated speech

**Early 2025: Multi-dimensional and audio-native**
- Full-Duplex-Bench ([arXiv:2503.04721](https://arxiv.org/abs/2503.04721)): First benchmark for turn-taking and interruption evaluation in streaming interactions. v1.5 adds overlapping phenomena.
- ICLR 2025: Audio LLMs as descriptive speech quality evaluators -- proves LLMs can judge speech quality with natural language explanations
- VocalBench ([arXiv:2505.15727](https://arxiv.org/abs/2505.15727)): 27 models, 14 capabilities across semantic, acoustic, conversational, and robustness dimensions in speech-instruction format

**Mid 2025: Agentic and production-oriented**
- VoiceAgentBench: tool calling and safety in multilingual settings
- aiewf-eval: 30-turn production-realistic conversations with tool use
- Testing the Testers: meta-evaluation revealing the simulation-vs-evaluation gap
- ClonEval: standardized voice cloning evaluation

**Late 2025 -- Early 2026: LLM-as-Judge and safety**
- SpeechLLM-as-Judges: chain-of-thought speech quality evaluation at scale
- TRACE: text-based reasoning over audio cues for cost-effective evaluation
- LALM-as-a-Judge: safety evaluation for spoken dialogues
- ICASSP 2026 HumDial: emotion + full-duplex with 100+ teams competing
- Audio MultiChallenge: even Gemini 3 Pro (Thinking) achieves only 54.65%

### 4.2 Paradigm Comparison

| Dimension | 2024 | Feb 2026 |
|-----------|------|----------|
| Primary metric | WER / MOS (single scalar) | Multi-dimensional (accuracy + latency + quality + safety) |
| Evaluation unit | Single utterance | 30+ turn conversations |
| Test data | Synthetic TTS-generated | Hybrid real + synthetic (VCB Bench, Audio MultiChallenge) |
| Architecture tested | Cascaded only (STT + LLM + TTS) | Both cascaded and speech-to-speech native |
| Evaluation method | Automated metrics only | Automated + LLM-judge + human preference |
| Safety | Not evaluated | Adversarial attacks, toxicity, injection, severity grading |
| Emotion | Not evaluated | Dedicated benchmarks (MULTI-Bench, HumDial Track I) |
| Full-duplex | Not evaluated | Multiple benchmarks (Full-Duplex-Bench, MTR-DuplexBench, HumDial Track II) |
| Turn-taking | Not evaluated | Explicit dimensions (pause, backchannel, interruption, overlap) |
| Judge type | Human MOS / simple automated | SpeechLLM-as-Judge with CoT, TRACE blueprints, LALM judges |
| Languages | English only | English + Chinese + Indic + (limited) European |
| Production realism | Low (clean, scripted) | Medium (tool calling, knowledge grounding, multi-turn) |

### 4.3 What Changed and What Didn't

**Changed**: The field moved from component-level to system-level evaluation, from single metrics to multi-dimensional assessment, and from human-only to LLM-assisted judging. The existence of aiewf-eval, VoiceAgentBench, and Audio MultiChallenge represents a genuine paradigm shift.

**Didn't change**: English dominance, synthetic data bias, and the absence of cost-quality tradeoff analysis. No benchmark tests cross-session consistency. Multi-speaker scenarios remain untested. The gap between benchmark performance and production reality remains wide -- the best platforms achieve only 0.92 F1 for evaluation and much lower for simulation.

---

## 5. Industry Evaluation Platforms

### 5.1 Platform Comparison

| Platform | Focus | Key Feature | Performance | Founded |
|----------|-------|-------------|-------------|---------|
| [Hamming AI](https://hamming.ai/) | Enterprise QA | 4M+ calls analyzed, 50+ built-in metrics | 95-96% human agreement | 2024 |
| [Coval](https://www.coval.dev/) | Simulation + regression | Waymo-inspired methodology, self-driving car testing principles | Industry simulation reports | 2024 (YC) |
| [Evalion](https://evalion.ai/) | Simulation + evaluation | Highest combined quality (Oxford/Pompeu Fabra collaboration) | 0.92 F1, 86.7% accuracy | 2025 |
| [Roark](https://roark.ai/) | Production monitoring | Real-world call replay with voice cloning | 40+ built-in metrics | 2024 (YC) |
| [Braintrust](https://www.braintrust.dev/) | Unified eval | Text + audio + multimodal in one platform | Broad observability | 2023 |

### 5.2 Hamming's 4-Layer Quality Framework

Hamming's framework, derived from evaluating 4M+ production voice agent calls across 10K+ agents (2025-2026), provides the most comprehensive production-oriented quality model:

1. **Infrastructure Layer**: Component latency (TTFB, TTFW), RTFx, packet loss, jitter, SNR, codec performance
2. **Agent Execution Layer**: Tool calling accuracy, instruction following, knowledge base grounding, prompt compliance, hallucination rate
3. **User Reaction Layer**: Sentiment analysis, satisfaction signals, frustration detection (vocal cues: long pauses, hesitation, tone changes), completion rates
4. **Business Outcome Layer**: Revenue impact, CSAT scores, resolution rate, cost per resolution

Their two-step evaluation pipeline first determines relevancy (should this assertion apply?), then evaluates -- eliminating false failures from irrelevant checks. This achieves 95-96% agreement with human evaluators, measured against 200+ expert annotations.

### 5.3 Coval's Waymo-Inspired Methodology

Coval ([TechCrunch coverage](https://techcrunch.com/2025/01/23/coval-evaluates-ai-voice-and-chat-agents-like-self-driving-cars/)) applies autonomous vehicle testing principles to voice agents:

- **Simulation-first**: Run thousands of simulations simultaneously before deployment
- **Regression testing**: Every code change tested against a baseline, like Waymo testing each engineering modification
- **Customizable environments**: Realistic voices, personas, and environmental conditions
- **Cross-modal**: Tests agents through both text and voice channels, including phone calls
- $3.3M seed round (MaC Venture Capital, Y Combinator, General Catalyst)

### 5.4 Roark's Production Replay

- Replays real production calls against newest AI logic before going live
- Clones original caller's voice for realistic re-testing
- Monitors sentiment and vocal cues (frustration, pauses, hesitation) often missed by text-based evaluation
- Golden set replay every few minutes to detect drift, outages, model changes, prompt regressions
- Integrates with VAPI, Retell, and custom APIs

### 5.5 Key Latency Targets (Industry Consensus)

| Target | Threshold | Source |
|--------|-----------|--------|
| Natural conversation | Sub-500ms TTFW | Daily/Pipecat |
| Acceptable production | ~800ms V2V | aiewf-eval data |
| Human neurological response | 200-300ms | Neuroscience literature |
| Industry median (actual) | 1,400-1,700ms | Hamming AI (4M calls) |
| Unacceptable (user drops) | >3,000ms | Multiple sources |

Track P95 and P99 latency, not averages. Gemini Live's 30,000ms max V2V latency in aiewf-eval illustrates why: the median of 2,624ms is bad, but the tail is catastrophic.

---

## 6. Recommendations for Music Attribution Voice Agent Evaluation

### 6.1 Metrics to Track

Based on the landscape analysis above, a music attribution voice agent should be evaluated across these dimensions:

| Metric | Target | Rationale |
|--------|--------|-----------|
| Task completion rate | >90% | Attribution queries successfully answered with correct information |
| TTFW (Time to First Word) | <500ms | Natural conversational pacing per Daily/Pipecat threshold |
| WER on music-domain vocabulary | <5% | Artist names, track titles, ISRC/ISWC codes have specialized vocabulary |
| Tool-calling accuracy | >95% | MusicBrainz, Discogs, AcoustID API calls must be correct |
| Turn-taking quality | Qualitative | Interruption handling during batch review workflows |
| Multi-turn consistency | >95% | Same query across 30-turn session produces consistent answers |
| User satisfaction | >4.0/5.0 | Post-session rating |
| Cost per successful query | Budget-dependent | Track to enable intelligence-latency optimization |
| Confidence communication | Qualitative | Does the voice convey certainty/uncertainty appropriately? |

### 6.2 What No Leaderboard Tests (But We Must)

These dimensions are critical for music attribution but absent from every existing benchmark:

1. **Music-domain vocabulary accuracy**: Artist names (especially non-English: Bjork, Sigur Ros, Iannis Xenakis), song titles with special characters, ISRC codes (e.g., "USRC17607839"), ISWC codes, label names. Standard ASR benchmarks use news/conversation transcripts, not music metadata.

2. **Multi-accent robustness for a global artist base**: A music attribution system serves artists worldwide. Nigerian Afrobeats producers, Japanese electronic musicians, Brazilian bossa nova artists, and Welsh choral composers all need accurate service. No benchmark tests this range.

3. **Cross-session attribution consistency**: If the system reports 85% confidence for a particular attribution on Monday, it should report the same on Thursday (absent new evidence). No benchmark tests temporal consistency of factual claims.

4. **Confidence communication quality**: The A0-A3 assurance levels central to our attribution framework must be conveyed vocally. Does the agent's tone, pacing, and word choice accurately reflect whether an attribution is A3 (artist-verified) vs A0 (no data)? This is a novel evaluation dimension with no existing benchmark.

5. **Digital twin persona fidelity**: If an artist creates a voice agent persona for their attribution queries, does the agent maintain consistent personality, knowledge boundaries, and communication style? Related to ClonEval's speaker similarity metrics but extends to behavioral consistency.

6. **Voice consent verification accuracy**: When a voice agent asks for consent to process attribution data, does the user's spoken response get correctly interpreted? Misinterpreting "no" as "know" has legal implications. No benchmark tests consent-critical speech recognition accuracy.

### 6.3 Evaluation Strategy Recommendations

**Phase 1 (MVP)**: Use aiewf-eval methodology adapted for music attribution scenarios. Build 10-15 multi-turn test conversations covering common attribution workflows. Use Claude as judge with music-domain-specific rubrics. Track TTFW and task completion rate.

**Phase 2 (Production)**: Integrate Hamming AI or Roark for production monitoring. Build a golden set of 50+ test calls that replay against every deployment. Monitor per-accent WER using real user recordings (with consent). Track cost per query alongside quality metrics.

**Phase 3 (Research)**: Develop a music-domain evaluation corpus analogous to VCB Bench but for English + top-10 music market languages. Create music-vocabulary-specific ASR benchmarks. Publish results to establish community baselines.

### 6.4 Model Selection Implications

Based on the aiewf-eval data, the current optimal choices for a music attribution voice agent are:

- **Speech-to-speech**: Ultravox v0.7 (97.7% pass rate, 864ms V2V) -- if latency budget allows ~900ms
- **Cascaded (fast)**: Nemotron 3 Nano 30B (91.0%, 171ms TTFB) or Gemini 2.5 Flash (93.7%, 594ms TTFB) for the LLM component
- **Cascaded (accurate)**: GPT-5.1 (100%, 916ms TTFB) when accuracy is paramount and latency is acceptable
- **STT component**: NVIDIA Canary-Qwen-2.5B (5.63% WER) for accuracy, Parakeet TDT 1.1B for speed, or Voxtral Mini 4B for open-source realtime streaming
- **TTS component**: Hume Octave or ElevenLabs Flash v2.5 for emotional expressiveness; Inworld TTS-1.5 for cost efficiency

The voice agent is designated as a Pro/premium feature in the music attribution scaffold. Given the intelligence-latency tradeoff, the recommendation is to start with a cascaded architecture (Voxtral Mini 4B + Gemini 2.5 Flash + quality TTS) for the MVP, with a migration path to speech-to-speech (Ultravox) as that ecosystem matures.

---

## Sources and References

### Leaderboards
- [HuggingFace Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)
- [TTS Arena V2](https://huggingface.co/spaces/TTS-AGI/TTS-Arena-V2)
- [Artificial Analysis Speech Arena](https://artificialanalysis.ai/text-to-speech/arena)
- [aiewf-eval GitHub](https://github.com/kwindla/aiewf-eval)
- [ClonEval Leaderboard](https://huggingface.co/spaces) (via arXiv:2504.20581)

### Benchmark Papers
- Open ASR Leaderboard: [arXiv:2510.06961](https://arxiv.org/abs/2510.06961)
- VoiceBench: [arXiv:2410.17196](https://arxiv.org/abs/2410.17196)
- SD-Eval: [arXiv:2406.13340](https://arxiv.org/abs/2406.13340)
- Full-Duplex-Bench: [arXiv:2503.04721](https://arxiv.org/abs/2503.04721)
- VocalBench: [arXiv:2505.15727](https://arxiv.org/abs/2505.15727)
- VoiceAgentBench: [arXiv:2510.07978](https://arxiv.org/abs/2510.07978)
- VCB Bench: [arXiv:2510.11098](https://arxiv.org/abs/2510.11098)
- VoiceAgentEval: [arXiv:2510.21244](https://arxiv.org/abs/2510.21244)
- MULTI-Bench: [arXiv:2511.00850](https://arxiv.org/abs/2511.00850)
- MTR-DuplexBench: [arXiv:2511.10262](https://arxiv.org/abs/2511.10262)
- Testing the Testers: [arXiv:2511.04133](https://arxiv.org/abs/2511.04133)
- Audio MultiChallenge: [arXiv:2512.14865](https://arxiv.org/abs/2512.14865)
- HumDial Challenge: [arXiv:2601.05564](https://arxiv.org/abs/2601.05564)
- TRACE: [arXiv:2601.13742](https://arxiv.org/abs/2601.13742)
- LALM-as-a-Judge: [arXiv:2602.04796](https://arxiv.org/abs/2602.04796)
- ClonEval: [arXiv:2504.20581](https://arxiv.org/abs/2504.20581)

### LLM-as-Judge for Voice
- SpeechLLM-as-Judges: [arXiv:2510.14664](https://arxiv.org/abs/2510.14664)
- Audio LLMs as Speech Quality Evaluators (ICLR 2025): [arXiv:2501.17202](https://arxiv.org/abs/2501.17202)

### Industry and Analysis
- [Daily blog: Benchmarking LLMs for Voice Agent Use Cases](https://www.daily.co/blog/benchmarking-llms-for-voice-agent-use-cases/)
- [Ultravox blog: Why speech-to-speech is the future](https://www.ultravox.ai/blog/why-speech-to-speech-is-the-future-for-ai-voice-agents-unpacking-the-aiewf-eval)
- [Coval/Pipecat/Ultravox: State of Voice AI Instruction Following](https://www.coval.dev/blog/the-state-of-voice-ai-instruction-following-in-2026-a-conversation-with-kwindla-from-pipecat-and-zach-from-ultravox)
- [Hamming AI: Voice Agent Evaluation Metrics Guide](https://hamming.ai/resources/voice-agent-evaluation-metrics-guide)
- [Hamming AI: 4-Layer Quality Framework](https://hamming.ai/resources/guide-to-ai-voice-agents-quality-assurance)
- [Northflank: Best Open Source STT Models 2026](https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks)
- [Inworld: Best TTS APIs for Real-Time Voice Agents 2026](https://inworld.ai/resources/best-voice-ai-tts-apis-for-real-time-voice-agents-2026-benchmarks)
- [Telnyx: AI Model Intelligence vs Latency](https://telnyx.com/resources/ai-model-intelligence-vs-latency)

### Fairness and Bias
- [ACM FAccT 2025: Accent Bias and Digital Exclusion](https://dl.acm.org/doi/10.1145/3715275.3732018)
- [ACM FAccT 2024: Speaking of Accent -- Misconceptions in ASR Research](https://dl.acm.org/doi/10.1145/3630106.3658969)

### Safety
- [MBZUAI: Voice Jailbreak Defense](https://mbzuai.ac.ae/news/your-voice-can-jailbreak-a-speech-model-heres-how-to-stop-it-without-retraining/)
- [Audio Jailbreak Benchmark: arXiv:2505.15406](https://arxiv.org/abs/2505.15406)
- [Gemini 2.0 Flash Audio Attack Success Rates](https://quantumzeitgeist.com/98-26-percent-reveal-success-rate-audio-attacks/)

### Model Cards
- [NVIDIA Canary-Qwen-2.5B](https://huggingface.co/nvidia/canary-qwen-2.5b)
- [IBM Granite Speech 3.3 8B](https://huggingface.co/ibm-granite/granite-speech-3.3-8b)
- [Microsoft Phi-4-Multimodal](https://huggingface.co/microsoft/Phi-4-multimodal-instruct)
- [Whisper Large V3 Turbo](https://huggingface.co/openai/whisper-large-v3-turbo)
- [Mistral Voxtral Mini 4B](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)
- [NVIDIA Parakeet TDT 1.1B](https://huggingface.co/nvidia/parakeet-tdt-1.1b)
