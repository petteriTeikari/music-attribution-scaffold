"""Discogs ETL connector.

Fetches release credits, artist profiles, and label information from the
Discogs API and transforms raw API responses into ``NormalizedRecord``
boundary objects.  Handles rate limiting (60 req/min authenticated,
25 req/min unauthenticated) and exponential-backoff retries.

Discogs is particularly valuable for detailed credit information (producer,
engineer, mix, mastering) that is often missing from other sources.  The
``source_confidence`` is set to 0.85, slightly below MusicBrainz, because
Discogs data is user-contributed without the same editorial review process.

Notes
-----
``python3-discogs-client`` is synchronous — all API calls are wrapped in
``asyncio.to_thread()`` to avoid blocking the event loop.

The ``_ROLE_MAP`` translates Discogs credit role strings (e.g.,
``"Producer"``, ``"Mixed By"``) into the normalised
``RelationshipTypeEnum``.  Discogs roles can be comma-separated (e.g.,
``"Producer, Engineer"``), so each role part is mapped independently.
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
    """Map a Discogs role string to a ``RelationshipTypeEnum``.

    Performs case-insensitive matching, first attempting a direct
    dictionary lookup and then falling back to substring containment.

    Parameters
    ----------
    role_str : str
        Raw role string from a Discogs credit entry (e.g.,
        ``"Executive Producer"``).

    Returns
    -------
    RelationshipTypeEnum or None
        The mapped relationship type, or ``None`` if no mapping exists.

    Examples
    --------
    >>> _map_role("Producer")
    <RelationshipTypeEnum.PRODUCED: 'produced'>
    >>> _map_role("Unknown Role") is None
    True
    """
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
    """ETL connector for the Discogs API.

    Provides async ``fetch_*`` methods that query the Discogs web
    service and ``transform_*`` methods that convert raw JSON responses
    into ``NormalizedRecord`` boundary objects.

    Parameters
    ----------
    user_agent : str
        User-Agent string for API compliance.  Discogs requires a
        unique user-agent identifying the application.
    token : str or None, optional
        Discogs personal access token.  When provided, the rate limit
        increases from 25 req/min to 60 req/min.
    rate : float or None, optional
        Override the requests-per-second cap.  If ``None`` (default),
        the rate is auto-selected based on authentication status.
    max_retries : int, optional
        Maximum retry attempts on transient errors, by default 3.
        Uses exponential backoff (2^attempt seconds).

    Attributes
    ----------
    _authenticated : bool
        Whether a personal access token was provided.
    _rate_limiter : TokenBucketRateLimiter
        Token-bucket limiter enforcing the per-second request cap.

    Examples
    --------
    >>> connector = DiscogsConnector("MyApp/1.0", token="secret")
    >>> records = await connector.fetch_release(12345)
    >>> len(records) > 0
    True
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

        Retrieves the release with full credits and tracklist, then
        transforms it into one ``NormalizedRecord`` per track plus one
        for the release itself.

        Parameters
        ----------
        release_id : int
            Discogs release ID (numeric).

        Returns
        -------
        list[NormalizedRecord]
            List containing one release-level record followed by one
            record per track.

        Raises
        ------
        Exception
            If the Discogs API returns an error after all retries.
        """
        release = await self._api_call(self._client.release, release_id)
        data = release.data
        return self.transform_release(data)

    async def fetch_artist(self, artist_id: int) -> NormalizedRecord:
        """Fetch an artist profile by Discogs ID.

        Retrieves the artist profile with name variations and transforms
        it into a ``NormalizedRecord``.

        Parameters
        ----------
        artist_id : int
            Discogs artist ID (numeric).

        Returns
        -------
        NormalizedRecord
            Normalised artist with alternative name variants.

        Raises
        ------
        Exception
            If the Discogs API returns an error after all retries.
        """
        artist = await self._api_call(self._client.artist, artist_id)
        return self.transform_artist(artist.data)

    async def search_releases(self, query: str) -> list[NormalizedRecord]:
        """Search for releases by a free-text query string.

        Parameters
        ----------
        query : str
            Search query (e.g., artist name, album title).

        Returns
        -------
        list[NormalizedRecord]
            Flattened list of ``NormalizedRecord`` objects from all
            matching releases (one per track plus one per release).

        Raises
        ------
        Exception
            If the Discogs API returns an error after all retries.
        """
        results = await self._api_call(self._client.search, query, type="release")
        records = []
        for result in results:
            if hasattr(result, "data"):
                records.extend(self.transform_release(result.data))
        return records

    def transform_release(self, data: dict) -> list[NormalizedRecord]:
        """Transform a Discogs release response into NormalizedRecords.

        Creates one ``NormalizedRecord`` for the release itself
        (``EntityTypeEnum.RELEASE``) and one per track
        (``EntityTypeEnum.RECORDING``).  Release-level credits from
        ``extraartists`` are attached to the release record, while
        track-level credits are attached to each track record.

        The ``source_confidence`` is set to 0.85 for all Discogs
        records.

        Parameters
        ----------
        data : dict
            Raw Discogs release dictionary as returned by the
            ``python3-discogs-client``.

        Returns
        -------
        list[NormalizedRecord]
            Release record followed by per-track recording records.
        """
        records: list[NormalizedRecord] = []
        release_id = data.get("id", 0)
        release_title = data.get("title", "")
        release_year = data.get("year")
        release_country = data.get("country")

        # Release-level relationships from extraartists
        release_relationships = self._extract_relationships(data.get("extraartists", []))

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
            track_relationships = self._extract_relationships(track.get("extraartists", []))

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
        """Transform a Discogs artist response into a NormalizedRecord.

        Extracts the artist's canonical name and all name variations
        from the raw Discogs response.

        Parameters
        ----------
        data : dict
            Raw Discogs artist dictionary.

        Returns
        -------
        NormalizedRecord
            Normalised artist with ``alternative_names`` populated from
            Discogs ``namevariations``.
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
        self,
        extraartists: list[dict],
    ) -> list[Relationship]:
        """Extract relationships from a Discogs ``extraartists`` list.

        Each credit entry may contain comma-separated roles (e.g.,
        ``"Producer, Engineer"``).  Each role part is mapped
        independently via ``_map_role()``.

        Parameters
        ----------
        extraartists : list[dict]
            List of Discogs credit dictionaries, each with ``role``
            and ``id`` keys.

        Returns
        -------
        list[Relationship]
            Normalised relationships with raw role preserved in
            ``attributes["role_raw"]``.
        """
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
        """Parse a duration string to milliseconds.

        Supports ``"M:SS"`` and ``"H:MM:SS"`` formats.

        Parameters
        ----------
        duration_str : str
            Duration string (e.g., ``"4:19"`` or ``"1:02:30"``).

        Returns
        -------
        int or None
            Duration in milliseconds, or ``None`` if the string is
            empty or unparseable.

        Examples
        --------
        >>> DiscogsConnector._parse_duration("4:19")
        259000
        >>> DiscogsConnector._parse_duration("") is None
        True
        """
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
        """Make a rate-limited API call with exponential-backoff retry.

        Acquires a token from the rate limiter before each attempt, then
        delegates the synchronous ``discogs_client`` call to a thread
        via ``asyncio.to_thread()``.

        Parameters
        ----------
        func : callable
            A ``discogs_client`` method or callable.
        *args : Any
            Positional arguments forwarded to *func*.
        **kwargs : Any
            Keyword arguments forwarded to *func*.

        Returns
        -------
        Any
            Raw API response object.

        Raises
        ------
        Exception
            If all ``max_retries`` attempts fail.
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
