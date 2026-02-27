"""Tests for piper_utils — Piper TTS model utilities."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from music_attribution.voice.config import DEFAULT_PIPER_VOICE_ID


class TestFindPiperModel:
    """Tests for find_piper_model()."""

    def test_finds_model_in_explicit_dir(self, tmp_path: Path) -> None:
        """Returns path when model exists in explicit model_dir."""
        from music_attribution.voice.piper_utils import find_piper_model

        model_file = tmp_path / f"{DEFAULT_PIPER_VOICE_ID}.onnx"
        model_file.write_bytes(b"fake-onnx-data")

        result = find_piper_model(DEFAULT_PIPER_VOICE_ID, model_dir=tmp_path)
        assert result is not None
        assert result == model_file

    def test_returns_none_when_not_found(self, tmp_path: Path) -> None:
        """Returns None when model doesn't exist anywhere."""
        from music_attribution.voice.piper_utils import find_piper_model

        with patch(
            "music_attribution.voice.piper_utils._MODEL_SEARCH_DIRS",
            [tmp_path / "nonexistent"],
        ):
            result = find_piper_model(DEFAULT_PIPER_VOICE_ID)
        assert result is None

    def test_finds_model_in_subdirectory(self, tmp_path: Path) -> None:
        """Finds model in a subdirectory via glob."""
        from music_attribution.voice.piper_utils import find_piper_model

        subdir = tmp_path / "voices" / "en"
        subdir.mkdir(parents=True)
        model_file = subdir / f"{DEFAULT_PIPER_VOICE_ID}.onnx"
        model_file.write_bytes(b"fake-onnx-data")

        with patch(
            "music_attribution.voice.piper_utils._MODEL_SEARCH_DIRS",
            [tmp_path],
        ):
            result = find_piper_model(DEFAULT_PIPER_VOICE_ID)
        assert result is not None
        assert result == model_file

    def test_explicit_dir_checked_first(self, tmp_path: Path) -> None:
        """model_dir is checked before default search dirs."""
        from music_attribution.voice.piper_utils import find_piper_model

        explicit = tmp_path / "explicit"
        explicit.mkdir()
        model_file = explicit / f"{DEFAULT_PIPER_VOICE_ID}.onnx"
        model_file.write_bytes(b"explicit-model")

        # Even if a model exists in search dirs, explicit dir wins
        default = tmp_path / "default"
        default.mkdir()
        (default / f"{DEFAULT_PIPER_VOICE_ID}.onnx").write_bytes(b"default-model")

        with patch(
            "music_attribution.voice.piper_utils._MODEL_SEARCH_DIRS",
            [default],
        ):
            result = find_piper_model(DEFAULT_PIPER_VOICE_ID, model_dir=explicit)
        assert result is not None
        assert result.read_bytes() == b"explicit-model"


class TestDownloadPiperModel:
    """Tests for download_piper_model()."""

    def test_downloads_to_specified_dir(self, tmp_path: Path) -> None:
        """Calls download_voice and returns expected model path."""
        pytest.importorskip("piper")
        from music_attribution.voice.piper_utils import download_piper_model

        model_path = tmp_path / f"{DEFAULT_PIPER_VOICE_ID}.onnx"

        def fake_download(voice_id: str, download_dir: Path, **kwargs: object) -> None:
            # Simulate download by creating the file
            (download_dir / f"{voice_id}.onnx").write_bytes(b"model-data")

        with patch(
            "piper.download_voices.download_voice",
            side_effect=fake_download,
        ):
            result = download_piper_model(DEFAULT_PIPER_VOICE_ID, download_dir=tmp_path)

        assert result == model_path
        assert result.is_file()

    def test_raises_if_download_fails(self, tmp_path: Path) -> None:
        """Raises FileNotFoundError if file not created after download."""
        pytest.importorskip("piper")
        from music_attribution.voice.piper_utils import download_piper_model

        with (
            patch(
                "piper.download_voices.download_voice",
                side_effect=lambda *_args, **_kwargs: None,
            ),
            pytest.raises(FileNotFoundError, match="model file not found"),
        ):
            download_piper_model(DEFAULT_PIPER_VOICE_ID, download_dir=tmp_path)

    def test_creates_download_dir_if_missing(self, tmp_path: Path) -> None:
        """Creates download_dir if it doesn't exist."""
        pytest.importorskip("piper")
        from music_attribution.voice.piper_utils import download_piper_model

        target = tmp_path / "new" / "dir"
        assert not target.exists()

        def fake_download(voice_id: str, download_dir: Path, **kwargs: object) -> None:
            (download_dir / f"{voice_id}.onnx").write_bytes(b"data")

        with patch(
            "piper.download_voices.download_voice",
            side_effect=fake_download,
        ):
            result = download_piper_model(DEFAULT_PIPER_VOICE_ID, download_dir=target)

        assert target.exists()
        assert result.is_file()


class TestEnsurePiperModel:
    """Tests for ensure_piper_model()."""

    def test_returns_existing_model_without_download(self, tmp_path: Path) -> None:
        """Returns existing model path without calling download."""
        from music_attribution.voice.piper_utils import ensure_piper_model

        model_file = tmp_path / f"{DEFAULT_PIPER_VOICE_ID}.onnx"
        model_file.write_bytes(b"existing-model")

        with patch("music_attribution.voice.piper_utils.download_piper_model") as mock_dl:
            result = ensure_piper_model(DEFAULT_PIPER_VOICE_ID, model_dir=tmp_path)

        mock_dl.assert_not_called()
        assert result == model_file

    def test_downloads_when_not_found(self, tmp_path: Path) -> None:
        """Calls download_piper_model when model not found locally."""
        from music_attribution.voice.piper_utils import ensure_piper_model

        expected_path = tmp_path / f"{DEFAULT_PIPER_VOICE_ID}.onnx"

        with (
            patch(
                "music_attribution.voice.piper_utils._MODEL_SEARCH_DIRS",
                [tmp_path / "empty"],
            ),
            patch(
                "music_attribution.voice.piper_utils.download_piper_model",
                return_value=expected_path,
            ) as mock_dl,
        ):
            result = ensure_piper_model(DEFAULT_PIPER_VOICE_ID, model_dir=tmp_path)

        mock_dl.assert_called_once_with(DEFAULT_PIPER_VOICE_ID, download_dir=tmp_path)
        assert result == expected_path


class TestLoadPiperVoice:
    """Tests for load_piper_voice()."""

    def test_loads_voice_from_model_path(self, tmp_path: Path) -> None:
        """Loads PiperVoice from an existing model path."""
        pytest.importorskip("piper")
        from music_attribution.voice.piper_utils import load_piper_voice

        model_file = tmp_path / f"{DEFAULT_PIPER_VOICE_ID}.onnx"
        model_file.write_bytes(b"model")

        mock_voice = MagicMock()
        with (
            patch(
                "music_attribution.voice.piper_utils.ensure_piper_model",
                return_value=model_file,
            ),
            patch(
                "piper.PiperVoice.load",
                return_value=mock_voice,
            ) as mock_load,
        ):
            voice = load_piper_voice(DEFAULT_PIPER_VOICE_ID, model_dir=tmp_path)

        mock_load.assert_called_once_with(str(model_file))
        assert voice is mock_voice


class TestSynthesizeSpeech:
    """Tests for synthesize_speech()."""

    def test_returns_float32_array_and_sample_rate(self) -> None:
        """synthesize_speech returns (float32 ndarray, int sample_rate)."""
        from music_attribution.voice.piper_utils import synthesize_speech

        # Create a mock PiperVoice that writes valid WAV data
        mock_voice = MagicMock()

        import wave

        def fake_synthesize(text: str, wav_file: wave.Wave_write) -> None:
            sample_rate = 22050
            n_samples = sample_rate  # 1 second
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            # Generate a simple sine wave as int16
            t = np.linspace(0, 1, n_samples, endpoint=False)
            audio = (np.sin(2 * np.pi * 440 * t) * 16000).astype(np.int16)
            wav_file.writeframes(audio.tobytes())

        mock_voice.synthesize_wav = fake_synthesize

        audio, sr = synthesize_speech(mock_voice, "hello world")
        assert isinstance(audio, np.ndarray)
        assert audio.dtype == np.float32
        assert sr == 22050
        assert len(audio) == 22050
        assert np.max(np.abs(audio)) <= 1.0

    def test_handles_empty_text(self) -> None:
        """synthesize_speech handles empty text gracefully."""
        import wave

        from music_attribution.voice.piper_utils import synthesize_speech

        mock_voice = MagicMock()

        def fake_synthesize(text: str, wav_file: wave.Wave_write) -> None:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(22050)
            # Write zero frames
            wav_file.writeframes(b"")

        mock_voice.synthesize_wav = fake_synthesize

        audio, sr = synthesize_speech(mock_voice, "")
        assert isinstance(audio, np.ndarray)
        assert sr == 22050
        assert len(audio) == 0
