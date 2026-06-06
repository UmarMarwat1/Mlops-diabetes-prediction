from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI(title="Diabetes Prediction API")

# 1. Load the saved model and columns 
model = joblib.load('diabetes_model.pkl')
training_columns = joblib.load('training_columns.pkl')

# 2. Define Pydantic model for input validation 
class PatientData(BaseModel):
    age: float 
    urea: float 
    cr: float 
    hba1c: float 
    chol: float 
    tg: float 
    hdl: float 
    ldl: float 
    vldl: float 
    bmi: float 
    gender: str 

# 4. Health check endpoint
@app.get("/")
def health_check():
    return {"status": "API is running"}

# 3. Predict endpoint 
@app.post("/predict")
def predict(data: PatientData): 
    if data.gender.upper() not in ['M', 'F']:
        raise HTTPException(status_code=422, detail="Invalid gender. Must be 'M' or 'F'.")
        
    # Convert input to DataFrame 
    input_data = data.dict()
    df_input = pd.DataFrame([input_data])
    
    # Perform one-hot encoding on gender 
    df_input['Gender_F'] = 1 if data.gender.upper() == 'F' else 0
    df_input['Gender_M'] = 1 if data.gender.upper() == 'M' else 0
    df_input = df_input.drop(columns=['gender'])
    
    # Ensure columns match training columns 
    df_final = pd.DataFrame(columns=training_columns)
    for col in training_columns:
        if col in df_input.columns:
            df_final[col] = df_input[col]
        else:
            df_final[col] = 0
            
    # Return the prediction result 
    prediction = model.predict(df_final)
    return {"prediction": prediction[0]}