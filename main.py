from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import numpy as np
import pandas as pd
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

model = joblib.load("model.pkl")
feature_names = joblib.load("feature_names.pkl")

class InputData(BaseModel):
    age: int
    gender: str
    speed_of_impact: float
    helmet_used: str
    seatbelt_used: str

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(request: Request):
    try:
        data = await request.json()
        
        input_df = pd.DataFrame({
            'age': [data["age"]],
            'gender': [data["gender"]],
            'speed_of_impact': [data["speed_of_impact"]],
            'helmet_used': [data["helmet_used"]],
            'seatbelt_used': [data["seatbelt_used"]]
        })
        
        input_encoded = pd.get_dummies(input_df)
        
        for col in feature_names:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
                
        input_encoded = input_encoded[feature_names]
        
        prediction = model.predict(input_encoded)[0]
        return {"prediction": "Survived" if prediction == 1 else "Not Survived"}
    
    except Exception as e:
        return {"error": str(e)}

@app.get("/result", response_class=HTMLResponse)
def result_page(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})