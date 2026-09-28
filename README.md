# Zomato-style Backend Scale (AI in ship loop) - Charan Teja
Gurgaon on-site backend: ownership, scale, AI built-in.

## Run
```bash
pip install -r requirements.txt
pytest -q
uvicorn app:app --reload
```

## What maps to JD
- Backend scale: FastAPI orders, cache (Redis-if-present else TTL), list/get, Docker
- AI built-in: ETA regressor (dist+prep->eta) cached per quote; anomaly/fraud pattern in Stripe-Anomaly repo
- Ownership: tests, tradeoffs in docs/SCALE.md (Postgres + Redis + queue next)
```
