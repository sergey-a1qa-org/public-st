import streamlit as st

image = st.file_uploader('Upload an image')
if image:
  st.image(image)
