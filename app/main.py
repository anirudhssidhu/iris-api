from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import storage
import joblib, os, tempfile

app = FastAPI(title="Iris API", version="1.0")

BUCKET = os.getenv("GCS_BUCKET", "mlops-course-vocal-marking-473407-c4-unique")
BLOB   = os.getenv("MODEL_BLOB", "my-models/iris-classifier-week-1/model.joblib")

def load_model_from_gcs(bucket: str, blob: str):
    client = storage.Client()
    b = client.bucket(bucket).blob(blob)
    with tempfile.NamedTemporaryFile(delete=False) as f:
        b.download_to_filename(f.name)
        model = joblib.load(f.name)
    return model

try:
    model = load_model_from_gcs(BUCKET, BLOB)
    MODEL_READY = True
except Exception as e:
    print(f"[WARN] Could not load model: {e}")
    model, MODEL_READY = None, False

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/healthz")
def health():
    return {"status": "ok", "model_ready": MODEL_READY}

@app.post("/predict")
def predict(x: IrisFeatures):
    if not MODEL_READY:
        return {"error": "model not loaded"}
    X = [[x.sepal_length, x.sepal_width, x.petal_length, x.petal_width]]
    y = model.predict(X).tolist()
    return {"prediction": y[0]}
