# app/routes/thumbnail.py

import requests

from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()


@router.get("/thumbnail")
def thumbnail(url: str):

    r = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    return Response(
        content=r.content,
        media_type=r.headers.get(
            "Content-Type",
            "image/jpeg"
        )
    )