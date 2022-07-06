import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  #data web app development
import helper

st.set_page_config(
    page_title="Reviews Analysis Dashboard",
    page_icon="📚",
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
        review_col = st.multiselect(
            'Select Column name with Text for Analysis',
            (df.columns))

    with col2:
        rating_options = df.columns.tolist()
        rating_options.append("None")
        rating_col = st.selectbox(
            'Select Column name with Ratings ',
             (rating_options))

    if rating_col != "None":
        st.dataframe(df[rating_col].groupby(df[rating_col]).count())

    df[review_col] = df[review_col].astype(str)
    df["final_text"] = df[review_col].agg(' - '.join, axis=1)

    st.dataframe(helper.prepocessing(df).head())
