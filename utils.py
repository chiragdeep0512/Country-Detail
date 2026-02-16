import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv("Data\gas_prices.csv")

df = load_data()