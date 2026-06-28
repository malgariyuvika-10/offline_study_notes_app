"""
Split long text into manageable chunks.
"""

from typing import List


class TextChunker:
    """Chunk text for LLM processing."""

    @staticmethod
    def chunk(text: str, chunk_size: int = 1000) -> List[str]:
        if not text:
            return []

        words = text.split()

        chunks = []

        current_chunk = []

        current_length = 0

        for word in words:

            if current_length + len(word) + 1 <= chunk_size:
                current_chunk.append(word)
                current_length += len(word) + 1
            else:
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]
                current_length = len(word)

        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks