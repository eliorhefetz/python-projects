def main():
    while True:
        print("\nAssignment 05 Menu")
        print("1. Hospital project")
        print("2. Stack exercises")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            from hospital_management import main as hospital_main
            print()
            hospital_main()
        elif choice == "2":
            from stack_exercises import run_stack_examples
            print()
            run_stack_examples()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
