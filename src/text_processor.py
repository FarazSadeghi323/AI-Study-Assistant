"""
Text processing utilities for AI Study Assistant.
"""


def split_text(text: str, chunk_size: int = 1000) -> list[str]:
    """
    Split a long text into smaller chunks.

    Args:
        text: Input text.
        chunk_size: Maximum number of characters per chunk.

    Returns:
        A list of text chunks.
    """

    chunks = []

    for index in range(0, len(text), chunk_size):
        chunks.append(text[index:index + chunk_size])

    return chunks