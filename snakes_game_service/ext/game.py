from fastapi import WebSocket
import enum
from .connections import Connections
from .sessions import SessionsManager
from .message import Message


class GameCode(enum.Enum):
    ENTER_LOBBY = 'ENTER_LOBBY'
    PLAYER_ENTER_LOBBY = 'PLAYER_ENTER_LOBBY'
    PLAYER_LEAVE_LOBBY = 'PLAYER_LEAVE_LOBBY'


class PlayerStatus(enum.Enum):
    HOST = 'HOST'
    PLAYER = 'PLAYER'


class GameManager:
    def __init__(self):
        self.__connections = Connections()
        self.__sessions = SessionsManager()

    @property
    def connections(self):
        return self.__connections

    def __allow_to_connect(self, session_id: str) -> bool:
        session = self.__sessions.get_session(session_id)
        return len(session['users']) < session['usersAmount']

    async def connect_player(self, websocket: WebSocket, player_id: str, session_id: str):
        if self.__allow_to_connect(session_id):
            session = self.__sessions.get_session(session_id)
            user = {'id': player_id, 'color': '#FF0000', 'status': PlayerStatus.HOST.value}
            await self.__connections.send_all(
                Message(data={'user': user}, code=GameCode.PLAYER_ENTER_LOBBY.value).dict()
            )
            self.__sessions.put_user(user, session_id)
            self.__connections.add(websocket, player_id, session_id)
            await websocket.send_json(
                Message(data={'session': session, 'user': user}, code=GameCode.ENTER_LOBBY.value).dict()
            )

    async def disconnect_player(self, player_id: str):
        con = self.__connections.pop(client_id=player_id)
        user = self.__sessions.pop_user(user_id=player_id, session_id=con.session_id)
        await self.__connections.send_all(
            Message(data={'user': user}, code=GameCode.PLAYER_LEAVE_LOBBY.value).dict()
        )


