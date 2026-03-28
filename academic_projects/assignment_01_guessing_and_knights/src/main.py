from guessing_game import run_guessing_game
from knights_battle import run_knights_battle


def main() -> None:
    while True:
        print("\nAssignment 01 Menu")
        print("1. Number guessing game")
        print("2. Knights battle")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_guessing_game()
        elif choice == "2":
            run_knights_battle()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
