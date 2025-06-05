"""Unit tests for the root route of the Playground API."""

import pytest
from fastapi.testclient import TestClient

from run import app

client = TestClient(app)

HTTP_OK: int = 200


def test_root() -> None:
    """Test that the root endpoint returns the welcome message."""
    response = client.get("/")

    if response.status_code != HTTP_OK:
        pytest.fail(f"Expected {HTTP_OK}, got {response.status_code}")
    expected = {"message": "Welcome to the Playground API"}
    if response.json() != expected:
        pytest.fail(f"Unexpected response body: {response.json()}")
