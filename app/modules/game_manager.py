from fastapi import WebSocket
from typing import List
import enum
import asyncio
from .connections import Connections
from .message import Message
from .player import Player, PlayerStatus
from .sessions import Sessions
from .game_engine import GameEngine


class GameCode(enum.Enum):
    ENTER_LOBBY = 'ENTER_LOBBY'
    PLAYER_ENTER_LOBBY = 'PLAYER_ENTER_LOBBY'
    PLAYER_LEAVE_LOBBY = 'PLAYER_LEAVE_LOBBY'

    GAME_STARTED = 'GAME_STARTED'


class GameManager:
    def __init__(self):
        self.__connections = Connections()
        self.__lobby = Sessions()
        self.__game_engine = GameEngine()

    async def connect_player(self, websocket: WebSocket, player_id: str, session_id: str, login: str) -> bool:
        slot = self.__lobby.get_empty_slot(session_id)
        if slot is not None:
            players = self.__lobby.get_players(session_id)

            # todo temporary
            if login == '111':
                player = Player(player_id, login, slot=slot, status=PlayerStatus.HOST.value)
            else:
                player = Player(player_id, login, slot=slot)

            if any(players):
                message = Message(data={'user': player.to_dict()}, code=GameCode.PLAYER_ENTER_LOBBY.value)
                await self.__notify_players(message, players)

            self.__lobby.put_player(session_id, player)
            self.__connections.add(websocket, player_id, session_id)
            old_players = [i.to_dict() if i else None for i in players]
            old_players[slot] = player.to_dict()
            message = Message(
                data={'users': old_players, 'user': player.to_dict()},
                code=GameCode.ENTER_LOBBY.value
            )
            await self.__notify_players(message, [player])

            return True

    async def disconnect_player(self, player_id: str):
        if self.__connections.get(player_id):
            con = self.__connections.pop(player_id)
            player = self.__lobby.pop_player(con.session_id, player_id)
            other_players = self.__lobby.get_players(con.session_id)
            message = Message(data={'user': player.to_dict()}, code=GameCode.PLAYER_LEAVE_LOBBY.value)
            await self.__notify_players(message, other_players)

    async def __notify_players(self, message: Message, players: List[Player or None]):
        await asyncio.gather(
            *[self.__connections.send(message.dict(), player.id) for player in players if player is not None]
        )

    # async def init_game(self, session_id: str):
    #     game = self.__lobby.get_game(session_id)
    #     game.init_game()
    #     players = game.players
    #     # todo хранить game в sessions и после инициализации игры делать репут плееров с позицией и длинной хвоста
    #     message = Message(data={'game': game}, code=GameCode.GAME_STARTED.value)
    #     await self.__notify_players(message, players)
