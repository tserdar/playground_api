"""Entry point for the Playground API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import chat_router, face_router, ocr_router

app = FastAPI(title="Playground API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],  # Only what's needed
    allow_headers=["*"],
)

# Mount OCR routes — no prefix since route path is already /ocr
app.include_router(ocr_router, tags=["OCR"])
app.include_router(face_router, tags=["Face"])
app.include_router(chat_router, tags=["Chat"])


@app.get("/")
def root() -> dict:
    """Test."""
    return {"message": "Welcome to the Playground API"}
