import streamlit as st
from transformers import pipeline

st.title("AI Content Buddy")

generator = pipeline("text-generation", model="distilgpt2")

prompt = st.text_input("Enter your idea or topic:")

if st.button("Generate"):
    if prompt.strip():
        with st.spinner("Generating content..."):
            result = generator(prompt, max_length=100, num_return_sequences=1)
            st.text_area("Generated Content", result[0]['generated_text'], height=200)
    else:
        st.warning("Please enter some text!")