import streamlit as st

st.set_page_config(page_title="AI & Data Science Portfolio", layout="wide")

st.title("Welcome to My Data Science and AI Portfolio")
st.markdown("This portfolio showcases various machine learning and deep learning projects.")

st.write("Select a project from the sidebar to explore.")
st.sidebar.title("Projects")

# List descriptions for clarity
st.sidebar.markdown(
    """
    ### Project Pages:
    - **Movie Sentiment Analysis**: Interactive sentiment analysis app.
    - **Brain Tumor Classification**: Upload MRI images for classification.
    - **Sentiment Analysis Notebook**: View the project notebook for sentiment analysis.
    - **Brain Tumor Notebook**: View the project notebook for brain tumor classification.
    """
)

