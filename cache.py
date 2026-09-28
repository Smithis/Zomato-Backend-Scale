import time
try:
    import redis
    _r = redis.Redis(host="localhost", port=6379, socket_connect_timeout=1)
    _r.ping()
    HAS_REDIS = True
except Exception:
    HAS_REDIS = False
    _r = None
_cache = {}
def cache_get(k):
    if HAS_REDIS:
        try:
            v = _r.get(k)
            return v.decode() if v else None
        except Exception:
            pass
    v = _cache.get(k)
    if v and v[1] > time.time():
        return v[0]
    return None
def cache_set(k, val, ttl=60):
    if HAS_REDIS:
        try:
            _r.setex(k, ttl, val)
            return
        except Exception:
            pass
    _cache[k] = (val, time.time() + ttl)
