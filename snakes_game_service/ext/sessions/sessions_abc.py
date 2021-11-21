from abc import ABC, abstractmethod


class SessionsManagerABC(ABC):

    @abstractmethod
    def create_session(self) -> str: pass

    @abstractmethod
    def get_session(self, session: str) -> str: pass

    @abstractmethod
    def get_session_users(self, session_key: str) -> list: pass

    @abstractmethod
    def create_session_user(self, session_key: str) -> bool: pass