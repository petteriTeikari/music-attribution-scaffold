"""Golden voice command corpus for STT regression testing.

Contains 20 domain-specific voice commands spanning music attribution
queries, actions, corrections, and confidence reporting.
"""

from __future__ import annotations

from typing import Any

GOLDEN_COMMANDS: list[dict[str, Any]] = [
    {
        "id": "cmd_01",
        "text": "Attribution saved for Headlock",
        "category": "action",
        "domain_keywords": ["attribution", "saved", "headlock"],
        "expected_action": "save_attribution",
    },
    {
        "id": "cmd_02",
        "text": "Confidence updated to 0.87",
        "category": "action",
        "domain_keywords": ["confidence", "updated"],
        "expected_action": "update_confidence",
    },
    {
        "id": "cmd_03",
        "text": "Three tracks queued for review",
        "category": "action",
        "domain_keywords": ["tracks", "queued", "review"],
        "expected_action": "queue_review",
    },
    {
        "id": "cmd_04",
        "text": "Found 12 results for Imogen Heap",
        "category": "query",
        "domain_keywords": ["results", "imogen", "heap"],
        "expected_action": "search_results",
    },
    {
        "id": "cmd_05",
        "text": "Permission denied, AI training requires artist consent",
        "category": "action",
        "domain_keywords": ["permission", "training", "artist", "consent"],
        "expected_action": "deny_permission",
    },
    {
        "id": "cmd_06",
        "text": "Search for tracks by Frou Frou",
        "category": "query",
        "domain_keywords": ["search", "tracks", "frou"],
        "expected_action": "search_tracks",
    },
    {
        "id": "cmd_07",
        "text": "Assurance level upgraded to A2",
        "category": "action",
        "domain_keywords": ["assurance", "level", "upgraded"],
        "expected_action": "upgrade_assurance",
    },
    {
        "id": "cmd_08",
        "text": "MusicBrainz and Discogs sources agree",
        "category": "query",
        "domain_keywords": ["musicbrainz", "discogs", "sources", "agree"],
        "expected_action": "check_agreement",
    },
    {
        "id": "cmd_09",
        "text": "Low confidence warning for track seven",
        "category": "query",
        "domain_keywords": ["confidence", "warning", "track"],
        "expected_action": "low_confidence_alert",
    },
    {
        "id": "cmd_10",
        "text": "Batch review complete, 15 of 20 approved",
        "category": "action",
        "domain_keywords": ["batch", "review", "complete", "approved"],
        "expected_action": "batch_review_complete",
    },
    {
        "id": "cmd_11",
        "text": "What is the confidence score for Hide and Seek?",
        "category": "query",
        "domain_keywords": ["confidence", "score", "hide", "seek"],
        "expected_action": "query_confidence",
    },
    {
        "id": "cmd_12",
        "text": "Show me low confidence attributions",
        "category": "query",
        "domain_keywords": ["low", "confidence", "attributions"],
        "expected_action": "filter_low_confidence",
    },
    {
        "id": "cmd_13",
        "text": "The songwriter should be Imogen Heap",
        "category": "action",
        "domain_keywords": ["songwriter", "imogen", "heap"],
        "expected_action": "correct_songwriter",
    },
    {
        "id": "cmd_14",
        "text": "I rate this attribution nine out of ten",
        "category": "action",
        "domain_keywords": ["rate", "attribution", "nine", "ten"],
        "expected_action": "rate_attribution",
    },
    {
        "id": "cmd_15",
        "text": "Correct the artist name to Frou Frou",
        "category": "action",
        "domain_keywords": ["correct", "artist", "frou"],
        "expected_action": "correct_artist",
    },
    {
        "id": "cmd_16",
        "text": "What does assurance level A2 mean?",
        "category": "query",
        "domain_keywords": ["assurance", "level", "mean"],
        "expected_action": "explain_assurance",
    },
    {
        "id": "cmd_17",
        "text": "Export attribution report for this album",
        "category": "action",
        "domain_keywords": ["export", "attribution", "report", "album"],
        "expected_action": "export_report",
    },
    {
        "id": "cmd_18",
        "text": "Compare confidence across all tracks",
        "category": "query",
        "domain_keywords": ["compare", "confidence", "tracks"],
        "expected_action": "compare_confidence",
    },
    {
        "id": "cmd_19",
        "text": "Flag this attribution for manual review",
        "category": "action",
        "domain_keywords": ["flag", "attribution", "manual", "review"],
        "expected_action": "flag_for_review",
    },
    {
        "id": "cmd_20",
        "text": "Cancel the last correction",
        "category": "action",
        "domain_keywords": ["cancel", "last", "correction"],
        "expected_action": "cancel_correction",
    },
]
