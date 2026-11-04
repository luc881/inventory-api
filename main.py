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
def list_products():
    return products

@app.put("/products/{pid}")
def replace(pid: int, p: Product):
    products[pid] = p.model_dump()
    return {"id": pid, **p.model_dump()}

@app.delete("/products/{pid}", status_code=204)
def delete(pid: int):
    if pid not in products:
        raise HTTPException(status_code=404, detail="Not found")
    del products[pid]
