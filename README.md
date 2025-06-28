# VisionScribe: AI-Powered Image Captioning Tools

This repository contains a suite of Python tools for generating descriptive captions for images using the Hugging Face `Salesforce/blip-image-captioning-base` model.

## Features

This project includes three main tools:
1.  **Gradio Web App (`image_captioning_app.py`):** A user-friendly web interface to upload a single image and receive a caption.
2.  **Batch Processor (`batch_captioner.py`):** A command-line tool that processes all images in a local folder (`/images_to_process`) and saves the captions to `captions.txt`.
3.  **Web Scraper (`automate_url_captioner.py`):** A tool that scrapes all images from a given URL, generates captions for them, and saves the results to `scraped_captions.txt`.

## Setup and Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/JNexusAI/VisionScribe.git](https://github.com/JNexusAI/VisionScribe.git)
    cd VisionScribe
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

### Web Application
To launch the Gradio web interface, run:
```bash
python image_captioning_app.py
```
Then navigate to the local URL provided in the terminal (usually `http://127.0.0.1:7860`).

### Batch Processor
1.  Place your image files (`.jpg`, `.png`, etc.) inside the `images_to_process` folder.
2.  Run the script:
    ```bash
    python batch_captioner.py
    ```
3.  Results will be saved in `captions.txt`.
