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
    def __init__(self, _id: str, login: str, status: PlayerStatus = None, slot: int = None, color: str = None):
        self.id = _id
        self.login = login
        self.slot = slot
        self.color = color or self.__get_color()
        self.status = status or PlayerStatus.PLAYER.value
        self.x = 0
        self.y = 0

    @staticmethod
    def __get_color():
        return random.choice([color.value for color in PlayerColor])

    def to_dict(self):
        return {
            'id': self.id,
            'login': self.login,
            'slot': self.slot,
            'color': self.color,
            'status': self.status,
            'x': self.x,
            'y': self.y
        }

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
