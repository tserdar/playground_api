"""Entry point for the Playground API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import face_router, ocr_router

app = FastAPI(title="Playground API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],  # Or ["POST"] for just what's needed
    allow_headers=["*"],
)

# Mount OCR routes — no prefix since route path is already /ocr
app.include_router(ocr_router, tags=["OCR"])
app.include_router(face_router, tags=["Face"])


@app.get("/")
def root() -> dict:
    """Test."""
    return {"message": "Welcome to the Playground API"}
