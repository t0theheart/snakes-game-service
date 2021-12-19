from snakes_game_service.ext.sessions.sessions_abc import SessionsManagerABC
import uuid


class SessionsManager(SessionsManagerABC):
    def __init__(self):
        self.__sessions = {}
        self.__sessions['123'] = {
            'sessionId': '123',
            'usersAmount': 3,
            'game': {
                'width': 1500,
                'height': 900,
            },
            'users': {
                
            }
        }

    def create_session(self) -> str:
        session_key = str(uuid.uuid4())
        self.__sessions[session_key] = {"status": "start"}
        return session_key

    def get_session(self, session_id: str) -> dict:
        return self.__sessions.get(session_id)

    def put_user(self, user: dict, session_id: str):
        self.__sessions[session_id]['users'][user['id']] = user

    def pop_user(self, user_id: str, session_id: str) -> dict:
        return self.__sessions[session_id]['users'].pop(user_id)



