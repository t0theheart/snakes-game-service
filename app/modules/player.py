import enum
import random


class PlayerColor(enum.Enum):
    RED = '#FF0000'
    BLUE = '#3f62f7'
    YELLOW = '#ffce0e'


class PlayerStatus(enum.Enum):
    HOST = 'HOST'
    PLAYER = 'PLAYER'


class Player:
    def __init__(self, _id: str, login: str, status: PlayerStatus, slot: int = None, color: str = None):
        self.id = _id
        self.login = login
        self.slot = slot
        self.color = color or self.__get_color()
        self.status = status

    @staticmethod
    def __get_color():
        return random.choice([color.value for color in PlayerColor])

    @classmethod
    def from_session(cls, user: dict):
        return cls(
            _id=user['id'],
            login=user['login'],
            status=user['status'],
            slot=user['slot'],
            color=user['color']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'login': self.login,
            'slot': self.slot,
            'color': self.color,
            'status': self.status
        }
