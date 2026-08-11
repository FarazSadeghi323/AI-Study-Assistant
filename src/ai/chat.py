from ai.provider import ask_ai


def chat_with_notes(summary, question, history=None):
    """
    Answer a user's question using the PDF summary
    and previous conversation history.
    """

    if history is None:
        history = []

    conversation = ""

    for item in history:
        conversation += f"""
User:
{item["question"]}

AI:
{item["answer"]}

"""

    prompt = f"""
You are an AI Study Assistant.

Your job is to answer questions about the document.

IMPORTANT RULES:

1. Use the document information to answer the question.
2. You may also use the conversation history to understand references.
3. If the user says things like:
   - "the second one"
   - "the first one"
   - "that"
   - "this"
   - "it"
   - "the previous one"

   resolve the reference using the conversation history.
4. Do NOT say that information is missing just because the current
   question does not repeat the full context.
5. If the requested information truly does not exist in the document,
   say exactly:

"I couldn't find that information in the document."

DOCUMENT:

{summary}

CONVERSATION HISTORY:

{conversation}

CURRENT QUESTION:

{question}

ANSWER:
"""

    return ask_ai(prompt)