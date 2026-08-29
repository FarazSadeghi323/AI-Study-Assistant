"""
Text processing utilities for AI Study Assistant.
"""


def split_text(
    text: str,
    chunk_size: int = 800,
    chunk_overlap: int = 200,
) -> list[str]:
    """
    Split long text into smaller overlapping chunks.

    The function tries to keep chunks readable by avoiding
    cutting in the middle of sentences when possible.

    Args:
        text: Input text.
        chunk_size: Maximum approximate number of characters
            in each chunk.
        chunk_overlap: Number of overlapping characters
            between consecutive chunks.

    Returns:
        A list of text chunks.
    """

    if not text.strip():
        return []

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size."
        )

    chunks = []
    text_length = len(text)
    start = 0

    while start < text_length:

        end = min(
            start + chunk_size,
            text_length,
        )

        # Try to avoid cutting in the middle of a sentence.
        if end < text_length:

            sentence_end = max(
                text.rfind(". ", start, end),
                text.rfind("? ", start, end),
                text.rfind("! ", start, end),
                text.rfind("\n", start, end),
            )

            if sentence_end > start:
                end = sentence_end + 1

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= text_length:
            break

        start = end - chunk_overlap

    return chunks