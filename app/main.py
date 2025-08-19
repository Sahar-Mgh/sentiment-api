from fastapi import FastAPI
from pydantic import BaseModel
import joblib

class Review(BaseModel):
    text: str

app = FastAPI(title="Sentiment Analysis API")

# --- FIX IS HERE ---
# Load the model and vectorizer from the correct path
model = joblib.load('models/sentiment_model.joblib')
vectorizer = joblib.load('models/sentiment_vectorizer.joblib')


@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API!"}


@app.post("/predict/")
def predict_sentiment(review: Review):
    """
    Predicts the sentiment of a given text review.
    - **text**: The review text to analyze.
    """
    vectorized_text = vectorizer.transform([review.text])
    prediction = model.predict(vectorized_text)[0]
    return {"sentiment": prediction}