import easyocr
import cv2
import numpy as np

_reader = None

def get_reader():
    global _reader
    if _reader is None:
        _reader = easyocr.Reader(["en"], gpu=False)
    return _reader

def analyze_text_easyocr(image):
    reader = get_reader()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    results = reader.readtext(gray)

    word_count = 0
    heights = []
    confidences = []

    for bbox, text, conf in results:
        if text.strip():
            word_count += 1
            confidences.append(conf)
            (tl, tr, br, bl) = bbox
            heights.append(abs(br[1] - tr[1]))

    avg_size = int(np.mean(heights)) if heights else 0
    avg_conf = round(float(np.mean(confidences)), 2) if confidences else 0.0

    analysis = []
    recommendations = []

    if word_count == 0:
        analysis.append("No readable text detected.")
        recommendations.append("Increase contrast and text size.")
    else:
        analysis.append(f"Detected {word_count} text elements.")
        if avg_size < 15:
            recommendations.append("Increase font size.")
        if avg_conf < 0.5:
            recommendations.append("Improve text contrast.")

    if not recommendations:
        recommendations.append("Text clarity looks good.")

    return {
        "word_count": word_count,
        "avg_text_size": avg_size,
        "confidence": avg_conf,
        "analysis": analysis,
        "recommendations": recommendations
    }