import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from players_tournament import (
    add_player,
    attack,
    battle,
    best_player,
    strongest_player,
    tournament,
)


class FakeRandom:
    def __init__(self, randint_values=None, randrange_values=None):
        self.randint_values = randint_values or []
        self.randrange_values = randrange_values or []
        self.randint_index = 0
        self.randrange_index = 0

    def randint(self, start, end):
        value = self.randint_values[self.randint_index]
        self.randint_index += 1
        return value

    def randrange(self, length):
        value = self.randrange_values[self.randrange_index]
        self.randrange_index += 1
        return value


class TestPlayersTournament(unittest.TestCase):
    def test_add_player_and_helpers(self):
        players = []
        add_player(players, "Moshe", 100, 100, 100, "extra attack")
        add_player(players, "Yosef", 90, 120, 100, "extra hp", wins=2)

        self.assertEqual(strongest_player(players), "Moshe")
        self.assertEqual(best_player(players), "Yosef")

    def test_attack_reduces_defense_then_hp(self):
        players = []
        add_player(players, "Attacker", 50, 100, 100, "extra attack")
        add_player(players, "Defender", 20, 40, 100, "extra hp")

        result = attack(players, "Attacker", "Defender")

        self.assertEqual(result["defense_after"], 0)
        self.assertEqual(result["hp_after"], 90)

    def test_battle_removes_loser_and_adds_win(self):
        players = []
        add_player(players, "Moshe", 100, 100, 100, "extra attack")
        add_player(players, "Yosef", 100, 100, 100, "extra hp")

        fake_random = FakeRandom(randint_values=[0, 0, 0, 0])
        result = battle(players, "Moshe", "Yosef", random_generator=fake_random)

        self.assertEqual(result["winner"], "Moshe")
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0]["name"], "Moshe")
        self.assertEqual(players[0]["wins"], 1)

    def test_tournament_returns_single_winner(self):
        players = []
        add_player(players, "Moshe", 100, 100, 100, "extra attack")
        add_player(players, "Yosef", 100, 100, 100, "extra hp")
        add_player(players, "Dodo", 100, 100, 100, "extra attack")

        fake_random = FakeRandom(
            randint_values=[0, 0, 0, 0, 0, 0, 0, 0],
            randrange_values=[0, 1, 0, 1],
        )
        result = tournament(players, random_generator=fake_random)

        self.assertEqual(len(players), 1)
        self.assertIn("winner", result)
        self.assertEqual(result["winner"], players[0]["name"])


if __name__ == "__main__":
    unittest.main()
