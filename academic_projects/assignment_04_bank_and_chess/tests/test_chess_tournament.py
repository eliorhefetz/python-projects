import unittest

from src.chess_tournament import bestPlayer, countGames, countPlayers, findPlayer, sortPlayers


class TestChessTournament(unittest.TestCase):
    def setUp(self):
        self.players = {
            "Elior": [3500, 40, 0],
            "Eli": [2800, 25, 6],
            "Or": [3100, 18, 4],
        }

    def test_sort_players_returns_names_by_power(self):
        self.assertEqual(sortPlayers(self.players), ["Eli", "Or", "Elior"])

    def test_count_players_returns_correct_count(self):
        self.assertEqual(countPlayers(self.players), 3)

    def test_count_games_returns_total_games(self):
        self.assertEqual(countGames(self.players), 46)

    def test_best_player_returns_highest_power_name(self):
        self.assertEqual(bestPlayer(self.players), "Elior")

    def test_find_player_returns_details(self):
        self.assertEqual(
            findPlayer("Elior", self.players),
            ["Power: 3500", "Wins: 40", "Losses: 0"],
        )


if __name__ == "__main__":
    unittest.main()
