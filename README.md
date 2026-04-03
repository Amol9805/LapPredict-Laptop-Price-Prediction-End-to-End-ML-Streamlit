# 💻 LapPredict: Laptop Price Prediction (End-to-End ML + Streamlit)

## 🔷 Project Overview:
LapPredict is an **end-to-end machine learning solution** designed to predict laptop prices using hardware specifications and brand attributes.  
The project implements a **robust preprocessing + modeling pipeline** and deploys it via a **Streamlit web application** for real-time predictions.

It enables data-driven pricing decisions, supports new product evaluation, and identifies key factors influencing laptop pricing.

---

## 🔷 Business Objective:  
- Predict laptop prices with high accuracy using technical specifications  
- Support competitive pricing and product positioning  
- Analyze **brand impact on pricing**  
- Enable **real-time predictions** through an interactive application  

---

## 🔷 Dataset  
- ~1300 laptop records  
- 13 features  
- Target variable: Price  

**Key Features:**  
- Brand  
- CPU  
- RAM  
- Storage (HDD/SSD)  
- Screen Resolution  
- PPI (engineered)  
- Weight  
- Operating System  

---

## 🔷 Tech Stack  
- **Programming:** Python  
- **ML Libraries:** scikit-learn, XGBoost  
- **Data Analysis:** pandas, numpy  
- **Visualization:** matplotlib, seaborn  
- **Deployment:** Streamlit  
- **Environment:** Jupyter Notebook  

---

## 🔷 Machine Learning Workflow  

### 1. Data Exploration  
- Identified key predictors: **Brand, RAM, SSD, PPI**  
- Detected skewness in price distribution  

### 2. Feature Engineering  
- Derived **PPI (Pixels Per Inch)** from screen resolution  
- Extracted meaningful attributes from raw features  
- Improved feature relevance for modeling  

### 3. Data Preprocessing  
- Applied **OneHot Encoding** for nominal categorical variables  
- Applied **Ordinal Encoding** where feature order is meaningful  
- Performed **log transformation** on target variable to handle skewness  

---

## 🔷 Pipeline Architecture (Key Highlight)  
- Built using **ColumnTransformer + Pipeline**  
- Combined preprocessing and model training into a single workflow  
- Ensured:
  - No data leakage  
  - Reproducibility  
  - Scalability for deployment  

---

## 🔷 Model Development  
Trained and evaluated multiple models:
- Linear Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor  
- XGBoost Regressor  

---

## 🔷 Model Optimization  
- Hyperparameter tuning (depth, estimators, learning rate)  
- Model evaluation using:
  - R² Score  
  - RMSE  
  - MAE  

---

## 🔷 Key Insights  
- **Brand significantly influences pricing** (premium segment effect)  
- **RAM and SSD capacity** are strong predictors  
- Higher **PPI correlates with higher price**  
- **Tree-based models outperform linear models** due to non-linear relationships  

---

## 🔷 Streamlit Application  
An interactive web application enabling real-time predictions.

### Features  
- User input for laptop specifications  
- Instant price prediction  
- Integrated ML pipeline for consistent preprocessing  
- Simple and intuitive UI  

---

## 🔷 Results  
- **R² Score:** ~0.91  
- **RMSE:** ~15,700  
- **MAE:** ~9,100  

The model delivers **reliable predictions across diverse laptop categories**.

---

## 🔷 Limitations  
- Limited dataset size (~1300 records)  
- Market trends and latest models not included   

---

## 🔷 Future Enhancements  
- Add latest market data and new laptop releases    
- Expand Streamlit app with comparison dashboards  


---

## 🏆 Conclusion  
This project demonstrates the practical implementation of a **production-ready machine learning pipeline**, combining feature engineering, encoding strategies, and model optimization.

By integrating ML with a Streamlit interface, it provides a **scalable, real-time pricing solution** for business decision-making and product evaluation.

---
