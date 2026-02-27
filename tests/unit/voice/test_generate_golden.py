"""Tests for golden dataset generation script."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest

# scripts/ is not a package — add to sys.path for importability
_SCRIPTS_DIR = Path(__file__).resolve().parents[3] / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

if TYPE_CHECKING:
    pass


class TestSynthesizeCommand:
    """Tests for synthesize_command()."""

    @pytest.mark.voice
    def test_synthesize_command_returns_audio_array(self) -> None:
        """synthesize_command returns a non-empty float32 numpy array."""
        pytest.importorskip("soundfile")
        import numpy as np_mod
        from generate_golden_dataset import synthesize_command

        # Mock Piper TTS to return fake 22050Hz int16 audio
        fake_audio = np_mod.random.randn(22050).astype(np_mod.float32) * 0.5
        with patch(
            "generate_golden_dataset._call_piper_tts",
            return_value=(fake_audio, 22050),
        ):
            audio, sr = synthesize_command("hello world")
        assert isinstance(audio, np_mod.ndarray)
        assert len(audio) > 0
        assert audio.dtype == np_mod.float32

    @pytest.mark.voice
    def test_synthesize_command_resampled_to_16k(self) -> None:
        """synthesize_command resamples Piper 22050Hz output to 16000Hz."""
        pytest.importorskip("soxr")
        import numpy as np_mod
        from generate_golden_dataset import synthesize_command

        # 1 second at 22050Hz
        fake_audio = np_mod.random.randn(22050).astype(np_mod.float32) * 0.5
        with patch(
            "generate_golden_dataset._call_piper_tts",
            return_value=(fake_audio, 22050),
        ):
            audio, sr = synthesize_command("hello world")
        assert sr == 16000
        # Length ratio should be approximately 16000/22050
        expected_len = int(22050 * 16000 / 22050)
        assert abs(len(audio) - expected_len) <= 2

    @pytest.mark.voice
    def test_generate_clean_fixtures_creates_20_files(self, tmp_path: Path) -> None:
        """generate_clean_fixtures creates 20 FLAC files."""
        pytest.importorskip("soundfile")
        import numpy as np_mod
        from generate_golden_dataset import generate_clean_fixtures

        fake_audio = np_mod.random.randn(16000).astype(np_mod.float32) * 0.5
        with patch(
            "generate_golden_dataset._call_piper_tts",
            return_value=(fake_audio, 22050),
        ):
            paths = generate_clean_fixtures(tmp_path)
        assert len(paths) == 20
        for p in paths:
            assert p.exists()
            assert p.suffix == ".flac"

    @pytest.mark.voice
    def test_clean_fixture_naming_convention(self, tmp_path: Path) -> None:
        """Clean fixtures are named cmd_01_clean.flac through cmd_20_clean.flac."""
        pytest.importorskip("soundfile")
        import numpy as np_mod
        from generate_golden_dataset import generate_clean_fixtures

        fake_audio = np_mod.random.randn(16000).astype(np_mod.float32) * 0.5
        with patch(
            "generate_golden_dataset._call_piper_tts",
            return_value=(fake_audio, 22050),
        ):
            paths = generate_clean_fixtures(tmp_path)
        names = sorted(p.name for p in paths)
        expected = sorted(f"cmd_{i:02d}_clean.flac" for i in range(1, 21))
        assert names == expected

    @pytest.mark.voice
    def test_synthesize_command_approximate_idempotency(self) -> None:
        """Deterministic mock input produces identical output."""
        pytest.importorskip("soxr")
        import numpy as np_mod
        from generate_golden_dataset import synthesize_command

        np_mod.random.seed(42)
        fake_audio = np_mod.random.randn(22050).astype(np_mod.float32) * 0.5

        with patch(
            "generate_golden_dataset._call_piper_tts",
            return_value=(fake_audio.copy(), 22050),
        ):
            out1, _ = synthesize_command("hello world")

        with patch(
            "generate_golden_dataset._call_piper_tts",
            return_value=(fake_audio.copy(), 22050),
        ):
            out2, _ = synthesize_command("hello world")

        assert np_mod.allclose(out1, out2, atol=1e-4)
