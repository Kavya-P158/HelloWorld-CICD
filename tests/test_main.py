# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app
 
client = TestClient(app)
 
def test_say_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello world from FastAPI"
 
def test_hello_name():
    response = client.get("/hello/FastAPI")
    assert response.status_code == 200
    assert response.json() == "HEllo FastAPI"
