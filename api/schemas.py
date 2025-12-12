from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field

class Row(BaseModel):
    timestamp: str = Field(..., description="ISO timestamp, e.g. 2025-01-01T00:00:00")
    x1: float
    x2: float
    x3: float

class PredictRequest(BaseModel):
    rows: List[Row]

class PredictResponse(BaseModel):
    model_id: str
    predictions: List[int]  # 1 normal, -1 anomaly
