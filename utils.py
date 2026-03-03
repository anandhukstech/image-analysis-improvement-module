import cv2
import numpy as np

def decode_image(uploaded_file):
    image_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Invalid image file")
    return image

def resize_image(image, max_width=900):
    h, w = image.shape[:2]
    if w <= max_width:
        return image
    ratio = max_width / w
    return cv2.resize(image, (max_width, int(h * ratio)))