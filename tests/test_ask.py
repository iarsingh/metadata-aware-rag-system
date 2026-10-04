from fastapi.testclient import TestClient
from metarag.main import app

client = TestClient(app)


def test_answers_and_refuses():
    hit = client.post("/ask", json={"question": 'When should you fail over the primary?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == "runbook"
    miss = client.post("/ask", json={"question": 'cafeteria'}).json()
    assert miss["answered"] is False


def test_empty_is_refused():
    assert client.post("/ask", json={"question": " "}).status_code == 422
