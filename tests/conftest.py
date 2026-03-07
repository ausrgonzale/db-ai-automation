import pytest
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import models
from data_gen.ai_generator import generate_ai_products, generate_fake_users

@pytest.fixture(scope="session", autouse=True)
def seed_database():
    """Drops and recreates all tables, then seeds with AI-generated data."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()
    try:
        # Seed users
        users = generate_fake_users(5)
        user_objects = [models.User(**u) for u in users]
        db.add_all(user_objects)
        db.commit()

        # Seed products (AI-generated)
        products = generate_ai_products(5)
        product_objects = [models.Product(**p) for p in products]
        db.add_all(product_objects)
        db.commit()

        print("\n✅ Database seeded with AI-generated data")
    finally:
        db.close()

    yield  # Tests run here

    Base.metadata.drop_all(bind=engine)
    print("\n🧹 Database cleaned up")
