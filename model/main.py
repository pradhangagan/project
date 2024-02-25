import io
import json
from PIL import Image
from fastapi import File,FastAPI
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./weights/best.pt', force_reload=True)

# Images
# imgs = ['.\data\images\Egg_Cartons.webp']   
# # Inference
# model.conf = 0.70
# results = model(imgs)

# # Results
# results.print()
# results.save()  # or .show()

# results.xyxy[0]  # img1 predictions (tensor)
# results.pandas().xyxy[0]  # img1 predictions (pandas)
# results.pandas().xyxy[0].to_json(orient="records")  # img1 predictions (json)

app = FastAPI()
@app.post("/objectdetection/")
async def get_body(file: bytes = File(...)):
    input_image = Image.open(io.BytesIO(file)).convert("RGB")
    model.conf = 0.70
    results = model(input_image)
    results_json = json.loads(results.pandas().xyxy[0].to_json(orient="records"))   
    return {"results": results_json}
