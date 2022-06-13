from .player import Player
from .game import Game
from typing import List


class Sessions:
    def __init__(self):
        self.__sessions = dict()
        self.__sessions['123'] = Game(_id='123', width=1500, height=900, players=[None, None, None])

    def get_player(self, session_id: str, player_id: str) -> Player or None:
        return self.get_game(session_id).get_player(player_id)

    def put_player(self, session_id: str, player: Player):
        self.get_game(session_id).put_player(player)

    def pop_player(self, session_id: str, player_id: str) -> Player or None:
        return self.get_game(session_id).pop_player(player_id)

    def get_players(self, session_id: str) -> List[Player or None]:
        return self.get_game(session_id).players

    def get_game(self, session_id: str) -> Game:
        return self.__sessions[session_id]

    def get_empty_slot(self, session_id: str) -> int:
        return self.get_game(session_id).get_empty_slot()
