
class Sessions:
    def __init__(self):
        self.__sessions = dict()
        self.__sessions['123'] = {
            'sessionId': '123',
            'users': [
                None,
                None,
                None
            ]
        }

    def get_session(self, session_id: str) -> dict:
        return self.__sessions.get(session_id)

    def put_user(self, session_id: str, slot: int, user: dict):
        self.__sessions[session_id]['users'][slot] = user

    def pop_user(self, session_id: str, slot: str) -> dict:
        user = self.__sessions[session_id]['users'][slot]
        self.__sessions[session_id]['users'][slot] = None
        return user
