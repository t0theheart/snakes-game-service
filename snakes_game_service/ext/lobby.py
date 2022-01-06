import enum
from .player import Player
from .sessions import Sessions


class PlayerColor(enum.Enum):
    RED = '#FF0000'


class Lobby:
    color_map = {
        0: PlayerColor.RED.value,
        1: PlayerColor.RED.value,
        2: PlayerColor.RED.value,
        3: PlayerColor.RED.value,
        4: PlayerColor.RED.value,
        5: PlayerColor.RED.value,
        6: PlayerColor.RED.value,
        7: PlayerColor.RED.value,
    }

    def __init__(self, sessions: Sessions):
        self.__sessions = sessions

    @staticmethod
    def __get_empty_slot(players: list) -> int:
        for n, item in enumerate(players):
            if item is None:
                return n

    @staticmethod
    def __get_player_slot(players: list, player_id: str):
        for n, item in enumerate(players):
            if item['id'] == player_id:
                return n

    def put_player(self, session_id: str, player: Player):
        players = self.get_players(session_id)
        slot = self.__get_empty_slot(players)
        if slot is not None:
            player.slot = slot
            player.color = self.color_map[slot]
            self.__sessions.put_user(session_id, slot, player.to_dict())

    def pop_player(self, session_id: str, player_id: str) -> dict:
        players = self.get_players(session_id)
        slot = self.__get_player_slot(players, player_id)
        if slot is not None:
            return self.__sessions.pop_user(session_id, slot)

    def get_players(self, session_id: str) -> list:
        session = self.__sessions.get_session(session_id)
        return session['users']
