"""File metadata reader using tinytag.

Reads metadata (title, artist, album, duration, year) from audio files
using tinytag (MIT-licensed, pure Python, zero dependencies). Produces
NormalizedRecords for the ETL pipeline.

Note: tinytag provides normalized high-level attributes only. Low-level
ID3 frames (TIPL, TMCL, TSRC) are not available. Credits come from
MusicBrainz/Discogs APIs instead. ISRC is not exposed by tinytag.
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

    Supports MP3, M4A, WAV, OGG, FLAC, WMA, AIFF via tinytag.
    """

    def read(self, file_path: Path) -> NormalizedRecord:
        """Read metadata from an audio file.

        Args:
            file_path: Path to the audio file.

        Returns:
            NormalizedRecord with extracted metadata.
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
        """Create a minimal NormalizedRecord for files with no/unreadable tags."""
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
