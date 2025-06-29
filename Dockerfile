# Start from an official, lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's layer caching.
# This layer only gets rebuilt if the requirements change.
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port that Gradio will run on
EXPOSE 7860

# Define the command to run your application when the container starts
CMD ["python", "image_captioning_app.py"]
