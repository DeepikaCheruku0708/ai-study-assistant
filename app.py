import streamlit as st

st.title("AI Study Assistant")

topic = st.text_input("Enter Topic")

if st.button("Generate Notes"):

    if topic.lower() == "python":

        st.subheader("Python")

        st.write("Python is a popular programming language used in AI, Data Science, and Web Development.")

    elif topic.lower() == "machine learning":

        st.subheader("Machine Learning")

        st.write("Machine Learning is a branch of Artificial Intelligence that allows computers to learn from data.")

    elif topic.lower() == "sql":

        st.subheader("SQL")

        st.write("SQL is used to store, retrieve, and manage data in databases.")

    elif topic.lower() == "artificial intelligence":

        st.subheader("Artificial Intelligence")

        st.write("AI enables machines to perform tasks that normally require human intelligence.")

    else:

        st.write("Sorry, notes are not available for this topic.")