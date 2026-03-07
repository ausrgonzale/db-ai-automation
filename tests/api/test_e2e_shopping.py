import httpx
import pytest

BASE_URL = "http://localhost:8000"

def test_full_shopping_experience():
    """
    Full end-to-end shopping test:
    1. Verify products exist in the store
    2. Pick a product
    3. Verify a user exists
    4. Place an order
    5. Verify the order shows up in order history
    """
    # Step 1 — Get all products
    products_response = httpx.get(f"{BASE_URL}/products")
    assert products_response.status_code == 200
    products = products_response.json()
    assert len(products) > 0, "No products available in the store"

    # Step 2 — Pick the first product
    selected_product = products[0]
    assert selected_product["price"] > 0
    print(f"\n🛒 Selected product: {selected_product['name']} at ${selected_product['price']}")

    # Step 3 — Get a valid user
    users_response = httpx.get(f"{BASE_URL}/users")
    assert users_response.status_code == 200
    users = users_response.json()
    assert len(users) > 0, "No users found"
    shopper = users[0]
    print(f"👤 Shopper: {shopper['name']} ({shopper['email']})")

    # Step 4 — Place the order
    order_response = httpx.post(f"{BASE_URL}/orders", params={
        "user_id": shopper["id"],
        "product_id": selected_product["id"],
        "quantity": 1
    })
    assert order_response.status_code == 200
    order = order_response.json()
    print(f"✅ Order placed! Order ID: {order['id']}")

    # Step 5 — Verify the order appears in order history
    orders_response = httpx.get(f"{BASE_URL}/orders")
    assert orders_response.status_code == 200
    all_orders = orders_response.json()
    order_ids = [o["id"] for o in all_orders]
    assert order["id"] in order_ids, f"Order {order['id']} not found in order history!"
    print(f"📋 Order confirmed in history — {len(all_orders)} total orders")
