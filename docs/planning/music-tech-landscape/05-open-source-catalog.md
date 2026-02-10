# Open-Source Library Catalog — Music Attribution Tooling

> **Parent**: [README.md](README.md) > Open-Source Library Catalog
> **Updated**: 2026-02-10

---

## How to Use This Catalog

This catalog maps every relevant open-source library for building music attribution infrastructure. Libraries are grouped by function and evaluated for:

- **Attribution relevance**: How directly the library supports attribution workflows
- **Maintenance status**: Is the library actively maintained?
- **Integration complexity**: How much custom code is needed to integrate
- **License compatibility**: Can we use it in an open-source scaffold?

---

## Python: Music Information Retrieval (MIR)

### librosa

| Attribute | Details |
|-----------|---------|
| **Repository** | [librosa/librosa](https://github.com/librosa/librosa) |
| **Stars** | ~8.2k |
| **License** | ISC |
| **Latest** | v0.11 (Mar 2025) |
| **Python** | 3.8+ |
| **Dependencies** | NumPy, SciPy, soundfile, audioread, lazy_loader |

**Capabilities**: Audio feature extraction (MFCCs, chroma, spectral contrast, tonnetz), beat tracking, tempo estimation, spectrograms, onset detection, harmonic-percussive separation.

**Attribution relevance**: Core audio analysis. Feature extraction is prerequisite for similarity computation, fingerprinting augmentation, and embedding-based attribution. Chroma features are particularly relevant for melodic similarity.

**Key functions for our use**:
- `librosa.feature.chroma_cqt()` — Chromagram for melodic comparison
- `librosa.feature.mfcc()` — Timbre fingerprinting
- `librosa.beat.beat_track()` — Rhythmic pattern analysis
- `librosa.effects.harmonic()` — Isolate harmonic content for melody attribution

**Limitations**: CPU-only; can be slow on large-scale batch processing. Consider `essentia` for performance-critical pipelines.

---

### essentia (Music Technology Group, UPF Barcelona)

| Attribute | Details |
|-----------|---------|
| **Repository** | [MTG/essentia](https://github.com/MTG/essentia) |
| **Stars** | ~3.4k |
| **License** | AGPL-3.0 |
| **Maintained** | Active development |
| **Language** | C++ with Python bindings |
| **Python** | Via `essentia` package |

**Capabilities**: Comprehensive audio analysis toolkit: spectral analysis, rhythmic analysis, tonal analysis, loudness computation, audio quality metrics, audio classification. Includes pre-trained models for genre classification, mood detection, instrument recognition.

**Attribution relevance**: More performant than librosa for production workloads. The pre-trained classifiers can help with genre/style cohort attribution (Lemonaide's approach). Tonal analysis helps with key/mode similarity.

**Key modules**:
- `essentia.standard.KeyExtractor` — Key and mode detection
- `essentia.standard.RhythmExtractor2013` — Detailed rhythmic analysis
- `essentia.standard.TensorflowPredictEffnetDiscogs` — Genre/style classification via Discogs taxonomy
- `essentia.standard.MusicExtractor` — All-in-one feature extraction

**License consideration**: AGPL-3.0 means derivative works must also be AGPL. For our open-source scaffold this is acceptable. Commercial users would need to evaluate.

**WASM port**: Available as `essentia.js` — see JavaScript section below.

---

### madmom (CPJKU, Johannes Kepler University)

| Attribute | Details |
|-----------|---------|
| **Repository** | [CPJKU/madmom](https://github.com/CPJKU/madmom) |
| **Stars** | ~1.6k |
| **License** | BSD / CC-BY-NC-SA (for models) |
| **Latest** | v0.16.1 (Nov 2018) |
| **Status** | Maintenance mode (no active development) |

**Capabilities**: Beat detection, tempo estimation, onset detection, chord recognition, key detection. Uses deep learning models for beat tracking — considered state-of-the-art in beat detection research at time of release.

**Attribution relevance**: Beat and onset detection are useful for temporal alignment between original and generated tracks. Chord recognition enables harmonic progression comparison.

**Assessment**: Still functional but dated. The pre-trained models work well but Python 3.10+ compatibility requires careful dependency management. Use librosa or essentia for new projects unless specifically needing madmom's beat tracking accuracy.

---

### mir_eval

| Attribute | Details |
|-----------|---------|
| **Repository** | [craffel/mir_eval](https://github.com/craffel/mir_eval) |
| **Stars** | ~687 |
| **License** | MIT |
| **Latest** | v0.8.2 (Feb 2025) |
| **Status** | Active |

**Capabilities**: Evaluation metrics for MIR systems: beat tracking evaluation, melody extraction evaluation, chord recognition evaluation, onset detection evaluation, separation quality metrics (SDR, SIR, SAR).

**Attribution relevance**: Critical for evaluating our attribution pipeline's quality. If we use audio similarity as a proxy for attribution influence, mir_eval metrics help measure how well our similarity detection works against ground truth.

**Key metrics**:
- `mir_eval.melody.evaluate()` — Melody accuracy, voicing recall/FA
- `mir_eval.beat.evaluate()` — Beat tracking F-measure
- `mir_eval.separation.bss_eval_sources()` — Source separation quality

---

### mirdata

| Attribute | Details |
|-----------|---------|
| **Repository** | [mir-dataset-tools/mirdata](https://github.com/mir-dataset-tools/mirdata) |
| **Stars** | ~398 |
| **License** | BSD-3-Clause |
| **Latest** | v1.0 (Sep 2025) |
| **Status** | Active |

**Capabilities**: Standardized loading for 50+ MIR datasets. Uniform API across diverse datasets: DALI (lyrics alignment), MedleyDB (multitrack), Orchset (orchestral), RWC (reference), MAESTRO (piano MIDI+audio).

**Attribution relevance**: Essential for benchmarking. We can validate entity resolution and confidence scoring against curated datasets with known ground truth attributions.

---

### aubio

| Attribute | Details |
|-----------|---------|
| **Repository** | [aubio/aubio](https://github.com/aubio/aubio) |
| **Stars** | ~3k |
| **License** | GPL-3.0 |
| **Language** | C with Python bindings |
| **Status** | Active |

**Capabilities**: Real-time audio analysis: pitch detection (Yin, YINFFT), onset detection, beat tracking, spectral analysis. Designed for real-time performance.

**Attribution relevance**: Useful for real-time audio fingerprinting in streaming contexts. The pitch detection is particularly robust for monophonic sources.

---

## Python: Audio Fingerprinting

### dejavu

| Attribute | Details |
|-----------|---------|
| **Repository** | [worldveil/dejavu](https://github.com/worldveil/dejavu) |
| **Stars** | ~6.7k |
| **License** | MIT |
| **Status** | ~2020 (community maintained) |

**Capabilities**: Shazam-like audio fingerprinting. Records audio fingerprints to a database (MySQL or PostgreSQL), then identifies unknown audio against the database. Based on the "An Industrial Strength Audio Search Algorithm" paper.

**How it works**:
1. Converts audio to spectrogram
2. Finds peak frequencies (constellation map)
3. Creates fingerprints from peak pairs
4. Stores fingerprints in database
5. Matches incoming audio against stored fingerprints

**Attribution relevance**: Can detect if AI-generated audio contains segments that are near-exact copies of training data. This is the "data replication detection" use case — complementary to the MiRA academic tool.

**Limitations**: Designed for exact/near-exact matching. Does not detect stylistic similarity, only audio reproduction. Not robust against pitch shifting or time stretching.

---

### Chromaprint / AcoustID

| Attribute | Details |
|-----------|---------|
| **Repository** | [acoustid/chromaprint](https://github.com/acoustid/chromaprint) |
| **Stars** | ~1.2k |
| **License** | LGPL-2.1 / MIT |
| **Latest** | v1.6 (Aug 2025) |
| **Language** | C/C++ |

**Capabilities**: Chromagram-based audio fingerprinting. Generates a compact fingerprint from audio that is robust to encoding quality differences, minor speed variations, and background noise. Used by the AcoustID service which links fingerprints to MusicBrainz recordings.

**How it works**:
1. Computes chromagram (12-bin pitch class profile)
2. Quantizes chromagram to binary fingerprint
3. Fingerprint is a compact integer array

**Attribution relevance**: Direct link to MusicBrainz's entity resolution. If we fingerprint audio and query AcoustID, we get MusicBrainz recording IDs back — instantly connecting audio to structured metadata.

**Integration path**: `pyacoustid` (Python bindings) → AcoustID API → MusicBrainz recording → full metadata graph.

---

### pyacoustid

| Attribute | Details |
|-----------|---------|
| **Repository** | [beetbox/pyacoustid](https://github.com/beetbox/pyacoustid) |
| **Stars** | ~373 |
| **License** | MIT |
| **Latest** | v1.3.0 |

**Capabilities**: Python wrapper for Chromaprint + AcoustID web service. Generates fingerprints locally, queries AcoustID API for matches.

**Usage**:
```python
import acoustid
# Fingerprint a file and look up metadata
for score, recording_id, title, artist in acoustid.match(api_key, audio_file):
    print(f"{artist} - {title} (score: {score})")
```

**Attribution relevance**: Most direct path from audio file → MusicBrainz entity. Essential for our A1→A2 assurance upgrade.

---

### audfprint

| Attribute | Details |
|-----------|---------|
| **Repository** | [dpwe/audfprint](https://github.com/dpwe/audfprint) |
| **Stars** | ~591 |
| **License** | MIT |
| **Author** | Dan Ellis (Google/Columbia) |
| **Status** | Active |

**Capabilities**: Large-scale audio fingerprinting. Optimized for matching against databases of millions of tracks. Stores fingerprints in hash tables for O(1) lookup.

**Attribution relevance**: When we need to check AI-generated audio against a large catalog of known tracks, audfprint is designed for exactly this scale. More suitable for batch processing than dejavu.

---

## Python: Music Metadata

### musicbrainzngs

| Attribute | Details |
|-----------|---------|
| **Repository** | [alastairUK/python-musicbrainzngs](https://github.com/alastairUK/python-musicbrainzngs) |
| **Stars** | ~500 |
| **License** | ISC (BSD-like) |
| **Status** | Maintained |

**Capabilities**: Complete Python bindings for the MusicBrainz XML Web Service v2. Supports searches (artist, recording, release, work, label), lookups by MBID, browsing related entities, and submitting data.

**Attribution relevance**: MusicBrainz is the most comprehensive open music metadata database. This library is our primary interface for:
- Artist entity resolution (name → MBID → canonical identity)
- Recording → Work relationships (master → composition)
- Credit relationships (who played what)
- ISRC → MBID linking

**Key API calls for our use**:
```python
import musicbrainzngs as mb
mb.set_useragent("music-attribution-scaffold", "0.1.0")

# Search for an artist
mb.search_artists(query="Imogen Heap")

# Get recording credits
mb.get_recording_by_id(mbid, includes=["artists", "isrcs", "work-rels"])

# Browse works by artist
mb.browse_works(artist=artist_mbid, includes=["recording-rels"])
```

**Rate limiting**: MusicBrainz API has a 1 request/second rate limit. Our entity resolution pipeline must respect this. Consider using a local MusicBrainz mirror for bulk operations.

---

### beets

| Attribute | Details |
|-----------|---------|
| **Repository** | [beetbox/beets](https://github.com/beetbox/beets) |
| **Stars** | ~12k+ |
| **License** | MIT |
| **Status** | Active |

**Capabilities**: Music library manager with powerful auto-tagging. Uses MusicBrainz for matching audio files to metadata. Plugin architecture supports custom functionality.

**Attribution relevance**: Beets' auto-tagging pipeline is essentially entity resolution for music files. Its matching algorithm (acoustic fingerprint + metadata heuristics) is a proven approach we can learn from. The plugin system is also relevant for our extensible architecture.

**Relevant plugins**:
- `chroma` — AcoustID fingerprint submission and lookup
- `mbsync` — MusicBrainz metadata synchronization
- `duplicates` — Find duplicate tracks (entity resolution)
- `lastgenre` — Genre classification via Last.fm

---

### discogs_client (python3-discogs-client)

| Attribute | Details |
|-----------|---------|
| **Repository** | [joalla/discern](https://github.com/joalla/discern) or PyPI `python3-discogs-client` |
| **Stars** | ~300+ |
| **License** | MIT |
| **Status** | Maintained |

**Capabilities**: Python bindings for Discogs API v2. Search releases, artists, labels. Access marketplace data, user collections.

**Attribution relevance**: Discogs is the world's largest music database for physical releases, with particularly strong coverage of:
- Session musicians and credits
- Liner notes data
- Label/pressing information
- Genre/style taxonomy

**Cross-reference value**: Discogs credits often contain information missing from MusicBrainz (especially for older recordings and niche genres). Our entity resolution should merge MusicBrainz + Discogs data.

---

### pylast

| Attribute | Details |
|-----------|---------|
| **Repository** | [pylast/pylast](https://github.com/pylast/pylast) |
| **Stars** | ~400+ |
| **License** | Apache-2.0 |
| **Status** | Active |

**Capabilities**: Last.fm API bindings. Access user listening data, artist metadata, similar artists, tags, top tracks.

**Attribution relevance**: Last.fm's "similar artists" graph and user-generated tags provide a social/behavioral layer of metadata that structured databases lack. Useful for:
- Genre/style cohort construction
- Artist similarity for sanity-checking entity resolution
- Popularity signals for confidence weighting

---

## Python: AI/ML for Music

### CLAP (Contrastive Language-Audio Pretraining)

| Attribute | Details |
|-----------|---------|
| **Repository** | [LAION-AI/CLAP](https://github.com/LAION-AI/CLAP) |
| **Stars** | ~1k |
| **License** | Apache-2.0 |
| **Maintainer** | LAION |

**Capabilities**: Joint audio-language embedding space. Maps both audio and text descriptions to the same embedding space — enabling cross-modal similarity search, zero-shot audio classification, and audio-text retrieval.

**Attribution relevance**: CLAP embeddings are used in the Barnett et al. (2024) paper for attribution influence estimation across 5M clips on VampNet. If an AI-generated output has a CLAP embedding close to a specific training track, that track is a candidate influence source.

**Integration for our scaffold**: Could power A1→A2 confidence upgrades — "this generated audio embeds near these training tracks" provides correlation evidence for attribution claims.

**Models available**: Multiple pre-trained checkpoints (music, general audio, speech).

---

### AudioLDM / AudioLDM2

| Attribute | Details |
|-----------|---------|
| **Repository** | [haoheliu/AudioLDM2](https://github.com/haoheliu/AudioLDM2) |
| **Stars** | ~3k |
| **License** | Apache-2.0 |

**Capabilities**: Text-to-audio latent diffusion model. AudioLDM2 supports text-to-audio, text-to-music, and text-to-speech in a unified framework.

**Attribution relevance**: Understanding the generation architecture helps us design attribution methods. AudioLDM2's latent space could be probed for training data influence using methods like DAS (Lin et al., 2024).

---

### muzic (Microsoft Research)

| Attribute | Details |
|-----------|---------|
| **Repository** | [microsoft/muzic](https://github.com/microsoft/muzic) |
| **Stars** | ~4k |
| **License** | MIT |

**Capabilities**: Research project covering music understanding and generation. Includes: SongMASS (song-to-lyrics), HiFiSinger (singing voice synthesis), MusicBERT (symbolic music understanding), DeepRapper (rap generation).

**Attribution relevance**: MusicBERT's symbolic music understanding could help with compositional attribution — identifying melodic and harmonic patterns that trace to specific training works.

---

### HeartMuLa

| Attribute | Details |
|-----------|---------|
| **Repository** | Open-source (recently released) |
| **Focus** | Music foundation models |
| **Status** | New/emerging |

**Capabilities**: Open-source music foundation models for various downstream tasks. Part of the trend toward foundational models in the music domain.

**Assessment**: Worth monitoring but too new for production use. May become important as the field matures.

---

## Python: Embedding & Similarity

### sentence-transformers

| Attribute | Details |
|-----------|---------|
| **Repository** | [UKPLab/sentence-transformers](https://github.com/UKPLab/sentence-transformers) |
| **Stars** | ~15k+ |
| **License** | Apache-2.0 |

**Capabilities**: State-of-the-art text embedding models. Supports semantic search, clustering, and similarity computation.

**Attribution relevance**: For text-based metadata matching — comparing song titles, artist names, credit descriptions across databases. Critical for entity resolution when acoustic fingerprinting isn't available (e.g., compositional works without recordings).

---

### FAISS (Facebook AI Similarity Search)

| Attribute | Details |
|-----------|---------|
| **Repository** | [facebookresearch/faiss](https://github.com/facebookresearch/faiss) |
| **Stars** | ~30k+ |
| **License** | MIT |

**Capabilities**: Efficient similarity search and clustering of dense vectors. Supports billion-scale vector search with approximate nearest neighbors (ANN).

**Attribution relevance**: When we have CLAP or other audio embeddings for millions of tracks, FAISS enables efficient nearest-neighbor search to find "most similar training data" for a given AI output.

**Integration note**: For our MVP, pgvector in PostgreSQL is sufficient. FAISS becomes necessary at scale (>1M vectors with <10ms latency requirements).

---

## Rust: Audio Processing

### symphonia

| Attribute | Details |
|-----------|---------|
| **Repository** | [pdeljanov/Symphonia](https://github.com/pdeljanov/Symphonia) |
| **Downloads** | 3.2M+ on crates.io |
| **License** | MPL-2.0 |
| **Status** | Active |

**Capabilities**: Pure Rust audio decoding. Supports MP3, FLAC, Ogg Vorbis, WAV, AAC, ALAC, MKA/WebM. Performance within ~15% of FFmpeg for most codecs. Memory-safe, no C dependencies.

**Attribution relevance**: If we need high-performance audio decoding in a microservice (e.g., fingerprint computation service), symphonia provides memory-safe decoding without FFmpeg dependency hell.

---

### rodio

| Attribute | Details |
|-----------|---------|
| **Repository** | [RustAudio/rodio](https://github.com/RustAudio/rodio) |
| **License** | MIT / Apache-2.0 |
| **Status** | Active |

**Capabilities**: Audio playback library for Rust. Simple API for playing audio from files or streams.

**Attribution relevance**: Limited direct relevance. Useful if we build a preview/playback feature for comparing original and generated audio.

---

### rubato

| Attribute | Details |
|-----------|---------|
| **Repository** | crates.io: `rubato` |
| **License** | MIT |
| **Status** | Growing adoption |

**Capabilities**: Sample rate conversion in Rust. Supports high-quality sinc interpolation and polynomial resampling.

**Attribution relevance**: Useful for normalizing audio to consistent sample rates before fingerprinting or embedding computation.

---

## JavaScript/TypeScript: Web Audio & Analysis

### Tone.js

| Attribute | Details |
|-----------|---------|
| **Repository** | [Tonejs/Tone.js](https://github.com/Tonejs/Tone.js) |
| **Stars** | ~13k+ |
| **License** | MIT |

**Capabilities**: Web Audio framework for creating interactive music in the browser. Instruments, effects, scheduling, transport.

**Attribution relevance**: Foundation for any browser-based audio comparison or playback tool. Could power the "listen and compare" feature in our expert feedback dashboard.

---

### Meyda

| Attribute | Details |
|-----------|---------|
| **Repository** | [meyda/meyda](https://github.com/meyda/meyda) |
| **Stars** | ~1.3k |
| **License** | MIT |

**Capabilities**: Audio feature extraction in the browser. Computes MFCCs, spectral features, loudness, ZCR in real-time via Web Audio API.

**Attribution relevance**: Enables client-side audio analysis. Could power real-time similarity visualization in the expert feedback dashboard without sending audio to the server.

---

### Essentia.js

| Attribute | Details |
|-----------|---------|
| **Repository** | [MTG/essentia.js](https://github.com/MTG/essentia.js) |
| **License** | AGPL-3.0 |

**Capabilities**: WebAssembly port of Essentia. Runs the full Essentia C++ library in the browser.

**Attribution relevance**: Brings production-grade audio analysis to the browser. Could compute audio features client-side for the expert dashboard, reducing server load and enabling offline capability.

---

## Metadata Standards & Identifiers

### ISRC (International Standard Recording Code)

| Attribute | Details |
|-----------|---------|
| **Managed by** | IFPI (International Federation of the Phonographic Industry) |
| **Format** | CC-XXX-YY-NNNNN (Country-Registrant-Year-Designation) |
| **Scope** | Individual sound recordings and music videos |

**Role in attribution**: The recording-level identifier. Every commercially released recording should have an ISRC. Links directly to SoundExchange's AI Registry. Our entity resolution must map audio → ISRC for A2+ assurance levels.

**Challenges**: ISRCs are not always unique (same recording re-released may get new ISRC), not always assigned (independent releases), and not always accurate (human data entry errors).

---

### ISWC (International Standard Musical Work Code)

| Attribute | Details |
|-----------|---------|
| **Managed by** | CISAC |
| **Format** | T-NNN.NNN.NNN-C (prefix-work number-check digit) |
| **Scope** | Musical compositions (independent of recordings) |

**Role in attribution**: The composition-level identifier. Critical for distinguishing "who wrote the song" from "who performed the recording." A song may have one ISWC but dozens of ISRCs (covers, remixes, live versions).

**Challenges**: ISWCs are assigned by national agencies with inconsistent coverage. Many compositions lack ISWCs, especially in non-Western markets.

---

### ISNI (International Standard Name Identifier)

| Attribute | Details |
|-----------|---------|
| **Managed by** | ISNI International Authority |
| **Format** | 16-digit number |
| **Scope** | Public identities of parties (creators, publishers, etc.) |

**Role in attribution**: The creator-level identifier. Maps to our A3 (Identity-Verified) assurance level. An ISNI-verified artist identity provides the strongest provenance guarantee.

**Integration**: ISNI database can be queried via API. Links to ORCID (academic), VIAF (libraries), MusicBrainz.

---

### DDEX (Digital Data Exchange)

| Attribute | Details |
|-----------|---------|
| **Website** | [ddex.net](https://ddex.net) |
| **Type** | Industry standard for B2B music metadata exchange |
| **Key standards** | ERN (Electronic Release Notification), MEAD (Musical Work Licensing), MWN (Musical Work Notification) |

**Role in attribution**: DDEX defines how metadata flows between labels, distributors, and DSPs. If our scaffold needs to ingest release metadata from labels, DDEX XML/JSON is the standard format.

**Complexity**: DDEX schemas are verbose and complex. Libraries like `ddex-parser` exist but are enterprise-grade. For MVP, direct MusicBrainz/Discogs APIs are simpler.

---

### MusicBrainz (Open Music Encyclopedia)

| Attribute | Details |
|-----------|---------|
| **Website** | [musicbrainz.org](https://musicbrainz.org) |
| **Type** | Community-maintained, open database |
| **Entities** | ~2M artists, ~30M recordings, ~3M releases, ~1.5M works |
| **API** | Free XML/JSON API (1 req/sec rate limit) |
| **License** | CC0 (core data), CC-BY-NC-SA (supplementary data) |

**Role in attribution**: The backbone of our entity resolution. MusicBrainz provides:
- Canonical artist identities (with aliases, disambiguation)
- Recording → Work relationships (which recording of which composition)
- Credit relationships (detailed performer/producer/engineer credits)
- External links (ISRC, ISWC, Discogs, Wikidata, etc.)
- Relationship types (samples, remixes, covers, translations)

**Local mirror option**: MusicBrainz offers a PostgreSQL database dump updated weekly. For bulk entity resolution, running a local mirror avoids rate limiting and provides <1ms query latency.

---

### AcoustID (Audio Fingerprint Database)

| Attribute | Details |
|-----------|---------|
| **Website** | [acoustid.org](https://acoustid.org) |
| **Type** | Audio fingerprint → MusicBrainz recording lookup |
| **Fingerprints** | Powered by Chromaprint |
| **API** | Free (API key required) |

**Role in attribution**: Bridges audio signals to structured metadata. Given raw audio, AcoustID returns MusicBrainz recording IDs. This is the A0→A1 upgrade path: unknown audio → identified recording.

---

## ML Tools & Frameworks (Attribution-Adjacent)

### scikit-learn

**Relevance**: Conformal prediction implementations (via `mapie` or `crepes` libraries built on sklearn). Our A0-A3 confidence scoring uses conformal prediction for statistically valid confidence intervals.

### MAPIE (Model Agnostic Prediction Interval Estimator)

| Attribute | Details |
|-----------|---------|
| **Repository** | [scikit-learn-contrib/MAPIE](https://github.com/scikit-learn-contrib/MAPIE) |
| **Stars** | ~1.5k |
| **License** | BSD-3-Clause |

**Capabilities**: Conformal prediction wrappers for any scikit-learn compatible model. Provides prediction intervals and prediction sets with coverage guarantees.

**Attribution relevance**: Direct implementation path for our conformal prediction confidence scoring. Wrapping our entity resolution model with MAPIE gives formal guarantees like "with 90% probability, the true attribution is within this set."

### crepes (Conformal Regressors and Predictive Systems)

| Attribute | Details |
|-----------|---------|
| **Repository** | [henrikbostrom/crepes](https://github.com/henrikbostrom/crepes) |
| **License** | BSD-3-Clause |

**Capabilities**: Conformal prediction for regression and classification. Supports Mondrian conformal prediction (different confidence for different subgroups).

**Attribution relevance**: Mondrian CP is particularly useful for attribution — different artist genres or catalog sizes may warrant different confidence calibration. Crepes enables group-conditional coverage guarantees.

---

## Standards-Related Libraries

### python-musicxml

For parsing MusicXML (symbolic music notation standard). Relevant if we need to compare compositional structure at the notation level.

### mido

MIDI file reading/writing in Python. Relevant for Lemonaide-style MIDI attribution.

### mutagen

Audio metadata reading/writing (ID3 tags, Vorbis comments, etc.). Essential for reading embedded metadata from audio files.

### tinytag

Lightweight audio metadata reader. Faster than mutagen for simple metadata extraction.

---

## Evaluation & Benchmarking Tools

### MiRA (Music Replication Assessment)

| Attribute | Details |
|-----------|---------|
| **Paper** | Batlle-Roca et al. (ISMIR 2024) |
| **arXiv** | [2407.14364](https://arxiv.org/abs/2407.14364) |
| **Status** | Open-source (code + examples available) |

**Capabilities**: Model-independent tool for detecting exact data replication in AI-generated music. Uses diverse audio music similarity metrics. Detects replication at rates exceeding 10%.

**Attribution relevance**: Complementary to our system. MiRA detects *replication* (copying); our system detects *influence* (contribution). Both are needed for comprehensive attribution.

---

### SSIMuse

| Attribute | Details |
|-----------|---------|
| **Paper** | Ji et al. (2025) |
| **arXiv** | [2509.13658](https://arxiv.org/abs/2509.13658) |
| **Status** | Implementation available |

**Capabilities**: Adapts SSIM (image similarity) to symbolic music (piano roll). Bar-level precision for replication detection. Two variants: SSIMuse-B (compositional) and SSIMuse-V (performance).

**Attribution relevance**: For MIDI/symbolic music attribution. Complementary to audio-domain tools.

---

## Library Selection Matrix for MVA

The following matrix maps our MVA components to recommended libraries:

| MVA Component | Primary Library | Backup | Notes |
|--------------|----------------|--------|-------|
| **Audio fingerprinting** | pyacoustid + chromaprint | audfprint | AcoustID gives MusicBrainz linkage |
| **Audio feature extraction** | librosa | essentia | librosa simpler; essentia faster |
| **Metadata lookup** | musicbrainzngs | discogs_client | MusicBrainz first, Discogs for gaps |
| **Text embedding** | sentence-transformers | OpenAI API | Local vs API tradeoff |
| **Audio embedding** | CLAP | OpenL3 | CLAP for text-audio; OpenL3 for audio-only |
| **Vector similarity** | pgvector | FAISS | pgvector for MVP; FAISS at scale |
| **Conformal prediction** | MAPIE | crepes | MAPIE more mature; crepes for Mondrian CP |
| **Audio metadata** | mutagen | tinytag | mutagen for read+write; tinytag for read-only |
| **Evaluation** | mir_eval + MiRA | — | Standard evaluation metrics |
| **Web audio (frontend)** | Tone.js + Meyda | Essentia.js | For expert dashboard |
