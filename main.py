#from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Add this import
# ... rest of your imports ...
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://amazon-saree-rating-predictor.netlify.app"],  # Allows all websites to talk to your API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = joblib.load("rating_predictor.pkl")

# These names MUST match the columns in your training DataFrame exactly
class PredictionInput(BaseModel):
    Prices: float
    is_Cotton: int
    is_Silk: int
    is_Chiffon: int
    is_Linen: int
    is_Ready_To_Wear: int

@app.post("/predict")
def predict_rating(data: PredictionInput):
    # 1. Convert to dictionary
    data_dict = data.dict()
    
    # 2. Convert to DataFrame
    input_data = pd.DataFrame([data_dict])
    
    # 3. Predict
    try:
        # If your training code used 'Prices', this will work.
        # If your training code used 'Reviews' as a feature, it will fail.
        prediction = model.predict(input_data)
        return {"predicted_rating": round(prediction[0], 2)}
    except Exception as e:
        # This will tell you exactly which column name is missing
        return {
            "error_type": type(e).__name__,
            "error_message": str(e),
            "tip": "Check if your Training features (X) match these FastAPI features."

        }
