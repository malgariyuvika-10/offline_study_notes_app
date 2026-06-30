"""
Speech-to-text engine.
"""

import whisper


class WhisperEngine:
    """Handles audio transcription."""

    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, audio_path: str) -> str:
        """Convert audio to text."""

        result = self.model.transcribe(audio_path)

        return result["text"]
