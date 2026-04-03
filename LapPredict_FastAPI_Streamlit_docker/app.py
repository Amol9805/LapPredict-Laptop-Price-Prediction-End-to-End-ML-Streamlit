import streamlit as st
import pickle
import requests
import pandas as pd
import numpy as np

API_URL = "http://localhost:8000/predict"

st.set_page_config(
    page_title="Laptop Price Predictor",
    layout="wide"
)

st.title("💻 Laptop Price Predictor (API Powered)")


with open('df.pkl','rb') as f:
   df = pickle.load(f)

col1, col2 = st.columns(2)
with col1:
   # Company
   company = st.selectbox('Company Brand',df['Company'].unique())

   # TypeName of laptop
   type = st.selectbox('TypeName',df['TypeName'].unique())


   # screensize
   inches = st.number_input('Screensize (Inches)',min_value=8.0, max_value=30.0, value=15.6 )

   # ram size
   ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

   # weight 
   weight = st.number_input('Weight(kg)', min_value=0.5, max_value=15.0, value=2.0)

   # Touchscreen 
   touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

   # IPS
   ips = st.selectbox('IPS', ['No', 'Yes'])

with col2:
   # resolution
   resolution = st.selectbox('Screen Resolution',['1920x1080', '1366x768','1600x900','3840x2160','3200x1800','2880x1800', '2560x1600', '2560x1440','2304x1440'])

   #cpubrand
   cpubrand = st.selectbox('Cpu Brand',df['Cpu Brand'].unique())

   #hdd
   hdd = st.selectbox('HDD(in GB)', [0,128,256,512,1024,2048])

   #ssd
   ssd = st.selectbox('SSD(in GB)', [0,128,256,512,1024,2048])

   #gpubrand
   gpubrand = st.selectbox('Gpu Brand',df['Gpu Brand'].unique())

   #OS
   os = st.selectbox('Operating System',df['System'].unique())

if st.button("Predict 🚀"):

    # PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2 + Y_res**2) ** 0.5) / inches

    input_data = {
        "Company": company,
        "TypeName": type,
        "Inches": inches,
        "Ram": ram,
        "Weight": weight,
        "Touchscreen": touchscreen,
        "IPS": ips,
        "ppi": ppi,
        "Cpu_Brand": cpubrand,
        "HDD": hdd,
        "SSD": ssd,
        "Gpu_Brand": gpubrand,
        "System": os
    }

  
    response = requests.post(API_URL, json=input_data)
    result = response.json()

    st.success(f"Predicted Price of Laptop is : ₹ {result['predicted_price']:,}")
