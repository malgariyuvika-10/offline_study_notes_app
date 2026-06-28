"""
Image OCR extraction.
"""

from PIL import Image
import pytesseract


class ImageExtractor:
    """Extract text from images using OCR."""

    def extract(self, image_path: str) -> str:
        try:
            image = Image.open(image_path)

            text = pytesseract.image_to_string(image)

            return text.strip()

        except Exception as error:
            raise Exception(f"OCR extraction failed: {error}")