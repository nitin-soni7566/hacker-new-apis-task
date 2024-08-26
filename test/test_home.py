from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_home():
    response = client.get(
        f"/",
    )
    assert response.status_code == 200
