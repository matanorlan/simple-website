import json
from app.main import app

def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_version_endpoint():
    client = app.test_client()
    res = client.get("/version")
    assert res.status_code == 200
    data = res.get_json()
    assert "version" in data
