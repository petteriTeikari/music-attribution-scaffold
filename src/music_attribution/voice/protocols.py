"""Protocol interfaces for swappable voice pipeline components.

Defines structural typing protocols for STT, TTS, and transport services.
Any class that implements these methods is compatible with the pipeline
factory — no inheritance required. This enables zero-refactor provider
swapping.

Example
-------
Writing a custom TTS service::

    class MyCustomTTS:
        async def synthesize(self, text: str) -> bytes:
            return my_tts_engine.speak(text)

        async def close(self) -> None:
            pass


    # MyCustomTTS automatically satisfies TTSServiceProtocol
    # because it has the required methods.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class STTServiceProtocol(Protocol):
    """Protocol for speech-to-text services.

    Any class with a ``transcribe`` method accepting audio bytes
    and returning a string satisfies this protocol.
    """

    async def transcribe(self, audio: bytes) -> str:
        """Convert audio bytes to text transcript.

        Parameters
        ----------
        audio : bytes
            Raw audio data (16kHz, 16-bit PCM).

        Returns
        -------
        str
            Transcribed text.
        """
        ...

    async def close(self) -> None:
        """Release resources held by the service."""
        ...


@runtime_checkable
class TTSServiceProtocol(Protocol):
    """Protocol for text-to-speech services.

    Any class with a ``synthesize`` method accepting text
    and returning audio bytes satisfies this protocol.
    """

    async def synthesize(self, text: str) -> bytes:
        """Convert text to audio bytes.

        Parameters
        ----------
        text : str
            Text to synthesize.

        Returns
        -------
        bytes
            Audio data (format depends on implementation).
        """
        ...

    async def close(self) -> None:
        """Release resources held by the service."""
        ...


@runtime_checkable
class DriftDetectorProtocol(Protocol):
    """Protocol for persona drift detection.

    Any class with a ``score`` method that compares a response
    to the persona reference embedding satisfies this protocol.
    """

    def score(self, response_text: str) -> float:
        """Compute drift score for a response.

        Parameters
        ----------
        response_text : str
            The agent's response text to evaluate.

        Returns
        -------
        float
            Cosine similarity with persona reference (0.0-1.0).
            Higher = more in sync.
        """
        ...

    def state(self) -> str:
        """Return current drift state.

        Returns
        -------
        str
            One of 'sync', 'drift', or 'desync'.
        """
        ...
