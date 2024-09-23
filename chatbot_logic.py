

# importing necessary libraries
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.question_answering import load_qa_chain
from prompt import prompt_template

#function to create a conversation chain between the custome prompt and model 
def conversation_chain(userName, userGrade, userSubject, numberQuestion, difficulty):
    """ conversational chain for the chat model with the proper prompt template to train the model on basis of user entered detail to generate a quiz
        Args: NONE
        Returns : chain 
        """
    # chatbot model of google genmini 
    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)
    # prompt template for the  gemini model with necessary input variable and prompt text 
    prompt = PromptTemplate(template = prompt_template, input_variables=["userName", "userGrade", "userSubject", "numberQuestion", "difficultyLevel"])
    # loading the gemini model and prompt to a single chain 
    chain = LLMChain(llm=model, prompt=prompt)
    # Generating a respone by invoking the model 
    response = chain.invoke(
        {"userName": userName,
        "userGrade": userGrade,
        "userSubject": userSubject,
        "numberQuestion": numberQuestion, 
        "difficultyLevel": difficulty}
        , return_only_outputs=True)

    return response