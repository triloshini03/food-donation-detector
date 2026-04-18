import streamlit as st
from PIL import Image
import random

st.title("Food Donation Detector")

st.write("Upload a food image to check whether it is fresh or spoiled.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button("Check Food Quality"):
        result = random.choice(["Fresh Food", "Spoiled Food"])
        st.success("Result: " + result)
