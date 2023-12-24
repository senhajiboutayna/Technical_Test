import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_question(client):
    response = client.post('/ask/TestQuestion')

    assert response.status_code == 200
    assert 'answer' in response.json

def test_error(client):
    response = client.post('/ask/TestQuestionError')

    assert response.status_code != 200
    assert 'answer' not in response.json

def test_favicon(client):
    response = client.get('/favicon.ico')

    assert response.status_code == 200
    assert response.data == b'Favicon requested'

