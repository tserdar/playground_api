"""Unit tests for the /ocr API route in the Playground API."""

from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from run import app

client = TestClient(app)

HTTP_OK: int = 200


@pytest.fixture(name="dummy_image")
def fixture_dummy_image() -> bytes:
    """Return dummy bytes to simulate an uploaded image."""
    return b"fake-image-bytes"


@patch("api.routes.ocr.EasyOCRWrapper.infer", return_value=["text"])
def test_ocr_infer(mock_infer: MagicMock, dummy_image: bytes) -> None:
    """Test that /ocr?visualize=false returns expected JSON."""
    files = {"file": ("test.jpg", dummy_image, "image/jpeg")}
    response = client.post("/ocr?visualize=false", files=files)

    if response.status_code != HTTP_OK:
        pytest.fail(f"Expected {HTTP_OK}, got {response.status_code}")
    if response.json() != {"results": ["text"]}:
        pytest.fail(f"Unexpected response: {response.json()}")

    mock_infer.assert_called_once()


@patch("cv2.imencode", return_value=(True, MagicMock(tobytes=lambda: b"img")))
@patch("api.routes.ocr.EasyOCRWrapper.visualize")
def test_ocr_visualize(
    mock_visualize: MagicMock,  # noqa: ARG001
    mock_imencode: MagicMock,  # noqa: ARG001
    dummy_image: bytes,
) -> None:
    """Test that /ocr?visualize=true returns a JPEG response."""
    files = {"file": ("test.jpg", dummy_image, "image/jpeg")}
    response = client.post("/ocr?visualize=true", files=files)

    if response.status_code != HTTP_OK:
        pytest.fail(f"Expected {HTTP_OK}, got {response.status_code}")
    content_type = response.headers.get("content-type")
    if content_type != "image/jpeg":
        pytest.fail(f"Expected image/jpeg, got {content_type}")
