"""Unit tests for the /face API route in the Playground API."""

from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from run import app

client = TestClient(app)

HTTP_OK: int = 200


@pytest.fixture(name="dummy_image")
def fixture_dummy_image() -> bytes:
    """Return dummy bytes to simulate an uploaded image."""
    return b"face-image"


@patch("api.routes.face.RetinaNetWrapper.infer", return_value=["face-data"])
def test_face_infer(mock_infer: MagicMock, dummy_image: bytes) -> None:
    """Test that /face?visualize=false returns expected JSON."""
    files = {"file": ("face.jpg", dummy_image, "image/jpeg")}
    response = client.post("/face?visualize=false", files=files)

    if response.status_code != HTTP_OK:
        pytest.fail(f"Expected 200 OK, got {response.status_code}")
    if response.json() != {"results": ["face-data"]}:
        pytest.fail(f"Unexpected response body: {response.json()}")

    mock_infer.assert_called_once()


@patch("cv2.imencode", return_value=(True, MagicMock(tobytes=lambda: b"img")))
def test_face_visualize(dummy_image: bytes) -> None:
    """Test that /face?visualize=true returns a JPEG image."""
    files = {"file": ("face.jpg", dummy_image, "image/jpeg")}
    response = client.post("/face?visualize=true", files=files)

    if response.status_code != HTTP_OK:
        pytest.fail(f"Expected 200 OK, got {response.status_code}")
    content_type = response.headers.get("content-type")
    if content_type != "image/jpeg":
        pytest.fail(f"Expected image/jpeg, got {content_type}")
