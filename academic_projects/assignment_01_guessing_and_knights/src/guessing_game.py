from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass(slots=True)
class GuessResult:
    is_correct: bool
    message: str
    hint: str | None = None
    is_disqualified: bool = False
    attempts_used: int = 0
    attempts_remaining: int = 0


class NumberGuessingGame:
    def __init__(
        self,
        secret_number: int | None = None,
        minimum_number: int = 1,
        maximum_number: int = 200,
        max_attempts: int = 7,
        hint_after_attempt: int = 3,
    ) -> None:
        if minimum_number >= maximum_number:
            raise ValueError("minimum_number must be smaller than maximum_number.")
        if max_attempts <= 0:
            raise ValueError("max_attempts must be greater than 0.")
        if hint_after_attempt <= 0:
            raise ValueError("hint_after_attempt must be greater than 0.")

        self.minimum_number = minimum_number
        self.maximum_number = maximum_number
        self.max_attempts = max_attempts
        self.hint_after_attempt = hint_after_attempt
        self.secret_number = secret_number if secret_number is not None else random.randint(minimum_number, maximum_number)

        if not self.minimum_number <= self.secret_number <= self.maximum_number:
            raise ValueError("secret_number must be within the configured range.")

        self.attempts_used = 0
        self.is_over = False
        self.player_won = False

    def guess(self, value: int) -> GuessResult:
        if self.is_over:
            raise RuntimeError("The game is already over.")
        if not self.minimum_number <= value <= self.maximum_number:
            raise ValueError(
                f"Guess must be between {self.minimum_number} and {self.maximum_number}."
            )

        self.attempts_used += 1
        attempts_remaining = self.max_attempts - self.attempts_used

        if value == self.secret_number:
            self.is_over = True
            self.player_won = True
            return GuessResult(
                is_correct=True,
                message="Correct guess. You won.",
                attempts_used=self.attempts_used,
                attempts_remaining=attempts_remaining,
            )

        hint: str | None = None
        if self.attempts_used == self.hint_after_attempt:
            hint = self._build_parity_hint()

        if self.attempts_used >= self.max_attempts:
            self.is_over = True
            return GuessResult(
                is_correct=False,
                message=f"Incorrect guess. You are disqualified. The correct number was {self.secret_number}.",
                hint=hint,
                is_disqualified=True,
                attempts_used=self.attempts_used,
                attempts_remaining=0,
            )

        comparison_message = "Too low." if value < self.secret_number else "Too high."
        return GuessResult(
            is_correct=False,
            message=comparison_message,
            hint=hint,
            attempts_used=self.attempts_used,
            attempts_remaining=attempts_remaining,
        )

    def _build_parity_hint(self) -> str:
        return "Hint: the number is even." if self.secret_number % 2 == 0 else "Hint: the number is odd."


def read_integer(prompt: str, minimum_value: int | None = None, maximum_value: int | None = None) -> int:
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if minimum_value is not None and value < minimum_value:
            print(f"Value must be at least {minimum_value}.")
            continue

        if maximum_value is not None and value > maximum_value:
            print(f"Value must be at most {maximum_value}.")
            continue

        return value


def run_guessing_game() -> None:
    game = NumberGuessingGame()
    print(
        f"Number guessing game: guess a number between {game.minimum_number} and {game.maximum_number}."
    )

    while not game.is_over:
        player_guess = read_integer(
            prompt="Enter your guess: ",
            minimum_value=game.minimum_number,
            maximum_value=game.maximum_number,
        )
        result = game.guess(player_guess)
        print(result.message)
        if result.hint:
            print(result.hint)
        if not result.is_correct and not result.is_disqualified:
            print(f"Attempts remaining: {result.attempts_remaining}")
