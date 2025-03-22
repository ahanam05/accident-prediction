#just testing out with a model now, choose final model based on accuracy later from other file

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('accident.csv')
df.dropna(inplace=True)

X = df.iloc[:, :-1] 
y = df.iloc[:, -1]   

X_encoded = pd.get_dummies(X)

feature_names = list(X_encoded.columns)
joblib.dump(feature_names, "feature_names.pkl")

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
print("Model saved successfully")