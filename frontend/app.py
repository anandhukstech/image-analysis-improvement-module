import streamlit as st
import requests

st.set_page_config(page_title="AI Marketing Evaluation", layout="centered")

st.title("📊 Image Analysis & Improvement Suggestion Module")

uploaded = st.file_uploader("Upload Marketing Image", type=["jpg", "png", "jpeg"])

if uploaded:
    st.image(uploaded, width=400)

    with st.spinner("Analyzing image..."):
        files = {"file": uploaded.getvalue()}
        response = requests.post("http://127.0.0.1:8000/analyze", files=files)
        data = response.json()

    st.subheader("📄 Detected Text")
    if data["detected_text"]:
        for t in data["detected_text"]:
            st.write("•", t)
    else:
        st.write("No text detected")

    st.subheader("✅ Improvement Suggestions")
    for s in data["suggestions"]:
        st.write("•", s)

    st.subheader("📈 Image Metrics")
    st.write("Brightness:", data["brightness"])
    st.write("Contrast:", data["contrast"])