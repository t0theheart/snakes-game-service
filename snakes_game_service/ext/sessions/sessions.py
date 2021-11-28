from snakes_game_service.ext.sessions.sessions_abc import SessionsManagerABC
import uuid


class SessionsManager(SessionsManagerABC):
    def __init__(self):
        self.sessions = {}

    def create_session(self) -> str:
        session_key = str(uuid.uuid4())
        self.sessions[session_key] = {"status": "start"}
        return session_key

    def get_session(self, session_key: str) -> dict:
        return self.sessions.get(session_key)

    def get_session_users(self, session_key: str) -> list:
        session = self.get_session(session_key)
        return session['users']

    def put_user_to_session(self, user: dict, sessions_id: str) -> bool:
        session = self.get_session(sessions_id)
        users = session['users']
        users_number = session['users_number']
        if users_number > len(users):
            user['color'] = '#FF0000'
            self.sessions[sessions_id]['users'].append(user)
            return True
        return False



