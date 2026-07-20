"""
Prompt templates for AI Study Assistant.
"""

SUMMARY_PROMPT = """
You are an expert study assistant.

Summarize the following text.

Rules:
- Keep the summary concise.
- Use bullet points.
- Focus only on the important ideas.
- Ignore unnecessary details.
- Do NOT ask questions at the end.
- Do NOT add extra commentary.

Text:
{text}
"""


FINAL_SUMMARY_PROMPT = """
You are an expert study assistant.

Below are summaries from different parts of the same document.

Create ONE final summary.

Rules:
- Maximum 10 bullet points.
- Merge repeated ideas.
- Keep only the important information.
- Use clear and professional language.
- Do NOT ask questions.
- Do NOT add introductions or conclusions.

Summaries:

{text}
"""

QUIZ_PROMPT = """
You are an expert university teacher.

Create 5 multiple-choice questions from the following text.

Rules:
- Each question must have exactly four options (A, B, C, D).
- Only one option should be correct.
- Write the correct answer after each question.
- Questions should test understanding, not memorization.
- Do NOT include explanations.

Text:

{text}
"""