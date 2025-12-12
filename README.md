# 🚨 Production-Oriented Anomaly Detection Pipeline



End-to-end anomaly detection system designed with **production constraints** in mind.  

This project emphasizes **reliability, reproducibility, and deployment readiness** rather than notebook-only experimentation.



---



## 🔍 Why This Project?



In real-world systems (IoT, monitoring, finance, manufacturing):



- anomalies are **rare but costly**

- labels are often **unavailable**

- **data issues** break pipelines more often than models



This project treats anomaly detection as a **system-level problem**, not just a modeling task.



---



## 🏗 System Architecture

Raw Data

↓

Schema Validation

↓

Preprocessing

↓

Feature Engineering

↓

Model Training

↓

Evaluation

↓

Model Registry

↓

FastAPI Inference Service

**Design goals**

- deterministic pipelines

- modular components

- easy model replacement

- reproducible execution



---



## 📊 Data Pipeline



### Data Ingestion

- Time-series data simulating sensor / log signals

- Controlled anomaly injection for validation



### Data Validation

- Explicit schema checks

- Strict timestamp parsing



> In production, **data reliability matters more than model complexity**.



---



## 🧠 Feature Engineering



Features are intentionally simple and interpretable:



- raw signals: `x1`, `x2`, `x3`

- temporal context: `hour`, `dayofweek`



All transformations are:

- deterministic

- shared between training and inference



---



## 🤖 Model Training



**Baseline model**

- Isolation Forest (unsupervised)



**Why Isolation Forest?**

- works without labeled anomalies

- fast inference

- commonly used in production monitoring systems



The training logic is **fully decoupled** from:

- data ingestion

- API serving



This allows model changes without system refactoring.



---



## 📦 Model Registry



Each trained model is:



- versioned with a unique ID

- saved with preprocessing artifacts

- stored alongside metadata (features, seed, data source)



This enables:

- reproducibility

- rollback

- auditability



---



## 📈 Evaluation



Evaluation focuses on:



- anomaly rate stability

- pipeline correctness

- failure detection



Rather than optimizing a single metric, the goal is **consistent system behavior**.



---



## 🚀 API Serving



Inference is exposed via **FastAPI**.



**Endpoints**

- `GET /health` – service health check

- `POST /predict` – batch anomaly inference



**Example request**

```json

{

  "rows": [

    {

      "timestamp": "2025-01-01T00:00:00",

      "x1": 0.1,

      "x2": 0.2,

      "x3": 0.3

    }

  ]

}

```



---



## 🔁 Reproducibility



Run the full pipeline locally:

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt



python -m src.ingestion --out data/raw/sample.csv

python -m src.train --data data/raw/sample.csv

python -m src.evaluate --data data/raw/sample.csv



uvicorn api.main:app --reload



---



## ⚖️ Design Trade-offs



- prioritizes clarity and modularity over maximum accuracy
- local-first MLOps (no cloud dependency)
- minimal tooling to ensure portability



---



## 🔮 Future Improvements



- data drift detection
- online inference optimization
- feature store integration
- CI-based model validation
