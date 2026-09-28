from fastapi import FastAPI
from pydantic import BaseModel
from cache import cache_get, cache_set
from eta_model import predict_eta
import time, itertools
app = FastAPI(title="Zomato-style Backend Scale - Charan Teja")
_orders = {}
_id = itertools.count(1)
class Order(BaseModel):
    restaurant: str
    dist_km: float
    prep_min: float
@app.get("/")
def root(): return {"status": "ok", "ai": "ETA predictor + cache + scale notes"}
@app.post("/orders")
def create(o: Order):
    oid = next(_id)
    key = f"eta:{o.dist_km}:{o.prep_min}"
    cached = cache_get(key)
    if cached is None:
        eta = predict_eta(o.dist_km, o.prep_min)
        cache_set(key, str(eta))
    else:
        eta = float(cached)
    _orders[oid] = {"id": oid, "restaurant": o.restaurant, "eta_min": round(eta, 1), "status": "PREPARING", "ts": time.time()}
    return _orders[oid]
@app.get("/orders/{oid}")
def get(oid: int): return _orders.get(oid, {"error": "not found"})
@app.get("/orders")
def list_orders(): return list(_orders.values())
