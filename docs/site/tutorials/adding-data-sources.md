# Adding Data Sources

This tutorial walks through adding a new ETL data source to the Music Attribution Scaffold. By the end, you will have a new extractor module, quality gate integration, tests, and registration in the orchestrator.

![How-to guide: five-step workflow for adding a new music metadata data source to the open-source attribution scaffold ETL pipeline, covering extractor creation, BaseExtractor interface implementation, orchestrator registration, quality gate configuration, and test coverage -- each step maps to a specific module path ensuring transparent confidence scoring from ingestion onward.](../figures/fig-howto-01-add-new-data-source.jpg)

*Five-step data source integration path for the Music Attribution Scaffold ETL pipeline. Each step corresponds to a specific module in the `src/music_attribution/etl/` package, enforcing the attribution-by-design principle that every new source must implement extraction, normalization, and validation before registration (Teikari, 2026).*

---

## Prerequisites

- Completed [Installation](../getting-started/installation.md)
- Familiar with the [Architecture Overview](../user-guide/architecture.md)
- Understanding of `NormalizedRecord` schema (see `src/music_attribution/schemas/normalized.py`)

---

## Overview

The ETL pipeline follows a consistent pattern for all data sources:

1. **Connector class** -- fetches raw data from an external API or file
2. **Transform methods** -- convert raw responses to `NormalizedRecord` boundary objects
3. **Rate limiting** -- respect API rate limits via `TokenBucketRateLimiter`
4. **Quality gate** -- validate batches before passing to Entity Resolution
5. **Persistence** -- store validated records in PostgreSQL

All connectors live in `src/music_attribution/etl/` and produce the same output type: `NormalizedRecord`.

---

## Step 1: Create the Extractor Module

Create a new file at `src/music_attribution/etl/your_source.py`. Follow the pattern established by the existing connectors.

Here is the typical structure:

```python
"""YourSource ETL connector.

Fetches data from YourSource API and transforms it into
NormalizedRecord boundary objects.
"""

from __future__ import annotations

import asyncio
import logging
from datetime import UTC, datetime

from music_attribution.etl.rate_limiter import TokenBucketRateLimiter
from music_attribution.schemas.enums import EntityTypeEnum, SourceEnum
from music_attribution.schemas.normalized import (
    IdentifierBundle,
    NormalizedRecord,
    Relationship,
    SourceMetadata,
)

logger = logging.getLogger(__name__)


class YourSourceConnector:
    """ETL connector for YourSource API.

    Args:
        api_key: API key for authentication.
        rate: Maximum requests per second.
        max_retries: Maximum retry attempts on transient errors.
    """

    def __init__(
        self,
        api_key: str,
        rate: float = 1.0,
        max_retries: int = 3,
    ) -> None:
        self._api_key = api_key
        self._rate_limiter = TokenBucketRateLimiter(rate=rate, capacity=1)
        self._max_retries = max_retries
        # Initialize your API client here

    async def fetch_recording(self, recording_id: str) -> NormalizedRecord:
        """Fetch a recording by source-specific ID.

        Args:
            recording_id: Source-specific recording identifier.

        Returns:
            NormalizedRecord for the recording.
        """
        data = await self._api_call(self._fetch_raw, recording_id)
        return self.transform_recording(data)

    def transform_recording(self, data: dict) -> NormalizedRecord:
        """Transform a raw API response to NormalizedRecord.

        Args:
            data: Raw API response dictionary.

        Returns:
            NormalizedRecord with normalized fields.
        """
        return NormalizedRecord(
            source=SourceEnum.YOUR_SOURCE,  # Add to SourceEnum first
            source_id=str(data.get("id", "")),
            entity_type=EntityTypeEnum.RECORDING,
            canonical_name=data.get("title", ""),
            identifiers=IdentifierBundle(
                isrc=data.get("isrc"),
                mbid=data.get("musicbrainz_id"),
            ),
            metadata=SourceMetadata(
                roles=data.get("artists", []),
                release_date=data.get("release_date"),
                duration_ms=data.get("duration_ms"),
            ),
            relationships=self._extract_relationships(data),
            fetch_timestamp=datetime.now(UTC),
            source_confidence=0.75,  # Set based on source reliability
            raw_payload=data,
        )

    def _extract_relationships(self, data: dict) -> list[Relationship]:
        """Extract relationships from the raw response."""
        relationships: list[Relationship] = []
        # Map source-specific role strings to RelationshipTypeEnum
        # See musicbrainz.py or discogs.py for examples
        return relationships

    async def _api_call(self, func, *args, **kwargs):
        """Make a rate-limited API call with retry logic.

        Args:
            func: Async or sync function to call.
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            API response.

        Raises:
            Exception: After max retries exhausted.
        """
        for attempt in range(self._max_retries):
            await self._rate_limiter.acquire()
            try:
                return await asyncio.to_thread(func, *args, **kwargs)
            except Exception as e:
                if attempt < self._max_retries - 1:
                    wait = 2**attempt
                    logger.warning(
                        "YourSource API error (attempt %d/%d): %s. Retrying in %ds.",
                        attempt + 1,
                        self._max_retries,
                        e,
                        wait,
                    )
                    await asyncio.sleep(wait)
                else:
                    raise

    def _fetch_raw(self, recording_id: str) -> dict:
        """Synchronous API call (wrapped in asyncio.to_thread)."""
        # Your API client call here
        raise NotImplementedError
```

### Key Patterns

**Rate limiting**: All connectors use `TokenBucketRateLimiter` from `etl/rate_limiter.py`. Set the `rate` parameter to match the API's rate limit policy.

**Sync wrapping**: Many Python API clients are synchronous. Wrap them with `asyncio.to_thread()` for async compatibility, as shown in the `_api_call` method.

**Source confidence**: Assign a `source_confidence` value between 0.0 and 1.0 reflecting how reliable this source is. This feeds into weighted aggregation in the Attribution Engine. Reference values:

| Source | Confidence |
|--------|-----------|
| MusicBrainz | 0.90 |
| Discogs | 0.85 |
| AcoustID | varies by match score |
| File metadata | 0.70 |
| Artist input | 0.60 |

---

## Step 2: Add the Source Enum

Add your new source to `SourceEnum` in `src/music_attribution/schemas/enums.py`:

```python
class SourceEnum(StrEnum):
    """Data source identifiers."""

    MUSICBRAINZ = "MUSICBRAINZ"
    DISCOGS = "DISCOGS"
    ACOUSTID = "ACOUSTID"
    ARTIST_INPUT = "ARTIST_INPUT"
    FILE_METADATA = "FILE_METADATA"
    YOUR_SOURCE = "YOUR_SOURCE"  # Add this line
```

---

## Step 3: Add the Source Weight

Add a reliability weight for your source in `src/music_attribution/constants.py`:

```python
SOURCE_RELIABILITY_WEIGHTS: dict[SourceEnum, float] = {
    SourceEnum.MUSICBRAINZ: 0.95,
    SourceEnum.DISCOGS: 0.85,
    SourceEnum.ACOUSTID: 0.80,
    SourceEnum.FILE_METADATA: 0.70,
    SourceEnum.ARTIST_INPUT: 0.60,
    SourceEnum.YOUR_SOURCE: 0.75,  # Add this line
}
```

This weight is used by `CreditAggregator` for weighted voting across sources.

---

## Step 4: Register in the Quality Gate

The `DataQualityGate` in `etl/quality_gate.py` validates batches automatically based on `NormalizedRecord` properties. No explicit registration is needed -- it works with any `SourceEnum` value.

However, if your source has special validation requirements, you can extend the gate:

```python
# In etl/quality_gate.py, add a new check method:
def _check_your_source_fields(
    self,
    records: list[NormalizedRecord],
) -> QualityCheckResult:
    """Validate YourSource-specific fields."""
    your_records = [r for r in records if r.source == SourceEnum.YOUR_SOURCE]
    if not your_records:
        return QualityCheckResult(
            check_name="your_source_fields",
            status="pass",
            message="No YourSource records in batch",
        )
    # Add your validation logic here
    return QualityCheckResult(
        check_name="your_source_fields",
        status="pass",
        message=f"Validated {len(your_records)} YourSource records",
    )
```

---

## Step 5: Write Tests

Create `tests/unit/test_your_source.py` following the project test pattern:

```python
"""Tests for YourSource ETL connector."""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import AsyncMock, patch

import pytest

from music_attribution.etl.your_source import YourSourceConnector
from music_attribution.schemas.enums import EntityTypeEnum, SourceEnum


class TestYourSourceConnector:
    """Tests for YourSourceConnector."""

    def test_transform_recording_basic(self) -> None:
        """Test basic recording transformation."""
        # Arrange
        connector = YourSourceConnector(api_key="test-key")
        raw_data = {
            "id": "abc-123",
            "title": "Test Track",
            "isrc": "USRC12345678",
            "artists": ["Test Artist"],
            "duration_ms": 240000,
        }

        # Act
        record = connector.transform_recording(raw_data)

        # Assert
        assert record.source == SourceEnum.YOUR_SOURCE
        assert record.source_id == "abc-123"
        assert record.entity_type == EntityTypeEnum.RECORDING
        assert record.canonical_name == "Test Track"
        assert record.identifiers.isrc == "USRC12345678"
        assert record.source_confidence == 0.75

    def test_transform_recording_missing_fields(self) -> None:
        """Test transformation with minimal data."""
        # Arrange
        connector = YourSourceConnector(api_key="test-key")
        raw_data = {
            "id": "minimal-123",
            "title": "Minimal Track",
        }

        # Act
        record = connector.transform_recording(raw_data)

        # Assert
        assert record.canonical_name == "Minimal Track"
        assert record.identifiers.isrc is None

    @pytest.mark.asyncio
    async def test_fetch_recording_with_retry(self) -> None:
        """Test that fetch retries on transient errors."""
        # Arrange
        connector = YourSourceConnector(api_key="test-key", max_retries=2)

        with patch.object(
            connector,
            "_fetch_raw",
            side_effect=[Exception("timeout"), {"id": "1", "title": "Track"}],
        ):
            # Act
            record = await connector.fetch_recording("1")

            # Assert
            assert record.canonical_name == "Track"
```

Run the tests:

```bash
.venv/bin/python -m pytest tests/unit/test_your_source.py -v
```

---

## Step 6: Update Seed Data (Optional)

If you want your new source to appear in the demo dataset, update the seed data script to include records from your source. The seed data is what populates the 9 Imogen Heap works visible in the frontend.

---

## Step 7: Add the Dependency

If your connector requires a third-party API client, add it to `pyproject.toml`:

```bash
uv add your-api-client
```

If the library lacks type stubs, add a mypy override in `pyproject.toml`:

```toml
[[tool.mypy.overrides]]
module = "your_api_client.*"
follow_untyped_imports = true
```

---

## Checklist

Before submitting your new data source:

- [ ] Connector class with `fetch_*` and `transform_*` methods
- [ ] `SourceEnum` extended with your source identifier
- [ ] Source weight added to `SOURCE_RELIABILITY_WEIGHTS`
- [ ] Rate limiting configured to match API policy
- [ ] Unit tests covering happy path and error cases
- [ ] `source_confidence` set to an appropriate value
- [ ] Third-party dependency added via `uv add`
- [ ] mypy overrides added if needed
- [ ] All existing tests still pass (`make test-local`)
- [ ] Pre-commit hooks pass (`pre-commit run --all-files`)

---

## Reference: Existing Connectors

Study these for patterns and conventions:

| Connector | File | Notable Pattern |
|-----------|------|-----------------|
| MusicBrainz | `etl/musicbrainz.py` | Relationship extraction from `artist-relation-list`, user-agent parsing |
| Discogs | `etl/discogs.py` | Comma-separated role parsing, per-track and per-release records |
| AcoustID | `etl/acoustid.py` | Fingerprint-first lookup, confidence from match score |
| File metadata | `etl/file_metadata.py` | Synchronous (no rate limiter needed), minimal fallback record |
