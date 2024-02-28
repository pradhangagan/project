import os  
import torch 
model = torch.hub.load('ultralytics/yolov5', 'custom', path='./weights/best.pt', force_reload=True)
 

# Images
imgs = ['.\data\images\egg.webp']   
# Inference
model.conf = 0.70
results = model(imgs)

# Results
results.print()
#results.save()  # or .show()

#results.xyxy[0]  # img1 predictions (tensor)
results.pandas().xyxy[0]  # img1 predictions (pandas)