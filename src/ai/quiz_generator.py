"""
Quiz generation utilities for AI Study Assistant.
"""

from ai.provider import ask_ai
from ai.prompts import QUIZ_PROMPT


def generate_quiz(text: str) -> str:
    """
    Generate a multiple-choice quiz from text.

    Args:
        text: Input text.

    Returns:
        AI-generated quiz.
    """

    prompt = QUIZ_PROMPT.format(
        text=text
    )

    return ask_ai(prompt)