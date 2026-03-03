import streamlit as st
import cv2
from main import process_image

st.set_page_config(
    page_title="Image Analysis and Improvement Suggestion Module",
    layout="wide"
)

st.title("🖼️ Image Analysis and Improvement Suggestion Module")
st.caption("Stable Enhancement • EasyOCR • Ollama LLM • Optimized Performance")

# AI toggle
use_ai = st.checkbox("🤖 Use AI Suggestions (Ollama)", value=True)

# Upload image
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    # 🔍 CLEAR PROCESSING INDICATOR
    with st.spinner("⚡ Enhancing image • 🔍 Reading text • 🤖 Analyzing with AI..."):
        result = process_image(uploaded_file, use_ai)

    st.success("✅ Analysis completed successfully")
    st.info(result["status"])

    # Show images
    col1, col2 = st.columns(2)

    with col1:
        st.image(
            cv2.cvtColor(result["original"], cv2.COLOR_BGR2RGB),
            caption="Original Image"
        )

    with col2:
        st.image(
            cv2.cvtColor(result["enhanced"], cv2.COLOR_BGR2RGB),
            caption="Enhanced Image (Stable Output)"
        )

    # Quality score
    st.subheader("📊 Image Quality Score")
    st.metric("Overall Score", f"{result['score']}/100")

    # Metrics
    st.subheader("📈 Image Quality Metrics")
    st.json(result["metrics"])

    # OCR results
    st.subheader("📝 Text Analysis (EasyOCR)")
    for line in result["text_data"]["analysis"]:
        st.write("•", line)

    st.subheader("✅ Text Improvement Recommendations")
    for rec in result["text_data"]["recommendations"]:
        st.success(rec)

    # AI results
    st.subheader("🤖 AI Improvement Suggestions (Ollama)")
    if use_ai:
        st.success(result["ai_suggestions"])
    else:
        st.warning("AI suggestions are turned OFF")

else:
    st.info("⬆️ Upload an image to start analysis")