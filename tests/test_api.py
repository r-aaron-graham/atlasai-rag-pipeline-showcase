from fastapi.testclient import TestClient

from serve.main import app


def test_fixture_cites_and_abstains(monkeypatch):
    monkeypatch.delenv("ATLASAI_PROVIDER", raising=False)
    client = TestClient(app)
    matched = client.post("/ask", json={"query": "What is the retention policy?"})
    assert matched.status_code == 200
    assert matched.json()["sources"] == ["fixture-retention"]
    assert "30 days" in matched.json()["response"]
    unmatched = client.post("/ask", json={"query": "Who runs payroll?"})
    assert unmatched.json() == {"response": None, "sources": []}
    assert client.post("/ask", json={"query": ""}).status_code == 422
