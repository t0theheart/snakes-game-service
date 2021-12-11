from fastapi import WebSocket


class ConnectionsManager:
    def __init__(self):
        self.connections = {}

    def add(self, websocket: WebSocket, connection_id: str):
        self.connections[connection_id] = websocket

    async def send(self, message: dict, connections_ids: list):
        for connections_id in connections_ids:
            websocket = self.connections[connections_id]
            await websocket.send_json(message)
