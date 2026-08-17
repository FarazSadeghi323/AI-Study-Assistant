"""
Simple text retrieval utilities for AI Study Assistant.
"""


def retrieve_relevant_chunks(
    chunks: list[str],
    question: str,
    top_k: int = 3,
) -> list[str]:
    """
    Retrieve the most relevant text chunks for a question.

    Args:
        chunks: List of document chunks.
        question: User's question.
        top_k: Maximum number of chunks to return.

    Returns:
        A list of the most relevant chunks.
    """

    if not chunks or not question.strip():
        return []

    stop_words = {
        "what",
        "is",
        "the",
        "a",
        "an",
        "of",
        "in",
        "to",
        "and",
        "or",
        "for",
        "on",
        "with",
        "how",
        "why",
        "when",
        "where",
        "who",
    }

    question_words = {
        word.strip(".,!?;:")
        for word in question.lower().split()
        if word.strip(".,!?;:") not in stop_words
    }

    scored_chunks = []

    for index, chunk in enumerate(chunks):
        chunk_words = set(
            chunk.lower().split()
        )

        score = len(
            question_words & chunk_words
        )

        scored_chunks.append(
            (score, index, chunk)
        )

    scored_chunks.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    relevant_chunks = [
        chunk
        for score, index, chunk in scored_chunks[:top_k]
        if score > 0
    ]

    return relevant_chunks