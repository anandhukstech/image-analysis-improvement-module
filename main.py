import streamlit as st

from enhancement import enhance_image
from enhancement_lock import image_hash
from image_analysis import analyze_image_quality
from scoring import calculate_quality_score
from text_analysis_easyocr import analyze_text_easyocr
from utils import decode_image, resize_image
from ollama_client import generate_ai_suggestions

# 🔒 Keeps track of already-enhanced images
ENHANCED_HASHES = set()

# ⚡ CACHE OCR (BIG SPEED BOOST)
@st.cache_data(show_spinner=False)
def cached_ocr(img_hash, image):
    return analyze_text_easyocr(image)

# ⚡ CACHE AI CALL (BIG SPEED BOOST)
@st.cache_data(show_spinner=False)
def cached_ai(img_hash, metrics, score, text_data):
    return generate_ai_suggestions(metrics, score, text_data)


def process_image(uploaded_file, use_ai=True):
    # Decode & resize image
    image = resize_image(decode_image(uploaded_file))

    # Hash original upload
    original_hash = image_hash(image)

    # 🚫 PREVENT RE-ENHANCEMENT
    if original_hash in ENHANCED_HASHES:
        enhanced = image
        final_hash = original_hash
        status = "✅ Image already enhanced. Stable output shown."
    else:
        enhanced = enhance_image(image)
        final_hash = image_hash(enhanced)
        ENHANCED_HASHES.add(final_hash)
        status = "✨ Image enhanced once. Locked for stability."

    # 📊 Image quality metrics (FAST)
    metrics = analyze_image_quality(enhanced)
    score = calculate_quality_score(metrics)

    # 📝 OCR (CACHED)
    text_data = cached_ocr(final_hash, enhanced)

    # 🤖 AI Suggestions (CACHED & OPTIONAL)
    if use_ai:
        ai_suggestions = cached_ai(final_hash, metrics, score, text_data)
    else:
        ai_suggestions = "AI analysis disabled by user."

    return {
        "original": image,
        "enhanced": enhanced,
        "metrics": metrics,
        "score": score,
        "text_data": text_data,
        "ai_suggestions": ai_suggestions,
        "status": status
    }