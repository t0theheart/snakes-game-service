import asyncio
from .abc import NotifierABC
from .message import Message
from typing import List
from app.modules.player import Player
from app.modules.connections import Connections


class PlayersNotifier(NotifierABC):
    def __init__(self, connections: Connections):
        self.__connections = connections

    async def notify(self, message: Message, players: List[Player or None]):
        await asyncio.gather(
            *[self.__connections.send(message.dict(), player.id) for player in players if player is not None]
        )
