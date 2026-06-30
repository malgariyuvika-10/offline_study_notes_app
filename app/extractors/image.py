"""
Image OCR extraction.
"""

import pytesseract
from PIL import Image


class ImageExtractor:
    """Extract text from images using OCR."""

    def extract(self, image_path: str) -> str:
        try:
            image = Image.open(image_path)

            text = pytesseract.image_to_string(image)

            return str(text).strip()

        except Exception as error:
            raise Exception(f"OCR extraction failed: {error}") from error