import pytest
from app.models import User, Product, Order


def test_user_model_instantiation():
    """User model should instantiate with name and email."""
    user = User(name="Ron Gonzalez", email="ron@example.com")
    assert user.name == "Ron Gonzalez"
    assert user.email == "ron@example.com"


def test_product_model_instantiation():
    """Product model should instantiate with required fields."""
    product = Product(name="Widget", description="A nice widget.", price=9.99, stock=50)
    assert product.name == "Widget"
    assert product.price == 9.99
    assert product.stock == 50


def test_order_model_instantiation():
    """Order model should instantiate with user_id, product_id, quantity."""
    order = Order(user_id=1, product_id=1, quantity=3)
    assert order.user_id == 1
    assert order.product_id == 1
    assert order.quantity == 3


def test_product_price_is_float():
    """Product price should be stored as a float."""
    product = Product(name="Widget", description="A widget.", price=19.99, stock=10)
    assert isinstance(product.price, float)


def test_order_quantity_is_int():
    """Order quantity should be stored as an int."""
    order = Order(user_id=1, product_id=1, quantity=5)
    assert isinstance(order.quantity, int)
