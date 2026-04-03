import pickle
import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel,Field,ConfigDict
from typing import Literal,Annotated


version = '2.0.0'

# -------------------------------
# Load Model
# -------------------------------
with open("laptop_price_pickle.pkl", "rb") as f:
    pipe = pickle.load(f)

app = FastAPI()

# -------------------------------
# Schema
# -------------------------------
class LaptopSpecs(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    Company: Literal[
        'Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI',
        'Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer',
        'Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG'
    ]

    TypeName: Literal[
        'Ultrabook', 'Notebook', 'Netbook',
        'Gaming', '2 in 1 Convertible', 'Workstation'
    ]

    Inches: Annotated[float, Field(gt=7, lt=20)]
    Ram: Annotated[int, Field(ge=2, le=64)]
    Weight: Annotated[float, Field(gt=0.5, lt=15.0)]

    Touchscreen: Literal['Yes', 'No']
    IPS: Literal['Yes', 'No']

    ppi: Annotated[float, Field(gt=50, lt=500)]

    Cpu_Brand: Literal[
        'Intel Core i5', 'Intel Core i7', 'AMD Processor',
        'Intel Core i3', 'Other Intel Processor'
    ] = Field(..., alias="Cpu Brand")

    HDD: Annotated[int, Field(ge=0, le=2048)]
    SSD: Annotated[int, Field(ge=0, le=2048)]

    Gpu_Brand: Literal['Intel', 'AMD', 'Nvidia'] = Field(..., alias="Gpu Brand")

    System: Literal['Mac', 'Others/No OS/Linux', 'Windows']


# -------------------------------
# Helper
# -------------------------------
def preprocess(data: dict):
    data['Touchscreen'] = 1 if data['Touchscreen'] == 'Yes' else 0
    data['IPS'] = 1 if data['IPS'] == 'Yes' else 0
    return data


# -------------------------------
# Predict API
# -------------------------------

@app.get("/")
def home():
    return {

        "message": "Laptop Price Prediction API is running.",

        "Status" : "Online",
        
        "Model_Version": version
     }


@app.post("/predict")
def predict(data: LaptopSpecs):

    input_dict=data.dict(by_alias=True)
    input_dict = preprocess(input_dict)

    df = pd.DataFrame([input_dict])

    # Prediction
    pred_log = pipe.predict(df)[0]
    price = float(np.exp(pred_log))


    return {
        "predicted_price": round(price, 2),
    }