import numpy as np
from sklearn.linear_model import LinearRegression
_model = None
def train():
    global _model
    rng = np.random.default_rng(5)
    dist = rng.uniform(0.5, 12.0, 300)
    prep = rng.uniform(5, 30, 300)
    eta = 8 + 3.2*dist + 0.9*prep + rng.normal(0, 2, 300)
    X = np.column_stack([dist, prep])
    _model = LinearRegression().fit(X, eta)
    return _model
def predict_eta(dist_km: float, prep_min: float) -> float:
    global _model
    if _model is None:
        train()
    return float(_model.predict([[dist_km, prep_min]])[0])
