"""
PDF text extraction.
"""

import pdfplumber


class PDFExtractor:
    """Extract text from PDF documents."""

    def extract(self, pdf_path: str) -> str:
        text = ""

        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

            return text.strip()

        except Exception as error:
            raise Exception(f"PDF extraction failed: {error}")