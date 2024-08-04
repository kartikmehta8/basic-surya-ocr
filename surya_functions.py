from PIL import Image  # Import the Image module from PIL for image processing
from surya.ocr import run_ocr  # Import the OCR function from the surya.ocr module
from surya.model.detection import segformer  # Import the detection model and processor
from surya.model.recognition.model import load_model  # Import the function to load the recognition model
from surya.model.recognition.processor import load_processor  # Import the function to load the recognition processor

def get_image_text(image_path, language=["en"]):
    """
    Extracts text from an image using OCR.

    Args:
        image_path (str): Path to the image file.
        language (list, optional): List of languages to use for text recognition. Default is ["en"].

    Returns:
        list: A list of extracted text lines from the image.
    """
    
    # Open the image file
    image = Image.open(image_path)

    # Load the detection model and processor
    det_processor, det_model = segformer.load_processor(), segformer.load_model()

    # Load the recognition model and processor
    rec_model, rec_processor = load_model(), load_processor()

    # Run the OCR process on the image
    predictions = run_ocr([image], [language], det_model, det_processor, rec_model, rec_processor)[0]

    # Extract text from the OCR predictions
    text = [line.text for line in list(predictions)[0][1]]
    
    return text
