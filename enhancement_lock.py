import hashlib

def image_hash(image):
    """
    Pixel-level hash to prevent re-enhancement
    """
    return hashlib.sha256(image.tobytes()).hexdigest()