"""
Semantic retrieval utilities for AI Study Assistant.
"""

from ai.embeddings import (
    create_embedding,
    cosine_similarity,
)


def retrieve_relevant_chunks(
    chunks: list[str],
    question: str,
    top_k: int = 3,
    min_similarity: float = 0.35,
) -> list[str]:
    """
    Retrieve the most relevant document chunks using
    semantic similarity.

    Args:
        chunks: List of document chunks.
        question: User's question.
        top_k: Maximum number of chunks to return.
        min_similarity: Minimum similarity score required.

    Returns:
        A list of the most relevant document chunks.
    """

    if not chunks or not question.strip():
        return []

    question_embedding = create_embedding(
        question
    )

    scored_chunks = []

    for index, chunk in enumerate(chunks):

        if not chunk.strip():
            continue

        chunk_embedding = create_embedding(
            chunk
        )

        similarity_score = cosine_similarity(
            question_embedding,
            chunk_embedding,
        )

        if similarity_score >= min_similarity:
            scored_chunks.append(
                (
                    similarity_score,
                    index,
                    chunk,
                )
            )

    scored_chunks.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return [
        chunk
        for score, index, chunk
        in scored_chunks[:top_k]
    ]


def retrieve_chunks_with_scores(
    chunks: list[str],
    question: str,
    top_k: int = 3,
) -> list[tuple[float, str]]:
    """
    Retrieve relevant chunks together with
    their semantic similarity scores.
    """

    if not chunks or not question.strip():
        return []

    question_embedding = create_embedding(
        question
    )

    scored_chunks = []

    for chunk in chunks:

        if not chunk.strip():
            continue

        chunk_embedding = create_embedding(
            chunk
        )

        similarity_score = cosine_similarity(
            question_embedding,
            chunk_embedding,
        )

        scored_chunks.append(
            (
                similarity_score,
                chunk,
            )
        )

    scored_chunks.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return scored_chunks[:top_k]