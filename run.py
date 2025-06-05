"""Entry point for the Playground API."""

import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import chat_router, face_router, ocr_router

load_dotenv()

app = FastAPI(title="Playground API")

allowed_origin_striped = os.environ.get("ALLOWED_ORIGIN_STRIPED", "")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        f"http://{allowed_origin_striped}",
        f"https://{allowed_origin_striped}",
        f"http://www.{allowed_origin_striped}",
        f"https://www.{allowed_origin_striped}",
    ],
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
