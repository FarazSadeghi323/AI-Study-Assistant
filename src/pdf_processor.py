"""
PDF processing utilities for AI Study Assistant.
"""

from pdf_reader import extract_text_from_pdf
from text_processor import split_text

from ai.summarizer import (
    summarize_chunks,
    summarize_document,
)


def process_pdf(pdf_path):
    """
    Read a PDF and return all processed data.

    Returns:
        dict containing:
        - text
        - chunks
        - summaries
        - final_summary
    """

    pdf_text = extract_text_from_pdf(pdf_path)

    chunks = split_text(pdf_text)

    if not chunks:
        raise ValueError("No readable text found.")

    summaries = summarize_chunks(chunks)

    final_summary = summarize_document(summaries)

    return {
        "text": pdf_text,
        "chunks": chunks,
        "summaries": summaries,
        "final_summary": final_summary,
    }