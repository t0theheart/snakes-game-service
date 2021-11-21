from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
import uvicorn

from snakes_game_service.ext.sessions.sessions import SessionsManager
from snakes_game_service.ext.connections.connections import ConnectionsManager


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    app.templates = Jinja2Templates(directory="static/templates")
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/scripts", StaticFiles(directory="static/js"), name="scripts")
    app.sessions = SessionsManager()
    app.connections = ConnectionsManager()

    app.sessions.sessions['123'] = {
        'session_key': '123',
        'users_number': 2,
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


@app.post("/sessions/{session_key}/users")
async def get_session_users(session_key: str, request: Request):
    is_created = request.app.sessions.create_session_user(session_key)
    if is_created:
        return Response(status_code=201)
    return Response(status_code=403)


@app.get("/sessions/{session_key}/users")
async def get_session_users(session_key: str, request: Request):
    return {"users": request.app.sessions.get_session_users(session_key)}


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    print('user_id:', user_id)
    await websocket.app.connections.create_connection(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_text()
            print('data', data)
    except WebSocketDisconnect:
        pass


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")


# @app.post("/sessions/{session_key}/users")

# @app.get("/sessions/{session_key}/users")

# @app.get("/sessions/{session_key}")

# @app.post("/sessions")
