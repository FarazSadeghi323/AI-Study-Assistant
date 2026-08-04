from tkinter import Tk
from tkinter.filedialog import askopenfilename

from pdf_info import get_pdf_information
from pdf_processor import process_pdf

from ai.quiz_generator import generate_quiz
from ai.flashcard_generator import generate_flashcards
from ai.chat import chat_with_notes
from file_manager import (
    save_text,
    save_markdown,
)

# ============================
# Cache
# ============================

pdf_cache = {}



def show_banner():
    print("=" * 50)
    print("        AI Study Assistant")
    print("=" * 50)


def show_menu():
    print("\nChoose an option:")
    print("1. Summarize PDF")
    print("2. Generate Quiz")
    print("3. Generate Flashcards")
    print("4. Chat with Notes")
    print("5. Exit")


def select_pdf():
    """
    Open a file picker and return the selected PDF path.
    """

    root = Tk()
    root.withdraw()

    pdf_path = askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )

    root.destroy()

    return pdf_path


def summarize_pdf(pdf_path):
    """
    Read a PDF and generate AI summaries.
    """

    try:

        info = get_pdf_information(pdf_path)

        if pdf_path in pdf_cache:
            data = pdf_cache[pdf_path]
        else:
            data = process_pdf(pdf_path)
            pdf_cache[pdf_path] = data


        chunks = data["chunks"]
        summaries = data["summaries"]
        final_summary = data["final_summary"]

        print("\n" + "=" * 50)
        print("PDF Information")
        print("=" * 50)

        print(f"📄 File Name : {info['file_name']}")
        print(f"📑 Pages     : {info['page_count']}")
        print(f"✍ Author     : {info['author']}")
        print(f"📝 Title      : {info['title']}")
        print(f"💾 Size       : {info['file_size']} MB")
        print(f"🧩 Text Chunks: {len(chunks)}")

        print("\n" + "=" * 50)
        print("PDF Preview")
        print("=" * 50)

        print(chunks[0])

        print("\n" + "=" * 50)
        print("AI Summaries")
        print("=" * 50)

        for index, summary in enumerate(summaries, start=1):
            print(f"\n----- Summary {index} -----\n")
            print(summary)

        print("\n" + "=" * 50)
        print("FINAL SUMMARY")
        print("=" * 50)

        print(final_summary)

        summary_file = save_text(
            "summary.txt",
            final_summary,
        )

        markdown_file = save_markdown(
            "summary.md",
            "AI Study Assistant - Summary",
            final_summary,
        )

        print(f"\n✅ Summary saved to: {summary_file}")
        print(f"✅ Markdown saved to: {markdown_file}")
        info = get_pdf_information(pdf_path)
        return f"""
        PDF Information

        File Name : {info['file_name']}
        Pages     : {info['page_count']}
        Author    : {info['author']}
        Title     : {info['title']}
        Size      : {info['file_size']} MB

        ==================================================

        FINAL SUMMARY

        {final_summary}
        """
    except Exception as error:

        print("\n" + "=" * 50)
        print("Failed to process PDF.")
        print(error)
        print("=" * 50)
        return f"Error:\n\n{error}"


def quiz_pdf(pdf_path):
    """
    Generate a quiz from the final AI summary.
    """

    try:

        print("\nProcessing PDF...\n")

        if pdf_path in pdf_cache:
            data = pdf_cache[pdf_path]
        else:
            data = process_pdf(pdf_path)
            pdf_cache[pdf_path] = data

        final_summary = data["final_summary"]

        print("\nGenerating quiz...\n")

        quiz = generate_quiz(final_summary)

        print("\n" + "=" * 50)
        print("QUIZ")
        print("=" * 50)

        print(quiz)

        quiz_file = save_text(
            "quiz.txt",
            quiz,
        )

        markdown_file = save_markdown(
            "quiz.md",
            "AI Study Assistant - Quiz",
            quiz,
        )

        print(f"\n✅ Quiz saved to: {quiz_file}")
        print(f"✅ Markdown saved to: {markdown_file}")

        info = get_pdf_information(pdf_path)

        return f"""
        PDF Information

        File Name : {info['file_name']}
        Pages     : {info['page_count']}
        Author    : {info['author']}
        Title     : {info['title']}
        Size      : {info['file_size']} MB

        ==================================================

        QUIZ

        {quiz}
        """

    except Exception as error:

        print("\n" + "=" * 50)
        print("Failed to generate quiz.")
        print(error)
        print("=" * 50)
        return f"Error:\n\n{error}"
        


def flashcards_pdf(pdf_path):
    """
    Generate AI flashcards from a PDF.
    """


    try:

        print("\nProcessing PDF...\n")

        if pdf_path in pdf_cache:
            data = pdf_cache[pdf_path]
        else:
            data = process_pdf(pdf_path)
            pdf_cache[pdf_path] = data

        final_summary = data["final_summary"]

        print("\nGenerating flashcards...\n")

        flashcards = generate_flashcards(final_summary)

        print("\n" + "=" * 50)
        print("FLASHCARDS")
        print("=" * 50)

        print(flashcards)

        flashcards_file = save_text(
            "flashcards.txt",
            flashcards,
        )

        markdown_file = save_markdown(
            "flashcards.md",
            "AI Study Assistant - Flashcards",
            flashcards,
        )

        print(f"\n✅ Flashcards saved to: {flashcards_file}")
        print(f"✅ Markdown saved to: {markdown_file}")

        info = get_pdf_information(pdf_path)

        return f"""
        PDF Information

        File Name : {info['file_name']}
        Pages     : {info['page_count']}
        Author    : {info['author']}
        Title     : {info['title']}
        Size      : {info['file_size']} MB

        ==================================================

        FLASHCARDS

        {flashcards}
        """
        
    except Exception as error:

        print("\n" + "=" * 50)
        print("Failed to generate flashcards.")
        print(error)
        print("=" * 50)


def chat_pdf(pdf_path,question):
    """
    Chat with a PDF using its AI-generated summary.
    """
    
    try:

        if pdf_path in pdf_cache:
            data = pdf_cache[pdf_path]
        else:
            data = process_pdf(pdf_path)
            pdf_cache[pdf_path] = data

        final_summary = data["final_summary"]

        answer = chat_with_notes(
            final_summary,
            question,
        )

        info = get_pdf_information(pdf_path)

        return f"""
    PDF Information

    File Name : {info['file_name']}
    Pages     : {info['page_count']}
    Author    : {info['author']}
    Title     : {info['title']}
    Size      : {info['file_size']} MB

    ==================================================

    Question

    {question}

    ==================================================

    Answer

    {answer}
    """

    except Exception as error:

        return f"Error:\n{error}"


def main():

    while True:

        show_banner()

        show_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            summarize_pdf()

        elif choice == "2":

            quiz_pdf()

        elif choice == "3":

            flashcards_pdf()

        elif choice == "4":

            chat_pdf()

        elif choice == "5":

            print("\nGoodbye Faraz! 👋")
            break

        else:

            print("\n❌ Invalid choice.\n")

        input("\nPress Enter to continue...")
        print()


if __name__ == "__main__":
    main()