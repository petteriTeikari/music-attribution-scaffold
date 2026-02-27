"""Tests for golden dataset generation script."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# scripts/ is not a package — add to sys.path for importability
_SCRIPTS_DIR = Path(__file__).resolve().parents[3] / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))


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


class TestGenerateDegradedFixtures:
    """Tests for generate_degraded_fixtures()."""

    @pytest.mark.voice
    def test_generate_degraded_creates_80_files(self, tmp_path: Path) -> None:
        """generate_degraded_fixtures creates 80 degraded FLACs (4 non-clean × 20)."""
        pytest.importorskip("soundfile")
        pytest.importorskip("audiomentations")
        import numpy as np_mod
        from generate_golden_dataset import generate_degraded_fixtures

        from music_attribution.voice.degradation import write_audio

        # Create 20 fake clean FLACs
        fake_audio = np_mod.random.randn(16000).astype(np_mod.float32) * 0.1
        for i in range(1, 21):
            write_audio(tmp_path / f"cmd_{i:02d}_clean.flac", fake_audio)

        paths = generate_degraded_fixtures(tmp_path, tmp_path, seed=42)
        assert len(paths) == 80
        for p in paths:
            assert p.exists()
            assert p.suffix == ".flac"

    @pytest.mark.voice
    def test_degraded_fixture_naming(self, tmp_path: Path) -> None:
        """Degraded files follow cmd_NN_preset.flac naming convention."""
        pytest.importorskip("soundfile")
        pytest.importorskip("audiomentations")
        import numpy as np_mod
        from generate_golden_dataset import generate_degraded_fixtures

        from music_attribution.voice.degradation import write_audio

        fake_audio = np_mod.random.randn(16000).astype(np_mod.float32) * 0.1
        for i in range(1, 21):
            write_audio(tmp_path / f"cmd_{i:02d}_clean.flac", fake_audio)

        paths = generate_degraded_fixtures(tmp_path, tmp_path, seed=42)
        names = sorted(p.name for p in paths)
        expected = sorted(
            f"cmd_{i:02d}_{preset}.flac"
            for i in range(1, 21)
            for preset in ["office", "codec", "noisy_cafe", "extreme"]
        )
        assert names == expected

    @pytest.mark.voice
    @pytest.mark.timeout(180)
    def test_degraded_fixtures_deterministic(self, tmp_path: Path) -> None:
        """Two runs with same seed produce byte-identical output."""
        pytest.importorskip("soundfile")
        pytest.importorskip("audiomentations")
        import numpy as np_mod
        from generate_golden_dataset import generate_degraded_fixtures

        from music_attribution.voice.degradation import write_audio

        # Use deterministic input audio (seeded RNG)
        np_mod.random.seed(99)
        fake_audio = np_mod.random.randn(16000).astype(np_mod.float32) * 0.1
        # Only 2 commands to keep test fast while still exercising all presets
        for i in range(1, 3):
            write_audio(tmp_path / f"cmd_{i:02d}_clean.flac", fake_audio)

        dir_a = tmp_path / "run_a"
        dir_b = tmp_path / "run_b"
        dir_a.mkdir()
        dir_b.mkdir()

        paths_a = generate_degraded_fixtures(tmp_path, dir_a, seed=42)
        paths_b = generate_degraded_fixtures(tmp_path, dir_b, seed=42)

        assert len(paths_a) == 8  # 2 commands × 4 presets
        for pa, pb in zip(sorted(paths_a), sorted(paths_b), strict=True):
            assert pa.read_bytes() == pb.read_bytes(), f"Mismatch: {pa.name}"


class TestGenerateManifest:
    """Tests for generate_manifest()."""

    @pytest.mark.voice
    def test_manifest_json_has_100_entries(self, tmp_path: Path) -> None:
        """Manifest contains exactly 100 entries (20 clean + 80 degraded)."""
        pytest.importorskip("soundfile")
        import numpy as np_mod
        from generate_golden_dataset import generate_manifest

        from music_attribution.voice.degradation import write_audio

        # Create 100 fake FLACs
        fake_audio = np_mod.random.randn(16000).astype(np_mod.float32) * 0.1
        paths = []
        for i in range(1, 21):
            for preset in ["clean", "office", "codec", "noisy_cafe", "extreme"]:
                p = tmp_path / f"cmd_{i:02d}_{preset}.flac"
                write_audio(p, fake_audio)
                paths.append(p)

        manifest = generate_manifest(tmp_path, paths)
        assert len(manifest["files"]) == 100

    @pytest.mark.voice
    def test_manifest_entry_has_required_fields(self, tmp_path: Path) -> None:
        """Each manifest entry has filename, command_id, preset, text, domain_keywords, sha256."""
        pytest.importorskip("soundfile")
        import numpy as np_mod
        from generate_golden_dataset import generate_manifest

        from music_attribution.voice.degradation import write_audio

        fake_audio = np_mod.random.randn(16000).astype(np_mod.float32) * 0.1
        p = tmp_path / "cmd_01_clean.flac"
        write_audio(p, fake_audio)

        manifest = generate_manifest(tmp_path, [p])
        entry = manifest["files"][0]
        required_fields = {"filename", "command_id", "preset", "text", "domain_keywords", "sha256"}
        assert required_fields.issubset(set(entry.keys()))

    @pytest.mark.voice
    def test_manifest_sha256_matches_content(self, tmp_path: Path) -> None:
        """SHA256 in manifest matches actual file hash."""
        pytest.importorskip("soundfile")
        import numpy as np_mod
        from generate_golden_dataset import generate_manifest

        from music_attribution.voice.degradation import write_audio

        fake_audio = np_mod.random.randn(16000).astype(np_mod.float32) * 0.1
        p = tmp_path / "cmd_01_clean.flac"
        write_audio(p, fake_audio)

        manifest = generate_manifest(tmp_path, [p])
        entry = manifest["files"][0]

        actual_sha = hashlib.sha256(p.read_bytes()).hexdigest()
        assert entry["sha256"] == actual_sha


class TestCLIEntryPoint:
    """Tests for main() CLI entry point."""

    @pytest.mark.voice
    def test_cli_runs_without_error(self, tmp_path: Path) -> None:
        """main() with mocked Piper completes with exit code 0."""
        pytest.importorskip("soundfile")
        pytest.importorskip("audiomentations")
        import numpy as np_mod
        from generate_golden_dataset import main

        fake_audio = np_mod.random.randn(16000).astype(np_mod.float32) * 0.1
        with patch(
            "generate_golden_dataset._call_piper_tts",
            return_value=(fake_audio, 22050),
        ):
            main(["--output-dir", str(tmp_path), "--seed", "42"])

        # Should have 100 FLAC files + manifest.json
        flacs = list(tmp_path.glob("*.flac"))
        assert len(flacs) == 100
        manifest_path = tmp_path / "manifest.json"
        assert manifest_path.exists()
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert len(manifest["files"]) == 100
