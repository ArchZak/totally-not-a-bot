from pydantic import BaseModel


class Message(BaseModel):
    content: str
    author_id: int
    channel_id: int
    timestamp: str
