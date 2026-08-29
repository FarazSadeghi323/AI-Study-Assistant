from ai.provider import ask_ai
from ai.retriever import retrieve_relevant_chunks


def chat_with_notes(summary, chunks, question, history=None):
    """
    Answer a user's question using the PDF summary,
    relevant document sections, and conversation history.
    """

    if history is None:
        history = []

    # -----------------------------
    # Build retrieval query
    # -----------------------------

    retrieval_query = question

    if history:

        previous_question = history[-1]["question"]
        previous_answer = history[-1]["answer"]

        retrieval_query = f"""
Previous question:
{previous_question}

Previous answer:
{previous_answer}

Follow-up question:
{question}
"""

    # -----------------------------
    # Retrieve relevant chunks
    # -----------------------------

    relevant_chunks = retrieve_relevant_chunks(
        chunks,
        retrieval_query,
        top_k=3,
    )

    conversation = ""
    retrieved_context = "\n\n".join(
        relevant_chunks
    )

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
   - "explain that"
   - "explain it"

   resolve the reference using the conversation history.
4. Do NOT say that information is missing just because the current
   question does not repeat the full context.
5. If the requested information truly does not exist in the document,
   say exactly:

"I couldn't find that information in the document."

6. If the user asks for a simpler explanation, example,
   clarification, or more detail about a previous answer,
   do not simply repeat the previous answer.

   Instead, explain the same idea in the requested way.

   If the user asks for an example, create a simple example
   that helps explain the idea.

7. Keep examples simple and directly related to the previous topic.

RELEVANT DOCUMENT SECTIONS:

{retrieved_context}

DOCUMENT SUMMARY:

{summary}

CONVERSATION HISTORY:

{conversation}

CURRENT QUESTION:

{question}

ANSWER:
"""

    return ask_ai(prompt)