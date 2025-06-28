import requests
from bs4 import BeautifulSoup
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration
import os
from io import BytesIO
from urllib.parse import urljoin

# --- 1. SETUP ---
print("Setting up the environment...")

# Load the pretrained processor and model
model_name = "Salesforce/blip-image-captioning-base"
processor = AutoProcessor.from_pretrained(model_name)
model = BlipForConditionalGeneration.from_pretrained(model_name)

# URL of the page to scrape and the output file
url = "https://en.wikipedia.org/wiki/IBM"
output_file = "scraped_captions.txt"

print(f"Setup complete. Scraping images from: {url}")

# --- 2. SCRAPE AND PARSE THE WEBPAGE ---
try:
    # Download the page
    response = requests.get(url)
    response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all img elements
    img_elements = soup.find_all('img')

except requests.exceptions.RequestException as e:
    print(f"Error downloading the page: {e}")
    exit()

# --- 3. PROCESS IMAGES AND GENERATE CAPTIONS ---
# Open the output file in write mode
with open(output_file, "w", encoding="utf-8") as f:
    print(f"Found {len(img_elements)} image tags. Processing...")
    
    # Iterate over each img element
    for i, img_element in enumerate(img_elements):
        # Get the image source URL from the 'src' attribute
        img_src = img_element.get('src')

        if not img_src:
            continue # Skip tags that have no src attribute

        # Convert relative URLs to absolute URLs
        # e.g., turn "/wiki/skins/Vector/resources/common/images/bullet-icon.svg" 
        # into "https://en.wikipedia.org/wiki/skins/Vector/resources/common/images/bullet-icon.svg"
        img_url = urljoin(url, img_src)

        try:
            # Download the image
            img_response = requests.get(img_url, stream=True)
            img_response.raise_for_status()

            # Open the image from the downloaded content
            image = Image.open(BytesIO(img_response.content)).convert("RGB")

            # --- Generate Caption (same logic as before) ---
            inputs = processor(images=image, return_tensors="pt")
            outputs = model.generate(**inputs, max_length=50)
            caption = processor.decode(outputs[0], skip_special_tokens=True)
            
            # Write the result to the file
            f.write(f"Image URL: {img_url}\n")
            f.write(f"Caption: {caption}\n")
            f.write("-" * 20 + "\n")
            
            print(f"  ({i+1}/{len(img_elements)}) Successfully captioned: {img_url}")

        except Exception as e:
            # This will catch errors from broken links, non-image content, etc.
            print(f"  ({i+1}/{len(img_elements)}) Could not process {img_url}. Reason: {e}")

print(f"\nProcessing complete. Results saved to '{output_file}'.")
