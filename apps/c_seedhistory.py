import streamlit as st
import pandas as pd
import numpy as np

def app():
    # title of the app
    st.markdown('Seed Success History Since 1985')
    df = pd.read_csv('notebooks/step04_SeedHistory.csv')
    df.index = df.index + 1
          
    st.dataframe(df, height=500)