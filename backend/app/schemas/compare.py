from pydantic import BaseModel


class CompareRequest(BaseModel):
    video_a_url: str
    video_b_url: str