import streamlit as st


def user_interface():
    st.title("Quiz Generator Chatbot")
    st.info("Generate a quiz question with 4 option and correct answer")

    with st.form(key='inputform'):
        userName = st.text_input("Enter your name")
        userGrade = st.text_input("For which grade are you planing to  generate a quiz")
        userSubject = st.text_input("Subject related to the entered grade")
        numberQuestion = st.text_input("Number of question")
        difficultyLevel = st.selectbox(
                            "Select the difficulty level",
                            ("Easy", "Medium", "Hard"),
                            )
user_interface()        