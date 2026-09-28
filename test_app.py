from fastapi.testclient import TestClient
from app import app
def test_flow():
    c = TestClient(app)
    assert c.get("/").status_code == 200
    r = c.post("/orders", json={"restaurant": "Biryani House", "dist_km": 4.0, "prep_min": 12})
    assert r.status_code == 200
    oid = r.json()["id"]
    assert c.get(f"/orders/{oid}").status_code == 200
    assert c.get("/orders").status_code == 200
def test_eta_cached():
    c = TestClient(app)
    a = c.post("/orders", json={"restaurant": "X", "dist_km": 4.0, "prep_min": 12}).json()["eta_min"]
    b = c.post("/orders", json={"restaurant": "Y", "dist_km": 4.0, "prep_min": 12}).json()["eta_min"]
    assert a == b
