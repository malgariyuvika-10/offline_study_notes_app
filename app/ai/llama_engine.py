"""
TinyLlama inference engine using llama-cpp-python.
"""

from llama_cpp import Llama
from app.backend.config import LLAMA_MODEL_PATH


class LlamaEngine:
    """Handles TinyLlama inference."""

    def __init__(self):
        self.model = Llama(
            model_path=str(LLAMA_MODEL_PATH),
            n_ctx=2048,
            n_threads=4
        )

    def generate(self, prompt: str) -> str:
        """Generate text using TinyLlama."""

        response = self.model(
            prompt,
            max_tokens=512,
            temperature=0.3,
            stop=["</s>"]
        )

        return response["choices"][0]["text"].strip()