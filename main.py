import streamlit as st  # Import the Streamlit library for creating the web app
from PIL import Image  # Import the Image module from PIL for image processing
from surya_functions import get_image_text  # Import the custom function to extract text from an image

def main():
    """
    Main function to run the Streamlit app for Surya OCR.
    Allows users to upload an image, display the image, and extract and display text from the image.
    """
    st.title("Surya OCR")  # Set the title of the web app

    # Create a file uploader widget for users to upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "webp"])

    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Open the uploaded image file
        image = Image.open(uploaded_file)
        
        # Display the uploaded image in the app
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Extract text from the uploaded image using the custom function
        extracted_text = get_image_text(uploaded_file)

        st.header("Extracted Text")  # Add a header for the extracted text section
        # Loop through the extracted text and display each line
        for text in extracted_text:
            st.write(text)

if __name__ == "__main__":
    main()  # Run the main function to start the app
