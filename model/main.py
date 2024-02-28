import io
import json
from PIL import Image
from fastapi import File, FastAPI, UploadFile
import asyncio
import torch
import sys
import contextlib
import logging

# Load your custom YOLOv5 model (replace the path with yours)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='./weights/best.pt', force_reload=True)




app = FastAPI()



@app.post("/objectdetection/")
async def get_object_detection(image: UploadFile = File(...)):
    """
    Processes an uploaded image and returns the object detection results.
    """

    try:
        # Open the image in RGB format
        input_image = Image.open(io.BytesIO(await image.read())).convert("RGB")

        # Set the confidence threshold (adjust as needed)
        model.conf = 0.70

        # Perform object detection using the model 
        results = model(input_image)

        # # Convert the results to a JSON format suitable for the web app
        # results_json = json.loads(results.pandas().xyxy[0].to_json(orient="records"))

        # # return {"results": results_json}
        # return {"results": results_json}

        
        

        # Extract detected object names and count
        detected_objects = [result["name"] for result in results.pandas().xyxy[0].to_dict(orient="records")]
        num_detections = len(detected_objects)
        
       

        return {"detected_objects": detected_objects, "num_detections": num_detections}



    except Exception as e:
        print(f"Error processing image: {e}")
        return {"message": "Error: Failed to process image."}
