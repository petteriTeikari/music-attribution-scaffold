"""Tests for Splink probabilistic record linkage."""

from __future__ import annotations

import pytest

from music_attribution.resolution.splink_linkage import SplinkMatcher


@pytest.fixture
def matcher() -> SplinkMatcher:
    """Create a SplinkMatcher."""
    return SplinkMatcher()


class TestSplinkMatcher:
    """Tests for Splink probabilistic record linkage."""

    def test_fellegi_sunter_parameter_estimation(self, matcher) -> None:
        """Test that parameters are estimated from data."""
        import pandas as pd

        records = pd.DataFrame({
            "unique_id": [1, 2, 3, 4],
            "canonical_name": ["The Beatles", "Beatles", "The Rolling Stones", "Rolling Stones"],
            "source": ["MUSICBRAINZ", "DISCOGS", "MUSICBRAINZ", "DISCOGS"],
            "isrc": ["GBAYE0601690", "GBAYE0601690", "GBAYE0601691", "GBAYE0601691"],
        })
        matcher.configure_model(["canonical_name", "isrc"])
        matcher.estimate_parameters(records)
        assert matcher._model_configured

    def test_predict_returns_valid_pairs(self, matcher) -> None:
        """Test that predict returns valid pair comparisons with correct columns."""
        import pandas as pd

        records = pd.DataFrame({
            "unique_id": range(20),
            "canonical_name": [f"Artist {i % 5}" for i in range(20)],
            "source": ["MUSICBRAINZ"] * 10 + ["DISCOGS"] * 10,
            "isrc": [f"ISRC{i % 5:04d}" for i in range(20)],
        })
        matcher.configure_model(["canonical_name", "isrc"])
        matcher.estimate_parameters(records)
        predictions = matcher.predict(records)
        # Predictions should have the required columns
        assert "unique_id_l" in predictions.columns
        assert "unique_id_r" in predictions.columns
        assert "match_probability" in predictions.columns
        # Should have at most N*(N-1)/2 pairs
        assert len(predictions) <= 20 * 19 / 2

    def test_linkage_score_calibrated(self, matcher) -> None:
        """Test that match probabilities are between 0 and 1."""
        import pandas as pd

        records = pd.DataFrame({
            "unique_id": [1, 2],
            "canonical_name": ["The Beatles", "The Beatles"],
            "source": ["MUSICBRAINZ", "DISCOGS"],
            "isrc": ["GBAYE0601690", "GBAYE0601690"],
        })
        matcher.configure_model(["canonical_name", "isrc"])
        matcher.estimate_parameters(records)
        predictions = matcher.predict(records)
        if len(predictions) > 0:
            assert all(0 <= p <= 1 for p in predictions["match_probability"])

    def test_cluster_threshold_configurable(self, matcher) -> None:
        """Test that clustering threshold can be configured."""
        import pandas as pd

        predictions = pd.DataFrame({
            "unique_id_l": [1, 1],
            "unique_id_r": [2, 3],
            "match_probability": [0.95, 0.50],
        })
        clusters_high = matcher.cluster(predictions, threshold=0.9)
        clusters_low = matcher.cluster(predictions, threshold=0.3)
        # Lower threshold should produce fewer but larger clusters
        assert len(clusters_high) >= len(clusters_low)

    def test_handles_missing_fields_in_comparison(self, matcher) -> None:
        """Test that missing fields don't cause errors."""
        import pandas as pd

        records = pd.DataFrame({
            "unique_id": [1, 2],
            "canonical_name": ["Artist A", "Artist A"],
            "source": ["MUSICBRAINZ", "DISCOGS"],
            "isrc": [None, "GBAYE0601690"],
        })
        matcher.configure_model(["canonical_name", "isrc"])
        matcher.estimate_parameters(records)
        # Should not raise
        predictions = matcher.predict(records)
        assert isinstance(predictions, pd.DataFrame)
