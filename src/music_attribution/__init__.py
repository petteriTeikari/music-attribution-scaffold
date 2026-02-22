"""Music Attribution Scaffold.

Open-source research scaffold for music attribution with transparent confidence scoring.
Companion code to Teikari (2026), SSRN No. 6109087.
"""

from __future__ import annotations

from music_attribution import attribution, chat, confidence, mcp, schemas

__version__ = "1.0.0"
__all__ = ["attribution", "chat", "confidence", "mcp", "schemas"]
