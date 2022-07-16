from abc import ABC, abstractmethod
from app.modules.game import GameABC


class InitPlayerStrategyABC(ABC):
    @abstractmethod
    def init_players(self, game: GameABC) -> None:
        pass
