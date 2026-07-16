"""
AI summarization utilities for AI Study Assistant.
"""

from ai.provider import ask_ai


def summarize_text(text: str) -> str:
    """
    Generate a summary of the given text using Gemma 3.

    Args:
        text: Input text.

    Returns:
        AI-generated summary.
    """

    prompt = f"""
You are an expert study assistant.

Your task is to summarize the following text.

Instructions:
- Write a concise summary.
- Use bullet points.
- Focus only on the important ideas.
- Remove unnecessary details.
- Keep technical terms when necessary.

Text:
{text}
"""

    return ask_ai(prompt)