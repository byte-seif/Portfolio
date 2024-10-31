import streamlit as st
from helper import display_notebook  # Assuming `display_notebook` is saved in `helper.py`

st.title("Sentiment Analysis - Project Notebook")
st.write("This notebook outlines the entire workflow for building the Sentiment Analysis model.")

# Display notebook
display_notebook("notebook_sentiment_analysis.ipynb")
