from abc import ABC, abstractmethod


class SessionsManagerABC(ABC):

    @abstractmethod
    def create_session(self) -> str: pass

    @abstractmethod
    def get_session(self, session_id: str) -> str: pass

    @abstractmethod
    def put_user(self, user: dict, sessions_id: str) -> bool: pass
