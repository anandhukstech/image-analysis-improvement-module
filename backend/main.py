from fastapi import FastAPI, UploadFile, File
import shutil
import os
from analysis import analyze_image

print("MAIN FILE LOADED")

app = FastAPI()

UPLOAD = "uploads"
os.makedirs(UPLOAD, exist_ok=True)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD, file.filename)

    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return analyze_image(path)
