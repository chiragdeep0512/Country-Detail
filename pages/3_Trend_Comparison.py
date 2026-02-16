import streamlit as st
import plotly.express as px
from utils import load_data

st.title("Country Comparison")

df = load_data()

countries = st.sidebar.multiselect(
    "Select Countries to Compare",
    df.columns[1:],
    default=["USA", "Germany"]
)

if countries:
    fig = px.line(
        df,
        x="Year",
        y=countries,
        title="Country Comparison Over Time"
    )
    st.plotly_chart(fig, use_container_width=True)
