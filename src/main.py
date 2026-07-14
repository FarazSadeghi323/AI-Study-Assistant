# Import the function that PDF information.
from pdf_reader import (
    get_pdf_page_count,
    extract_text_from_pdf,
)

#Display the project title.
def show_banner():
    print("=" * 50)
    print("        AI Study Assistant")
    print("=" * 50)


#Show the main menu options
def show_menu():
    print("\nChoose an option:")
    print("1. Summarize PDF")
    print("2. Generate Quiz")
    print("3. Chat with Notes")
    print("4. Exit")


#Main function that controls the application flow.
def main():
    # Ask the user to enter the PDF file path.
    pdf_path = input("Enter the PDF path: ").strip()

    import fitz

    document = fitz.open(pdf_path)

    print(document)
    print(document.page_count)
    #Get the total number of pages in the selected PDF.
    page_count = get_pdf_page_count(pdf_path)

    #Display the page count to the user.
    print(f"PDF has {page_count} pages.")

    # Extract all text from the PDF.
    pdf_text = extract_text_from_pdf(pdf_path)

    # Display the extracted text.
    print("\n===== PDF Content =====\n")
    
    # Display the first 1000 characters of the extracted text.
    print(pdf_text[:1000])

    input("Press Enter to continue...")

    #Keep the application runing until the user exits.
    while True:
        show_banner()
        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n📄 Summarize PDF feature (Coming Soon)\n")

        elif choice == "2":
            print("\n📝 Quiz Generator (Coming Soon)\n")

        elif choice == "3":
            print("\n🤖 Chat with Notes (Coming Soon)\n")

        elif choice == "4":
            print("\nGoodbye Faraz! 👋")
            break

        else:
            print("\n❌ Invalid choice!\n")

        input("Press Enter to continue...")
        print()


if __name__ == "__main__":
    main()