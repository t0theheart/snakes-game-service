from fastapi import WebSocket


class Connection:
    def __init__(self, websocket: WebSocket, client_id: str, session_id: str):
        self.client_id = client_id
        self.session_id = session_id
        self.websocket = websocket


class Connections:
    def __init__(self):
        self.__connections = {}

    def add(self, websocket: WebSocket, client_id: str, session_id: str):
        con = Connection(websocket, client_id, session_id)
        self.__connections[client_id] = con

    def get(self, client_id: str) -> Connection:
        return self.__connections[client_id]

    def pop(self, client_id: str) -> Connection:
        return self.__connections.pop(client_id)

    async def send(self, message: dict, client_id: str):
        websocket = self.__connections[client_id].websocket
        await websocket.send_json(message)

    async def send_all(self, message: dict):
        for con in self.__connections.values():
            await self.send(message, client_id=con.client_id)
