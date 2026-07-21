from tkinter import Tk
from tkinter.filedialog import askopenfilename

from pdf_reader import extract_text_from_pdf
from pdf_info import get_pdf_information
from text_processor import split_text

from ai.summarizer import (
    summarize_chunks,
    summarize_document,
)

from ai.quiz_generator import generate_quiz
from ai.flashcard_generator import generate_flashcards


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


def summarize_pdf():
    """
    Read a PDF and generate AI summaries.
    """

    pdf_path = select_pdf()

    if not pdf_path:
        print("\nNo file selected.\n")
        return

    try:

        info = get_pdf_information(pdf_path)

        pdf_text = extract_text_from_pdf(pdf_path)

        chunks = split_text(pdf_text)

        if not chunks:
            print("\nNo readable text found.\n")
            return

        summaries = summarize_chunks(chunks)

        final_summary = summarize_document(summaries)

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

    except Exception as error:

        print("\n" + "=" * 50)
        print("Failed to process PDF.")
        print(error)
        print("=" * 50)


def quiz_pdf():
    """
    Generate a quiz from the final AI summary.
    """

    pdf_path = select_pdf()

    if not pdf_path:
        print("\nNo file selected.\n")
        return

    try:

        pdf_text = extract_text_from_pdf(pdf_path)

        chunks = split_text(pdf_text)

        if not chunks:
            print("\nNo readable text found.\n")
            return

        print("\nGenerating summaries...\n")

        summaries = summarize_chunks(chunks)

        final_summary = summarize_document(summaries)

        print("\nGenerating quiz...\n")

        quiz = generate_quiz(final_summary)

        print("\n" + "=" * 50)
        print("QUIZ")
        print("=" * 50)

        print(quiz)

    except Exception as error:

        print("\n" + "=" * 50)
        print("Failed to generate quiz.")
        print(error)
        print("=" * 50)


def flashcards_pdf():
    """
    Generate AI flashcards from a PDF.
    """

    pdf_path = select_pdf()

    if not pdf_path:
        print("\nNo file selected.\n")
        return

    try:

        pdf_text = extract_text_from_pdf(pdf_path)

        chunks = split_text(pdf_text)

        if not chunks:
            print("\nNo readable text found.\n")
            return

        print("\nGenerating summaries...\n")

        summaries = summarize_chunks(chunks)

        final_summary = summarize_document(summaries)

        print("\nGenerating flashcards...\n")

        flashcards = generate_flashcards(final_summary)

        print("\n" + "=" * 50)
        print("FLASHCARDS")
        print("=" * 50)

        print(flashcards)

    except Exception as error:

        print("\n" + "=" * 50)
        print("Failed to generate flashcards.")
        print(error)
        print("=" * 50)


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

            print("\n🤖 Chat with Notes (Coming Soon)\n")

        elif choice == "5":

            print("\nGoodbye Faraz! 👋")
            break

        else:

            print("\n❌ Invalid choice.\n")

        input("\nPress Enter to continue...")
        print()


if __name__ == "__main__":
    main()