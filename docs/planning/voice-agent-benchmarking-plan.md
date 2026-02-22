# Voice Agent Benchmarking Plan

**Status:** Planning
**Created:** 2026-02-22
**Context:** Upgrade `scripts/benchmark_voice.py` from component-level benchmarks with wrong dependencies to a fully automated end-to-end benchmarking suite with synthetic voice commands and optional microphone support.

**Related:**
- `scripts/benchmark_voice.py` — Current benchmark script (to be modified)
- `docs/prd/decisions/L5-operations/voice-pipeline-benchmarking.decision.yaml` — PRD decision node
- `src/music_attribution/voice/pipeline.py` — Pipecat pipeline factory
- `src/music_attribution/voice/config.py` — VoiceConfig (single source of truth)
- `src/music_attribution/voice/drift.py` — DriftDetector
- `src/music_attribution/observability/voice_metrics.py` — Prometheus metrics

---

## 1. Current State Analysis

### 1.1 What Exists

`scripts/benchmark_voice.py` provides three component benchmarks:

| Component | What It Measures | Status |
|-----------|-----------------|--------|
| **STT** | Whisper model load + inference (per model x device) | **Wrong library** (`openai-whisper` instead of `faster-whisper`) |
| **TTS** | Piper synthesis latency | **Wrong integration** (standalone `piper` instead of pipecat integration) |
| **Drift** | Embedding encode + cosine similarity scoring | Working |

### 1.2 Problems

**Problem 1: Wrong STT library.** The script imports `whisper` (OpenAI's package). The project uses `faster-whisper` via `pipecat-ai[whisper]`.

- Current: `import whisper; model = whisper.load_model("small", device="cuda")`
- Correct: `from faster_whisper import WhisperModel; model = WhisperModel("small", device="cuda", compute_type="float16")`
- API difference: `faster_whisper` returns `(segments_generator, info)`, not a dict. Segments must be consumed to measure full transcription time.

**Problem 2: Wrong TTS integration.** The script imports `from piper import PiperVoice` and expects a local model file. The project uses Pipecat's `PiperTTSService`. For component benchmarks, direct Piper usage is correct (measures raw synthesis), but the model path discovery is broken.

**Problem 3: No end-to-end pipeline benchmarking.** The production pipeline is `Transport In -> Silero VAD -> STT -> Context Aggregator -> LLM -> TTS -> Transport Out`. Total user-perceived latency is not measured.

**Problem 4: No synthetic voice commands.** The 440 Hz sine wave measures raw STT throughput but produces no meaningful transcription. No way to verify accuracy or benchmark the conversational loop.

**Problem 5: No microphone support.** No way to benchmark with real audio input.

### 1.3 What Works Well (Keep)

- `detect_hardware()` — Robust CPU/GPU/VRAM/CUDA detection
- `generate_test_audio()` — Valid WAV generation for raw throughput tests
- `_get_rss_mb()` / `_get_vram_mb()` — Memory usage tracking
- `_should_skip_model()` — VRAM guard logic with correct thresholds
- JSON output format with hardware metadata and timestamp
- The argparse CLI structure with `--models`, `--cpu-only`, `--output`

---

## 2. Proposed Changes

### 2.1 Fix STT: openai-whisper -> faster-whisper

```python
from faster_whisper import WhisperModel

model = WhisperModel(
    model_name,
    device=device,
    compute_type="float16" if device == "cuda" else "int8",
)

segments, info = model.transcribe(str(audio_path))
for _ in segments:
    pass  # Force full decode — generator is lazy
```

### 2.2 Fix TTS: Model Path Discovery

Keep direct `PiperVoice` for component measurement (Pipecat overhead captured in end-to-end). Fix model path to auto-discover or accept `--piper-model` CLI arg.

### 2.3 Add Synthetic Voice Commands

Text -> Piper TTS -> WAV -> faster-whisper STT -> measure transcription accuracy + round-trip latency.

### 2.4 Add --with-microphone Flag

Optional real-time microphone capture using `sounddevice` (soft dependency).

---

## 3. Synthetic Voice Command Design

### 3.1 Command Corpus

**Category A: Simple queries (short, single intent)**

| ID | Utterance | Expected Tool Call |
|----|-----------|-------------------|
| A1 | "What is the confidence score for Hide and Seek?" | `explain_confidence` |
| A2 | "Search for tracks by Imogen Heap" | `search_attributions` |
| A3 | "Show me low confidence attributions" | `search_attributions` |
| A4 | "What does assurance level A2 mean?" | None (general knowledge) |

**Category B: Action commands (corrections, feedback)**

| ID | Utterance | Expected Tool Call |
|----|-----------|-------------------|
| B1 | "The songwriter for Headlock should be Imogen Heap, not unknown" | `suggest_correction` |
| B2 | "I rate this attribution a nine out of ten" | `submit_feedback` |
| B3 | "Correct the artist name to Frou Frou" | `suggest_correction` |

**Category C: Multi-turn conversational (tests context retention)**

| ID | Utterance Sequence |
|----|--------------------|
| C1 | "Search for Hide and Seek" -> "Explain the confidence for the first result" |
| C2 | "What sources disagree on this track?" -> "Submit a correction for the artist field" |

### 3.2 WAV Generation

Each utterance is pre-synthesized to WAV using Piper TTS before the benchmark timer starts. This simulates realistic speech input without requiring a microphone. WAV files are generated once at benchmark start and reused across iterations. Format: 16 kHz, 16-bit, mono.

### 3.3 STT Accuracy Measurement

After transcribing each synthetic WAV, compute:

- **Word Error Rate (WER):** Inline implementation (~15 lines, Levenshtein on word sequences). No `jiwer` dependency.
- **Domain Token Accuracy:** Check if key domain terms survived the TTS->STT round trip: artist names, track titles, technical terms.

---

## 4. End-to-End Pipeline Benchmarking

### 4.1 Level 1: STT + LLM + TTS (No Transport)

```
Pre-generated WAV -> faster-whisper -> LLM agent call -> Piper TTS -> output WAV
                     |--- STT ---|--- LLM ---|--- TTS ---|
                     |------------ total latency ---------|
```

Call components directly (not through Pipecat frames).

### 4.2 LLM Handling

| Mode | Flag | Description |
|------|------|-------------|
| Mock (default) | `--mock-llm` | Fixed response after configurable delay (default 500ms) |
| Live | `--live-llm` | Real PydanticAI agent. Requires API key. |

### 4.3 Latency Breakdown

| Metric | Description |
|--------|-------------|
| `stt_ms` | WAV input -> transcript text |
| `llm_ms` | Transcript -> LLM response |
| `tts_ms` | Response text -> output WAV |
| `total_ms` | Wall-clock end-to-end |
| `overhead_ms` | `total - (stt + llm + tts)` |
| `rtf` | Real-time factor: `total_ms / input_audio_duration_ms`. RTF < 1.0 = faster than real-time |

---

## 5. Implementation Phases

### Phase 1: Fix Existing Benchmarks

- Replace `openai-whisper` with `faster-whisper` in STT benchmark
- Fix Piper model path discovery
- Remove TTS placeholder warmup loop
- Validate: `uv run python scripts/benchmark_voice.py --models tiny --cpu-only`

### Phase 2: Add Synthetic Voice Commands

- Add `SYNTHETIC_COMMANDS` corpus
- Add `generate_command_wavs()` — pre-synthesize all commands to WAV
- Add `benchmark_synthetic_stt()` — round-trip accuracy measurement
- Add inline `compute_wer()` helper
- Add `--skip-synthetic` CLI flag
- New JSON output section: `synthetic_stt`

### Phase 3: Add End-to-End Pipeline Benchmark

- Add `benchmark_end_to_end()` — STT -> LLM -> TTS latency breakdown
- Add `MockLLM` class with configurable delay
- Add `--mock-llm`, `--live-llm`, `--llm-delay-ms` CLI flags
- New JSON output section: `end_to_end`

### Phase 4: Add Microphone Support

- Add `--with-microphone` and `--record-seconds` CLI flags
- Add `capture_microphone()` using `sounddevice` (soft dependency)
- Feeds captured audio into the same pipeline as synthetic commands
- Add `sounddevice>=0.5` to voice dependency group

### Phase 5: Pipecat Pipeline-Level Benchmark (Deferred)

Full Pipecat pipeline with mock transport injecting audio frames. Significantly more complex. Deferred until Phases 1-4 validated.

---

## 6. Expected Output Format

### 6.1 JSON Schema

```json
{
  "hardware": {
    "cpu": "x86_64",
    "gpu": "NVIDIA GeForce RTX 2070 SUPER",
    "vram_gb": 8.0,
    "cuda_available": true,
    "torch_version": "2.5.1+cu124"
  },
  "timestamp": "2026-02-22T14:30:00+00:00",
  "benchmarks": {
    "stt": [
      {
        "model": "small", "device": "cuda", "compute_type": "float16",
        "load_ms": 1200.0, "inference_ms": 380.0,
        "audio_duration_s": 10.0, "rtf": 0.038,
        "rss_mb": 1450.0, "vram_mb": 1200.0
      }
    ],
    "tts": [
      {
        "provider": "piper", "model": "en_US-lessac-medium",
        "synthesis_ms": 95.0, "text_length": 56, "audio_duration_ms": 3200.0
      }
    ],
    "drift": [
      { "method": "embedding", "model": "all-MiniLM-L6-v2", "score_ms": 12.0 }
    ],
    "synthetic_stt": [
      {
        "command_id": "A1",
        "original_text": "What is the confidence score for Hide and Seek?",
        "transcribed_text": "What is the confidence score for hide and seek?",
        "wer": 0.0,
        "domain_keywords_found": ["confidence", "score", "hide", "seek"],
        "domain_keywords_missed": [],
        "stt_ms": 350.0, "model": "small", "device": "cuda"
      }
    ],
    "end_to_end": [
      {
        "command_id": "A1",
        "stt_ms": 350.0, "llm_ms": 500.0, "llm_mode": "mock",
        "tts_ms": 95.0, "total_ms": 960.0, "overhead_ms": 15.0,
        "input_audio_duration_ms": 2400.0, "rtf": 0.40
      }
    ],
    "microphone": null
  }
}
```

### 6.2 CLI Interface (Final)

```bash
# Quick component benchmark
uv run python scripts/benchmark_voice.py --models tiny,small --cpu-only --skip-synthetic

# Full automated benchmark (synthetic commands + end-to-end with mock LLM)
uv run python scripts/benchmark_voice.py --models small --output benchmark-results.json

# With real LLM (requires ANTHROPIC_API_KEY)
uv run python scripts/benchmark_voice.py --models small --live-llm

# With microphone
uv run python scripts/benchmark_voice.py --models small --with-microphone --record-seconds 5
```

| Flag | Phase | Default | Description |
|------|-------|---------|-------------|
| `--skip-synthetic` | 2 | False | Skip synthetic command benchmarks |
| `--piper-model` | 1 | Auto-discover | Path to Piper ONNX model file |
| `--mock-llm` | 3 | True | Use mock LLM for end-to-end |
| `--live-llm` | 3 | False | Use real PydanticAI agent |
| `--llm-delay-ms` | 3 | 500 | Mock LLM response delay |
| `--with-microphone` | 4 | False | Enable microphone capture |
| `--record-seconds` | 4 | 5 | Microphone recording duration |

---

## 7. Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Piper model not downloaded | Auto-download via piper-tts, or clear error with download instructions |
| CUDA OOM on medium/large models | Existing VRAM guard; RTX 2070 Super (8 GB) safely runs up to medium |
| Synthetic WAV quality degrades STT accuracy | Feature, not bug — measures actual TTS->STT degradation |
| Mock LLM hides real latency | `--live-llm` flag provides real measurement when needed |
| `sounddevice` unavailable in CI/headless | `--with-microphone` is opt-in; CI runs without it |
| WER metric sensitive to casing/punctuation | Normalize both texts (lowercase, strip punctuation) before comparison |
