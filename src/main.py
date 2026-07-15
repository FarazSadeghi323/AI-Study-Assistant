from tkinter import Tk
from tkinter.filedialog import askopenfilename

from pdf_reader import (
    get_pdf_page_count,
    extract_text_from_pdf,
)


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

    root = Tk()
    root.withdraw()

    pdf_path = askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )

    root.destroy()

    return pdf_path


def summarize_pdf():

    pdf_path = select_pdf()

    if not pdf_path:
        print("\nNo file selected.\n")
        return

    try:
        print(f"\nSelected file: {pdf_path}")

        import fitz
        doc = fitz.open(pdf_path)
        print(f"Direct page count: {doc.page_count}")
        page_count = get_pdf_page_count(pdf_path)

        pdf_text = extract_text_from_pdf(pdf_path)

        print(f"\nPDF has {page_count} pages.\n")

        print("=" * 50)
        print("PDF Preview")
        print("=" * 50)

        print(pdf_text[:1000])

    except Exception as error:

        print("\n===================================")
        print("Failed to read PDF.")
        print(error)
        print("===================================\n")


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

            print("\nInvalid choice.\n")

        input("Press Enter to continue...")
        print()


if __name__ == "__main__":
    main()