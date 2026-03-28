def main():
    while True:
        print("\nAssignment 04 Menu")
        print("1. Bank project")
        print("2. Chess project")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            from bank import run_bank_examples
            print()
            run_bank_examples()
        elif choice == "2":
            from chess_tournament import run_chess_examples
            print()
            run_chess_examples()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
