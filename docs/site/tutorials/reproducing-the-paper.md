# Reproducing the Paper

This tutorial maps the claims in the SSRN preprint to running code in this repository, so you can verify every assertion for yourself.

![Tutorial diagram: three-column reproducibility map linking academic paper sections on music attribution to corresponding open-source code modules and test commands, covering confidence scoring, multi-source entity resolution, A0-A3 assurance levels, and MCP consent infrastructure -- every substantive claim is verifiable by running a single make test command.](../figures/fig-howto-02-reproduce-paper-claims.jpg)

*Paper-to-code reproducibility map for SSRN No. 6109087 (Teikari, 2026). Each row connects a manuscript section -- from transparent confidence scoring to the Oracle Problem -- to the specific module and test keyword that validates it, making the music attribution scaffold a fully auditable companion to the research.*

!!! info "Paper Reference"
    Teikari, P. (2026). *Governing Generative Music: Attribution Limits, Platform Incentives, and the Future of Creator Income*. SSRN No. 6109087.
    [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087)

---

## Section-to-Code Mapping

The following table maps each major paper section to the code module that implements it.

| Paper Section | Code Module | What It Implements |
|---|---|---|
| Section 3 -- Five-Source ETL | `src/music_attribution/etl/` | MusicBrainz, Discogs, AcoustID, tinytag file metadata, artist input extractors |
| Section 4 -- Entity Resolution | `src/music_attribution/resolution/` | Identifier matching, string similarity, embedding similarity, LLM disambiguation, Splink linkage, graph resolution |
| Section 5 -- Attribution Engine | `src/music_attribution/attribution/` | Weighted source aggregation via `CreditAggregator`, conformal calibration via `ConformalScorer` |
| Section 6 -- A0-A3 Assurance Levels | `src/music_attribution/schemas/enums.py` | `AssuranceLevelEnum` (LEVEL_0 through LEVEL_3) plus classification logic in the resolution orchestrator |
| Section 7 -- MCP Consent Infrastructure | `src/music_attribution/mcp/server.py` | Machine-readable permission queries: `query_attribution`, `check_permission`, `list_permissions` |
| Section 8 -- Agent Interface | `src/music_attribution/chat/agent.py` | PydanticAI agent with 4 tools: `explain_confidence`, `search_attributions`, `suggest_correction`, `submit_feedback` |

### Detailed Module Breakdown

#### ETL Pipeline (Section 3)

The paper describes a five-source ETL pipeline. Each source has a dedicated connector module:

| Source | Module | Key Class | Source Confidence |
|--------|--------|-----------|-------------------|
| MusicBrainz | `etl/musicbrainz.py` | `MusicBrainzConnector` | 0.90 |
| Discogs | `etl/discogs.py` | `DiscogsConnector` | 0.85 |
| AcoustID | `etl/acoustid.py` | `AcoustIDConnector` | varies by fingerprint match score |
| File metadata | `etl/file_metadata.py` | `FileMetadataReader` | 0.70 (0.30 for unreadable tags) |
| Artist input | via `SourceEnum.ARTIST_INPUT` | user-submitted records | 0.60 |

All connectors produce `NormalizedRecord` boundary objects (defined in `src/music_attribution/schemas/normalized.py`) with:

- `IdentifierBundle` -- standard music industry identifiers (ISRC, ISWC, ISNI, IPI, MBID, Discogs ID, AcoustID)
- `SourceMetadata` -- roles, release date, duration, genres
- `Relationship` -- typed links to other entities (PERFORMED, WROTE, PRODUCED, etc.)
- `source_confidence` -- per-source reliability weight

The `DataQualityGate` in `etl/quality_gate.py` validates batches before passing them to Entity Resolution, checking identifier coverage, duplicate detection, and source distribution.

#### Entity Resolution (Section 4)

The `ResolutionOrchestrator` in `resolution/orchestrator.py` implements a cascading resolution pipeline:

1. **Identifier matching** (`resolution/identifier_match.py`) -- exact ISRC/ISWC/ISNI/MBID match (weight: 1.0)
2. **String similarity** (`resolution/string_similarity.py`) -- fuzzy name matching (weight: 0.6)
3. **Embedding similarity** (`resolution/embedding_match.py`) -- vector cosine similarity (weight: 0.7)
4. **Graph evidence** (`resolution/graph_resolution.py`) -- path-based confidence from knowledge graph (weight: 0.75)
5. **LLM disambiguation** (`resolution/llm_disambiguation.py`) -- Claude-based disambiguation for ambiguous cases (weight: 0.85)
6. **Splink linkage** (`resolution/splink_linkage.py`) -- probabilistic record linkage (weight: 0.8)

The output is a `ResolvedEntity` (defined in `src/music_attribution/schemas/resolved.py`) with per-method confidence breakdown, conflict detection, and assurance level classification.

#### Attribution Engine (Section 5)

The `CreditAggregator` in `attribution/aggregator.py` performs weighted voting across sources using reliability weights defined in `src/music_attribution/constants.py`:

```python
SOURCE_RELIABILITY_WEIGHTS = {
    SourceEnum.MUSICBRAINZ: 0.95,
    SourceEnum.DISCOGS: 0.85,
    SourceEnum.ACOUSTID: 0.80,
    SourceEnum.FILE_METADATA: 0.70,
    SourceEnum.ARTIST_INPUT: 0.60,
}
```

The `ConformalScorer` in `attribution/conformal.py` wraps confidence scores in Adaptive Prediction Sets (APS), ensuring that "90% confident" actually achieves 90% coverage. It produces `ConformalSet` objects with calibration error metrics.

#### Assurance Levels (Section 6)

The paper's A0-A3 assurance levels map directly to `AssuranceLevelEnum` in `schemas/enums.py`. The classification logic lives in `ResolutionOrchestrator._compute_assurance_level()`:

| Level | Criteria | Meaning |
|-------|----------|---------|
| A3 | ISNI present + multiple sources agree | Artist-verified, identity-confirmed |
| A2 | Multiple sources + standard identifier (ISRC/ISWC/MBID) | Multi-source corroboration |
| A1 | At least one standard identifier | Single-source with identifier |
| A0 | No identifiers | No provenance data |

#### MCP Consent (Section 7)

The `MCPAttributionServer` in `mcp/server.py` implements the "Permission Patchbay" described in the paper. It exposes three MCP tools:

- `query_attribution(work_id)` -- retrieve a full attribution record
- `check_permission(entity_id, permission_type)` -- check a specific permission (AI_TRAINING, VOICE_CLONING, SYNC_LICENSE, etc.)
- `list_permissions(entity_id)` -- list all permissions for an entity

Permission types are defined in `PermissionTypeEnum` and include granular AI-related categories: `AI_TRAINING_COMPOSITION`, `AI_TRAINING_RECORDING`, `AI_TRAINING_STYLE`, `VOICE_CLONING`, `STYLE_LEARNING`, `LYRICS_IN_CHATBOTS`.

Permission values use a tri-state model plus conditions: `ALLOW`, `DENY`, `ASK`, `ALLOW_WITH_ATTRIBUTION`, `ALLOW_WITH_ROYALTY`.

---

## Running the Demo

The scaffold ships with 9 Imogen Heap works spanning the full confidence range (0.00 to 0.95). To see them:

### 1. Start the infrastructure

```bash
make setup
```

This starts PostgreSQL via Docker Compose and runs database migrations.

### 2. Start the backend

```bash
make agent
```

The FastAPI server starts on [http://localhost:8000](http://localhost:8000). Verify it is running:

```bash
curl http://localhost:8000/health
# {"status": "healthy", "service": "music-attribution-api"}
```

### 3. Start the frontend

```bash
make dev-frontend
```

The Next.js development server starts on [http://localhost:3000](http://localhost:3000).

### 4. Explore the works

Navigate to [http://localhost:3000/works](http://localhost:3000/works). You will see the 9 seeded works:

| Work | Confidence | Assurance | Needs Review |
|------|-----------|-----------|--------------|
| Hide and Seek | 0.95 | A3 | No |
| Tiny Human | 0.91 | A3 | No |
| The Moment I Said It | 0.82 | A2 | No |
| Goodnight and Go | 0.72 | A2 | No |
| Headlock | 0.58 | A1 | Yes |
| What Have You Done To Me? | 0.48 | A1 | Yes |
| Just for Now | 0.35 | A1 | Yes |
| 2-1 | 0.28 | A1 | Yes |
| Blanket | 0.00 | A0 | Yes |

These works demonstrate the full spectrum:

- **High confidence (green, >= 0.85)**: Multiple sources agree, strong identifiers present
- **Medium confidence (amber, 0.50-0.84)**: Some source agreement, partial identifiers
- **Low confidence (red, < 0.50)**: Sparse data, conflicts, or missing identifiers

### 5. Try the agent (optional)

If you have `ANTHROPIC_API_KEY` set in your environment, the CopilotKit sidebar on the frontend allows natural language queries:

```
"Why is Hide and Seek confidence 95%?"
"Which works need review?"
"What permissions does Hide and Seek have for AI training?"
```

---

## Tracing a Confidence Score

This section walks through how a single confidence score flows from raw source data through the pipeline to the UI display.

### Step 1: Source extraction

Each ETL connector assigns a `source_confidence` to its `NormalizedRecord`. For example, the `MusicBrainzConnector` assigns 0.90 to recordings it fetches:

```python
# In etl/musicbrainz.py, MusicBrainzConnector.transform_recording()
return NormalizedRecord(
    source=SourceEnum.MUSICBRAINZ,
    source_confidence=0.9,
    ...
)
```

### Step 2: Quality gate

The `DataQualityGate` validates the batch. It does not modify confidence scores, but it can reject entire batches if identifier coverage is zero or if critical quality checks fail.

### Step 3: Entity resolution

The `ResolutionOrchestrator` groups records that represent the same entity and computes a combined `resolution_confidence` using weighted signals:

```python
# In resolution/orchestrator.py
_DEFAULT_WEIGHTS = {
    "identifier": 1.0,   # Exact ID match
    "splink": 0.8,       # Probabilistic linkage
    "string": 0.6,       # Fuzzy string match
    "embedding": 0.7,    # Vector similarity
    "graph": 0.75,       # Knowledge graph paths
    "llm": 0.85,         # LLM disambiguation
}
```

If two records share an ISRC, the identifier signal contributes 1.0 with weight 1.0. If they also have a string similarity of 0.92, that contributes 0.92 with weight 0.6. The combined score is the weighted average.

### Step 4: Attribution aggregation

The `CreditAggregator` produces a final `confidence_score` on the `AttributionRecord` by averaging per-credit weighted confidences using `SOURCE_RELIABILITY_WEIGHTS`:

```python
# In attribution/aggregator.py
confidence = sum(c.confidence for c in credits) / len(credits)
```

Works with confidence below `REVIEW_THRESHOLD` (0.50) are automatically flagged with `needs_review=True`.

### Step 5: Conformal calibration

The `ConformalScorer` wraps the confidence in an Adaptive Prediction Set at the 90% coverage level. The `ConformalSet` includes:

- `marginal_coverage` -- the achieved coverage
- `calibration_error` -- deviation from target coverage
- `prediction_sets` -- the set of roles included in the prediction

### Step 6: API delivery

The REST API at `/api/v1/attributions/` returns the `AttributionRecord` as JSON, including all confidence metadata, provenance chain, and conformal set.

### Step 7: Frontend display

The frontend renders confidence using the three-tier color system:

- Green (`--color-confidence-high`): confidence >= 0.85
- Amber (`--color-confidence-medium`): 0.50 <= confidence < 0.85
- Red (`--color-confidence-low`): confidence < 0.50

The `ConfidenceGauge` component uses `role="meter"` for accessibility and displays the score as a percentage.

---

## Running the Tests

To verify the paper's claims through tests:

```bash
# Run all backend tests (351 unit + 42 integration)
make test-local

# Run frontend tests (265 Vitest tests)
make test-frontend

# Run only attribution-related tests
.venv/bin/python -m pytest tests/unit/test_aggregator.py tests/unit/test_conformal.py -v

# Run only ETL tests
.venv/bin/python -m pytest tests/unit/test_musicbrainz.py tests/unit/test_discogs.py tests/unit/test_acoustid.py tests/unit/test_file_metadata.py -v

# Run only resolution tests
.venv/bin/python -m pytest tests/unit/test_orchestrator.py tests/unit/test_identifier_match.py tests/unit/test_string_similarity.py -v
```

---

## Citation

If you use this scaffold in your research, please cite:

```bibtex
@article{teikariGoverningGenerativeMusic2026,
    title = {Governing Generative Music: Attribution Limits, Platform Incentives, and the Future of Creator Income},
    url = {https://doi.org/10.2139/ssrn.6109087},
    doi = {10.2139/ssrn.6109087},
    publisher = {Social Science Research Network},
    author = {Teikari, Petteri},
    year = {2026},
}
```
