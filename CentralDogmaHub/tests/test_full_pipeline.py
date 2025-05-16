from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the Bioinformatics API!" in response.json()["message"]

# pwd = /home/vartika/FASTAPI
# export PYTHONPATH=$PWD
# pytest
