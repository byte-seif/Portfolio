import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model("simplified_cnn_model.h5")
    return model

model = load_model()
class_labels = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

def preprocess_image(image: Image.Image) -> np.array:
    image = ImageOps.fit(image, (150, 150), Image.ANTIALIAS)
    img_array = np.asarray(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

st.title("Brain Tumor Classification from MRI Scans")

# User-uploaded image
uploaded_file = st.file_uploader("Upload an MRI image for classification", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)
    
    # Preprocess and classify the image
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    confidence = np.max(predictions)
    predicted_class = class_labels[np.argmax(predictions)]
    
    st.write(f"**Prediction:** {predicted_class}")
    st.write(f"**Confidence:** {confidence:.2f}")
