import streamlit as st
from PIL import Image
# from your_module import YourCustomTextGenerationModel  # Import your custom model

# Instantiate your custom model
# model = YourCustomTextGenerationModel()

# def generate_text(image, prompt):
#     # Generate text using your custom model
#     text = model.generate(image, prompt)
#     return text
import runModel

def main():
    st.title("Visual Question Answering System")

    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)

        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Input prompt
        prompt = st.text_input("Enter a prompt for generating text")

        if st.button("Generate Text"):
            if prompt:

                st.write("Generated Text:",runModel.execute(prompt,image))
            else:
                st.error("Please enter a prompt.")

if __name__ == "__main__":
    main()
