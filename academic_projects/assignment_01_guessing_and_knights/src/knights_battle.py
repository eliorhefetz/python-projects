from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Knight:
    name: str
    hp: int
    attack_power: int

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Knight name cannot be empty.")
        if self.hp <= 0:
            raise ValueError("Knight HP must be greater than 0.")
        if self.attack_power <= 0:
            raise ValueError("Knight attack power must be greater than 0.")

    @property
    def is_alive(self) -> bool:
        return self.hp > 0


@dataclass(slots=True)
class BattleRound:
    round_number: int
    attacker_name: str
    defender_name: str
    damage: int
    defender_hp_after_attack: int
    healing_applied: bool = False


@dataclass(slots=True)
class BattleResult:
    winner_name: str | None
    rounds: list[BattleRound]
    final_hp: dict[str, int]
    is_draw: bool


class KnightsBattle:
    def __init__(self, first_knight: Knight, second_knight: Knight, heal_every_n_rounds: int = 3, heal_amount: int = 5) -> None:
        if heal_every_n_rounds <= 0:
            raise ValueError("heal_every_n_rounds must be greater than 0.")
        if heal_amount < 0:
            raise ValueError("heal_amount cannot be negative.")

        self.first_knight = Knight(first_knight.name, first_knight.hp, first_knight.attack_power)
        self.second_knight = Knight(second_knight.name, second_knight.hp, second_knight.attack_power)
        self.heal_every_n_rounds = heal_every_n_rounds
        self.heal_amount = heal_amount

    def simulate(self) -> BattleResult:
        rounds: list[BattleRound] = []
        round_number = 0

        while self.first_knight.is_alive and self.second_knight.is_alive:
            round_number += 1

            self._perform_attack(
                attacker=self.first_knight,
                defender=self.second_knight,
                round_number=round_number,
                rounds=rounds,
            )
            if not self.second_knight.is_alive:
                break

            self._perform_attack(
                attacker=self.second_knight,
                defender=self.first_knight,
                round_number=round_number,
                rounds=rounds,
            )
            if not self.first_knight.is_alive:
                break

            if round_number % self.heal_every_n_rounds == 0:
                self.first_knight.hp += self.heal_amount
                self.second_knight.hp += self.heal_amount
                rounds[-1].healing_applied = True

        winner_name: str | None
        is_draw = False
        if self.first_knight.is_alive and not self.second_knight.is_alive:
            winner_name = self.first_knight.name
        elif self.second_knight.is_alive and not self.first_knight.is_alive:
            winner_name = self.second_knight.name
        else:
            winner_name = None
            is_draw = True

        return BattleResult(
            winner_name=winner_name,
            rounds=rounds,
            final_hp={
                self.first_knight.name: self.first_knight.hp,
                self.second_knight.name: self.second_knight.hp,
            },
            is_draw=is_draw,
        )

    def _perform_attack(self, attacker: Knight, defender: Knight, round_number: int, rounds: list[BattleRound]) -> None:
        defender.hp = max(defender.hp - attacker.attack_power, 0)
        rounds.append(
            BattleRound(
                round_number=round_number,
                attacker_name=attacker.name,
                defender_name=defender.name,
                damage=attacker.attack_power,
                defender_hp_after_attack=defender.hp,
            )
        )


def read_positive_integer(prompt: str) -> int:
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


def read_non_empty_text(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty.")


def build_knight_from_input(order_label: str) -> Knight:
    name = read_non_empty_text(f"Enter the name of the {order_label} knight: ")
    hp = read_positive_integer(f"Enter the HP of the {order_label} knight: ")
    attack_power = read_positive_integer(f"Enter the attack power of the {order_label} knight: ")
    return Knight(name=name, hp=hp, attack_power=attack_power)


def run_knights_battle() -> None:
    print("Knights battle simulation")
    first_knight = build_knight_from_input("first")
    second_knight = build_knight_from_input("second")
    battle = KnightsBattle(first_knight, second_knight)
    result = battle.simulate()

    print("\nBattle started.\n")
    for battle_round in result.rounds:
        print(
            f"Round {battle_round.round_number}: {battle_round.attacker_name} attacked {battle_round.defender_name} "
            f"for {battle_round.damage} damage. {battle_round.defender_name} now has "
            f"{battle_round.defender_hp_after_attack} HP."
        )
        if battle_round.healing_applied:
            print("Both knights received 5 HP after the round.")

    print("\nBattle finished.")
    if result.is_draw:
        print("The battle ended in a draw.")
    else:
        print(f"The winner is: {result.winner_name}")
