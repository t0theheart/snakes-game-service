from fastapi import WebSocket


class ConnectionsManager:
    def __init__(self):
        self.users_connections = {}

    async def create_connection(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.users_connections[user_id] = websocket
