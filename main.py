from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import numpy as np
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(
    request: Request,
    age: int = Form(...),  
    speed: float = Form(...),  
    helmet: str = Form(...),
    seatbelt: str = Form(...),
    gender: str = Form(...)
):
    try:
        gender_value = 1 if gender.lower().strip() == "male" else 0
        helmet_value = 1 if helmet.lower().strip() == "yes" else 0
        seatbelt_value = 1 if seatbelt.lower().strip() == "yes" else 0

        input_data = np.array([[age, speed, helmet_value, seatbelt_value, gender_value]])

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)[0]
        result = {"prediction": "Survived" if prediction == 1 else "Not Survived"}

        return JSONResponse(content=result)

    except ValueError as ve:
        return JSONResponse(content={"error": f"Invalid input: {str(ve)}"}, status_code=400)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/result", response_class=HTMLResponse)
def result_page(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})