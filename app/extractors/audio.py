"""
Audio transcription.
"""

import whisper


class AudioExtractor:
    """Convert speech to text."""

    def __init__(self):
        self.model = whisper.load_model("base")

    def extract(self, audio_path: str) -> str:
        try:
            result = self.model.transcribe(audio_path)

            return str(result["text"]).strip()

        except Exception as error:
            raise Exception(f"Audio transcription failed: {error}") from error
