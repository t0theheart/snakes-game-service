from .player import Player
from .sessions import Sessions
from typing import List


class Lobby:
    def __init__(self, sessions: Sessions):
        self.__sessions = sessions

    def get_empty_slot(self, session_id: str) -> int:
        users = self.__sessions.get_session_users(session_id)
        for n, user in enumerate(users):
            if user is None:
                return n

    def put_player(self, session_id: str, player: Player):
        self.__sessions.put_user(session_id, player.slot, player.to_dict())

    def pop_player(self, session_id: str, player_id: str) -> Player or None:
        player = self.get_player(session_id, player_id)
        if player:
            self.__sessions.pop_user(session_id, player.slot)
            return player

    def get_players(self, session_id: str) -> List[Player or None]:
        users = self.__sessions.get_session_users(session_id)
        players = [Player.from_session(u) if u else None for u in users]
        return players

    def get_player(self, session_id: str, player_id: str) -> Player or None:
        players = self.get_players(session_id)
        for p in players:
            if p is not None and p.id == player_id:
                return p

    def get_game_settings(self, session_id: str):
        return self.__sessions.get_game(session_id)
