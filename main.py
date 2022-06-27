import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  #data web app development

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

st.experimental_set_query_params(
     show_map=True,
     selected=["asia", "america"],
 )




# dashboard title
st.title("Text Analytics")

input_file = st.file_uploader("Upload a CSV File",type=['csv'])
if input_file is not None:
    #read csv
    df=pd.read_csv(input_file, index_col=0, low_memory=False)
    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        review = st.multiselect(
            'Select Column name with Text for Analysis',
            (df.columns))

    with col2:
        rating = st.selectbox(
            'Select Column name with Ratings ',
             (df.columns))


