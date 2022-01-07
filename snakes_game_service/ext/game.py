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

    async def connect_player(self, websocket: WebSocket, player_id: str, session_id: str, login: str) -> bool:
        slot = self.__lobby.get_empty_slot(session_id)
        if slot is not None:
            player = Player(player_id, login, PlayerStatus.HOST.value)
            print()
            player = self.__lobby.give_slot_to_player(player, slot)
            self.__lobby.put_player(session_id, player, slot)
            await self.notify_all(
                data={'user': player.to_dict()},
                code=GameCode.PLAYER_ENTER_LOBBY
            )
            self.__connections.add(websocket, player_id, session_id)
            players = self.__lobby.get_players(session_id)
            await self.notify_one(
                data={'users': players, 'user': player.to_dict()},
                code=GameCode.ENTER_LOBBY,
                player_id=player_id
            )
            return True

    async def disconnect_player(self, player_id: str):
        con = self.__connections.pop(client_id=player_id)
        user = self.__lobby.pop_player(session_id=con.session_id, player_id=player_id)
        await self.notify_all(
            data={'user': user},
            code=GameCode.PLAYER_LEAVE_LOBBY
        )

    async def notify_one(self, data: dict, code: GameCode, player_id: str):
        await self.__connections.send(
            message=Message(data=data, code=code.value).dict(),
            client_id=player_id
        )

    async def notify_all(self, data: dict, code: GameCode):
        await self.__connections.send_all(
            message=Message(data=data, code=code.value).dict(),
        )
