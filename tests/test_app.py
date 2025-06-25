from http.client import responses

import pytest

from app.main import app

@pytest.fixture
def client():
    app.config
    with app.test_client() as client:
        yield client
def test_version_endpoint(client):
    response = client.get('/version')
    assert response.status_code == 200
    assert response.json == {"version": "0.1.0"}

def test_healthz_endpoint(client):
    response = client.get('/healthz')
    assert response.status_code == 200
    assert response.json == {"status": "healthy", "message": "API is running"}

def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to HiveBox API" in response.data




