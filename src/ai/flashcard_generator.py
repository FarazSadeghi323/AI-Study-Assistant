from ai.provider import ask_ai
from ai.prompts import flashcard_prompt


def generate_flashcards(text):
    """ 
    Generate study flashcards using AI.
    """
    
    prompt = flashcard_prompt(text)
    
    return ask_ai(prompt)                       