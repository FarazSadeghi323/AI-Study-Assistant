from tkinter import Tk
from tkinter.filedialog import askopenfilename

from pdf_reader import extract_text_from_pdf
from pdf_info import get_pdf_information
from text_processor import split_text
from ai.summarizer import summarize_text


def show_banner():
    print("=" * 50)
    print("        AI Study Assistant")
    print("=" * 50)


def show_menu():
    print("\nChoose an option:")
    print("1. Summarize PDF")
    print("2. Generate Quiz")
    print("3. Chat with Notes")
    print("4. Exit")


def select_pdf():
    """Open a file picker and return the selected PDF path."""

    root = Tk()
    root.withdraw()

    pdf_path = askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )

    root.destroy()

    return pdf_path


def summarize_pdf():
    """Read a PDF and generate an AI summary."""

    pdf_path = select_pdf()

    if not pdf_path:
        print("\nNo file selected.\n")
        return

    try:
        # Read PDF information
        info = get_pdf_information(pdf_path)

        # Extract text
        pdf_text = extract_text_from_pdf(pdf_path)

        # Split into chunks
        chunks = split_text(pdf_text)

        if not chunks:
            print("\nNo readable text found in this PDF.\n")
            return

        # Summarize the first chunk
        first_chunk = chunks[0]
        summary = summarize_text(first_chunk)

        # Display PDF information
        print("\n" + "=" * 50)
        print("PDF Information")
        print("=" * 50)

        print(f"📄 File Name : {info['file_name']}")
        print(f"📑 Pages     : {info['page_count']}")
        print(f"✍ Author     : {info['author']}")
        print(f"📝 Title      : {info['title']}")
        print(f"💾 Size       : {info['file_size']} MB")
        print(f"🧩 Text Chunks: {len(chunks)}")

        # Display AI summary
        print("\n" + "=" * 50)
        print("AI Summary")
        print("=" * 50)

        print(summary)

    except Exception as error:
        print("\n" + "=" * 50)
        print("Failed to process PDF.")
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

            print("\n📝 Quiz Generator (Coming Soon)\n")

        elif choice == "3":

            print("\n🤖 Chat with Notes (Coming Soon)\n")

        elif choice == "4":

            print("\nGoodbye Faraz! 👋")
            break

        else:

            print("\n❌ Invalid choice.\n")

        input("Press Enter to continue...")
        print()


if __name__ == "__main__":
    main()