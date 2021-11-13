from snakes_game_service.ext.sessions_abc import SessionsABC
import uuid


class Sessions(SessionsABC):
    def __init__(self):
        self.sessions = {}

    def create_session(self) -> str:
        session = str(uuid.uuid4())
        self.sessions[session] = {"status": "start"}
        return session

    def get_session(self, session: str) -> str:
        return self.sessions.get(session)
