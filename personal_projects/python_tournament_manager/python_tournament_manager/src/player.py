class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name.strip()
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0
        if self.player_id <= 0:
            raise ValueError("Player ID must be greater than 0.")
        if not self.name:
            raise ValueError("Player name cannot be empty.")

    def record_win(self):
        self.wins += 1
        self.points += 3

    def record_loss(self):
        self.losses += 1

    def record_draw(self):
        self.draws += 1
        self.points += 1

    def to_dict(self):
        return {
            "player_id": self.player_id,
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "draws": self.draws,
            "points": self.points,
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data["player_id"], data["name"])
        player.wins = data["wins"]
        player.losses = data["losses"]
        player.draws = data["draws"]
        player.points = data["points"]
        return player
