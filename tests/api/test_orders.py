import httpx
import pytest
from app.database import SessionLocal
from app import models

BASE_URL = "http://localhost:8000"

def test_create_order():
    """Place an order and verify it returns 200 with correct fields."""
    response = httpx.post(f"{BASE_URL}/orders", params={
        "user_id": 1,
        "product_id": 1,
        "quantity": 2
    })
    assert response.status_code == 200
    order = response.json()
    assert order["user_id"] == 1
    assert order["product_id"] == 1
    assert order["quantity"] == 2
    assert "id" in order
    assert "created_at" in order

def test_create_order_verified_in_db():
    """Place an order via API then query MySQL directly to confirm the row exists."""
    response = httpx.post(f"{BASE_URL}/orders", params={
        "user_id": 1,
        "product_id": 2,
        "quantity": 3
    })
    assert response.status_code == 200
    order_id = response.json()["id"]

    # Query the DB directly to verify the row exists
    db = SessionLocal()
    try:
        db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
        assert db_order is not None, f"Order {order_id} not found in database!"
        assert db_order.user_id == 1
        assert db_order.product_id == 2
        assert db_order.quantity == 3
    finally:
        db.close()

def test_get_all_orders():
    """Verify the orders endpoint returns a list."""
    response = httpx.get(f"{BASE_URL}/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_order_count_matches_db():
    """Verify the API order count matches the DB count."""
    response = httpx.get(f"{BASE_URL}/orders")
    api_count = len(response.json())

    db = SessionLocal()
    try:
        db_count = db.query(models.Order).count()
        assert api_count == db_count, f"API returned {api_count} orders but DB has {db_count}"
    finally:
        db.close()
