from fastapi import WebSocket
from typing import List
import enum
from .connections import Connections
from .sessions import Sessions
from .message import Message
from .player import Player, PlayerStatus
from .lobby import Lobby
from .game_engine import GameEngine


class GameCode(enum.Enum):
    ENTER_LOBBY = 'ENTER_LOBBY'
    PLAYER_ENTER_LOBBY = 'PLAYER_ENTER_LOBBY'
    PLAYER_LEAVE_LOBBY = 'PLAYER_LEAVE_LOBBY'


class GameManager:
    def __init__(self):
        self.__connections = Connections()
        self.__lobby = Lobby(sessions=Sessions())
        self.__game = GameEngine()

    @property
    def connections(self):
        return self.__connections

    async def connect_player(self, websocket: WebSocket, player_id: str, session_id: str, login: str) -> bool:
        slot = self.__lobby.get_empty_slot(session_id)
        if slot is not None:
            players = self.__lobby.get_players(session_id)
            player = Player(player_id, login, PlayerStatus.HOST.value)
            player = self.__lobby.put_player(session_id, player, slot)

            if any(players):
                message = Message(data={'user': player.to_dict()}, code=GameCode.PLAYER_ENTER_LOBBY.value)
                await self.__notify_players(message, players)

            self.__connections.add(websocket, player_id, session_id)
            old_players = [i.to_dict() if i else None for i in players]
            old_players[slot] = player.to_dict()
            message = Message(
                data={'users': old_players, 'user': player.to_dict()},
                code=GameCode.ENTER_LOBBY.value
            )
            await self.__notify_players(message, [player])

            return True

    async def disconnect_player(self, player_id: str):
        con = self.__connections.pop(client_id=player_id)
        user = self.__lobby.pop_player(session_id=con.session_id, player_id=player_id)
        other_players = self.__lobby.get_players(con.session_id)
        message = Message(data={'user': user}, code=GameCode.PLAYER_LEAVE_LOBBY.value)
        await self.__notify_players(message, other_players)

    async def __notify_players(self, message: Message, players: List[Player]):
        for player in players:
            if player:
                await self.__connections.send(message.dict(), player.id)
