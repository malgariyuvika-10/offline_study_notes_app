"""
OCR engine using Tesseract.
"""

from PIL import Image
import pytesseract


class OCREngine:
    """Extract text from images."""

    def extract(self, image_path: str) -> str:
        image = Image.open(image_path)

        text = pytesseract.image_to_string(image)

        return text.strip()