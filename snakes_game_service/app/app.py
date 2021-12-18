from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
import uvicorn
import enum

from snakes_game_service.ext.game import GameManager


app = FastAPI()
game = GameManager()

game.sessions.sessions['123'] = {
        'sessionId': '123',
        'usersAmount': 3,
        'game': {
            'width': 1500,
            'height': 900,
        },
        'users': [
            # {
            #     'color': '#FF0000',
            #     'number': 1,
            #     # 'x': 1500 // 5,
            #     # 'y': 900 - 90,
            # }
        ]
    }


class GameCode(enum.Enum):
    ENTER_LOBBY = 'ENTER_LOBBY'
    NEW_PLAYER_ENTER_LOBBY = 'NEW_PLAYER_ENTER_LOBBY'


class PlayerStatus(enum.Enum):
    HOST = 'HOST'
    PLAYER = 'PLAYER'


@app.on_event("startup")
async def startup_event():
    app.templates = Jinja2Templates(directory="static/templates")
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/scripts", StaticFiles(directory="static/js"), name="scripts")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return request.app.templates.TemplateResponse("index.html", {"request": request})


@app.post("/sessions")
async def create_session(request: Request):
    return {"session": request.app.sessions.create_session()}


@app.get("/sessions/{session_key}/users")
async def get_session_users(session_key: str, request: Request):
    return {"users": request.app.sessions.get_session_users(session_key)}


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            if data['code'] == 'CONNECT_TO_SESSION':
                session_id = data['sessionId']
                await game.connect_new_player_to_lobby(websocket, player_id=user_id, lobby_id=session_id)
            else:
                raise WebSocketDisconnect
    except WebSocketDisconnect:
        await websocket.close(code=3051)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")
