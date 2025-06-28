import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Define the model name from Hugging Face
model_name = "Salesforce/blip-image-captioning-base"

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained(model_name)
model = BlipForConditionalGeneration.from_pretrained(model_name)

def generate_caption(image):
    # The function takes a PIL Image object as input
    
    # Pre-process the image and generate the input tensors
    # We don't need a text prompt for basic image captioning
    inputs = processor(images=image, return_tensors="pt")
    
    # Generate the caption using the model
    # max_length can be adjusted to control the caption length
    outputs = model.generate(**inputs, max_length=50)
    
    # Decode the generated tokens into a human-readable string
    # skip_special_tokens=True removes any special tokens like [CLS], [SEP]
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    
    return caption

# Create the Gradio interface
# The `inputs` component is an Image block, which allows users to upload an image.
# We specify type="pil" to ensure the input to our function is a PIL Image object.
# The `outputs` component is a Text block to display the caption.
demo = gr.Interface(
    fn=generate_caption, 
    inputs=gr.Image(type="pil", label="Upload an Image"),
    outputs=gr.Text(label="Generated Caption"),
    title="Image Captioning with BLIP",
    description="Upload an image and see the AI-generated caption for it."
)

# Launch the application
demo.launch()
