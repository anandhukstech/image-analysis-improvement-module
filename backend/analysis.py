import cv2
import numpy as np
import easyocr
import requests

# Load OCR once
reader = easyocr.Reader(['en'], gpu=False)

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "tinyllama"

def analyze_image(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Invalid image")

        img = cv2.resize(img, (800, 800))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        brightness = round(float(np.mean(gray)), 2)
        contrast = round(float(np.std(gray)), 2)

        # OCR
        ocr_results = reader.readtext(image_path)
        texts = [t[1] for t in ocr_results]

        if not texts:
            texts = ["No readable text detected"]

        # Prompt
        prompt = f"""
You are a senior digital marketing expert.

Evaluate this marketing creative and give 4 professional improvement suggestions.

Extracted text:
{texts[:8]}

Brightness: {brightness}
Contrast: {contrast}

Focus on:
- Message clarity
- CTA effectiveness
- Visual hierarchy
- Branding consistency

Give short bullet points.
"""

        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()

        ai_text = response.json()["response"]

        suggestions = [
            line.strip("-• ")
            for line in ai_text.split("\n")
            if line.strip()
        ]

        return {
            "detected_text": texts,
            "suggestions": suggestions,
            "brightness": brightness,
            "contrast": contrast
        }

    except Exception as e:
        return {
            "detected_text": [],
            "suggestions": [f"Processing error: {str(e)}"],
            "brightness": None,
            "contrast": None
        }