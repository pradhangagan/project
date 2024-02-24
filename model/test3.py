from PIL import Image
import os
import torch
import numpy as np

# Model loading and configuration
model = torch.hub.load('ultralytics/yolov5', 'custom', path='./weights/best-fp16.tflite', force_reload=True)


model.conf = 0.70

# Define target size based on your model's input requirements
target_size = (640, 640)

# Function to resize and process an image
def process_image(image_path):
  try:
    # Open and resize the image
    img = Image.open(image_path)
    resized_img = img.resize(target_size, Image.Resampling.LANCZOS)

    

    # Run inference
    results = model([resized_img])

    # Do something with the results (e.g., print, save)
    results.print()
    results.save()  # or results.show()
    results.xyxy[0]  # img1 predictions (tensor)
    results.pandas().xyxy[0]  # img1 predictions (pandas)

  except Exception as e:
    print(f"Error processing image: {image_path}. {e}")

# Process your list of images
images = ['.\data\images\Egg_Cartons.webp']
for image_path in images:
  process_image(image_path)
