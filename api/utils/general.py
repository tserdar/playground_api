"""General utility functions that are used more than one place."""

import shutil
from pathlib import Path

from fastapi import UploadFile


def save_upload_file(upload_file: UploadFile, destination: Path) -> None:
    """Save uploaded file to disk."""
    with destination.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
