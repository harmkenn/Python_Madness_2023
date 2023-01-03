import streamlit as st
import pandas as pd
import numpy as np

def app():
    # title of the app
    st.markdown('Seed Success History Since 1985')
    df = pd.read_csv('notebooks/step04_SeedHistory.csv')
    df.insert(loc= 0 , column= 'Seed', value= np.arange(1,17))
    
    # CSS to inject contained in a string
    hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
          
    st.dataframe(df, height=600)