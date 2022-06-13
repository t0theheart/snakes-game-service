from typing import List
from .player import Player


class Game:
    def __init__(self, _id: str, width: int, height: int, players: List[Player or None]):
        self.id: str = _id
        self.width: int = width
        self.height: int = height
        self.players: List[Player or None] = players

    def put_player(self, player: Player):
        self.players[player.slot] = player

    def pop_player(self, player_id: str) -> Player or None:
        player = self.get_player(player_id)
        if player:
            self.players[player.slot] = None
            return player

    def get_player(self, player_id: str) -> Player or None:
        players = self.players
        for p in players:
            if p is not None and p.id == player_id:
                return p

    def get_empty_slot(self) -> int:
        for n, player in enumerate(self.players):
            if player is None:
                return n
