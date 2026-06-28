"""
Text cleaning utilities.
"""

import re


class TextCleaner:
    """Clean extracted text."""

    @staticmethod
    def clean(text: str) -> str:
        if not text:
            return ""

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n+", "\n", text)

        # Remove unwanted characters
        text = re.sub(r"[^\w\s.,!?():;\"'-]", "", text)

        return text.strip()