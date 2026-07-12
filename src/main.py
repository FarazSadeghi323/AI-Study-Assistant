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


def main():
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