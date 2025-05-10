import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login_success(client):
    resp = client.post('/login', json={'username':'user1','password':'password123'})
    assert resp.status_code == 200
    assert 'token' in resp.json

def test_login_failure(client):
    resp = client.post('/login', json={'username':'user1','password':'wrong'})
    assert resp.status_code == 401

def test_health(client):
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.data == b'OK'
