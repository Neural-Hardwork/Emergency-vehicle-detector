from fastapi import FastAPI
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# get /check and return True and False randomly
@app.get("/check")
async def check():
    return random.choice([True, False])
