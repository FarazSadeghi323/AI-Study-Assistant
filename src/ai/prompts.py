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

Create {num_questions} multiple-choice questions from the source text.

Difficulty: {difficulty}

Rules:
- Use ONLY information supported by the source text.
- Each question must have exactly four options.
- Options must be labeled A, B, C, D.
- Only one option must be correct.
- Questions should test understanding and reasoning, not simple memorization.
- The difficulty must match the requested level.
- Include a short explanation for why the correct answer is correct.
- Do NOT add introductions.
- Do NOT add conclusions.
- Do NOT ask follow-up questions.

IMPORTANT:
Return the result in EXACTLY this format:

QUESTION 1:
<question>

A) <option>
B) <option>
C) <option>
D) <option>

ANSWER: <A/B/C/D>
EXPLANATION: <short explanation>

QUESTION 2:
<question>

A) <option>
B) <option>
C) <option>
D) <option>

ANSWER: <A/B/C/D>
EXPLANATION: <short explanation>

Continue the same format for all questions.

SOURCE TEXT:

{text}
"""

def flashcard_prompt(text):
    return f"""
You are an expert study assistant.

Create study flashcards from the following text.

Rules:
- Generate exactly 10 flashcards.
- Use this format only:

Q: ...
A: ...

- Keep answers short.
- Do not explain.
- Do not write introductions.
- Do not write conclusions.
- Do not ask follow-up questions.
- Output only the flashcards.

Text:

{text}
"""