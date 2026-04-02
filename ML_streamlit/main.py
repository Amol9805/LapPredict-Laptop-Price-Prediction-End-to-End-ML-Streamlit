import streamlit  as st
import pickle 
import numpy as np
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Laptop Price Predictor", layout="wide")

# Import DataFrame
with open('df.pkl','rb') as f:
   df = pickle.load(f)

# Import Model
with open('laptop_price_pickle.pkl','rb') as f:
   model = pickle.load(f)


st.title("Laptop Price Predictor")
st.markdown("Enter the specifications: ")

col1, col2 = st.columns(2)
with col1:
   # Company
   comapny = st.selectbox('Company Brand',df['Company'].unique())

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


if st.button('Predict Price'):

   # input query
   if touchscreen == 'Yes':
      touchscreen =1
   else:
      touchscreen=0

   if ips == 'Yes':
      ips = 1
   else:
      ips = 0 
   if inches <=0:
      st.error("Please enter valid screen size.")

   # ppi calculation  
   X_res = int(resolution.split('x')[0])
   Y_res = int(resolution.split('x')[1])
   ppi = ((X_res**2) + (Y_res**2))**0.5/inches

   # dataframe creation
   query = [comapny,type,inches,ram,weight,touchscreen,ips,ppi,cpubrand,hdd,ssd,gpubrand,os]
   columns = ['Company', 'TypeName','Inches', 'Ram', 'Weight', 'Touchscreen', 'IPS', 'ppi', 'Cpu Brand', 'HDD', 'SSD', 'Gpu Brand', 'System']

   query_df = pd.DataFrame([query],columns=columns)
   prediction = model.predict(query_df)
   final_price = int(np.exp(prediction[0]))

   st.success(f"### The estimated price for this laptop is: ₹{final_price:,}")