"""
AI summarization utilities for AI Study Assistant.
"""

from ai.provider import ask_ai
from ai.prompts import SUMMARY_PROMPT, FINAL_SUMMARY_PROMPT


def summarize_text(text: str) -> str:
    """
    Generate a summary for one chunk.
    """

    prompt = SUMMARY_PROMPT.format(text=text)

    return ask_ai(prompt)


def summarize_chunks(chunks: list[str]) -> list[str]:
    """
    Generate summaries for multiple chunks.
    """

    summaries = []

    chunks = chunks[:3]
    total = len(chunks)

    for index, chunk in enumerate(chunks, start=1):

        print(f"\nSummarizing chunk {index}/{total}...")

        summary = summarize_text(chunk)

        summaries.append(summary)

    return summaries


def summarize_document(summaries: list[str]) -> str:
    """
    Generate one final summary from multiple chunk summaries.
    """

    combined_summary = "\n\n".join(summaries)

    prompt = FINAL_SUMMARY_PROMPT.format(
        text=combined_summary
    )

    print("\nGenerating final summary...\n")

    return ask_ai(prompt)