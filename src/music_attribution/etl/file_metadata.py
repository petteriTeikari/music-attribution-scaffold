"""File metadata reader using tinytag.

Reads metadata (title, artist, album, duration, year) from audio files
using tinytag (MIT-licensed, pure Python, zero dependencies) and produces
``NormalizedRecord`` objects for the ETL pipeline.

This is the lowest-confidence data source (``source_confidence = 0.7``)
because embedded file metadata is often incomplete, inconsistent, or
user-edited.  It serves as a *baseline* that is enriched by higher-
confidence sources (MusicBrainz, Discogs, AcoustID).

Notes
-----
tinytag provides normalised high-level attributes only.  Low-level
ID3 frames (TIPL, TMCL, TSRC) are not available through tinytag:

* **ISRC**: Not exposed by tinytag.  Use AcoustID fingerprinting or
  MusicBrainz lookup to obtain ISRCs.
* **Credits (TIPL/TMCL)**: Not available.  Detailed credits come from
  MusicBrainz and Discogs APIs instead.

Supported formats: MP3, M4A, WAV, OGG, FLAC, WMA, AIFF.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from pathlib import Path

from tinytag import TinyTag

from music_attribution.schemas.enums import EntityTypeEnum, SourceEnum
from music_attribution.schemas.normalized import (
    IdentifierBundle,
    NormalizedRecord,
    SourceMetadata,
)

logger = logging.getLogger(__name__)


class FileMetadataReader:
    """Reads audio file metadata and produces NormalizedRecords.

    A stateless reader that extracts embedded metadata from audio files
    using tinytag.  When metadata cannot be read (corrupted file, DRM,
    unsupported codec), a minimal fallback record is produced using only
    the filename.

    Supported formats: MP3, M4A, WAV, OGG, FLAC, WMA, AIFF.

    Examples
    --------
    >>> reader = FileMetadataReader()
    >>> record = reader.read(Path("hide_and_seek.mp3"))
    >>> record.canonical_name
    'Hide and Seek'
    >>> record.source
    <SourceEnum.FILE_METADATA: 'file_metadata'>
    """

    def read(self, file_path: Path) -> NormalizedRecord:
        """Read metadata from an audio file.

        Extracts title, artist, album, year, and duration from the
        file's embedded tags.  Falls back to a minimal record (using
        the filename stem as title) if tags cannot be read.

        The ``source_confidence`` is set to 0.7 for successfully read
        files and 0.3 for fallback records.

        Parameters
        ----------
        file_path : Path
            Path to the audio file.

        Returns
        -------
        NormalizedRecord
            Normalised recording with extracted metadata.  The
            ``identifiers`` bundle will be empty (no ISRC from tinytag).
        """
        try:
            tag = TinyTag.get(str(file_path))
        except Exception:
            logger.warning("Failed to read metadata from %s", file_path)
            return self._minimal_record(file_path)

        title = tag.title or file_path.stem
        artist = tag.artist or ""
        album = tag.album or ""
        year = tag.year
        duration = tag.duration

        # TODO: ISRC not available in tinytag — add via raw ID3 parser if needed
        # TODO: TIPL credits not available in tinytag — credits come from MusicBrainz/Discogs APIs

        return NormalizedRecord(
            source=SourceEnum.FILE_METADATA,
            source_id=str(file_path),
            entity_type=EntityTypeEnum.RECORDING,
            canonical_name=title,
            identifiers=IdentifierBundle(),
            metadata=SourceMetadata(
                roles=[artist] if artist else [],
                release_date=str(year) if year else None,
                duration_ms=int(duration * 1000) if duration else None,
            ),
            relationships=[],
            fetch_timestamp=datetime.now(UTC),
            source_confidence=0.7,
            raw_payload={"file_path": str(file_path), "album": album},
        )

    def _minimal_record(self, file_path: Path, duration: float | None = None) -> NormalizedRecord:
        """Create a minimal NormalizedRecord for files with no/unreadable tags.

        Used as a fallback when tinytag cannot parse the file's metadata.
        The ``source_confidence`` is set to 0.3 to reflect the very low
        certainty of filename-only identification.

        Parameters
        ----------
        file_path : Path
            Path to the audio file (used for ``source_id`` and
            ``canonical_name`` via ``file_path.stem``).
        duration : float or None, optional
            Duration in seconds if known from another source, by default
            ``None``.

        Returns
        -------
        NormalizedRecord
            Minimal recording record with filename-derived title and
            empty identifiers.
        """
        return NormalizedRecord(
            source=SourceEnum.FILE_METADATA,
            source_id=str(file_path),
            entity_type=EntityTypeEnum.RECORDING,
            canonical_name=file_path.stem,
            identifiers=IdentifierBundle(),
            fetch_timestamp=datetime.now(UTC),
            source_confidence=0.3,
            metadata=SourceMetadata(
                duration_ms=int(duration * 1000) if duration else None,
            ),
            raw_payload={"file_path": str(file_path)},
        )
