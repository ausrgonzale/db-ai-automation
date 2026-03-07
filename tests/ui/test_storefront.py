from playwright.sync_api import Page
import pytest

BASE_URL = "http://localhost:8000/docs"

def test_swagger_ui_loads(page: Page):
    """Verify the Swagger UI loads and has the correct title."""
    page.goto(BASE_URL)
    assert "DB AI Automation API" in page.title()

def test_products_endpoint_visible(page: Page):
    """Expand GET /products, execute it, and verify a 200 response."""
    page.goto(BASE_URL)
    page.locator("span.opblock-summary-path", has_text="/products").first.click()
    page.get_by_role("button", name="Try it out").click()
    page.get_by_role("button", name="Execute").click()
    page.wait_for_timeout(2000)
    elements = page.locator(".response-col_status").all()
    for el in elements:
        print(f"Found element: '{el.inner_text()}'")
    assert any("200" in el.inner_text() for el in elements)

def test_users_endpoint_visible(page: Page):
    """Expand GET /users, execute it, and verify a 200 response."""
    page.goto(BASE_URL)
    page.locator("span.opblock-summary-path", has_text="/users").first.click()
    page.get_by_role("button", name="Try it out").click()
    page.get_by_role("button", name="Execute").click()
    page.wait_for_timeout(2000)
    elements = page.locator(".response-col_status").all()
    for el in elements:
        print(f"Found element: '{el.inner_text()}'")
    assert any("200" in el.inner_text() for el in elements)

def test_orders_endpoint_visible(page: Page):
    """Expand GET /orders, execute it, and verify a 200 response."""
    page.goto(BASE_URL)
    page.locator("span.opblock-summary-path", has_text="/orders").first.click()
    page.get_by_role("button", name="Try it out").click()
    page.get_by_role("button", name="Execute").click()
    page.wait_for_timeout(2000)
    elements = page.locator(".response-col_status").all()
    for el in elements:
        print(f"Found element: '{el.inner_text()}'")
    assert any("200" in el.inner_text() for el in elements)
