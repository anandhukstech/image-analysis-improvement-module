import cv2
import numpy as np
import easyocr
from openai import OpenAI

# IMPORTANT: Put your real OpenAI key here (dev mode)
client = OpenAI(api_key="OPENAI_API_KEY")

# Load OCR model ONCE (performance optimization)
reader = easyocr.Reader(['en'])

def analyze_image(path):

    # Load and resize image
    img = cv2.imread(path)
    img = cv2.resize(img, (800, 800))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Image quality metrics
    brightness = float(np.mean(gray))
    contrast = float(np.std(gray))

    # OCR text extraction
    result = reader.readtext(path)
    texts = [r[1] for r in result]

    # Limit OCR content sent to LLM
    short_texts = texts[:8]

    # Prompt engineering for marketing expert behavior
    prompt = f"""
You are a senior digital marketing creative analyst.

Analyze the following marketing image and provide professional improvement suggestions.

Extracted Text:
{short_texts}

Brightness Level: {brightness}
Contrast Level: {contrast}

Give exactly 4 concise bullet-point suggestions focusing on:

1. Content clarity and text density
2. Layout and visual hierarchy
3. Call-To-Action effectiveness
4. Overall design appeal

Avoid generic advice. Be specific and actionable.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )

        llm_output = response.choices[0].message.content
        suggestions = [s.strip("- ") for s in llm_output.split("\n") if s.strip()]

    except Exception:
        suggestions = [
            "Reduce text density and highlight key services.",
            "Improve spacing between sections for better visual flow.",
            "Add a prominent Call-To-Action button.",
            "Adjust brightness and contrast for improved readability."
        ]

    return {
        "brightness": round(brightness, 2),
        "contrast": round(contrast, 2),
        "detected_text": texts,
        "suggestions": suggestions
    }
