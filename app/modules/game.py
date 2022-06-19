from typing import List
from .player import Player


class Game:
    def __init__(self, _id: str, width: int, height: int, players: List[Player or None]):
        self.id: str = _id
        self.width: int = width
        self.height: int = height
        self.body_size: int = 30
        self.body_length: int = 2
        self.players: List[Player or None] = players

    def to_dict(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'players': [p.to_dict() for p in self.players if p]
        }

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

    def init_game(self) -> None:
        self.__remove_empty_slots()
        self.__init_players()

    def __init_players(self) -> None:
        step = self.width // len(self.players)
        x = step//2
        for n, p in enumerate(self.players, start=1):
            if n % 2 == 0:
                y = 90
                reversed_body = True
            else:
                y = self.height - 90
                reversed_body = False

            p.body_size = self.body_size
            p.body_length = self.body_length
            p.create_start_body(x=x, y=y, reversed_body=reversed_body)
            x += step

    def __remove_empty_slots(self) -> None:
        self.players = [p for p in self.players if p]
