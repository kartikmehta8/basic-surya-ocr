from PIL import Image
from surya.ocr import run_ocr
from surya.model.detection import segformer
from surya.model.recognition.model import load_model
from surya.model.recognition.processor import load_processor

def get_image_text(image_path, language=["en"]):

    image = Image.open(image_path)
    det_processor, det_model = segformer.load_processor(), segformer.load_model()
    rec_model, rec_processor = load_model(), load_processor()

    predictions = run_ocr([image], [language], det_model, det_processor, rec_model, rec_processor)[0]

    text = [line.text for line in list(predictions)[0][1]]
    
    return text