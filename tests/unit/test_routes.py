import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from app.main import app

client = TestClient(app)


def test_get_users_returns_200():
    """GET /users should return 200."""
    response = client.get("/users")
    assert response.status_code == 200


def test_get_products_returns_200():
    """GET /products should return 200."""
    response = client.get("/products")
    assert response.status_code == 200


def test_get_orders_returns_200():
    """GET /orders should return 200."""
    response = client.get("/orders")
    assert response.status_code == 200


def test_get_nonexistent_user_returns_404():
    """GET /users/{id} with invalid id should return 404."""
    response = client.get("/users/99999")
    assert response.status_code == 404


def test_get_nonexistent_product_returns_404():
    """GET /products/{id} with invalid id should return 404."""
    response = client.get("/products/99999")
    assert response.status_code == 404


def test_create_order_zero_quantity_returns_400():
    """POST /orders with zero quantity should return 400."""
    response = client.post("/orders?user_id=1&product_id=1&quantity=0")
    assert response.status_code == 400


def test_create_order_negative_quantity_returns_400():
    """POST /orders with negative quantity should return 400."""
    response = client.post("/orders?user_id=1&product_id=1&quantity=-5")
    assert response.status_code == 400
