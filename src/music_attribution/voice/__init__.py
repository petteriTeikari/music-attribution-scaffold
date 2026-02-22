"""Voice agent module for music attribution.

Provides a Pipecat-based voice pipeline that wraps the existing PydanticAI
text agent with speech-to-text and text-to-speech capabilities. All
components are swappable via configuration — open-source defaults ship
out of the box; commercial alternatives are one-line config changes.

Architecture
------------
Transport → Silero VAD → STT → LLM (PydanticAI agent) → TTS → Transport

Modules
-------
config
    ``VoiceConfig`` settings model (single source of truth for all voice config).
pipeline
    Pipecat pipeline factory — assembles the voice loop from config.
persona
    Multi-dimensional persona prompt builder with periodic reinforcement.
tools
    Bridge between PydanticAI domain tools and Pipecat function calling.
server
    FastAPI router for WebSocket voice endpoint.
drift
    Embedding-based persona drift detector (cosine similarity + EWMA).
protocols
    Protocol interfaces for swappable STT/TTS/transport services.
"""
