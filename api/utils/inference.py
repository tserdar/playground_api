"""Inference-related utility functions that are used more than one place."""

from pathlib import Path

import cv2
import numpy as np


def read_image_from_path(impath: str | Path) -> np.ndarray:
    """Read an image from a given file path and resize it to a default size.

    Args:
        impath (str | Path): Path to the image file.

    Returns:
        np.ndarray: The loaded and resized image as a NumPy array.

    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the image cannot be read (e.g., unsupported format).

    """
    if not isinstance(impath, Path):
        impath = Path(impath)

    if not impath.exists():
        raise FileNotFoundError

    img = cv2.imread(str(impath.resolve()))
    if img is None:
        raise ValueError

    return resize_image(img)


def resize_image(img: np.ndarray, size: tuple[int] = (640, 640)) -> np.ndarray:
    """Resize an image to a target size using linear interpolation.

    Args:
        img (np.ndarray): Input image.
        size (tuple): Desired size as (width, height).

    Returns:
        np.ndarray: The resized image.

    """
    return cv2.resize(img, size, interpolation=cv2.INTER_LINEAR)
