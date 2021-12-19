from fastapi import WebSocket
import enum
from .connections import Connections
from .sessions import SessionsManager
from .message import Message


class GameCode(enum.Enum):
    ENTER_LOBBY = 'ENTER_LOBBY'
    NEW_PLAYER_ENTER_LOBBY = 'NEW_PLAYER_ENTER_LOBBY'


class PlayerStatus(enum.Enum):
    HOST = 'HOST'
    PLAYER = 'PLAYER'


class GameManager:
    def __init__(self):
        self.connections = Connections()
        self.sessions = SessionsManager()

    def __allow_to_connect(self, session_id: str) -> bool:
        session = self.sessions.get_session(session_id)
        return len(session['users']) < session['usersAmount']

    async def connect_player(self, websocket: WebSocket, player_id: str, session_id: str):
        if self.__allow_to_connect(session_id):
            session = self.sessions.get_session(session_id)
            user = {'id': player_id, 'color': '#FF0000', 'status': PlayerStatus.HOST.value}
            await self.connections.send_all(
                Message(data={'user': user}, code=GameCode.NEW_PLAYER_ENTER_LOBBY.value).dict()
            )
            self.sessions.put_user(user, session_id)
            self.connections.add(websocket, player_id, session_id)
            await websocket.send_json(
                Message(data={'session': session, 'user': user}, code=GameCode.ENTER_LOBBY.value).dict()
            )


