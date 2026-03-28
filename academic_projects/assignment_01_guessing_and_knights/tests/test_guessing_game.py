import unittest

from src.guessing_game import NumberGuessingGame


class TestNumberGuessingGame(unittest.TestCase):
    def test_correct_guess_finishes_game(self) -> None:
        game = NumberGuessingGame(secret_number=50)
        result = game.guess(50)

        self.assertTrue(result.is_correct)
        self.assertTrue(game.is_over)
        self.assertTrue(game.player_won)

    def test_hint_is_returned_after_third_wrong_attempt(self) -> None:
        game = NumberGuessingGame(secret_number=40)
        game.guess(10)
        game.guess(20)
        result = game.guess(30)

        self.assertEqual(result.hint, "Hint: the number is even.")
        self.assertFalse(result.is_correct)

    def test_game_disqualifies_after_seventh_wrong_attempt(self) -> None:
        game = NumberGuessingGame(secret_number=100)
        for value in [1, 2, 3, 4, 5, 6]:
            game.guess(value)
        result = game.guess(7)

        self.assertTrue(result.is_disqualified)
        self.assertTrue(game.is_over)


if __name__ == "__main__":
    unittest.main()
