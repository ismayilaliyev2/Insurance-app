import streamlit as st
import numpy as np
import joblib

# Load the trained model
regressor = joblib.load("regression_model.pkl")

# Page setup
st.set_page_config(page_title="Insurance Cost Estimator", layout="centered")
st.title("💰 Insurance Cost Estimator")
st.markdown("Estimate individual medical costs billed by health insurance.")

# User input
age = st.slider("Age", 18, 100, 31)
sex = st.radio("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.74, step=0.1)
children = st.number_input("Number of Children", 0, 10, 0)
smoker = st.radio("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Map categorical inputs to numeric
sex_num = 1 if sex == "Male" else 0
smoker_num = 1 if smoker == "Yes" else 0
region_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region_code = region_map[region]

# Prepare input
input_data = (age, sex_num, bmi, children, smoker_num, region_code)
input_array = np.asarray(input_data).reshape(1, -1)

# Predict
if st.button("Predict Insurance Cost"):
    prediction = regressor.predict(input_array)
    st.success(f"🏷️ Estimated Insurance Cost: **${prediction[0]:,.2f}**")
