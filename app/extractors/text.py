"""
Plain text extraction.
"""


class TextExtractor:
    """Read text files."""

    def extract(self, file_path: str) -> str:
        try:
            with open(file_path, encoding="utf-8") as file:
                text = file.read()

            return text.strip()

        except Exception as error:
            raise Exception(f"Text extraction failed: {error}") from error
