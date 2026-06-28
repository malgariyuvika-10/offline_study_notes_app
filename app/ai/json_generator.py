"""
Generate structured JSON output.
"""

import json


class JSONGenerator:
    """Convert AI output into structured JSON."""

    @staticmethod
    def generate(
        title: str,
        summary: str,
        topics: list,
        flashcards: list
    ) -> dict:

        data = {
            "title": title,
            "summary": summary,
            "topics": topics,
            "flashcards": flashcards
        }

        return data

    @staticmethod
    def save(data: dict, output_path: str):

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )