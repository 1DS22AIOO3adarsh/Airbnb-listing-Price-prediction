from fastapi import FastAPI
import joblib
import pandas as pd
from prometheus_fastapi_instrumentator import Instrumentator
# Load pipeline
pipeline = joblib.load("model.pkl")

# Create app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Airbnb Price Prediction API is running!"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = pipeline.predict(df)[0]
    return {"predicted_log_price": prediction}

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)
