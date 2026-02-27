import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model


@st.cache_resource
def load_dr_model():
    model_path = "dr_binary_model.h5"
    model = load_model(model_path)
    return model


def preprocess_image(image: Image.Image, target_size=(224, 224)):
    image = image.convert("RGB")
    image = image.resize(target_size)
    img_array = np.array(image, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def get_risk_category(prob: float) -> str:
    if prob < 0.2:
        return "Low Risk"
    if prob <= 0.4:
        return "Borderline"
    if prob <= 0.7:
        return "Moderate Risk"
    return "High Risk"


def main():
    st.set_page_config(
        page_title="Diabetic Retinopathy Screening",
        page_icon="👁️",
        layout="centered",
    )

    st.title("Diabetic Retinopathy Screening")
    st.markdown(
        "Upload a **retinal fundus image** to screen for Diabetic Retinopathy using a "
        "pre-trained deep learning model."
    )

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload a retinal image",
        type=["jpg", "jpeg", "png"],
        help="Supported formats: JPG, JPEG, PNG",
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("Uploaded Image")
            st.image(image)

        with col2:
            st.subheader("Prediction")

            with st.spinner("Analyzing image..."):
                model = load_dr_model()
                input_tensor = preprocess_image(image)
                prob = float(model.predict(input_tensor)[0][0])

            threshold = 0.4
            has_dr = prob > threshold

            label_text = "DR Detected" if has_dr else "No DR"
            label_color = "red" if has_dr else "green"

            st.markdown(
                f"<h3 style='color:{label_color};'>Prediction: {label_text}</h3>",
                unsafe_allow_html=True,
            )

            st.markdown(f"**DR Probability:** `{prob:.4f}`")

            risk_category = get_risk_category(prob)
            st.markdown(f"**Risk Category:** {risk_category}")

            st.caption(
                "Threshold for positive DR prediction is probability > 0.4."
            )

    else:
        st.info("Please upload a retinal image to begin.")


if __name__ == '__main__':
    main()

