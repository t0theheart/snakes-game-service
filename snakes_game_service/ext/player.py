import enum


class PlayerStatus(enum.Enum):
    HOST = 'HOST'
    PLAYER = 'PLAYER'


class Player:
    def __init__(self, player_id: str, login: str, status: PlayerStatus, slot=None, color=None):
        self.player_id = player_id
        self.login = login
        self.slot = slot
        self.color = color
        self.status = status

    def to_dict(self):
        return {
            'player_id': self.player_id,
            'login': self.login,
            'slot': self.slot,
            'color': self.color,
            'status': self.status
        }
