from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.routes.comparison import (
    router as comparison_router
)

from app.routes.chat import (
    router as chat_router
)

from app.routes.stream import (
    router as stream_router
)

from app.routes.context import (
    router as context_router
)

from app.routes.thumbnail import router as thumbnail_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    comparison_router,
)
app.include_router(
    chat_router
)

app.include_router(
    stream_router
)

app.include_router(
    context_router
)

app.include_router(thumbnail_router)

@app.get("/")
def health():

    return {
        "status": "ok"
    }