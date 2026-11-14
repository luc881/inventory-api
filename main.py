from decimal import Decimal
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Product
from schemas import ProductCreate, ProductRead

app = FastAPI()

@app.post("/products", response_model=ProductRead, status_code=201)
def create(data: ProductCreate, db: Session = Depends(get_db)):
    product = Product(name=data.name, price=data.price)    # esquema -> objeto del ORM
    db.add(product)
    db.commit()
    db.refresh(product)                                    # trae el id que asignó PostgreSQL
    return product

@app.get("/products", response_model=list[ProductRead])
def list_products(max_price: Decimal | None = None, db: Session = Depends(get_db)):
    stmt = select(Product)
    if max_price is not None:
        stmt = stmt.where(Product.price <= max_price)
    return db.scalars(stmt.order_by(Product.id)).all()     # ORDER BY: sin él el orden no está garantizado

@app.get("/products/{pid}", response_model=ProductRead)
def get_product(pid: int, db: Session = Depends(get_db)):
    product = db.get(Product, pid)
    if product is None:
        raise HTTPException(status_code=404, detail="Not found")
    return product

@app.put("/products/{pid}", response_model=ProductRead)
def replace(pid: int, data: ProductCreate, db: Session = Depends(get_db)):
    product = db.get(Product, pid)
    if product is None:
        raise HTTPException(status_code=404, detail="Not found")
    product.name = data.name
    product.price = data.price
    db.commit()
    db.refresh(product)
    return product

@app.delete("/products/{pid}", status_code=204)
def delete(pid: int, db: Session = Depends(get_db)):
    product = db.get(Product, pid)
    if product is None:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(product)
    db.commit()