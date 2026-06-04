from pydantic import BaseModel


class StreamRequest(BaseModel):
    question: str