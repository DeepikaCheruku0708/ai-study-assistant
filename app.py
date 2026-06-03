import streamlit as st

st.title("AI Study Assistant")

topic = st.text_input("Enter Topic")

if st.button("Generate Notes"):
    st.write("You entered:", topic)