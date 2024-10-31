# Template for a notebook viewer page
import streamlit as st
import nbformat
from nbconvert import HTMLExporter

def display_notebook(notebook_file):
    with open(notebook_file, "r") as f:
        notebook_content = f.read()
    notebook_node = nbformat.reads(notebook_content, as_version=4)
    html_exporter = HTMLExporter()
    html_exporter.template_name = 'basic'
    (body, _) = html_exporter.from_notebook_node(notebook_node)
    st.components.v1.html(body, height=800, scrolling=True)
