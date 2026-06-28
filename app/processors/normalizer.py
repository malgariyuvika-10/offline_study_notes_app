"""
Text normalization utilities.
"""

import re


class TextNormalizer:
    """Normalize extracted text."""

    @staticmethod
    def normalize(text: str) -> str:
        if not text:
            return ""

        # Convert to lowercase
        text = text.lower()

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove duplicate spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()