"""
Format structured AI output.
"""

import json


class OutputFormatter:
    """Format processed results."""

    @staticmethod
    def to_json(
        title: str,
        summary: str,
        topics: list,
        flashcards: list
    ) -> str:

        data = {
            "title": title,
            "summary": summary,
            "topics": topics,
            "flashcards": flashcards
        }

        return json.dumps(data, indent=4, ensure_ascii=False)