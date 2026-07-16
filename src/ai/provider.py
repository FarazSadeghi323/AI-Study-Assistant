"""
AI provider for AI Study Assistant.

This module handles communication with the local Ollama model.
"""

import ollama

MODEL_NAME = "gemma3:4b"


def ask_ai(prompt: str) -> str:
    """
    Send a prompt to the AI model and return its response.

    Args:
        prompt: User prompt.

    Returns:
        AI response as a string.
    """

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]