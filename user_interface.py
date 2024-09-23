import streamlit as st
from chatbot_logic import conversation_chain 
from dotenv import load_dotenv
import google.generativeai as genai
import json 
load_dotenv()

def user_interface():

    st.title("Quiz Generator Chatbot")
    st.info("Generate a quiz question with 4 option and correct answer")

    with st.form(key='inputform'):
        userName = st.text_input("Enter your name")
        userGrade = st.text_input("Grade")
        userSubject = st.text_input("Subject related to the entered grade")
        numberQuestion = st.text_input("Number of question")
        difficultyLevel = st.selectbox(
                            "Select the difficulty level",
                            ("Easy", "Medium", "Hard"),
                            )
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if name_validation(userName) == True and is_empty(userName, userGrade,userSubject,numberQuestion,difficultyLevel) == False:
                input_detail(userName,userGrade,userSubject,numberQuestion,difficultyLevel)
                
                st.session_state.userName = userName 
                st.session_state.userGrade = userGrade
                st.session_state.userSubject = userSubject
                st.session_state.numberQuestion = numberQuestion
                st.session_state.difficultyLevel = difficultyLevel

                
                with st.spinner("Processing..."):
                     response = conversation_chain(userName, userGrade,userSubject,numberQuestion,difficultyLevel)
                     
                        

                     st.success("Processed")
                with st.container():
                    st.write(response['text'])
                    
                    
            else:
                st.error("Error while process, please check the input")

def input_detail(name,grade,subject,numberqn,difficultylevel):
    with st.container():
        st.write("Your name: " + name)
        st.write("Entered grade : " + grade)
        st.write("subject : " + subject)
        st.write("Number of question : "+ numberqn)
        st.write("Difficulty level : " + difficultylevel)




def name_validation(name):
    if name.replace(" ","").isalpha(): 
        return True
    else :
        False

def is_empty(name,grade,subject,numberqn,difficultylevel):
    if not name or not grade or not subject or not numberqn or not difficultylevel:
        return True
    else:
        return False

user_interface()        