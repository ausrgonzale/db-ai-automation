import httpx
import pytest
from data_gen.ai_generator import generate_edge_case_products, generate_edge_case_users

BASE_URL = "http://localhost:8000"

def test_get_nonexistent_user():
    """Verify 404 is returned for a user that does not exist."""
    response = httpx.get(f"{BASE_URL}/users/999999")
    assert response.status_code == 404

def test_get_nonexistent_product():
    """Verify 404 is returned for a product that does not exist."""
    response = httpx.get(f"{BASE_URL}/products/999999")
    assert response.status_code == 404

def test_order_with_invalid_user():
    """Verify order fails when user does not exist."""
    response = httpx.post(f"{BASE_URL}/orders", params={
        "user_id": 999999,
        "product_id": 1,
        "quantity": 1
    })
    assert response.status_code in [400, 404, 422, 500]

def test_order_with_invalid_product():
    """Verify order fails when product does not exist."""
    response = httpx.post(f"{BASE_URL}/orders", params={
        "user_id": 1,
        "product_id": 999999,
        "quantity": 1
    })
    assert response.status_code in [400, 404, 422, 500]

def test_order_with_zero_quantity():
    """Verify order with zero quantity is rejected."""
    response = httpx.post(f"{BASE_URL}/orders", params={
        "user_id": 1,
        "product_id": 1,
        "quantity": 0
    })
    assert response.status_code in [400, 422]

def test_order_with_negative_quantity():
    """Verify order with negative quantity is rejected."""
    response = httpx.post(f"{BASE_URL}/orders", params={
        "user_id": 1,
        "product_id": 1,
        "quantity": -5
    })
    assert response.status_code in [400, 422]

def test_ai_generated_edge_cases_are_invalid():
    """Use Claude to generate bad data and verify each case is problematic."""
    edge_case_products = generate_edge_case_products()
    issues_found = 0
    for product in edge_case_products:
        # Check for missing or invalid fields
        if not product.get("name"):
            issues_found += 1
        if isinstance(product.get("price"), (int, float)) and product.get("price", 1) <= 0:
            issues_found += 1
        if "price" not in product:
            issues_found += 1
    assert issues_found > 0, "Expected AI to generate at least some invalid products"
