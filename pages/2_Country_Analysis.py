import streamlit as st
import plotly.express as px
from utils import load_data

st.title("Country Trend Analysis")

df = load_data()

country = st.sidebar.selectbox(
    "Select Country",
    df.columns[1:]
)

fig = px.line(
    df,
    x="Year",
    y=country,
    title=f"{country} Trend Over Time"
)

st.plotly_chart(fig, use_container_width=True)
