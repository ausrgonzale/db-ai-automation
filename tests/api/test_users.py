import httpx
import pytest

BASE_URL = "http://localhost:8000"

def test_get_all_users():
    response = httpx.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_user_by_id():
    response = httpx.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    user = response.json()
    assert "name" in user
    assert "email" in user

def test_user_not_found():
    response = httpx.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404

def test_users_have_valid_emails():
    response = httpx.get(f"{BASE_URL}/users")
    users = response.json()
    for user in users:
        assert "@" in user["email"], f"User {user['name']} has invalid email"
