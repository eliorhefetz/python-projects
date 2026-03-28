from tournament_manager import TournamentManager
from storage import save_data, load_data
from utils import read_int, read_non_empty_text


def show_players(manager):
    if not manager.players:
        print("No players found.")
        return
    for player in manager.get_rankings():
        print(
            f"ID: {player.player_id} | Name: {player.name} | "
            f"W: {player.wins} L: {player.losses} D: {player.draws} | Points: {player.points}"
        )


def main():
    manager = TournamentManager()
    while True:
        print("\nTournament Manager")
        print("1. Add player")
        print("2. Update player")
        print("3. Remove player")
        print("4. Record match")
        print("5. Show rankings")
        print("6. Search players")
        print("7. Save")
        print("8. Load")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()
        try:
            if choice == "1":
                manager.add_player(read_int("Enter player ID: ", 1), read_non_empty_text("Enter player name: "))
                print("Player added successfully.")
            elif choice == "2":
                manager.update_player(read_int("Enter player ID: ", 1), read_non_empty_text("Enter new name: "))
                print("Player updated successfully.")
            elif choice == "3":
                manager.remove_player(read_int("Enter player ID: ", 1))
                print("Player removed successfully.")
            elif choice == "4":
                manager.record_match(
                    read_int("Enter first player ID: ", 1),
                    read_int("Enter second player ID: ", 1),
                    read_non_empty_text("Enter result (1 / 2 / draw): "),
                )
                print("Match recorded successfully.")
            elif choice == "5":
                show_players(manager)
            elif choice == "6":
                keyword = read_non_empty_text("Enter search keyword: ")
                results = manager.search_players(keyword)
                if not results:
                    print("No matching players found.")
                else:
                    for player in results:
                        print(f"ID: {player.player_id} | Name: {player.name}")
            elif choice == "7":
                save_data("tournament_data.json", manager.players, manager.matches)
                print("Data saved successfully.")
            elif choice == "8":
                manager.players, manager.matches = load_data("tournament_data.json")
                print("Data loaded successfully.")
            elif choice == "9":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
