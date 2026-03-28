import json
from pathlib import Path

from player import Player
from match import Match


def save_data(file_path, players, matches):
    payload = {
        "players": [player.to_dict() for player in players],
        "matches": [match.to_dict() for match in matches],
    }
    Path(file_path).write_text(json.dumps(payload, indent=4), encoding="utf-8")


def load_data(file_path):
    path = Path(file_path)
    if not path.exists():
        return [], []
    payload = json.loads(path.read_text(encoding="utf-8"))
    players = [Player.from_dict(item) for item in payload.get("players", [])]
    matches = [Match.from_dict(item) for item in payload.get("matches", [])]
    return players, matches
