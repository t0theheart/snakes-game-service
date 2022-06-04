
class Sessions:
    def __init__(self):
        self.__sessions = dict()
        self.__sessions['123'] = {
            'sessionId': '123',
            'users': [
                None,
                None,
                None
            ],
            'game': {
                'width': 1500,
                'height': 900
            }
        }

        self.__sessions['456'] = {
            'sessionId': '456',
            'users': [
                None,
                None,
                None
            ],
            'game': {
                'width': 1500,
                'height': 900
            }
        }

    def __get_session(self, session_id: str) -> dict:
        return self.__sessions.get(session_id)

    def put_user(self, session_id: str, slot: int, user: dict):
        self.__get_session(session_id)['users'][slot] = user

    def pop_user(self, session_id: str, index: int) -> dict:
        user = self.__get_session(session_id)['users'][index]
        self.__get_session(session_id)['users'][index] = None
        return user

    def get_session_users(self, session_id: str) -> list:
        session = self.__get_session(session_id)
        return session['users']