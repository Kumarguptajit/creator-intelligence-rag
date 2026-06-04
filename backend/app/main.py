from fastapi import FastAPI

from app.routes.comparison import (
    router as comparison_router
)

app = FastAPI()

app.include_router(
    comparison_router
)

@app.get("/")
def health():

    return {
        "status": "ok"
    }