import pytest
from app.database import SessionLocal
from app import models

def test_no_orphaned_orders():
    """Verify every order has a valid user and product."""
    db = SessionLocal()
    try:
        orders = db.query(models.Order).all()
        for order in orders:
            user = db.query(models.User).filter(models.User.id == order.user_id).first()
            product = db.query(models.Product).filter(models.Product.id == order.product_id).first()
            assert user is not None, f"Order {order.id} has orphaned user_id {order.user_id}"
            assert product is not None, f"Order {order.id} has orphaned product_id {order.product_id}"
    finally:
        db.close()

def test_no_duplicate_emails():
    """Verify all user emails are unique in the DB."""
    db = SessionLocal()
    try:
        users = db.query(models.User).all()
        emails = [user.email for user in users]
        assert len(emails) == len(set(emails)), "Duplicate emails found in database!"
    finally:
        db.close()

def test_all_products_have_positive_prices():
    """Verify all products in DB have a price greater than zero."""
    db = SessionLocal()
    try:
        products = db.query(models.Product).all()
        for product in products:
            assert product.price > 0, f"Product '{product.name}' has invalid price {product.price}"
    finally:
        db.close()

def test_all_users_have_valid_emails():
    """Verify all user emails in DB contain an @ symbol."""
    db = SessionLocal()
    try:
        users = db.query(models.User).all()
        for user in users:
            assert "@" in user.email, f"User '{user.name}' has invalid email {user.email}"
    finally:
        db.close()

def test_product_stock_non_negative():
    """Verify no product has negative stock."""
    db = SessionLocal()
    try:
        products = db.query(models.Product).all()
        for product in products:
            assert product.stock >= 0, f"Product '{product.name}' has negative stock {product.stock}"
    finally:
        db.close()

def test_orders_have_positive_quantity():
    """Verify all orders have a quantity of at least 1."""
    db = SessionLocal()
    try:
        orders = db.query(models.Order).all()
        for order in orders:
            assert order.quantity > 0, f"Order {order.id} has invalid quantity {order.quantity}"
    finally:
        db.close()
