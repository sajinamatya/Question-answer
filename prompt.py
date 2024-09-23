prompt_template = """
    Generate a "Quiz with four option per question with the correct answer" based detail given below.\n\n
    Grade:\n {userGrade}\n
    Subject:\n {userSubject}\n
    Topic:\n {userGrade}\n
    Dificulity level : \n{difficultyLevel}\n
    Number of question to generate: \n{numberQuestion}\n
    ---
    Maintain spacing between the question, option and answer
    ---
    Create it in a **Formatted Nested JSON code**
    --- 
    Don't forget to "greet the user with their name provide below 
    User Information:\n
    Name: \n{userName}\n
    ---
    Heading should  include the grade, number of question and difficulty level 
  
    Answer:
    """