import streamlit as st
import os
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit import session_state

st.title('Hello World')
st.header('Singh Saab The Great')
st.write('jaisa ki aap jaane ho , ki AA HOOO JIIII')


### Page Configuration
st.set_page_config(page_title='Ki Haal Hai',
                   page_icon=" ",
                   layout="wide")

### Titles & Headings
st.subheader('Titles & Headings')
st.title('AHJ')
st.header('Singh Saab The Great')
st.subheader('Ki haal hai')

### Simple Text
st.subheader('Simple Text')
st.text('jaisa ki aap jaane ho')
st.write("ki AA HOOO JIIII")

### Markdown
st.text('Markdown')
st.markdown("### This is Markdown")
st.markdown("**Bold Text**") ### BOld
st.markdown("*Italic Text*") ### Italic
st.markdown("- Point 1\n- Point 2\n- Point 3\n- Point 4")

### Status Messages
st.text('Status Messages')
st.success("Message Sent")
st.error("Error didn't sent")
st.warning("Warning Error")
st.info("Some Little bit info. for you")

### Divider
st.divider()

## Button
if st.button('Submit'):
    st.success('Submitted')

## check Box
show_data = st.checkbox('Show Data')
Aina = st.checkbox('Aina')
Meena = st.checkbox('Meena')
Dika = st.checkbox('Dika')

## Radio
option = st.radio('Which Medal', ('Gold', 'Silver', 'Bronze'))
st.write(f"You selected {option} Medal")

## Select Box
select = st.selectbox("Select Country :",["India","USA","Australia"])
st.write(f"You selected {select} Country")

## Multiselect
Multiselect = st.multiselect("Select Country :",["India","USA","Australia"])

## Slider
slider = st.slider("Born in:",1947,2026,2002)
st.write(f"You selected {slider} Monthly Income")

## Number Input
age = st.number_input("Age",min_value=18,max_value=55,value=23)
st.success("You are allowed")

## Text Input
name = st.text_input("Name Please")
st.write(f"Hi {name} , WELCOME")
if name == "":
    st.warning("Please enter your name ")

## File Uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["pdf"])
if uploaded_file is not None:
    os.makedirs('uploaded_files', exist_ok=True)
    filepath = os.path.join('uploaded_files', uploaded_file.name)
    with open(filepath,'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.success('Uploaded File successfully')

### chapter 4
## Display DataFrame
@st.cache_data
def load_data():
    return pd.read_csv("D:\Do not open this file (DS)\matplotlib_tutorial-master\gas_prices.csv")

df = load_data()
st.write(df.head(3))

## Column Selection
st.dataframe(df[['Year','Canada']].head(3))

## Filtering Data
Desh = st.sidebar.selectbox('Select Country :',['Australia','Canada','France','Germany',
     'Italy','Japan','Mexico',
     'South Korea','UK','USA'])

filter_df = df[['Year', Desh]]

st.dataframe(filter_df.head(3))

## Multi-Filter
year = st.slider('Select Year: ',int(df["Year"].min()), int(df["Year"].max()))

filtered_df = df[(df['Year']==year)]
st.dataframe(filtered_df.head(5))

## Sorting Data
st.write("Sort Data")
sorted_df = df.sort_values(by=['Canada'],ascending=False)
st.dataframe(sorted_df.head(3))

## Aggregation
summary = df.groupby('Year')[['Australia','Canada','France','Germany',
     'Italy','Japan','Mexico',
     'South Korea','UK','USA']].sum()
st.dataframe(summary.head(3))

### Data Visualization


## Line Chart
st.line_chart(df[Desh])

## Bar Chart

st.bar_chart(df.set_index('Year')[Desh])

## Area Chart
st.area_chart(df.set_index('Year')[Desh])

## Plotly Integration
## Bar
fig = px.bar(df,x='Year',y=Desh,title=f"{Desh} & Year")
st.plotly_chart(fig)

## Line
fig = px.line(df,x='Year',y=Desh,title=f"{Desh} & Year")
st.plotly_chart(fig)


### CHAPTER 6 Layout & Design
## Wide Layout
st.set_page_config(layout='wide')

## Sidebars
st.sidebar.title('Filter')



## Column
col1 , col2 = st.columns(2)

with col1:
    st.metric("Total of Years", len(df))

with col2:
    st.metric("Selected Country", Desh)

## Tabs
tab1, tab2 = st.tabs(["Year", Desh])

with tab1:
    st.write("Overall statistics")

with tab2:
    st.write(Desh)

## container
container = st.container()

with container:
    st.write("This is inside container")

## Session State
st.title("User DashBoard")

if 'logged_in'not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state.logged_in:
    if st.button("Login"):
        st.session_state.logged_in = True

if session_state.logged_in:
    st.success("You are logged in successfully")
    if st.button("Logout"):
        st.session_state.logged_in = False