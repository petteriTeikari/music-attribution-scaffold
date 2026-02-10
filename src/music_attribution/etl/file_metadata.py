"""File metadata reader using mutagen.

Reads ID3/Vorbis/FLAC/MP4 metadata from audio files. Extracts ISRC,
credits, and other embedded metadata into NormalizedRecords.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from pathlib import Path

import mutagen

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

# Mapping from TIPL/TMCL role strings to our RelationshipTypeEnum
_CREDIT_ROLE_MAP: dict[str, RelationshipTypeEnum] = {
    "producer": RelationshipTypeEnum.PRODUCED,
    "engineer": RelationshipTypeEnum.ENGINEERED,
    "mix": RelationshipTypeEnum.MIXED,
    "mixing": RelationshipTypeEnum.MIXED,
    "mastering": RelationshipTypeEnum.MASTERED,
    "arranger": RelationshipTypeEnum.ARRANGED,
    "remixer": RelationshipTypeEnum.REMIXED,
    "composer": RelationshipTypeEnum.WROTE,
    "lyricist": RelationshipTypeEnum.WROTE,
    "writer": RelationshipTypeEnum.WROTE,
    "performer": RelationshipTypeEnum.PERFORMED,
    "vocals": RelationshipTypeEnum.PERFORMED,
    "guitar": RelationshipTypeEnum.PERFORMED,
    "bass": RelationshipTypeEnum.PERFORMED,
    "drums": RelationshipTypeEnum.PERFORMED,
    "keyboards": RelationshipTypeEnum.PERFORMED,
    "piano": RelationshipTypeEnum.PERFORMED,
}


class FileMetadataReader:
    """Reads audio file metadata and produces NormalizedRecords.

    Supports ID3v2.3/v2.4 (MP3), Vorbis (FLAC/OGG), and MP4 metadata.
    """

    def read(self, file_path: Path) -> NormalizedRecord:
        """Read metadata from an audio file.

        Args:
            file_path: Path to the audio file.

        Returns:
            NormalizedRecord with extracted metadata.
        """
        audio = mutagen.File(str(file_path))

        if audio is None:
            # Corrupt or unrecognized file
            return self._minimal_record(file_path)

        tags = audio.tags
        if tags is None:
            return self._minimal_record(file_path, duration=getattr(audio.info, "length", None))

        # Detect format and extract accordingly
        return self._extract_from_tags(file_path, audio)

    def _extract_from_tags(self, file_path: Path, audio: mutagen.FileType) -> NormalizedRecord:
        """Extract metadata from mutagen tags."""
        tags = audio.tags
        duration = getattr(audio.info, "length", None)

        # Try ID3 first (MP3), then Vorbis-style (FLAC/OGG), then MP4
        title = self._get_id3_text(tags, "TIT2") or self._get_vorbis_text(tags, "title") or file_path.stem
        artist = self._get_id3_text(tags, "TPE1") or self._get_vorbis_text(tags, "artist") or ""
        album = self._get_id3_text(tags, "TALB") or self._get_vorbis_text(tags, "album") or ""
        date = self._get_id3_text(tags, "TDRC") or self._get_vorbis_text(tags, "date") or None
        isrc = self._get_id3_text(tags, "TSRC") or self._get_vorbis_text(tags, "isrc") or None

        # Extract credits from TIPL (Involved People List)
        relationships = self._extract_credits(tags)

        return NormalizedRecord(
            source=SourceEnum.FILE_METADATA,
            source_id=str(file_path),
            entity_type=EntityTypeEnum.RECORDING,
            canonical_name=title,
            identifiers=IdentifierBundle(isrc=isrc),
            metadata=SourceMetadata(
                roles=[artist] if artist else [],
                release_date=str(date) if date else None,
                duration_ms=int(duration * 1000) if duration else None,
            ),
            relationships=relationships,
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

    @staticmethod
    def _get_id3_text(tags, frame_id: str) -> str | None:
        """Get text from an ID3 frame."""
        frame = tags.get(frame_id) if hasattr(tags, "get") else None
        if frame is None:
            return None
        if hasattr(frame, "text") and frame.text:
            return str(frame.text[0])
        return None

    @staticmethod
    def _get_vorbis_text(tags, key: str) -> str | None:
        """Get text from Vorbis-style tags."""
        if hasattr(tags, "get"):
            values = tags.get(key)
            if values and isinstance(values, list) and values:
                return str(values[0])
        return None

    @staticmethod
    def _extract_credits(tags) -> list[Relationship]:
        """Extract credits from TIPL/TMCL frames."""
        relationships = []

        # TIPL: Involved People List (ID3v2.4)
        tipl = tags.get("TIPL") if hasattr(tags, "get") else None
        if tipl and hasattr(tipl, "people"):
            for role_str, person_name in tipl.people:
                role_lower = role_str.strip().lower()
                mapped_type = _CREDIT_ROLE_MAP.get(role_lower)
                if mapped_type is None:
                    # Try partial match
                    for key, value in _CREDIT_ROLE_MAP.items():
                        if key in role_lower:
                            mapped_type = value
                            break
                if mapped_type is not None:
                    relationships.append(
                        Relationship(
                            relationship_type=mapped_type,
                            target_source=SourceEnum.FILE_METADATA,
                            target_source_id=person_name,
                            target_entity_type=EntityTypeEnum.ARTIST,
                            attributes={"role_raw": role_str.strip()},
                        )
                    )

        return relationships
