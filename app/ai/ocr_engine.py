"""
OCR engine using Tesseract.
"""

import pytesseract
from PIL import Image


class OCREngine:
    """Extract text from images."""

    def extract(self, image_path: str) -> str:
        image = Image.open(image_path)

        text = pytesseract.image_to_string(image)

        return str(text).strip()