from __future__ import annotations

import pandas as pd
from fastapi import FastAPI, HTTPException

from api.schemas import PredictRequest, PredictResponse
from src.preprocessing import validate_schema, parse_timestamp, build_features, transform
from src.registry import latest, load_registered

app = FastAPI(title="Anomaly Detection API", version="0.1.0")

def _load_latest():
    reg = latest(prefix="anomaly")
    if reg is None:
        raise RuntimeError("No registered model found. Train a model first.")
    bundle = load_registered(reg.model_id)
    return reg.model_id, bundle["model"], bundle["preprocess"]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    try:
        model_id, model, prep = _load_latest()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    df = pd.DataFrame([r.model_dump() for r in req.rows])
    # validate & features
    validate_schema(df)
    df = parse_timestamp(df)
    feats = build_features(df)

    X = transform(feats, prep)
    preds = model.predict(X).tolist()  # 1 normal, -1 anomaly

    return PredictResponse(model_id=model_id, predictions=preds)
