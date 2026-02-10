"""Discogs ETL connector.

Fetches release credits, artist profiles, and label info from the Discogs API.
Transforms raw API responses into NormalizedRecord boundary objects.
Handles rate limiting (60 req/min authenticated, 25 req/min unauthenticated).

Note: python3-discogs-client is synchronous — all calls are wrapped in
asyncio.to_thread() for async compatibility.
"""

from __future__ import annotations

import asyncio
import logging
from datetime import UTC, datetime

import discogs_client

from music_attribution.etl.rate_limiter import TokenBucketRateLimiter
from music_attribution.schemas.enums import (
    EntityTypeEnum,
    RelationshipTypeEnum,
    SourceEnum,
)
from music_attribution.schemas.normalized import (
    IdentifierBundle,
    NormalizedRecord,
    Relationship,
    SourceMetadata,
)

logger = logging.getLogger(__name__)

# Mapping from Discogs role strings to our RelationshipTypeEnum
_ROLE_MAP: dict[str, RelationshipTypeEnum] = {
    "producer": RelationshipTypeEnum.PRODUCED,
    "co-producer": RelationshipTypeEnum.PRODUCED,
    "executive producer": RelationshipTypeEnum.PRODUCED,
    "engineer": RelationshipTypeEnum.ENGINEERED,
    "recording engineer": RelationshipTypeEnum.ENGINEERED,
    "mixed by": RelationshipTypeEnum.MIXED,
    "mix": RelationshipTypeEnum.MIXED,
    "mastered by": RelationshipTypeEnum.MASTERED,
    "mastering": RelationshipTypeEnum.MASTERED,
    "vocals": RelationshipTypeEnum.PERFORMED,
    "guitar": RelationshipTypeEnum.PERFORMED,
    "bass": RelationshipTypeEnum.PERFORMED,
    "drums": RelationshipTypeEnum.PERFORMED,
    "keyboards": RelationshipTypeEnum.PERFORMED,
    "piano": RelationshipTypeEnum.PERFORMED,
    "percussion": RelationshipTypeEnum.PERFORMED,
    "written-by": RelationshipTypeEnum.WROTE,
    "written by": RelationshipTypeEnum.WROTE,
    "songwriter": RelationshipTypeEnum.WROTE,
    "lyrics by": RelationshipTypeEnum.WROTE,
    "music by": RelationshipTypeEnum.WROTE,
    "composed by": RelationshipTypeEnum.WROTE,
    "arranged by": RelationshipTypeEnum.ARRANGED,
    "remix": RelationshipTypeEnum.REMIXED,
    "remixed by": RelationshipTypeEnum.REMIXED,
}


def _map_role(role_str: str) -> RelationshipTypeEnum | None:
    """Map a Discogs role string to a RelationshipTypeEnum."""
    normalized = role_str.strip().lower()
    # Direct match
    if normalized in _ROLE_MAP:
        return _ROLE_MAP[normalized]
    # Partial match — check if any key is contained in the role
    for key, value in _ROLE_MAP.items():
        if key in normalized:
            return value
    return None


class DiscogsConnector:
    """ETL connector for Discogs API.

    Args:
        user_agent: User-Agent string for API compliance.
        token: Discogs personal access token (optional, for higher rate limits).
        rate: Override requests per second (default: auto based on auth).
        max_retries: Maximum retry attempts on transient errors.
    """

    def __init__(
        self,
        user_agent: str,
        token: str | None = None,
        rate: float | None = None,
        max_retries: int = 3,
    ) -> None:
        self._user_agent = user_agent
        self._max_retries = max_retries
        self._authenticated = token is not None

        if token:
            self._client = discogs_client.Client(user_agent, user_token=token)
        else:
            self._client = discogs_client.Client(user_agent)

        # Rate limits: 60/min auth (1/s), 25/min unauth (~0.42/s)
        if rate is not None:
            effective_rate = rate
        elif self._authenticated:
            effective_rate = 1.0  # 60 per minute
        else:
            effective_rate = 25.0 / 60.0  # ~0.42 per second

        self._rate_limiter = TokenBucketRateLimiter(rate=effective_rate, capacity=1)

    async def fetch_release(self, release_id: int) -> list[NormalizedRecord]:
        """Fetch a release by Discogs ID.

        Args:
            release_id: Discogs release ID.

        Returns:
            List of NormalizedRecords (tracks + release-level record).
        """
        release = await self._api_call(self._client.release, release_id)
        data = release.data
        return self.transform_release(data)

    async def fetch_artist(self, artist_id: int) -> NormalizedRecord:
        """Fetch an artist by Discogs ID.

        Args:
            artist_id: Discogs artist ID.

        Returns:
            NormalizedRecord for the artist.
        """
        artist = await self._api_call(self._client.artist, artist_id)
        return self.transform_artist(artist.data)

    async def search_releases(self, query: str) -> list[NormalizedRecord]:
        """Search for releases by query string.

        Args:
            query: Search query.

        Returns:
            List of NormalizedRecords from matching releases.
        """
        results = await self._api_call(self._client.search, query, type="release")
        records = []
        for result in results:
            if hasattr(result, "data"):
                records.extend(self.transform_release(result.data))
        return records

    def transform_release(self, data: dict) -> list[NormalizedRecord]:
        """Transform a Discogs release response to NormalizedRecords.

        Creates one NormalizedRecord per track (RECORDING entity type) and
        one for the release itself (RELEASE entity type).

        Args:
            data: Raw Discogs release dict.

        Returns:
            List of NormalizedRecords.
        """
        records: list[NormalizedRecord] = []
        release_id = data.get("id", 0)
        release_title = data.get("title", "")
        release_year = data.get("year")
        release_country = data.get("country")

        # Release-level relationships from extraartists
        release_relationships = self._extract_relationships(
            data.get("extraartists", [])
        )

        # Release-level record
        primary_artists = data.get("artists", [])
        artist_names = [a.get("name", "") for a in primary_artists if a.get("name")]

        release_record = NormalizedRecord(
            source=SourceEnum.DISCOGS,
            source_id=str(release_id),
            entity_type=EntityTypeEnum.RELEASE,
            canonical_name=release_title,
            identifiers=IdentifierBundle(discogs_id=release_id),
            metadata=SourceMetadata(
                roles=artist_names,
                release_date=str(release_year) if release_year else None,
                release_country=release_country,
            ),
            relationships=release_relationships,
            fetch_timestamp=datetime.now(UTC),
            source_confidence=0.85,
            raw_payload=data,
        )
        records.append(release_record)

        # Per-track records
        for track in data.get("tracklist", []):
            track_title = track.get("title", "")
            track_relationships = self._extract_relationships(
                track.get("extraartists", [])
            )

            # Parse duration string like "4:19" to milliseconds
            duration_ms = self._parse_duration(track.get("duration", ""))

            track_record = NormalizedRecord(
                source=SourceEnum.DISCOGS,
                source_id=f"{release_id}-{track.get('position', '')}",
                entity_type=EntityTypeEnum.RECORDING,
                canonical_name=track_title,
                identifiers=IdentifierBundle(discogs_id=release_id),
                metadata=SourceMetadata(
                    roles=artist_names,
                    release_date=str(release_year) if release_year else None,
                    release_country=release_country,
                    duration_ms=duration_ms,
                ),
                relationships=track_relationships,
                fetch_timestamp=datetime.now(UTC),
                source_confidence=0.85,
                raw_payload=track,
            )
            records.append(track_record)

        return records

    def transform_artist(self, data: dict) -> NormalizedRecord:
        """Transform a Discogs artist response to NormalizedRecord.

        Args:
            data: Raw Discogs artist dict.

        Returns:
            NormalizedRecord for the artist.
        """
        name_variations = data.get("namevariations", [])
        alternative_names = [n for n in name_variations if n]

        return NormalizedRecord(
            source=SourceEnum.DISCOGS,
            source_id=str(data.get("id", 0)),
            entity_type=EntityTypeEnum.ARTIST,
            canonical_name=data.get("name", ""),
            alternative_names=alternative_names,
            identifiers=IdentifierBundle(discogs_id=data.get("id")),
            fetch_timestamp=datetime.now(UTC),
            source_confidence=0.85,
            raw_payload=data,
        )

    def _extract_relationships(
        self, extraartists: list[dict],
    ) -> list[Relationship]:
        """Extract relationships from Discogs extraartists list."""
        relationships = []
        for credit in extraartists:
            role_str = credit.get("role", "")
            # Discogs roles can be comma-separated: "Producer, Engineer"
            for role_part in role_str.split(","):
                mapped_type = _map_role(role_part)
                if mapped_type is None:
                    continue
                relationships.append(
                    Relationship(
                        relationship_type=mapped_type,
                        target_source=SourceEnum.DISCOGS,
                        target_source_id=str(credit.get("id", "")),
                        target_entity_type=EntityTypeEnum.ARTIST,
                        attributes={"role_raw": role_part.strip()},
                    )
                )
        return relationships

    @staticmethod
    def _parse_duration(duration_str: str) -> int | None:
        """Parse a duration string like '4:19' to milliseconds."""
        if not duration_str:
            return None
        parts = duration_str.split(":")
        try:
            if len(parts) == 2:
                minutes, seconds = int(parts[0]), int(parts[1])
                return (minutes * 60 + seconds) * 1000
            if len(parts) == 3:
                hours, minutes, seconds = int(parts[0]), int(parts[1]), int(parts[2])
                return (hours * 3600 + minutes * 60 + seconds) * 1000
        except ValueError:
            return None
        return None

    async def _api_call(self, func, *args, **kwargs):
        """Make a rate-limited API call with retry logic.

        Args:
            func: discogs_client method to call.
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
                        "Discogs API error (attempt %d/%d): %s. Retrying in %ds.",
                        attempt + 1,
                        self._max_retries,
                        e,
                        wait,
                    )
                    await asyncio.sleep(wait)
                else:
                    raise
