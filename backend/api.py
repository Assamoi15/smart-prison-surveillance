from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
import cv2
import numpy as np
import os

app = FastAPI(title="Prison Surveillance API", description="API pour la détection d'armes")

# Chemin du modèle
model_path = "ai/models/best.pt"
if not os.path.exists(model_path):
    model_path = "yolov8n.pt"

model = YOLO(model_path)

@app.get("/")
def home():
    return {
        "message": "Prison Surveillance API",
        "status": "online",
        "model": model_path
    }

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    """Détecte les armes dans une image uploadée"""
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    results = model(img)
    detections = []
    
    for box in results[0].boxes:
        detections.append({
            "class": int(box.cls[0]),
            "confidence": float(box.conf[0]),
            "bbox": box.xyxy[0].tolist()
        })
    
    return {
        "detections": detections,
        "count": len(detections)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
