"""
Embedding utilities for AI Study Assistant.

This module creates vector embeddings using a local Ollama
embedding model.
"""

import ollama


EMBEDDING_MODEL = "nomic-embed-text"


def create_embedding(text: str) -> list[float]:
    """
    Create a vector embedding for a text.

    Args:
        text: Input text.

    Returns:
        A list of floating-point embedding values.
    """

    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=text,
    )

    return response["embeddings"][0]

def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    """
    Calculate cosine similarity between two vectors.
    """

    dot_product = sum(
        a * b
        for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = sum(
        a * a
        for a in vector_a
    ) ** 0.5

    magnitude_b = sum(
        b * b
        for b in vector_b
    ) ** 0.5

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (
        magnitude_a * magnitude_b
    )

