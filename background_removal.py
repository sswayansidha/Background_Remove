import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Background Remover", layout="centered")

st.title("✂️ AI Background Remover")
st.write("Upload an image to remove the background instantly!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the original image
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Original")
        st.image(image, use_container_width=True)

    # Process the image
    with st.spinner("Removing background..."):
        # Convert image to bytes for rembg
        result = remove(image)
        
        # Prepare for download
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        byte_im = buf.getvalue()

    with col2:
        st.header("Result")
        st.image(result, use_container_width=True)

    # Download button
    st.download_button(
        label="Download Result",
        data=byte_im,
        file_name="nobg_image.png",
        mime="image/png"
    )