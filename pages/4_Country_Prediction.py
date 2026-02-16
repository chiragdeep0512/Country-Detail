import streamlit as st
import pickle
import numpy as np

st.title("Country Prediction")

@st.cache_resource
def load_models():
    return pickle.load(open("D:\DS_Improvement\Streamlit\country_models.pkl", "rb"))

models = load_models()

# Select Country
country = st.selectbox(
    "Select Country",
    list(models.keys())
)

# Input Year
year = st.number_input(
    "Enter Year for Prediction",
    min_value=1990,
    max_value=2050,
    step=1
)

# Prediction
if st.button("Predict"):
    model = models[country]
    prediction = model.predict(np.array([[year]]))

    st.success(f"Predicted {country} Value in {year}: {prediction[0]:.2f}")
