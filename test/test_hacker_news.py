from fastapi.testclient import TestClient
from src.main import app
import pytest

client = TestClient(app)

COUNT = [10, 5, 15, 5, 15, 10]


@pytest.mark.parametrize("count", COUNT)
def test_new_api(count):
    response = client.get(
        f"/top-news?count={count}",
    )
    assert response.status_code == 200
