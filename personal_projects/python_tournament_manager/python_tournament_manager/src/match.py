class Match:
    def __init__(self, first_player_id, second_player_id, result):
        self.first_player_id = first_player_id
        self.second_player_id = second_player_id
        self.result = result.strip().lower()
        if self.first_player_id == self.second_player_id:
            raise ValueError("A player cannot play against themselves.")
        if self.result not in {"1", "2", "draw"}:
            raise ValueError("Result must be '1', '2', or 'draw'.")

    def to_dict(self):
        return {
            "first_player_id": self.first_player_id,
            "second_player_id": self.second_player_id,
            "result": self.result,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["first_player_id"], data["second_player_id"], data["result"])
