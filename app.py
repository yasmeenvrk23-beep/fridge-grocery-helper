import streamlit as st
from PIL import Image

st.set_page_config(page_title="Fridge-to-Grocery Helper", page_icon="🥬")

st.title("🥬 The Lazy Fridge-to-Grocery Helper")
st.write("Snap a photo of your fridge, and let AI build your shopping list so you don't have to think.")

# Image uploader (works seamlessly with your phone camera)
uploaded_file = st.file_uploader("Upload a photo of your fridge or pantry", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Fridge", use_container_width=True)
    
    if st.button("Generate Grocery List 🛒"):
        with st.spinner("Analyzing your fridge contents with Gemma..."):
            # Simulated AI output for the hackathon demo
            st.success("Done! Here is your smart shopping list:")
            st.markdown("""
            * **Produce:** Fresh spinach, tomatoes, bell peppers
            * **Dairy:** Almond milk, Greek yogurt
            * **Pantry:** Olive oil, garlic paste
            """)
  
