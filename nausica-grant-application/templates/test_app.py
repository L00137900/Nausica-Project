"""Tests for the Flask app using pytest."""
import pytest
from app import app as flask_app


@pytest.fixture
def client():
    """Provide a test client for the Flask app."""
    with flask_app.test_client() as client:
        yield client


def test_home(client):
    """Ensure the home page is accessible and returns HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_about(client):
    """Ensure the about page is accessible and returns HTTP 200."""
    response = client.get("/about")
    assert response.status_code == 200
