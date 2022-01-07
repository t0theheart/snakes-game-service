from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from snakes_game_service.ext.game import GameManager


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    app.templates = Jinja2Templates(directory="static/templates")
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/scripts", StaticFiles(directory="static/js"), name="scripts")
    app.game = GameManager()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return request.app.templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    game = websocket.app.game
    try:
        while True:
            data = await websocket.receive_json()
            if data['code'] == 'CONNECT_TO_SESSION':
                session_id = data['sessionId'][:30]
                login = data['login'][:30]
                connected = await game.connect_player(websocket, session_id=session_id, player_id=user_id, login=login)
                if not connected:
                    raise WebSocketDisconnect
            else:
                pass

    except WebSocketDisconnect:
        if game.connections.get(user_id):
            await game.disconnect_player(player_id=user_id)
        await websocket.close()


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")
