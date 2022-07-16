from .abc import GameABC
from typing import List
from app.modules.player import Player
from app.modules.game.init_players_strategy import InitPlayerStrategyABC


class Game(GameABC):
    def __init__(
            self, _id: str, width: int, height: int, players: List[Player or None],
            init_players_strategy: InitPlayerStrategyABC
    ):
        self.id: str = _id
        self.__width: int = width
        self.__height: int = height
        self.__object_size: int = 30
        self.__start_snake_length: int = 2
        self.__players: List[Player or None] = players
        self.__init_players_strategy = init_players_strategy

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def players(self) -> List[Player or None]:
        return self.__players

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'players': [p.to_dict() for p in self.players if p]
        }

    def put_player(self, player: Player) -> None:
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
        self.__init_players_strategy.init_players(game=self)

    def __remove_empty_slots(self) -> None:
        self.__players = [p for p in self.players if p]
