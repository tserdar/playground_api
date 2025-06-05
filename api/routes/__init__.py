"""Init file for routes."""

from api.routes.face import router as face_router
from api.routes.ocr import router as ocr_router

__all__ = ["face_router", "ocr_router"]
