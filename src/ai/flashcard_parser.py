import re


def parse_flashcards(text):
    """
    Parse AI-generated flashcards.

    Expected format:

    Q: Question
    A: Answer

    Q: Question
    A: Answer
    """

    flashcards = []

    pattern = re.compile(
        r"Q:\s*(.*?)\s*A:\s*(.*?)(?=\n\s*Q:|\Z)",
        re.DOTALL | re.IGNORECASE,
    )

    matches = pattern.findall(text)

    for question, answer in matches:

        question = question.strip()
        answer = answer.strip()

        if not question or not answer:
            continue

        flashcards.append(
            {
                "question": question,
                "answer": answer,
            }
        )

    return flashcards


