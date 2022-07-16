from abc import ABC, abstractmethod
from app.modules.player import Player
from typing import List


class GameABC(ABC):

    @property
    @abstractmethod
    def width(self) -> int:
        pass

    @property
    @abstractmethod
    def height(self) -> int:
        pass

    @property
    @abstractmethod
    def players(self) -> List[Player or None]:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @abstractmethod
    def put_player(self, player: Player) -> None:
        pass

    @abstractmethod
    def pop_player(self, player_id: str) -> Player or None:
        pass

    @abstractmethod
    def get_player(self, player_id: str) -> Player or None:
        pass

    @abstractmethod
    def get_empty_slot(self) -> int:
        pass

    @abstractmethod
    def init_game(self) -> None:
        pass
