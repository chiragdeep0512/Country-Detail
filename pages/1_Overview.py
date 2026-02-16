import streamlit as st

from utils import load_data

st.title("Overview")

df = load_data()

st.subheader("Data review")
st.dataframe(df)

## KPI Example
st.subheader("Latest Year Snapshot")

latest_year = df["Year"].max()
latest_data = df[df["Year"] == latest_year]

st.write(f"Year :{latest_data}")

# Column
col1, col2, col3 = st.columns(3)

countries = df.columns[1:4]

col1.metric(countries[0],float(latest_data[countries[0]]))
col2.metric(countries[0],float(latest_data[countries[0]]))
col3.metric(countries[0],float(latest_data[countries[0]]))