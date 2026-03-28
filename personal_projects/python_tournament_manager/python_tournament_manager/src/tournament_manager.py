from player import Player
from match import Match


class TournamentManager:
    def __init__(self):
        self.players = []
        self.matches = []

    def add_player(self, player_id, name):
        if self.find_player_by_id(player_id) is not None:
            raise ValueError(f"Player with ID {player_id} already exists.")
        self.players.append(Player(player_id, name))

    def update_player(self, player_id, new_name):
        player = self.find_player_by_id(player_id)
        if player is None:
            raise ValueError("Player not found.")
        cleaned_name = new_name.strip()
        if not cleaned_name:
            raise ValueError("Player name cannot be empty.")
        player.name = cleaned_name

    def remove_player(self, player_id):
        player = self.find_player_by_id(player_id)
        if player is None:
            raise ValueError("Player not found.")
        self.players.remove(player)
        self.matches = [
            match for match in self.matches
            if match.first_player_id != player_id and match.second_player_id != player_id
        ]

    def find_player_by_id(self, player_id):
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None

    def search_players(self, keyword):
        cleaned_keyword = keyword.strip().lower()
        return [player for player in self.players if cleaned_keyword in player.name.lower()]

    def record_match(self, first_player_id, second_player_id, result):
        first_player = self.find_player_by_id(first_player_id)
        second_player = self.find_player_by_id(second_player_id)
        if first_player is None or second_player is None:
            raise ValueError("Both players must exist before recording a match.")
        match = Match(first_player_id, second_player_id, result)
        self.matches.append(match)
        if match.result == "1":
            first_player.record_win()
            second_player.record_loss()
        elif match.result == "2":
            second_player.record_win()
            first_player.record_loss()
        else:
            first_player.record_draw()
            second_player.record_draw()

    def get_rankings(self):
        return sorted(self.players, key=lambda player: (-player.points, -player.wins, player.name.lower()))
