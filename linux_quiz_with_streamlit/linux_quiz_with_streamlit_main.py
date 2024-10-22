import streamlit as st
import json


# load quiz data
def load_quiz_data(pathx=r'linux_quiz_with_streamlit/linux_quiz_data.json'):
    with open(pathx, 'r') as file_to_read:
        file_content = file_to_read.read()
    quiz_datax = json.loads(file_content)
    return quiz_datax


# if script is a port of the question write script or pass
def write_question_script(question_script):
    if question_script:
        st.code(question_script)


def save_quiz_data_with_answers(quiz_data_with_answers):
    with open(r'linux_quiz_with_streamlit/linux_quiz_data_with_answers.json', 'w', encoding='utf-8') as file_to_save:
        json.dump(quiz_data_with_answers, file_to_save, ensure_ascii=False, indent=4)


# function to display quiz questions and collect user responses
def display_quiz(question_setx):

    # create a form
    with st.form('Linux question'):
        for index, question_datax in enumerate(question_setx):

            st.write(f"{index + 1}. {question_datax['Question']}")

            write_question_script(question_datax['Bash script'])

            # display options using radio buttons
            user_answer = st.radio('Select your answer:',
                                   [question_datax['Answer A'],
                                    question_datax['Answer B'],
                                    question_datax['Answer C'],
                                    question_datax['Answer D']],
                                   index=None)

            # check if the selected answer is correct
            if user_answer == question_datax["Correct Answer"]:
                question_datax['Answer_color'] = 'green'
            else:
                question_datax['Answer_color'] = 'red'

            # store user answer in variable
            answers = [question_datax['Answer A'], question_datax['Answer B'], question_datax['Answer C'],
                       question_datax['Answer D']]

            # Find the index of the user's answer in the list
            if user_answer in answers:
                question_datax['User answer'] = answers.index(user_answer)
            else:
                question_datax['User answer'] = None

            # display an empty line between questions
            st.write('')

        # submit button to calculate the score
        finish_quiz_button = st.form_submit_button('Submit answers')

        # display the message after the user submits the quiz
        if finish_quiz_button:
            save_quiz_data_with_answers(question_setx)
            st.session_state.quiz_submitted = True
            st.rerun()


# MAIN PART OF THE QUIZ APP
# Set a session state variable to track if the quiz has been submitted
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False

# add steps to remove DuplicateWidgetID error
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# Load data, display image and question sets
quiz_question_data = load_quiz_data()
question_category = ['Shell Scripting', 'Shell Scripting 2: Regular expressions', 'User and Group Management',
                     'Process Management', 'Package Management', 'File Viewing and Editing',
                     'System Information and Management', 'Network Configuration and Monitoring']
question_set_picked = st.radio(
    'Choose a set of questions',
    question_category
)
question_set = [item for item in quiz_question_data if item["Category"] == question_set_picked]

st.image('linux_quiz_with_streamlit/Linux_image2.jpg')
st.title('Linux knowledge quiz')

if not st.session_state.quiz_submitted:
    display_quiz(question_set)

# Display results after submission
if st.session_state.quiz_submitted:
    question_set_with_answers = load_quiz_data(r'linux_quiz_with_streamlit/linux_quiz_data_with_answers.json')
    st.write('You finished the quiz!')
    with st.form('Linux answers'):
        for index, question_data2 in enumerate(question_set_with_answers):
            st.write(f"{index + 1}. :{question_data2['Answer_color']}[{question_data2['Question']}]")

            write_question_script(question_data2['Bash script'])

            # display answers using radio buttons
            user_answer2 = st.radio('Select your answer:',
                                    [question_data2['Answer A'],
                                     question_data2['Answer B'],
                                     question_data2['Answer C'],
                                     question_data2['Answer D']],
                                    index=question_data2['User answer'],
                                    disabled=True)

            if user_answer2 != question_data2['Correct Answer']:
                st.write(f"The correct answer is: :red[{question_data2['Correct Answer']}]")

        # Quiz submission button
        new_quiz = st.form_submit_button('Submit')

# source: https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/linux/linux-quiz.md
