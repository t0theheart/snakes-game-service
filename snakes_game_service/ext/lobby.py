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

    def get_empty_slot(self, session_id: str) -> int:
        slots = self.get_players(session_id)
        for n, slot in enumerate(slots):
            if slot is None:
                return n

    def get_player_slot(self, session_id: str, player_id: str) -> int:
        slots = self.get_players(session_id)
        for n, slot in enumerate(slots):
            if slot is not None and slot['player_id'] == player_id:
                return n

    def __give_slot_to_player(self, player: Player, slot: int) -> Player:
        player.slot = slot
        player.color = self.color_map[slot]
        return player

    def put_player(self, session_id: str, player: Player, slot: int) -> Player:
        player = self.__give_slot_to_player(player, slot)
        self.__sessions.put_user(session_id, slot, player.to_dict())
        return player

    def pop_player(self, session_id: str, player_id: str) -> dict:
        slot = self.get_player_slot(session_id, player_id)
        if slot is not None:
            return self.__sessions.pop_user(session_id, slot)

    def get_players(self, session_id: str):
        session = self.__sessions.get_session(session_id)
        return [i for i in session['users']]
