import random


def addPlayer(players):
    name = read_non_empty_text("Enter player name: ")
    power = read_non_negative_integer("Enter power rating: ")
    wins = read_non_negative_integer("Enter number of wins: ")
    losses = read_non_negative_integer("Enter number of losses: ")

    players[name] = [power, wins, losses]
    return players


def removePlayer(players, name):
    if name in players:
        del players[name]
    return players


def Game(players):
    names = list(players.keys())

    if len(names) < 2:
        return players

    player_1, player_2 = random.sample(names, 2)
    winner = random.choice([player_1, player_2])

    if winner == player_1:
        players[player_1][1] += 1
        players[player_2][2] += 1
    else:
        players[player_2][1] += 1
        players[player_1][2] += 1

    return players


def sortPlayers(players):
    names = list(players.keys())

    for i in range(1, len(names)):
        key = names[i]
        j = i - 1
        while j >= 0 and players[names[j]][0] > players[key][0]:
            names[j + 1] = names[j]
            j -= 1
        names[j + 1] = key

    return names


def bestPlayer(players):
    names = list(players.keys())
    if len(names) == 0:
        return "No players"
    return _bestPlayer_recursive(players, names, 0, names[0])


def _bestPlayer_recursive(players, names, index, best_name):
    if index == len(names):
        return best_name
    if players[names[index]][0] > players[best_name][0]:
        best_name = names[index]
    return _bestPlayer_recursive(players, names, index + 1, best_name)


def countPlayers(players):
    names = list(players.keys())
    return _countPlayers_recursive(names, 0)


def _countPlayers_recursive(names, index):
    if index == len(names):
        return 0
    return 1 + _countPlayers_recursive(names, index + 1)


def countGames(players):
    names = list(players.keys())
    return _countGames_recursive(players, names, 0) // 2


def _countGames_recursive(players, names, index):
    if index == len(names):
        return 0
    wins = players[names[index]][1]
    losses = players[names[index]][2]
    return wins + losses + _countGames_recursive(players, names, index + 1)


def findPlayer(name, players):
    if name not in players:
        return "Player not found"
    return _findPlayer_recursive(players[name], 0)


def _findPlayer_recursive(details, index):
    labels = ["Power", "Wins", "Losses"]
    if index == len(details):
        return []
    return [f"{labels[index]}: {details[index]}"] + _findPlayer_recursive(details, index + 1)


def read_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty.")


def read_non_negative_integer(prompt):
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if value < 0:
            print("Value cannot be negative.")
            continue

        return value


def run_chess_examples():
    players = {
        "Elior": [3500, 40, 0],
        "Eli": [2800, 25, 6],
        "Or": [3100, 18, 4],
    }

    print("Game result:", Game(players.copy()))
    print("Sorted players:", sortPlayers(players))
    print("Best player:", bestPlayer(players))
    print("Players count:", countPlayers(players))
    print("Games count:", countGames(players))
    print("Find Elior:", findPlayer("Elior", players))
    print("Remove Or:", removePlayer(players.copy(), "Or"))


if __name__ == "__main__":
    run_chess_examples()
