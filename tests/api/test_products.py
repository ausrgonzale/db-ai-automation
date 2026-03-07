import httpx
import pytest

BASE_URL = "http://localhost:8000"

def test_get_all_products():
    response = httpx.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0
    assert "name" in products[0]
    assert "price" in products[0]

def test_products_have_valid_prices():
    response = httpx.get(f"{BASE_URL}/products")
    products = response.json()
    for product in products:
        assert product["price"] > 0, f"Product {product['name']} has invalid price"

def test_products_have_stock():
    response = httpx.get(f"{BASE_URL}/products")
    products = response.json()
    for product in products:
        assert product["stock"] >= 0

def test_get_product_by_id():
    response = httpx.get(f"{BASE_URL}/products/1")
    assert response.status_code == 200
    product = response.json()
    assert "name" in product
    assert "price" in product

def test_product_not_found():
    response = httpx.get(f"{BASE_URL}/products/99999")
    assert response.status_code == 404
