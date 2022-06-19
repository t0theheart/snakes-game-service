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

        self.body = []
        self.body_size: int = 30
        self.body_length: int = 2

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
            'body': self.body
        }

    def create_start_body(self, x: int, y: int, reversed_body: bool = False):
        head = (x, y)
        self.body.append(head)

        if reversed_body:
            body_elem_1 = (x, y - self.body_size)
            body_elem_2 = (x, y - self.body_size * 2)
        else:
            body_elem_1 = (x, y + self.body_size)
            body_elem_2 = (x, y + self.body_size * 2)

        self.body.append(body_elem_1)
        self.body.append(body_elem_2)
