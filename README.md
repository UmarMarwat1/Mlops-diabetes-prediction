# MLOps Diabetes Prediction

## Project Overview

This project trains and serves a diabetes prediction model using scikit-learn and FastAPI. The training pipeline is implemented in `data_model.ipynb` and the API is in `app.py`.

## Requirements

- Python 3.8+ (3.14 tested)
- A virtual environment (recommended)
- Dependencies: see `requirements.txt`

## Setup

1. Create and activate a virtual environment (PowerShell):

   ```powershell
   python -m venv venv
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

## Data

- The project expects cleaned input data file `diabetes_unclean.csv` in the repository root.
- If you only have a pickle (`diabetes_unclean.pkl`), convert it like:

  ```powershell
  python -c "import pickle, pandas as pd; df = pickle.load(open('path\\to\\diabetes_unclean.pkl','rb')); df.to_csv('diabetes_unclean.csv', index=False)"
  ```

## Train and generate model artifacts

1. Open and run `data_model.ipynb` (Run all cells). This will:
   - Load `diabetes_unclean.csv`
   - Clean and preprocess the data
   - Train multiple models and select the best one (Random Forest)
   - Save artifacts:
     - `diabetes_model.pkl` (trained model)
     - `training_columns.pkl` (feature columns list)

2. Verify the files `diabetes_model.pkl` and `training_columns.pkl` are present in the project root after running the notebook.

## Run the API

1. With the virtual environment activated and artifacts present, start the FastAPI server:

   ```powershell
   uvicorn app:app --reload
   ```

2. Example request (PowerShell `curl` or `Invoke-WebRequest` differences noted):

   ```powershell
   curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"age":65, "urea":7.5, "cr":52.0, "hba1c":11.2, "chol":6.1, "tg":2.8, "hdl":0.9, "ldl":3.5, "vldl":1.2, "bmi":32.5, "gender":"M"}'
   ```

   Note: PowerShell's `Invoke-WebRequest`/`curl` may bind `-H`/`--header` differently; prefer using `curl` from Git Bash or use Postman for testing.

## Files of interest

- `data_model.ipynb` - training notebook (produces model artifacts)
- `app.py` - FastAPI application that loads `diabetes_model.pkl` and `training_columns.pkl`
- `requirements.txt` - Python dependencies

## Troubleshooting

- If you see `FileNotFoundError` for `diabetes_unclean.pkl` or `diabetes_unclean.csv`, verify the file exists in the repository root and the working directory is the project root.
- To activate the venv in PowerShell use `.`\venv\\Scripts\\Activate.ps1` (not `source` which is for bash).
- If the API fails at startup due to missing `diabetes_model.pkl`, run the notebook to generate the artifact.

## Author

Author: Umar Shehzad

Reg No: 04162213005

Institute: Institute of Information Technology, Quaid-i-Azam University, Islamabad

Instructor: Dr. Tehreem Qasim
