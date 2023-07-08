import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# loading the datat
@st.cache_data
def load_data():
    path = 'DATA/kc_house_data.csv'
    df = pd.read_csv(path)
    return df

#call the load data function
with st.spinner('Loading Data.........'):
    df = load_data()

#create a title for your app
st.title('House Price Data Analysis              ')

#display the data
if st.checkbox('Show Dataset',True):
    st.subheader('Dataset.')
    st.dataframe(df)