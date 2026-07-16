"""
PDF information utilities for AI Study Assistant.
"""

import os
import fitz


def get_pdf_information(pdf_path: str) -> dict:
    """
    Return basic information about a PDF file.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        A dictionary containing:
        - file_name
        - page_count
        - title
        - author
        - file_size (MB)
    """

    with fitz.open(pdf_path) as document:
        metadata = document.metadata

        return {
            "file_name": os.path.basename(pdf_path),
            "page_count": document.page_count,
            "title": metadata.get("title") or "Unknown",
            "author": metadata.get("author") or "Unknown",
            "file_size": round(
                os.path.getsize(pdf_path) / (1024 * 1024),
                2,
            ),
        }