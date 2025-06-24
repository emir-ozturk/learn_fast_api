# tests/test_users.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_and_get_user(monkeypatch):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json={"email": "a@b.com", "full_name": "Ali Veli"})
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == "a@b.com"

        uid = data["id"]
        response = await ac.get(f"/users/{uid}")
        assert response.status_code == 200
        assert response.json()["full_name"] == "Ali Veli"
