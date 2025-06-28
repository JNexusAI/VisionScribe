# VisionScribe Product Roadmap

## Vision
To become the most intuitive and developer-friendly API for automated media understanding, starting with image captioning and expanding to video and audio analysis.

---

### Now (What's Done)
- **BLIP Model Integration:** Core captioning engine using the `Salesforce/blip-image-captioning-base` model.
- **Gradio UI:** A simple web interface for demoing single-image captioning.
- **Batch Processing:** A script for processing a local folder of images.
- **Web Scraper:** A tool to extract and caption images from a live URL.

### Next (Q3 2025)
- **BLIP-2 Model Upgrade:** Integrate the more powerful BLIP-2 model for higher-quality captions.
- **REST API Development:** Expose the captioning functionality as a simple REST API that other developers can use.
- **Performance Evaluation:** Establish a baseline for caption quality using BLEU/ROUGE scores against a test dataset.
- **UI Enhancements:** Add support for drag-and-drop and URL input directly in the Gradio UI.

### Later (Q4 2025 & Beyond)
- **Video Captioning:** Expand the service to accept video files and generate scene-by-scene descriptions.
- **Multi-language Support:** Allow users to request captions in different languages.
- **Analytics Dashboard:** For API users, provide a dashboard to track usage and performance.
- **SOC 2 Compliance:** Explore security and compliance for potential enterprise customers.