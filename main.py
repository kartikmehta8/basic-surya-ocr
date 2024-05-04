import streamlit as st
from PIL import Image
from surya_functions import get_image_text

def main():
    st.title("Surya OCR")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "webp"])

    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        extracted_text = get_image_text(uploaded_file)

        st.header("Extracted Text")
        for text in extracted_text:
            st.write(text)

if __name__ == "__main__":
    main()