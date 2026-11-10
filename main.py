from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
products = {}
next_id = 1

class Product(BaseModel):
    name: str
    price: float

@app.post("/products", status_code=201)
def create(p: Product):
    global next_id
    products[next_id] = p.model_dump()
    next_id += 1
    return {"id": next_id - 1, **p.model_dump()}

@app.get("/products")
def list_products(max_price: float | None = None):
    if max_price is None:                       # sin ?max_price: devuelve todo
        return products
    filtered = {}
    for pid, product in products.items():       # pid = id, product = {"name": ..., "price": ...}
        if product["price"] <= max_price:
            filtered[pid] = product
    return filtered

@app.get("/products/{pid}")
def get_product(pid: int):
    if pid not in products:
        raise HTTPException(status_code=404, detail="Not found")
    return products[pid]

@app.put("/products/{pid}")
def replace(pid: int, p: Product):
    products[pid] = p.model_dump()
    return {"id": pid, **p.model_dump()}

@app.delete("/products/{pid}", status_code=204)
def delete(pid: int):
    if pid not in products:
        raise HTTPException(status_code=404, detail="Not found")
    del products[pid]
