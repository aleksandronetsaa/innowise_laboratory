# tests/test_api.py
# --- ----
# Simple tests for API

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_book():
    resp = client.post("/books/", json={"title": "Test Book", "author": "Author", "year": 2020})
    assert resp.status_code == 200
    data = resp.json()
    book_id = data["id"]

    resp = client.get(f"/books/{book_id}")
    assert resp.status_code == 200

    resp = client.delete(f"/books/{book_id}")
    assert resp.status_code == 200
    assert resp.json()["ok"] is True
