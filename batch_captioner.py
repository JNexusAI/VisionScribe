import torch
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration
import os

print("Libraries imported successfully.")

# Define the model name from Hugging Face
model_name = "Salesforce/blip-image-captioning-base"

# Load the pretrained processor and model
# This will use the cached version on your computer, so it will be fast
processor = AutoProcessor.from_pretrained(model_name)
model = BlipForConditionalGeneration.from_pretrained(model_name)

print("Model and processor loaded successfully.")

# Define the path to the folder containing images
image_folder = "images_to_process"
# Define the name for the output file
output_file = "captions.txt"

# Get a list of all image files in the folder
# This will filter for common image file extensions
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

print(f"Found {len(image_files)} images to process.")
print(image_files)

# --- 4. Loop Through Images and Generate Captions (Robust Version) ---
print("\nStarting caption generation...")

# Get a list of ALL files in the folder
all_files = os.listdir(image_folder)

# Open the output file in write mode
with open(output_file, "w", encoding="utf-8") as f:
    # Iterate over each file
    for i, filename in enumerate(all_files):
        try:
            # Create the full path to the file
            full_path = os.path.join(image_folder, filename)
            
            # Try to open the file as an image
            image = Image.open(full_path).convert("RGB")

            # If successful, it's a valid image. Proceed to generate a caption.
            inputs = processor(images=image, return_tensors="pt")
            outputs = model.generate(**inputs, max_length=50)
            caption = processor.decode(outputs[0], skip_special_tokens=True)

            # Write the result to the file
            f.write(f"File: {filename}\n")
            f.write(f"Caption: {caption}\n")
            f.write("-" * 20 + "\n")
            
            print(f"  ({i+1}/{len(all_files)}) ✔ Successfully captioned: {filename}")

        except Exception as e:
            # If Image.open() fails, it's not a valid image file we can read.
            # Silently skip it, or print a message for debugging.
            print(f"  ({i+1}/{len(all_files)}) ✖ Skipping (not a valid image): {filename}")

print(f"\nProcessing complete. All valid images have been captioned in '{output_file}'.")
