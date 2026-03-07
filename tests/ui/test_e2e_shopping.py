from playwright.sync_api import Page
import httpx
import pytest

BASE_URL = "http://localhost:8000"
DOCS_URL = f"{BASE_URL}/docs"

def test_e2e_swagger_ui_place_order(page: Page):
    """End-to-end test through the Swagger UI — place a real order via the browser."""
    # Navigate to docs
    page.goto(DOCS_URL)
    assert "DB AI Automation API" in page.title()

    # Expand the POST /orders block
    page.locator("span.opblock-summary-path", has_text="/orders").first.click()
    page.get_by_role("button", name="Try it out").click()

    # Fill in parameters using data-param-name selectors
    page.locator("tr[data-param-name='user_id'] input").fill("1")
    page.locator("tr[data-param-name='product_id'] input").fill("1")
    page.locator("tr[data-param-name='quantity'] input").fill("1")

    page.get_by_role("button", name="Execute").click()
    page.wait_for_timeout(2000)

    # Verify 200 response
    elements = page.locator(".response-col_status").all()
    assert any("200" in el.inner_text() for el in elements), "Order placement did not return 200"
