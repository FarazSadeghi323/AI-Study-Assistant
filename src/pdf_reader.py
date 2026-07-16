"""
PDF reading utilities for AI Study Assistant.
"""

import fitz


def get_pdf_page_count(pdf_path: str) -> int:
    """
    Return the total number of pages in a PDF file.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        Total number of pages.
    """

    with fitz.open(pdf_path) as document:
        return document.page_count


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract all text from a PDF file.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        All extracted text from the PDF.
    """

    with fitz.open(pdf_path) as document:
        text = ""

        for page in document:
            text += page.get_text()

    return text