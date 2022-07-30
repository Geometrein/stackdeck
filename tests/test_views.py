from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


def test_grid_search():
    response = client.get("/search/")
    assert response.status_code == 200


def test_dashboard():
    response = client.get("/deck/dashboard")
    assert response.status_code == 200


def test_docs():
    response = client.get("/docs/")
    assert response.status_code == 200


def test_not_existing_page():
    response = client.get("/EndpointThatDoesntExist/")
    assert response.status_code == 404
