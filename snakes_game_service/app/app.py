from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
import uvicorn

from snakes_game_service.ext.sessions import Sessions


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    app.templates = Jinja2Templates(directory="static/templates")
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/scripts", StaticFiles(directory="static/js"), name="js")
    app.sessions = Sessions()

    app.sessions.sessions['123'] = {'123': 123}


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return request.app.templates.TemplateResponse("index.html", {"request": request})


@app.post("/sessions")
async def root(request: Request):
    return {"session": request.app.sessions.create_session()}


@app.get("/sessions")
async def root(key: str, request: Request):
    session = request.app.sessions.get_session(key)
    if session:
        return Response(status_code=200)
    return Response(status_code=404)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")
