from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app import models

Base.metadata.create_all(bind=engine)
app = FastAPI(title="DB AI Automation API")

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/orders")
def create_order(user_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    order = models.Order(user_id=user_id, product_id=product_id, quantity=quantity)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()
