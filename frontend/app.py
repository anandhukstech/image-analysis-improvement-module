import streamlit as st
import requests

st.set_page_config(page_title="Image Analysis & Improvement")

st.title("📊 Image Analysis & Improvement Suggestion Module")

uploaded = st.file_uploader(
    "Upload Marketing Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:
    st.image(uploaded, width=400)

    if st.button("Analyze Image"):
        with st.spinner("Analyzing with AI..."):
            files = {"file": uploaded.getvalue()}
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                files=files
            )

            if response.status_code == 200:
                data = response.json()

                st.subheader("📄 Detected Text")
                for t in data.get("detected_text", []):
                    st.write(t)

                st.subheader("✅ Improvement Suggestions")
                for s in data.get("suggestions", []):
                    st.write("•", s)

                st.subheader("📈 Image Metrics")
                st.write("Brightness:", data.get("brightness"))
                st.write("Contrast:", data.get("contrast"))
            else:
                st.error("Backend not responding")
