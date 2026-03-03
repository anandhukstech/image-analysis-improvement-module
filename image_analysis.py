import cv2
import numpy as np

def analyze_image_quality(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return {
        "brightness": round(float(np.mean(gray)), 2),
        "contrast": round(float(np.std(gray)), 2),
        "sharpness": round(float(cv2.Laplacian(gray, cv2.CV_64F).var()), 2)
    }