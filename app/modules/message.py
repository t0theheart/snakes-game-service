from pydantic import BaseModel


class Message(BaseModel):
    data: dict
    code: str
