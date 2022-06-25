from fastapi import FastAPI
import random
from fastapi.middleware.cors import CORSMiddleware
import cv2
from main import run

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cap = cv2.VideoCapture(0)

# get /check and return True and False randomly
@app.get("/check")
async def check():
    # read camera and save image to file
    ret, frame = cap.read()
    cv2.imwrite('results/image.jpg', frame)
    # read image from file
    source = 'results/image.jpg'
    weights = "models/300_epochs/weights/best.pt"
    device = 'cpu'
    imgsz = (1280, 1024)
    return await run(source=source, weights=weights, device=device, imgsz=imgsz)

# @app.get("/check")
# async def check():
#     return random.choice([True, False])