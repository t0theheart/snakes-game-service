from snakes_game_service.ext.sessions_abc import SessionsABC
import uuid


class Sessions(SessionsABC):
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

    def create_session_user(self, session_key: str) -> bool:
        session = self.get_session(session_key)
        users = session['users']
        users_number = session['users_number']
        if users_number > len(users):
            user = {
                'color': '#FF0000'
            }
            self.sessions[session_key]['users'].append(user)
            return True
        return False



