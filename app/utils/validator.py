"""
Validation utilities.
"""

import json


class OutputValidator:
    """
    Validate generated JSON output.
    """

    REQUIRED_FIELDS = ["title", "summary", "topics", "flashcards"]

    @classmethod
    def validate_json(cls, data: dict) -> bool:

        for field in cls.REQUIRED_FIELDS:
            if field not in data:
                return False

        return True

    @staticmethod
    def save_json(data: dict, output_path: str):

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
