import enum


class PlayerStatus(enum.Enum):
    HOST = 'HOST'
    PLAYER = 'PLAYER'


class Player:
    def __init__(self, _id: str, status: PlayerStatus):
        self.id = _id
        self.slot = None
        self.color = None
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'slot': self.slot,
            'color': self.color,
            'status': self.status
        }
