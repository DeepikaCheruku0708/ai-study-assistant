import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


st.title("AI Study Assistant")

topic = st.text_input("Enter a Topic")

if st.button("Generate Notes"):

    prompt = f"""
    Explain {topic} for a beginner.

    Also provide:
    1. Short Explanation
    2. Key Points
    3. Interview Questions
    """

    response = model.generate_content(prompt)

    st.write(response.text)