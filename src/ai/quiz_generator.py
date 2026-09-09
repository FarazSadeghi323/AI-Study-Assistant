"""
Quiz generation utilities for AI Study Assistant.
"""

from ai.provider import ask_ai
from ai.prompts import QUIZ_PROMPT


def generate_quiz(
    text: str,
    num_questions: int = 5,
    difficulty: str = "medium",
) -> str:
    """
    Generate a multiple-choice quiz from text.

    Args:
        text: Input text.
        num_questions: Number of questions.
        difficulty: Quiz difficulty.

    Returns:
        AI-generated quiz.
    """

    prompt = QUIZ_PROMPT.format(
        text=text,
        num_questions=num_questions,
        difficulty=difficulty,
    )

    return ask_ai(prompt)