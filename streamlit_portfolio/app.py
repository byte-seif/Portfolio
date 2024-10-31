import streamlit as st

st.set_page_config(page_title="AI & Data Science Portfolio", layout="wide")

st.title("Data Science and AI Portfolio")
st.markdown("Explore various machine learning and deep learning projects. Each project includes an interactive app and a Jupyter notebook for detailed analysis.")

st.sidebar.title("Projects")
st.sidebar.markdown(
    """
    ### Project Pages:
    - [Movie Sentiment Analysis App](1_Movie_Sentiment_Analysis)
    - [Sentiment Analysis Notebook](3_Sentiment_Notebook)
    - [Brain Tumor Classification App](2_Brain_Tumor_Classification)
    - [Brain Tumor Classification Notebook](4_Brain_Tumor_Notebook)
    """
)
