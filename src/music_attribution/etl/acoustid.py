"""AcoustID fingerprint connector.

Audio fingerprinting via AcoustID/Chromaprint. Given an audio file, generates
a fingerprint and looks up against the AcoustID database to find MusicBrainz
recording IDs. This is the "what recording is this?" step.

Note: acoustid.fingerprint_file is synchronous — wrapped in asyncio.to_thread().
"""

from __future__ import annotations

import asyncio
import logging
from datetime import UTC, datetime
from pathlib import Path

import acoustid

from music_attribution.etl.rate_limiter import TokenBucketRateLimiter
from music_attribution.schemas.enums import EntityTypeEnum, SourceEnum
from music_attribution.schemas.normalized import (
    IdentifierBundle,
    NormalizedRecord,
    SourceMetadata,
)

logger = logging.getLogger(__name__)


class AcoustIDConnector:
    """ETL connector for AcoustID fingerprint service.

    Args:
        api_key: AcoustID API key.
        rate: Maximum requests per second (default: 3.0 per AcoustID policy).
        max_retries: Maximum retry attempts on transient errors.
    """

    def __init__(
        self,
        api_key: str,
        rate: float = 3.0,
        max_retries: int = 3,
    ) -> None:
        self._api_key = api_key
        self._rate_limiter = TokenBucketRateLimiter(rate=rate, capacity=3)
        self._max_retries = max_retries

    async def fingerprint_file(self, file_path: Path) -> tuple[str, int]:
        """Generate a Chromaprint fingerprint from an audio file.

        Args:
            file_path: Path to the audio file.

        Returns:
            Tuple of (fingerprint_string, duration_in_seconds).
        """
        duration, fingerprint = await asyncio.to_thread(acoustid.fingerprint_file, str(file_path))
        return fingerprint, duration

    async def lookup(self, fingerprint: str, duration: int) -> list[NormalizedRecord]:
        """Look up a fingerprint against AcoustID database.

        Args:
            fingerprint: Chromaprint fingerprint string.
            duration: Audio duration in seconds.

        Returns:
            List of NormalizedRecords for matching recordings.
        """
        response = await self._api_call(
            acoustid.lookup,
            self._api_key,
            fingerprint,
            duration,
            meta="recordings",
        )
        return self.transform_lookup_results(response)

    def transform_lookup_results(self, response: dict) -> list[NormalizedRecord]:
        """Transform AcoustID lookup response to NormalizedRecords.

        Args:
            response: Raw AcoustID response dict.

        Returns:
            List of NormalizedRecords sorted by confidence (descending).
        """
        records: list[NormalizedRecord] = []

        for result in response.get("results", []):
            score = result.get("score", 0.0)
            acoustid_id = result.get("id", "")

            for recording in result.get("recordings", []):
                mbid = recording.get("id", "")
                title = recording.get("title", "")
                duration = recording.get("duration")

                artists = recording.get("artists", [])
                artist_names = [a.get("name", "") for a in artists if a.get("name")]

                record = NormalizedRecord(
                    source=SourceEnum.ACOUSTID,
                    source_id=acoustid_id,
                    entity_type=EntityTypeEnum.RECORDING,
                    canonical_name=title,
                    identifiers=IdentifierBundle(
                        mbid=mbid,
                        acoustid=acoustid_id,
                    ),
                    metadata=SourceMetadata(
                        roles=artist_names,
                        duration_ms=duration * 1000 if duration else None,
                    ),
                    fetch_timestamp=datetime.now(UTC),
                    source_confidence=score,
                    raw_payload=result,
                )
                records.append(record)

        # Sort by confidence descending
        records.sort(key=lambda r: r.source_confidence, reverse=True)
        return records

    async def _api_call(self, func, *args, **kwargs):
        """Make a rate-limited API call with retry logic.

        Args:
            func: acoustid function to call.
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            API response dict.

        Raises:
            acoustid.WebServiceError: After max retries exhausted.
        """
        for attempt in range(self._max_retries):
            await self._rate_limiter.acquire()
            try:
                return await asyncio.to_thread(func, *args, **kwargs)
            except acoustid.WebServiceError as e:
                if attempt < self._max_retries - 1:
                    wait = 2**attempt
                    logger.warning(
                        "AcoustID API error (attempt %d/%d): %s. Retrying in %ds.",
                        attempt + 1,
                        self._max_retries,
                        e,
                        wait,
                    )
                    await asyncio.sleep(wait)
                else:
                    raise
