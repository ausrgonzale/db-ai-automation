import anthropic
import json
from faker import Faker
from dotenv import load_dotenv

load_dotenv()
fake = Faker()
client = anthropic.Anthropic()

def generate_ai_products(count: int = 5) -> list[dict]:
    """Ask Claude to generate realistic product data as JSON."""
    prompt = f"""Generate {count} fake e-commerce products as a JSON array.
    Each product must have: name, description (1-2 sentences), price (float), stock (int 1-100).
    Return ONLY valid JSON, no explanation, no markdown backticks."""
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(message.content[0].text)

def generate_fake_users(count: int = 5) -> list[dict]:
    """Use Faker to generate user data."""
    return [
        {"name": fake.name(), "email": fake.unique.email()}
        for _ in range(count)
    ]

def generate_edge_case_products() -> list[dict]:
    """Ask Claude to generate invalid/edge case product data for negative testing."""
    prompt = """Generate a JSON array of 5 intentionally invalid e-commerce products for negative testing.
    Include edge cases like: empty name, negative price, zero stock, extremely long description (500+ chars), 
    price as string instead of float, missing fields.
    Return ONLY valid JSON array, no explanation, no markdown backticks."""
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(message.content[0].text)

def generate_edge_case_users() -> list[dict]:
    """Ask Claude to generate invalid user data for negative testing."""
    prompt = """Generate a JSON array of 5 intentionally invalid users for negative testing.
    Include edge cases like: missing email, invalid email format (no @), empty name,
    extremely long name (200+ chars), special characters in name.
    Return ONLY valid JSON array, no explanation, no markdown backticks."""
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(message.content[0].text)
