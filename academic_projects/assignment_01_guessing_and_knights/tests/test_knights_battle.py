import unittest

from src.knights_battle import Knight, KnightsBattle


class TestKnightsBattle(unittest.TestCase):
    def test_battle_returns_winner(self) -> None:
        first_knight = Knight(name="Arthur", hp=30, attack_power=10)
        second_knight = Knight(name="Lancelot", hp=20, attack_power=5)

        battle = KnightsBattle(first_knight, second_knight)
        result = battle.simulate()

        self.assertEqual(result.winner_name, "Arthur")
        self.assertFalse(result.is_draw)

    def test_invalid_knight_hp_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            Knight(name="Arthur", hp=0, attack_power=10)


if __name__ == "__main__":
    unittest.main()
