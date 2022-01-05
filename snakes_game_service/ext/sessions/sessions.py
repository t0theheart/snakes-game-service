from snakes_game_service.ext.sessions.sessions_abc import SessionsManagerABC
import uuid


class Lobby:
    def __init__(self, users: list):
        self.__slots = users

    def get_empty_slot(self) -> int:
        for n, item in enumerate(self.__slots):
            if item is None:
                return n

    def get_user_slot(self, user_id: str):
        for n, item in enumerate(self.__slots):
            if item['id'] == user_id:
                return n

    def put(self, user: dict):
        index = self.get_empty_slot()
        if index is not None:
            user['slot'] = index
            self.__slots[index] = user

    def pop(self, user_id: str):
        user_slot = self.get_user_slot(user_id)
        user = self.__slots[user_slot]
        self.__slots[user_slot] = None
        return user


class SessionsManager(SessionsManagerABC):
    def __init__(self):
        self.__sessions = dict()
        self.__sessions['123'] = {
            'sessionId': '123',
            'usersAmount': 3,
            'game': {
                'width': 1500,
                'height': 900,
            },
            'users': [
                None,
                None,
                None
            ]
        }

    def create_session(self) -> str:
        session_key = str(uuid.uuid4())
        self.__sessions[session_key] = {"status": "start"}
        return session_key

    def get_session(self, session_id: str) -> dict:
        return self.__sessions.get(session_id)

    def get_empty_slot(self, session_id: str) -> int:
        session = self.__sessions[session_id]
        slot = Lobby(session['users']).get_empty_slot()
        if slot is not None:
            return slot

    def put_user(self, user: dict, session_id: str):
        session = self.__sessions[session_id]
        Lobby(session['users']).put(user)

    def pop_user(self, user_id: str, session_id: str) -> dict:
        session = self.__sessions[session_id]
        user = Lobby(session['users']).pop(user_id)
        return user
