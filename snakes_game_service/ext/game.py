from fastapi import WebSocket
import enum
from .connections import ConnectionsManager
from .sessions import SessionsManager


class GameCode(enum.Enum):
    ENTER_LOBBY = 'ENTER_LOBBY'
    NEW_PLAYER_ENTER_LOBBY = 'NEW_PLAYER_ENTER_LOBBY'


class PlayerStatus(enum.Enum):
    HOST = 'HOST'
    PLAYER = 'PLAYER'


class GameManager:
    def __init__(self):
        self.connections = ConnectionsManager()
        self.sessions = SessionsManager()

    async def connect_new_player_to_lobby(self, websocket: WebSocket, player_id: str, lobby_id: str):
        session = self.sessions.get_session(lobby_id)
        if len(session['users']) < session['usersAmount']:
            other_users_ids = [user['id'] for user in session['users']]

            user = {'id': player_id, 'color': '#FF0000', 'status': PlayerStatus.HOST.value}

            self.sessions.put_user_to_session(user, lobby_id)
            self.connections.add(websocket, player_id)
            await websocket.send_json({'session': session, 'code': GameCode.ENTER_LOBBY.value, 'user': user})
            await self.connections.send(
                message={'data': user, 'code': GameCode.NEW_PLAYER_ENTER_LOBBY.value},
                connections_ids=other_users_ids
            )

