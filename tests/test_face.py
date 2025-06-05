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

    assert response.status_code == HTTP_OK  # noqa: S101
    assert response.json() == {"results": ["face-data"]}  # noqa: S101
    mock_infer.assert_called_once()


@patch("cv2.imencode", return_value=(True, MagicMock(tobytes=lambda: b"img")))
@patch("api.routes.face.RetinaNetWrapper.visualize")
def test_face_visualize(
    mock_visualize: MagicMock,  # noqa: ARG001
    mock_imencode: MagicMock,  # noqa: ARG001
    dummy_image: bytes,
) -> None:
    """Test that /face?visualize=true returns a JPEG image."""
    files = {"file": ("face.jpg", dummy_image, "image/jpeg")}
    response = client.post("/face?visualize=true", files=files)

    assert response.status_code == HTTP_OK  # noqa: S101
    assert response.headers.get("content-type") == "image/jpeg"  # noqa: S101
