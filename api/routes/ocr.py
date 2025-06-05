"""API route for /ocr."""

import logging
import uuid
from io import BytesIO
from pathlib import Path
from typing import Annotated

import cv2
from fastapi import APIRouter, File, Query, UploadFile
from fastapi.responses import JSONResponse, Response, StreamingResponse

from api.modules.ocr.models import EasyOCRWrapper
from api.utils.general import save_upload_file

logger = logging.getLogger(__name__)
router = APIRouter()
ocr_model = EasyOCRWrapper()


@router.post("/ocr")
async def run_ocr(
    file: Annotated[UploadFile, File()],
    *,
    visualize: Annotated[bool, Query()] = False,
) -> Response:
    """Extract text from an uploaded image using OCR.

    Optionally returns a visualization filename if requested.
    """
    temp_dir = Path("temp")
    temp_dir.mkdir(exist_ok=True)
    suffix = Path(file.filename).suffix
    temp_path = temp_dir / f"{uuid.uuid4().hex}{suffix}"

    try:
        save_upload_file(file, temp_path)

        if visualize:
            image = ocr_model.visualize(temp_path)

            success, encoded_image = cv2.imencode(".jpg", image)
            if not success:
                return JSONResponse(status_code=500, content={"error": "Failed to encode image."})

            buffer = BytesIO(encoded_image.tobytes())
            return StreamingResponse(
                content=buffer,
                media_type="image/jpeg",
                headers={"Content-Disposition": "inline; filename=visualization.jpg"},
            )

        results = ocr_model.infer(temp_path)
        return JSONResponse(content={"results": results})

    finally:
        if temp_path.exists():
            try:
                temp_path.unlink()
            except OSError as e:
                logger.warning("Failed to delete temp file %s: %s", temp_path, e)
