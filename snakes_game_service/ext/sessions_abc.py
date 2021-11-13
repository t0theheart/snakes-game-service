from abc import ABC, abstractmethod


class SessionsABC(ABC):

    @abstractmethod
    def create_session(self) -> str: pass

    @abstractmethod
    def get_session(self, session: str) -> str: pass
