import cv2
import numpy as np
import easyocr

# Load OCR once
reader = easyocr.Reader(['en'], gpu=False)


def analyze_image(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Invalid image file")

        img = cv2.resize(img, (800, 800))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        brightness = float(np.mean(gray))
        contrast = float(np.std(gray))

        # OCR
        ocr_result = reader.readtext(image_path)
        detected_text = [t[1] for t in ocr_result]

        suggestions = []

        # -------- MARKETING RULE ENGINE -------- #

        # Rule 1: Text overload
        if len(detected_text) > 10:
            suggestions.append(
                "Reduce text content to improve readability and visual hierarchy."
            )

        # Rule 2: CTA detection
        cta_keywords = ["call", "contact", "join", "buy", "register", "learn more"]
        if not any(any(k.lower() in t.lower() for k in cta_keywords) for t in detected_text):
            suggestions.append(
                "Add a clear Call-To-Action (CTA) to guide user engagement."
            )

        # Rule 3: Brightness
        if brightness < 80:
            suggestions.append(
                "Increase image brightness to improve visibility and user attention."
            )
        elif brightness > 200:
            suggestions.append(
                "Reduce brightness slightly to avoid visual fatigue."
            )

        # Rule 4: Contrast
        if contrast < 40:
            suggestions.append(
                "Improve contrast between text and background for better legibility."
            )

        # Rule 5: Branding
        branding_keywords = ["logo", "brand", "company"]
        if not any(any(k.lower() in t.lower() for k in branding_keywords) for t in detected_text):
            suggestions.append(
                "Ensure brand elements like logo or brand name are clearly visible."
            )

        if not suggestions:
            suggestions.append(
                "Overall design is balanced. Minor refinements can further enhance visual appeal."
            )

        return {
            "detected_text": detected_text if detected_text else ["No text detected"],
            "brightness": round(brightness, 2),
            "contrast": round(contrast, 2),
            "suggestions": suggestions
        }

    except Exception as e:
        return {
            "detected_text": ["No text detected"],
            "brightness": None,
            "contrast": None,
            "suggestions": [str(e)]
        }
