from fastapi import WebSocket
import enum
from .connections import Connections
from .sessions import Sessions
from .message import Message
from .player import Player, PlayerStatus
from .lobby import Lobby


class GameCode(enum.Enum):
    ENTER_LOBBY = 'ENTER_LOBBY'
    PLAYER_ENTER_LOBBY = 'PLAYER_ENTER_LOBBY'
    PLAYER_LEAVE_LOBBY = 'PLAYER_LEAVE_LOBBY'


class GameManager:
    def __init__(self):
        self.__connections = Connections()
        self.__lobby = Lobby(sessions=Sessions())

    @property
    def connections(self):
        return self.__connections

    async def connect_player(self, websocket: WebSocket, player_id: str, session_id: str):
        players = self.__lobby.get_players(session_id)
        player = Player(player_id, PlayerStatus.HOST.value)
        self.__lobby.put_player(session_id, player)
        await self.__connections.send_all(
            Message(data={'user': player.to_dict()}, code=GameCode.PLAYER_ENTER_LOBBY.value).dict()
        )
        self.__connections.add(websocket, player_id, session_id)
        await self.__connections.send(
            message=Message(
                data={'users': players, 'user': player.to_dict()},
                code=GameCode.ENTER_LOBBY.value
            ).dict(),
            client_id=player_id
        )

    async def disconnect_player(self, player_id: str):
        con = self.__connections.pop(client_id=player_id)
        user = self.__lobby.pop_player(session_id=con.session_id, player_id=player_id)
        await self.__connections.send_all(
            Message(data={'user': user}, code=GameCode.PLAYER_LEAVE_LOBBY.value).dict()
        )


