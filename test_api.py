import pytest
from fastapi.testclient import TestClient
import main

@pytest.fixture
def client():
    main.products.clear()
    main.next_id = 1
    return TestClient(main.app)

def test_create_product(client):
    r = client.post("/products", json={"name": "Terrarium", "price": 250})
    assert r.status_code == 201
    assert r.json()["id"] == 1

def test_invalid_price(client):
    r = client.post("/products", json={"name": "Terrarium", "price": "abc"})
    assert r.status_code == 422

def test_delete_missing_product(client):
    r = client.delete("/products/99")
    assert r.status_code == 404

def test_find_product(client):
    client.post("/products", json={"name": "Terrarium", "price": 301})
    r =  client.get("/products/1")
    assert r.json()["name"] == "Terrarium"
    assert r.json()["price"] == 301

