import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL_NAME = os.getenv("OLLAMA_MODEL")
TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", 120))

def generate_ai_suggestions(metrics, score, text_data):
    prompt = f"""
You are an image and text quality expert.

Image Quality:
Brightness: {metrics['brightness']}
Contrast: {metrics['contrast']}
Sharpness: {metrics['sharpness']}
Score: {score}/100

Text Analysis:
Word count: {text_data['word_count']}
Average text size: {text_data['avg_text_size']}
Confidence: {text_data['confidence']}

Give 3 professional improvement suggestions.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 120
        }
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=TIMEOUT
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"AI suggestions unavailable. Error: {str(e)}"