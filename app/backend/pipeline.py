"""
Main processing pipeline for Offline Study Notes AI.
"""

from backend.logger import logger
import re
from collections import Counter
from typing import Dict, List


class StudyNotesPipeline:
    """
    Converts raw unstructured text into structured study notes:
    - Title
    - Summary
    - Key Topics
    """

    def __init__(self):
        logger.info("Study Notes Pipeline initialized")

    def process(self, text: str) -> Dict:
        if not text or not isinstance(text, str):
            logger.warning("Empty or invalid input received")
            return {
                "title": "Untitled Document",
                "summary": "No content available.",
                "topics": []
            }

        cleaned_text = self.clean_text(text)

        return {
            "title": self.generate_title(cleaned_text),
            "summary": self.generate_summary(cleaned_text),
            "topics": self.extract_topics(cleaned_text)
        }

    def clean_text(self, text: str) -> str:
        """
        Normalize whitespace and clean raw text.
        """
        text = re.sub(r'\s+', ' ', text)  # collapse multiple spaces/newlines
        return text.strip()

    def generate_title(self, text: str) -> str:
        """
        Extract first meaningful line or sentence as title.
        """
        # Try line-based title first
        for line in text.split("\n"):
            line = line.strip()
            if line:
                return line[:90]

        # Fallback: first sentence
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for s in sentences:
            if s.strip():
                return s.strip()[:90]

        return "Untitled Document"

    def generate_summary(self, text: str) -> str:
        """
        Create a short 2–3 sentence summary.
        """
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]

        if not sentences:
            return "No summary available."

        return " ".join(sentences[:3])

    def extract_topics(self, text: str) -> List[str]:
        """
        Extract most frequent meaningful keywords.
        """

        words = re.findall(r"\b[a-zA-Z]{5,}\b", text.lower())

        stopwords = {
            "which", "there", "their", "about", "would",
            "could", "should", "these", "those", "using",
            "study", "notes", "because", "where", "while",
            "this", "that", "with", "from", "have", "been",
            "they", "them", "then", "into", "over"
        }

        # Filter words
        filtered_words = [
            w for w in words
            if w not in stopwords and len(w) >= 5
        ]

        if not filtered_words:
            return []

        freq = Counter(filtered_words)

        # Most common topics first
        topics = [word for word, _ in freq.most_common(8)]

        return [t.title() for t in topics]