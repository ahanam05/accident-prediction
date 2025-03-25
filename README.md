# ML Accident Survival Prediction Application

## Overview
This is a full-stack machine learning application that predicts the survival probability in an accident based on various input parameters using a Support Vector Machine (SVM) model.

## Features
- Web interface for accident survival prediction
- Custom cursor design
- Responsive UI with modern styling
- Machine learning model for survival prediction
- Deployed using FastAPI

## Tech Stack
- **Backend**: Python, FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas, NumPy

## Project Structure
```
accident-prediction/
│
├── static/
│   ├── script.js      # Frontend JavaScript
│   └── styles.css     # Application styling
│
├── templates/
│   ├── index.html     # Main prediction input page
│   └── result.html    # Prediction result page
│
├── main.py            # FastAPI application
├── train_model.py     # Model training script
├── new_accident.csv   # Training dataset
├── model.pkl          # Trained model
└── scaler.pkl         # Data scaling transformer
```

## Model Details
- **Algorithm**: Support Vector Machine (SVM)
- **Preprocessing**: L1 Normalization
- **Features**:
  - Age
  - Speed of Impact
  - Helmet Usage
  - Seatbelt Usage
  - Gender

## Input Parameters
- **Age**: Numerical value representing the person's age
- **Speed of Impact**: Speed at which the accident occurred (km/h)
- **Helmet**: Whether a helmet was used (Yes/No)
- **Seatbelt**: Whether a seatbelt was used (Yes/No)
- **Gender**: Male/Female

## Prediction Output
The model predicts two possible outcomes:
- "Survived"
- "Not Survived"

## Data Source
The prediction model is trained on a custom dataset `new_accident.csv` containing anonymized accident data.
