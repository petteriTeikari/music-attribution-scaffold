"""Tests for file metadata reader (tinytag-based, unit tests with mocks)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from music_attribution.etl.file_metadata import FileMetadataReader
from music_attribution.schemas.normalized import NormalizedRecord


@pytest.fixture
def reader() -> FileMetadataReader:
    """Create a FileMetadataReader."""
    return FileMetadataReader()


def _make_mock_tag(
    *,
    title: str | None = "Come Together",
    artist: str | None = "The Beatles",
    album: str | None = "Abbey Road",
    year: str | None = "1969",
    duration: float | None = 259.0,
) -> MagicMock:
    """Create a mock TinyTag object with standard attributes."""
    tag = MagicMock()
    tag.title = title
    tag.artist = artist
    tag.album = album
    tag.year = year
    tag.duration = duration
    return tag


class TestFileMetadataReader:
    """Unit tests for file metadata reader."""

    def test_read_mp3_returns_title_artist_duration(self, reader, tmp_path) -> None:
        """Test reading metadata from an audio file."""
        mock_tag = _make_mock_tag()

        with patch("music_attribution.etl.file_metadata.TinyTag.get", return_value=mock_tag):
            record = reader.read(tmp_path / "test.mp3")
            assert isinstance(record, NormalizedRecord)
            assert record.canonical_name == "Come Together"
            assert record.source == "FILE_METADATA"
            assert record.metadata.duration_ms == 259000
            assert record.metadata.roles == ["The Beatles"]

    def test_read_flac_returns_metadata(self, reader, tmp_path) -> None:
        """Test reading metadata from FLAC file."""
        mock_tag = _make_mock_tag(title="Something", duration=180.0)

        with patch("music_attribution.etl.file_metadata.TinyTag.get", return_value=mock_tag):
            record = reader.read(tmp_path / "test.flac")
            assert isinstance(record, NormalizedRecord)
            assert record.canonical_name == "Something"
            assert record.metadata.duration_ms == 180000

    def test_read_file_with_no_tags_returns_filename_as_title(self, reader, tmp_path) -> None:
        """Test that files with no title fall back to filename stem."""
        mock_tag = _make_mock_tag(title=None, artist=None, album=None, year=None, duration=120.0)

        with patch("music_attribution.etl.file_metadata.TinyTag.get", return_value=mock_tag):
            record = reader.read(tmp_path / "untitled.mp3")
            assert record.canonical_name == "untitled"
            assert record.metadata.roles == []

    def test_read_unrecognized_file_returns_minimal_record(self, reader, tmp_path) -> None:
        """Test that unrecognized files return a minimal record."""
        with patch("music_attribution.etl.file_metadata.TinyTag.get", side_effect=Exception("Unsupported")):
            record = reader.read(tmp_path / "corrupt.mp3")
            assert isinstance(record, NormalizedRecord)
            assert record.canonical_name == "corrupt"
            assert record.source_confidence == 0.3

    def test_graceful_degradation_on_unreadable_file(self, reader, tmp_path) -> None:
        """Test that exceptions produce a minimal record, not a crash."""
        with patch("music_attribution.etl.file_metadata.TinyTag.get", side_effect=RuntimeError("IO error")):
            record = reader.read(tmp_path / "broken.wav")
            assert isinstance(record, NormalizedRecord)
            assert record.canonical_name == "broken"

    def test_transform_to_normalized_record(self, reader, tmp_path) -> None:
        """Test that the output is a valid NormalizedRecord with correct types."""
        mock_tag = _make_mock_tag()

        with patch("music_attribution.etl.file_metadata.TinyTag.get", return_value=mock_tag):
            record = reader.read(tmp_path / "test.mp3")
            assert record.entity_type == "RECORDING"
            # Should serialize to JSON
            json_str = record.model_dump_json()
            assert "Come Together" in json_str

    def test_release_date_from_year(self, reader, tmp_path) -> None:
        """Test that year is mapped to release_date."""
        mock_tag = _make_mock_tag(year="2005")

        with patch("music_attribution.etl.file_metadata.TinyTag.get", return_value=mock_tag):
            record = reader.read(tmp_path / "test.mp3")
            assert record.metadata.release_date == "2005"
