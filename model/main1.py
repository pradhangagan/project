# from fastapi import FastAPI, File, UploadFile
# import asyncio  # Added import

# app = FastAPI()


# @app.post("/upload-image")
# async def upload_image(image: UploadFile = File(...)):
#     # Simulate processing the image (replace with your actual logic)
#     content = await image.read()
#     print(f"Received image data: {len(content)} bytes")
#     return {"message": "Image uploaded successfully!"}

import io
import json
from PIL import Image
from fastapi import File,FastAPI, UploadFile
import asyncio
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./weights/best.pt', force_reload=True)

app = FastAPI()
@app.post("/objectdetection/")
async def get_body(file: UploadFile = File(...)):
    input_image = Image.open(io.BytesIO(file)).convert("RGB")
    model.conf = 0.70
    results = model(input_image)
    results_json = json.loads(results.pandas().xyxy[0].to_json(orient="records"))   
    return {"results": results_json}
