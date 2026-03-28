def main() -> None:
    while True:
        print("\nAssignment 03 Menu")
        print("1. Store project")
        print("2. Factory project")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            from store import run_store_examples
            print()
            run_store_examples()
        elif choice == "2":
            from factory import run_factory_examples
            print()
            run_factory_examples()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
