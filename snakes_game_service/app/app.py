from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
import uvicorn
import enum

from snakes_game_service.ext.sessions.sessions import SessionsManager
from snakes_game_service.ext.connections.connections import ConnectionsManager


app = FastAPI()


class GameCode(enum.Enum):
    ENTER_LOBBY = 'ENTER_LOBBY'


class PlayerStatus(enum.Enum):
    HOST = 'HOST'
    PLAYER = 'PLAYER'


@app.on_event("startup")
async def startup_event():
    app.templates = Jinja2Templates(directory="static/templates")
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/scripts", StaticFiles(directory="static/js"), name="scripts")
    app.sessions = SessionsManager()
    app.connections = ConnectionsManager()

    app.sessions.sessions['123'] = {
        'sessionId': '123',
        'usersAmount': 2,
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
    await websocket.app.connections.create_connection(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_json()
            session_id = data['sessionId']
            user = {'user_id': user_id, 'color': '#FF0000', 'status': PlayerStatus.HOST.value}
            if not websocket.app.sessions.put_user_to_session(user=user, session_id=session_id):
                raise WebSocketDisconnect
            else:
                session = websocket.app.sessions.get_session(session_id=session_id)
                await websocket.send_json(data={'data': session, 'code': GameCode.ENTER_LOBBY.value})
    except WebSocketDisconnect:
        await websocket.close(code=3051)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")
