import cv2
import numpy as np

def enhance_image(image):
    """
    Deterministic, text-safe enhancement
    """

    # LAB color space for contrast control
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l = clahe.apply(l)

    lab = cv2.merge((l, a, b))
    enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    # Mild denoising
    enhanced = cv2.fastNlMeansDenoisingColored(
        enhanced, None, 6, 6, 7, 21
    )

    # Edge-preserving sharpening (text clarity)
    blur = cv2.GaussianBlur(enhanced, (0, 0), 1.0)
    enhanced = cv2.addWeighted(enhanced, 1.4, blur, -0.4, 0)

    return enhanced