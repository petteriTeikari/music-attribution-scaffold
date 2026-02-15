"""MusicBrainz ETL connector.

Fetches recordings, works, artists, and relationships from the MusicBrainz
API and transforms raw API responses into ``NormalizedRecord`` boundary
objects.  Handles rate limiting (1 req/s per MusicBrainz policy),
pagination, and exponential-backoff retries.

MusicBrainz is the highest-confidence open data source (``source_confidence
= 0.9``) because it is community-curated with editorial review.  It provides
ISRC, ISWC, and ISNI identifiers that map directly to the A0-A3 assurance
levels described in the companion paper (Section 3).

Notes
-----
``musicbrainzngs`` is synchronous — all API calls are wrapped in
``asyncio.to_thread()`` to avoid blocking the event loop.

The ``_RELATION_TYPE_MAP`` translates MusicBrainz relationship type
strings (e.g., ``"producer"``, ``"lyricist"``) into the normalised
``RelationshipTypeEnum`` used throughout the attribution pipeline.
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
    """ETL connector for the MusicBrainz API.

    Provides async ``fetch_*`` methods that query the MusicBrainz web
    service and ``transform_*`` methods that convert raw JSON responses
    into ``NormalizedRecord`` boundary objects for the downstream entity
    resolution pipeline.

    Parameters
    ----------
    user_agent : str
        User-Agent string for API compliance.  Must include the
        application name, version, and contact email (e.g.,
        ``"MusicAttribution/0.1.0 (user@example.com)"``).
    rate : float, optional
        Maximum requests per second, by default 1.0 (MusicBrainz
        policy).
    max_retries : int, optional
        Maximum retry attempts on transient API errors, by default 3.
        Uses exponential backoff (2^attempt seconds).

    Attributes
    ----------
    _rate_limiter : TokenBucketRateLimiter
        Token-bucket limiter enforcing the per-second request cap.

    Examples
    --------
    >>> connector = MusicBrainzConnector("MusicAttribution/0.1.0 (user@example.com)")
    >>> record = await connector.fetch_recording("some-mbid")
    >>> record.source
    <SourceEnum.MUSICBRAINZ: 'musicbrainz'>
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
        """Parse a user-agent string into musicbrainzngs components.

        Parameters
        ----------
        ua : str
            User-agent string in the format
            ``"AppName/version (contact@email.com)"``.

        Returns
        -------
        tuple[str, str, str]
            ``(app_name, version, contact_info)`` for
            ``musicbrainzngs.set_useragent()``.
        """
        parts = ua.split("/", 1)
        app = parts[0] if parts else "MusicAttribution"
        rest = parts[1] if len(parts) > 1 else "0.1.0"
        version_parts = rest.split(" ", 1)
        version = version_parts[0]
        contact = version_parts[1].strip("()") if len(version_parts) > 1 else ""
        return app, version, contact

    async def fetch_recording(self, mbid: str) -> NormalizedRecord:
        """Fetch a recording by MusicBrainz ID.

        Retrieves the recording with artist credits, ISRCs, releases,
        and artist relationships, then transforms the response into a
        ``NormalizedRecord``.

        Parameters
        ----------
        mbid : str
            MusicBrainz recording UUID (e.g.,
            ``"b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d"``).

        Returns
        -------
        NormalizedRecord
            Normalised recording with relationships and identifiers.

        Raises
        ------
        musicbrainzngs.WebServiceError
            If the MusicBrainz API returns an error after all retries.
        """
        data = await self._api_call(
            musicbrainzngs.get_recording_by_id,
            mbid,
            includes=["artists", "isrcs", "releases", "artist-rels"],
        )
        return self.transform_recording(data["recording"])

    async def fetch_artist(self, mbid: str) -> NormalizedRecord:
        """Fetch an artist by MusicBrainz ID.

        Retrieves the artist profile with aliases, then transforms the
        response into a ``NormalizedRecord`` with ISNI identifiers and
        alternative name variants.

        Parameters
        ----------
        mbid : str
            MusicBrainz artist UUID.

        Returns
        -------
        NormalizedRecord
            Normalised artist with identifiers and alternative names.

        Raises
        ------
        musicbrainzngs.WebServiceError
            If the MusicBrainz API returns an error after all retries.
        """
        data = await self._api_call(
            musicbrainzngs.get_artist_by_id,
            mbid,
            includes=["aliases"],
        )
        return self.transform_artist(data["artist"])

    def transform_recording(self, data: dict) -> NormalizedRecord:
        """Transform a MusicBrainz recording response to a NormalizedRecord.

        Extracts ISRC identifiers, artist relationships, and structured
        metadata (roles, release date, country, duration) from the raw
        API response.  The ``source_confidence`` is set to 0.9
        reflecting MusicBrainz's community-curated editorial quality.

        Parameters
        ----------
        data : dict
            Raw MusicBrainz recording dictionary as returned by
            ``musicbrainzngs.get_recording_by_id()``.

        Returns
        -------
        NormalizedRecord
            Normalised recording with identifiers, relationships, and
            source metadata.
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
        """Transform a MusicBrainz artist response to a NormalizedRecord.

        Extracts ISNI identifiers and alias-list name variants.  The
        ``source_confidence`` is set to 0.9 reflecting MusicBrainz's
        community-curated editorial quality.

        Parameters
        ----------
        data : dict
            Raw MusicBrainz artist dictionary as returned by
            ``musicbrainzngs.get_artist_by_id()``.

        Returns
        -------
        NormalizedRecord
            Normalised artist with identifiers and alternative names.
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
        """Extract artist relationships from a MusicBrainz response.

        Iterates over ``artist-relation-list`` entries and maps each
        MusicBrainz relation type to the normalised
        ``RelationshipTypeEnum`` via ``_RELATION_TYPE_MAP``.  Unmapped
        relation types are silently skipped.

        Parameters
        ----------
        data : dict
            Raw MusicBrainz recording or work dictionary containing
            an ``artist-relation-list`` key.

        Returns
        -------
        list[Relationship]
            List of normalised relationships, empty if none are found.
        """
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
        """Extract structured metadata from a recording response.

        Pulls release date, country, duration, and artist credit roles
        from the raw MusicBrainz recording dictionary.

        Parameters
        ----------
        data : dict
            Raw MusicBrainz recording dictionary.

        Returns
        -------
        SourceMetadata
            Structured metadata with roles, release date, country,
            and duration in milliseconds.
        """
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
        """Make a rate-limited API call with exponential-backoff retry.

        Acquires a token from the rate limiter before each attempt, then
        delegates the synchronous ``musicbrainzngs`` call to a thread
        via ``asyncio.to_thread()``.

        Parameters
        ----------
        func : callable
            A ``musicbrainzngs`` function (e.g.,
            ``musicbrainzngs.get_recording_by_id``).
        *args : Any
            Positional arguments forwarded to *func*.
        **kwargs : Any
            Keyword arguments forwarded to *func*.

        Returns
        -------
        dict
            Raw API response dictionary.

        Raises
        ------
        musicbrainzngs.WebServiceError
            If all ``max_retries`` attempts fail.
        """
        for attempt in range(self._max_retries):
            await self._rate_limiter.acquire()
            try:
                return await asyncio.to_thread(func, *args, **kwargs)
            except musicbrainzngs.WebServiceError as e:
                if attempt < self._max_retries - 1:
                    wait = 2**attempt
                    logger.warning(
                        "MusicBrainz API error (attempt %d/%d): %s. Retrying in %ds.",
                        attempt + 1,
                        self._max_retries,
                        e,
                        wait,
                    )
                    await asyncio.sleep(wait)
                else:
                    raise
