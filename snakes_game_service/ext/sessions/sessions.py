from snakes_game_service.ext.sessions.sessions_abc import SessionsManagerABC
import uuid


class SessionsManager(SessionsManagerABC):
    def __init__(self):
        self.sessions = {}

    def create_session(self) -> str:
        session_key = str(uuid.uuid4())
        self.sessions[session_key] = {"status": "start"}
        return session_key

    def get_session(self, session_id: str) -> dict:
        return self.sessions.get(session_id)

    def put_user(self, user: dict, session_id: str):
        self.sessions[session_id]['users'][user['id']] = user




