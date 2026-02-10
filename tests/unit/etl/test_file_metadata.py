"""Tests for file metadata reader (mutagen-based, unit tests with temp files)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from music_attribution.etl.file_metadata import FileMetadataReader
from music_attribution.schemas.normalized import NormalizedRecord


@pytest.fixture
def reader() -> FileMetadataReader:
    """Create a FileMetadataReader."""
    return FileMetadataReader()


@pytest.fixture
def mock_mp3_tags() -> dict:
    """Mock mutagen MP3 tag data."""
    return {
        "TIT2": MagicMock(text=["Come Together"]),
        "TPE1": MagicMock(text=["The Beatles"]),
        "TALB": MagicMock(text=["Abbey Road"]),
        "TDRC": MagicMock(text=["1969"]),
        "TSRC": MagicMock(text=["GBAYE0601690"]),
        "TIPL": MagicMock(people=[["producer", "George Martin"], ["engineer", "Geoff Emerick"]]),
    }


@pytest.fixture
def mock_flac_tags() -> dict:
    """Mock mutagen FLAC tag data (Vorbis comments use lowercase keys)."""
    return {
        "title": ["Something"],
        "artist": ["The Beatles"],
        "album": ["Abbey Road"],
        "date": ["1969"],
        "isrc": ["GBAYE0601691"],
    }


class TestFileMetadataReader:
    """Unit tests for file metadata reader."""

    def test_read_mp3_id3_tags(self, reader, mock_mp3_tags, tmp_path) -> None:
        """Test reading ID3 tags from MP3 file."""
        mock_file = MagicMock()
        mock_file.tags = mock_mp3_tags
        mock_file.info = MagicMock(length=259.0)

        with patch("mutagen.File", return_value=mock_file):
            record = reader.read(tmp_path / "test.mp3")
            assert isinstance(record, NormalizedRecord)
            assert record.canonical_name == "Come Together"
            assert record.source == "FILE_METADATA"

    def test_read_flac_vorbis_comments(self, reader, mock_flac_tags, tmp_path) -> None:
        """Test reading Vorbis comments from FLAC file."""
        mock_file = MagicMock()
        mock_file.tags = mock_flac_tags
        mock_file.info = MagicMock(length=180.0)
        # FLAC uses dict-like access, not ID3 frame objects
        mock_file.__getitem__ = lambda _self, key: mock_flac_tags.get(key, [])
        mock_file.__contains__ = lambda _self, key: key in mock_flac_tags
        mock_file.get = lambda key, default=None: mock_flac_tags.get(key, default)

        with patch("mutagen.File", return_value=mock_file):
            record = reader.read(tmp_path / "test.flac")
            assert isinstance(record, NormalizedRecord)
            assert record.canonical_name == "Something"

    def test_extract_isrc_from_tsrc_frame(self, reader, mock_mp3_tags, tmp_path) -> None:
        """Test that ISRC is extracted from TSRC frame."""
        mock_file = MagicMock()
        mock_file.tags = mock_mp3_tags
        mock_file.info = MagicMock(length=259.0)

        with patch("mutagen.File", return_value=mock_file):
            record = reader.read(tmp_path / "test.mp3")
            assert record.identifiers.isrc == "GBAYE0601690"

    def test_extract_credits_from_tipl_frame(self, reader, mock_mp3_tags, tmp_path) -> None:
        """Test that credits are extracted from TIPL (Involved People) frame."""
        mock_file = MagicMock()
        mock_file.tags = mock_mp3_tags
        mock_file.info = MagicMock(length=259.0)

        with patch("mutagen.File", return_value=mock_file):
            record = reader.read(tmp_path / "test.mp3")
            # Should have relationships for producer and engineer
            assert len(record.relationships) >= 1

    def test_handles_missing_tags_gracefully(self, reader, tmp_path) -> None:
        """Test that files with no tags are handled gracefully."""
        mock_file = MagicMock()
        mock_file.tags = None
        mock_file.info = MagicMock(length=120.0)

        with patch("mutagen.File", return_value=mock_file):
            record = reader.read(tmp_path / "test.mp3")
            assert isinstance(record, NormalizedRecord)
            assert record.canonical_name == "test"  # Falls back to filename stem

    def test_handles_corrupt_file_gracefully(self, reader, tmp_path) -> None:
        """Test that corrupt files return a minimal record."""
        with patch("mutagen.File", return_value=None):
            record = reader.read(tmp_path / "corrupt.mp3")
            assert isinstance(record, NormalizedRecord)
            assert record.canonical_name == "corrupt"

    def test_transform_to_normalized_record(self, reader, mock_mp3_tags, tmp_path) -> None:
        """Test that the output is a valid NormalizedRecord."""
        mock_file = MagicMock()
        mock_file.tags = mock_mp3_tags
        mock_file.info = MagicMock(length=259.0)

        with patch("mutagen.File", return_value=mock_file):
            record = reader.read(tmp_path / "test.mp3")
            assert record.entity_type == "RECORDING"
            assert record.metadata.duration_ms == 259000
            # Should serialize to JSON
            json_str = record.model_dump_json()
            assert "Come Together" in json_str
