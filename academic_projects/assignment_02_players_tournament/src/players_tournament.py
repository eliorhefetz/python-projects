import random


SPECIAL_EXTRA_HP = "extra hp"
SPECIAL_EXTRA_ATTACK = "extra attack"


def create_player(name, attack_points, defense, hp, special, wins=0):
    cleaned_name = name.strip()
    cleaned_special = special.strip().lower()

    if not cleaned_name:
        raise ValueError("Player name cannot be empty.")
    if attack_points <= 0:
        raise ValueError("Attack points must be greater than 0.")
    if defense < 0:
        raise ValueError("Defense cannot be negative.")
    if hp <= 0:
        raise ValueError("HP must be greater than 0.")
    if cleaned_special not in {SPECIAL_EXTRA_HP, SPECIAL_EXTRA_ATTACK}:
        raise ValueError("Special must be 'extra hp' or 'extra attack'.")
    if wins < 0:
        raise ValueError("Wins cannot be negative.")

    return {
        "name": cleaned_name,
        "attack": attack_points,
        "defense": defense,
        "hp": hp,
        "special": cleaned_special,
        "wins": wins,
    }


def add_player(players_list, name, attack_points, defense, hp, special, wins=0):
    if find_player(players_list, name) is not None:
        raise ValueError(f"Player '{name}' already exists.")

    player = create_player(name, attack_points, defense, hp, special, wins)
    players_list.append(player)
    return players_list


def find_player(players_list, name):
    for player in players_list:
        if player["name"].lower() == name.strip().lower():
            return player
    return None


def show_details(players_list, name):
    player = find_player(players_list, name)
    if player is None:
        return None

    return {
        "name": player["name"],
        "attack": player["attack"],
        "defense": player["defense"],
        "hp": player["hp"],
        "special": player["special"],
        "wins": player["wins"],
    }


def strongest_player(players_list):
    if not players_list:
        return None
    return max(players_list, key=lambda player: player["attack"])["name"]


def best_player(players_list):
    if not players_list:
        return None
    return max(players_list, key=lambda player: player["wins"])["name"]


def add_victory(players_list, name):
    player = find_player(players_list, name)
    if player is None:
        raise ValueError(f"Player '{name}' was not found.")
    player["wins"] += 1
    return players_list


def add_hp(players_list, name, amount=10):
    player = find_player(players_list, name)
    if player is None:
        raise ValueError(f"Player '{name}' was not found.")
    if amount <= 0:
        raise ValueError("HP amount must be greater than 0.")

    player["hp"] += amount
    return players_list


def add_attack(players_list, name, amount=10):
    player = find_player(players_list, name)
    if player is None:
        raise ValueError(f"Player '{name}' was not found.")
    if amount <= 0:
        raise ValueError("Attack amount must be greater than 0.")

    player["attack"] += amount
    return players_list


def attack(players_list, attacker_name, defender_name):
    attacker = find_player(players_list, attacker_name)
    defender = find_player(players_list, defender_name)

    if attacker is None:
        raise ValueError(f"Attacker '{attacker_name}' was not found.")
    if defender is None:
        raise ValueError(f"Defender '{defender_name}' was not found.")
    if attacker["name"] == defender["name"]:
        raise ValueError("A player cannot attack themselves.")

    damage = attacker["attack"]
    original_defense = defender["defense"]

    if defender["defense"] >= damage:
        defender["defense"] -= damage
        hp_damage = 0
    else:
        hp_damage = damage - defender["defense"]
        defender["defense"] = 0
        defender["hp"] = max(defender["hp"] - hp_damage, 0)

    return {
        "attacker": attacker["name"],
        "defender": defender["name"],
        "damage": damage,
        "defense_before": original_defense,
        "defense_after": defender["defense"],
        "hp_after": defender["hp"],
        "hp_damage": hp_damage,
    }


def is_alive(players_list, name):
    player = find_player(players_list, name)
    if player is None:
        raise ValueError(f"Player '{name}' was not found.")
    return player["hp"] > 0


def apply_special(players_list, name):
    player = find_player(players_list, name)
    if player is None:
        raise ValueError(f"Player '{name}' was not found.")

    if player["special"] == SPECIAL_EXTRA_HP:
        add_hp(players_list, name)
        return f"{player['name']} used special move and gained 10 HP."
    if player["special"] == SPECIAL_EXTRA_ATTACK:
        add_attack(players_list, name)
        return f"{player['name']} used special move and gained 10 attack."

    raise ValueError("Unknown special move.")


def battle(players_list, name1, name2, random_generator=None):
    if len(players_list) < 2:
        raise ValueError("At least two players are required for a battle.")
    if name1.strip().lower() == name2.strip().lower():
        raise ValueError("A player cannot battle themselves.")

    if not is_alive(players_list, name1):
        raise ValueError(f"Player '{name1}' is not alive.")
    if not is_alive(players_list, name2):
        raise ValueError(f"Player '{name2}' is not alive.")

    rng = random_generator if random_generator is not None else random
    battle_log = []
    round_number = 0

    while is_alive(players_list, name1) and is_alive(players_list, name2):
        round_number += 1
        action = rng.randint(0, 3)

        if action == 0:
            details = attack(players_list, name1, name2)
            action_text = f"{name1} attacked {name2}"
        elif action == 1:
            action_text = apply_special(players_list, name1)
            details = None
        elif action == 2:
            details = attack(players_list, name2, name1)
            action_text = f"{name2} attacked {name1}"
        else:
            action_text = apply_special(players_list, name2)
            details = None

        first_player = find_player(players_list, name1)
        second_player = find_player(players_list, name2)

        battle_log.append(
            {
                "round": round_number,
                "action": action_text,
                "details": details,
                "player_1_hp": first_player["hp"],
                "player_2_hp": second_player["hp"],
            }
        )

    winner = name1 if is_alive(players_list, name1) else name2
    loser = name2 if winner == name1 else name1

    add_victory(players_list, winner)

    for index, player in enumerate(players_list):
        if player["name"].lower() == loser.strip().lower():
            del players_list[index]
            break

    return {
        "winner": winner,
        "loser": loser,
        "rounds": battle_log,
    }


def tournament(players_list, random_generator=None):
    if len(players_list) < 2:
        raise ValueError("At least two players are required for a tournament.")

    rng = random_generator if random_generator is not None else random
    tournament_log = []

    while len(players_list) > 1:
        first_index = rng.randrange(len(players_list))
        second_index = first_index

        while second_index == first_index:
            second_index = rng.randrange(len(players_list))

        first_name = players_list[first_index]["name"]
        second_name = players_list[second_index]["name"]

        battle_result = battle(players_list, first_name, second_name, random_generator=rng)
        tournament_log.append(battle_result)

    return {
        "winner": players_list[0]["name"],
        "battles": tournament_log,
    }


def read_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty.")


def read_positive_integer(prompt):
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if value <= 0:
            print("Value must be greater than 0.")
            continue

        return value


def read_special_move(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in {SPECIAL_EXTRA_HP, SPECIAL_EXTRA_ATTACK}:
            return value
        print("Invalid special move. Enter 'extra hp' or 'extra attack'.")


def build_players_from_input():
    players = []
    player_count = read_positive_integer("Enter number of players: ")

    for index in range(1, player_count + 1):
        print(f"\nPlayer {index}")
        name = read_non_empty_text("Enter player name: ")
        attack_points = read_positive_integer("Enter attack points: ")
        defense = read_positive_integer("Enter defense points: ")
        hp = read_positive_integer("Enter HP: ")
        special = read_special_move("Enter special move (extra hp / extra attack): ")
        add_player(players, name, attack_points, defense, hp, special)

    return players


def run_players_tournament():
    print("Players tournament simulation")
    players = build_players_from_input()
    result = tournament(players)

    print("\nTournament started.\n")
    for battle_result in result["battles"]:
        print(
            f"Battle winner: {battle_result['winner']} | "
            f"Loser removed: {battle_result['loser']} | "
            f"Rounds played: {len(battle_result['rounds'])}"
        )

    print(f"\nTournament winner: {result['winner']}")


if __name__ == "__main__":
    run_players_tournament()
