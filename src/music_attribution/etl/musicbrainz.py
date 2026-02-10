"""MusicBrainz ETL connector.

Fetches recordings, works, artists, and relationships from the MusicBrainz
API. Transforms raw API responses into NormalizedRecord boundary objects.
Handles rate limiting (1 req/s), pagination, and retries.

Note: musicbrainzngs is synchronous — all calls are wrapped in
asyncio.to_thread() for async compatibility.
"""

from __future__ import annotations

import asyncio
import logging
from datetime import UTC, datetime

import musicbrainzngs

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

# Mapping from MusicBrainz relation types to our RelationshipTypeEnum
_RELATION_TYPE_MAP: dict[str, RelationshipTypeEnum] = {
    "producer": RelationshipTypeEnum.PRODUCED,
    "performer": RelationshipTypeEnum.PERFORMED,
    "composer": RelationshipTypeEnum.WROTE,
    "lyricist": RelationshipTypeEnum.WROTE,
    "arranger": RelationshipTypeEnum.ARRANGED,
    "engineer": RelationshipTypeEnum.ENGINEERED,
    "mix": RelationshipTypeEnum.MIXED,
    "mastering": RelationshipTypeEnum.MASTERED,
    "remixer": RelationshipTypeEnum.REMIXED,
    "vocal": RelationshipTypeEnum.PERFORMED,
    "instrument": RelationshipTypeEnum.PERFORMED,
}


class MusicBrainzConnector:
    """ETL connector for MusicBrainz API.

    Args:
        user_agent: User-Agent string for API compliance.
            Must include app name and contact info.
        rate: Maximum requests per second (default: 1.0 per MusicBrainz policy).
        max_retries: Maximum retry attempts on transient errors.
    """

    def __init__(
        self,
        user_agent: str,
        rate: float = 1.0,
        max_retries: int = 3,
    ) -> None:
        self._user_agent = user_agent
        self._rate_limiter = TokenBucketRateLimiter(rate=rate, capacity=1)
        self._max_retries = max_retries
        musicbrainzngs.set_useragent(*self._parse_user_agent(user_agent))

    @staticmethod
    def _parse_user_agent(ua: str) -> tuple[str, str, str]:
        """Parse user agent string into (app, version, contact)."""
        parts = ua.split("/", 1)
        app = parts[0] if parts else "MusicAttribution"
        rest = parts[1] if len(parts) > 1 else "0.1.0"
        version_parts = rest.split(" ", 1)
        version = version_parts[0]
        contact = version_parts[1].strip("()") if len(version_parts) > 1 else ""
        return app, version, contact

    async def fetch_recording(self, mbid: str) -> NormalizedRecord:
        """Fetch a recording by MusicBrainz ID.

        Args:
            mbid: MusicBrainz recording ID.

        Returns:
            NormalizedRecord for the recording.
        """
        data = await self._api_call(
            musicbrainzngs.get_recording_by_id,
            mbid,
            includes=["artists", "isrcs", "releases", "artist-rels"],
        )
        return self.transform_recording(data["recording"])

    async def fetch_artist(self, mbid: str) -> NormalizedRecord:
        """Fetch an artist by MusicBrainz ID.

        Args:
            mbid: MusicBrainz artist ID.

        Returns:
            NormalizedRecord for the artist.
        """
        data = await self._api_call(
            musicbrainzngs.get_artist_by_id,
            mbid,
            includes=["aliases", "isnis"],
        )
        return self.transform_artist(data["artist"])

    def transform_recording(self, data: dict) -> NormalizedRecord:
        """Transform a MusicBrainz recording response to NormalizedRecord.

        Args:
            data: Raw MusicBrainz recording dict.

        Returns:
            NormalizedRecord for the recording.
        """
        isrc_list = data.get("isrc-list", [])
        isrc = isrc_list[0] if isrc_list else None

        relationships = self._extract_relationships(data)
        metadata = self._extract_recording_metadata(data)

        return NormalizedRecord(
            source=SourceEnum.MUSICBRAINZ,
            source_id=data["id"],
            entity_type=EntityTypeEnum.RECORDING,
            canonical_name=data.get("title", ""),
            identifiers=IdentifierBundle(isrc=isrc, mbid=data["id"]),
            metadata=metadata,
            relationships=relationships,
            fetch_timestamp=datetime.now(UTC),
            source_confidence=0.9,
            raw_payload=data,
        )

    def transform_artist(self, data: dict) -> NormalizedRecord:
        """Transform a MusicBrainz artist response to NormalizedRecord.

        Args:
            data: Raw MusicBrainz artist dict.

        Returns:
            NormalizedRecord for the artist.
        """
        isni_list = data.get("isni-list", [])
        isni = isni_list[0] if isni_list else None

        alias_list = data.get("alias-list", [])
        alternative_names = [a.get("alias", "") for a in alias_list if a.get("alias")]

        return NormalizedRecord(
            source=SourceEnum.MUSICBRAINZ,
            source_id=data["id"],
            entity_type=EntityTypeEnum.ARTIST,
            canonical_name=data.get("name", ""),
            alternative_names=alternative_names,
            identifiers=IdentifierBundle(isni=isni, mbid=data["id"]),
            fetch_timestamp=datetime.now(UTC),
            source_confidence=0.9,
            raw_payload=data,
        )

    def _extract_relationships(self, data: dict) -> list[Relationship]:
        """Extract relationships from MusicBrainz response."""
        relationships = []
        for rel in data.get("artist-relation-list", []):
            rel_type = rel.get("type", "").lower()
            mapped_type = _RELATION_TYPE_MAP.get(rel_type)
            if mapped_type is None:
                continue

            artist = rel.get("artist", {})
            relationships.append(
                Relationship(
                    relationship_type=mapped_type,
                    target_source=SourceEnum.MUSICBRAINZ,
                    target_source_id=artist.get("id", ""),
                    target_entity_type=EntityTypeEnum.ARTIST,
                    attributes={str(i): str(v) for i, v in enumerate(rel.get("attributes", []))},
                )
            )
        return relationships

    def _extract_recording_metadata(self, data: dict) -> SourceMetadata:
        """Extract structured metadata from recording response."""
        release_list = data.get("release-list", [])
        first_release = release_list[0] if release_list else {}

        artist_credits = data.get("artist-credit", [])
        roles = []
        for credit in artist_credits:
            if isinstance(credit, dict) and "artist" in credit:
                roles.append(credit["artist"].get("name", ""))

        return SourceMetadata(
            roles=roles,
            release_date=first_release.get("date"),
            release_country=first_release.get("country"),
            duration_ms=data.get("length"),
        )

    async def _api_call(self, func, *args, **kwargs):
        """Make a rate-limited API call with retry logic.

        Args:
            func: musicbrainzngs function to call.
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            API response dict.

        Raises:
            musicbrainzngs.WebServiceError: After max retries exhausted.
        """
        for attempt in range(self._max_retries):
            await self._rate_limiter.acquire()
            try:
                return await asyncio.to_thread(func, *args, **kwargs)
            except musicbrainzngs.WebServiceError as e:
                if attempt < self._max_retries - 1:
                    wait = 2**attempt
                    logger.warning("MusicBrainz API error (attempt %d/%d): %s. Retrying in %ds.", attempt + 1, self._max_retries, e, wait)
                    await asyncio.sleep(wait)
                else:
                    raise
