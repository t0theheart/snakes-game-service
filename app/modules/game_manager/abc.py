from abc import ABC, abstractmethod
from fastapi import WebSocket


class GameManagerABC(ABC):
    @abstractmethod
    async def connect_player(self, websocket: WebSocket, player_id: str, session_id: str, login: str) -> bool:
        pass

    @abstractmethod
    async def disconnect_player(self, player_id: str):
        pass

    @abstractmethod
    async def start_game(self, session_id: str):
        pass
