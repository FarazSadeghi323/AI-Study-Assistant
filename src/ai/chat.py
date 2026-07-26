from ai.provider import ask_ai


def chat_with_notes(summary, question):
    """
    Answer a user's question using the PDF summary.
    """

    prompt = f"""
You are an AI study assistant.

Answer ONLY using the information below.

If the answer is not contained in the notes,
say:

"I couldn't find that information in the document."

Document:

{summary}

Question:

{question}

Answer:
"""

    return ask_ai(prompt)