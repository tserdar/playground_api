"""Init file for routes."""

from api.routes.chat import router as chat_router
from api.routes.face import router as face_router
from api.routes.ocr import router as ocr_router

__all__ = ["chat_router", "face_router", "ocr_router"]
