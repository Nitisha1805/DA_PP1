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
st.subheader('Key Performace Indicator')

#to get the list of all col
cols = df.columns.tolist()
selected_cols = st.multiselect('Select Columns',cols)
st.write(f'You Selected :{len(selected_cols)} columns')

st.metric(label='Average Price',
          value=round(df['price'].mean()),
          delta=round(df['price'].std()))


for col in selected_cols:
    st.subheader(f'Column : {col}')
    try:
            st.metric(label=f'Mean {col}',
                      value=round(df[col].mean()),
                      delta=round(df[col].std()))
            st.line_chart(df[col],use_container_width=True)
    except:
            st.error(f'Cannot Display {col} Numeric data')
            
