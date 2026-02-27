"""Tests for golden commands corpus."""

from __future__ import annotations

from music_attribution.voice.golden_commands import GOLDEN_COMMANDS


class TestGoldenCommands:
    """Tests for GOLDEN_COMMANDS corpus."""

    def test_golden_commands_has_20_entries(self) -> None:
        """Corpus has exactly 20 commands."""
        assert len(GOLDEN_COMMANDS) == 20

    def test_golden_command_ids_unique(self) -> None:
        """All command IDs are unique."""
        ids = [cmd["id"] for cmd in GOLDEN_COMMANDS]
        assert len(ids) == len(set(ids))

    def test_golden_command_ids_sequential(self) -> None:
        """IDs are cmd_01 through cmd_20."""
        expected = [f"cmd_{i:02d}" for i in range(1, 21)]
        actual = [cmd["id"] for cmd in GOLDEN_COMMANDS]
        assert actual == expected

    def test_golden_commands_have_required_fields(self) -> None:
        """Each entry has: id, text, category, domain_keywords, expected_action."""
        required = {"id", "text", "category", "domain_keywords", "expected_action"}
        for cmd in GOLDEN_COMMANDS:
            assert required.issubset(cmd.keys()), f"Missing fields in {cmd.get('id', '?')}"

    def test_golden_commands_categories(self) -> None:
        """All categories are 'query' or 'action'."""
        for cmd in GOLDEN_COMMANDS:
            assert cmd["category"] in {"query", "action"}, f"Bad category in {cmd['id']}"

    def test_golden_commands_domain_keywords_nonempty(self) -> None:
        """Each command has at least 2 domain keywords."""
        for cmd in GOLDEN_COMMANDS:
            assert len(cmd["domain_keywords"]) >= 2, f"Too few keywords in {cmd['id']}"

    def test_golden_commands_text_nonempty(self) -> None:
        """Each command text is non-empty with len > 10."""
        for cmd in GOLDEN_COMMANDS:
            assert len(cmd["text"]) > 10, f"Text too short in {cmd['id']}"
