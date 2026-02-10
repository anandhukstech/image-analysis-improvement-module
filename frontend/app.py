import streamlit as st
import requests

st.set_page_config(page_title="Image Analysis Module")

st.title("📊 Image Analysis & Improvement Suggestion Module")

uploaded = st.file_uploader(
    "Upload Marketing Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded:
    st.image(uploaded, caption="Uploaded Image", use_container_width=True)

    if st.button("Analyze Image"):

        with st.spinner("Analyzing..."):
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                files={"file": uploaded}
            )

        if response.status_code == 200:
            data = response.json()

            st.subheader("📄 Detected Text")
            st.write(data["detected_text"])

            st.subheader("✅ Improvement Suggestions")
            for s in data["suggestions"]:
                st.success(s)

            st.subheader("📈 Image Metrics")
            st.write("Brightness:", data["brightness"])
            st.write("Contrast:", data["contrast"])

        else:
            st.error("Backend not responding.")
