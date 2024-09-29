import streamlit as st
import json


# load quiz data
def load_quiz_data():
    with open(r'linux_quiz_with_streamlit/linux_quiz_data.json', 'r') as file_to_read:
        file_content = file_to_read.read()
    quiz_datax = json.loads(file_content)
    return quiz_datax


# if script is a port of the question write script or pass
def write_question_script(question_script):
    if question_script:
        st.code(question_script)


# function to display quiz questions and collect user responses
def display_quiz(question_set):
    right_answers_total = 0
    wrong_answers = dict()
    all_answers = list()

    # create a form
    with st.form('Linux question'):
        for index, question_data in enumerate(question_set):
            st.write(f"{index + 1}. {question_data['Question']}")

            st.write(question_data['Bash script'])

            # display options using radio buttons
            user_answer = st.radio('Select your answer:',
                                   [question_data['Answer A'],
                                    question_data['Answer B'],
                                    question_data['Answer C'],
                                    question_data['Answer D']],
                                   index=None)

            # check if the selected answer is correct
            if user_answer == question_data["Correct Answer"]:
                all_answers.append(user_answer)
            else:
                all_answers.append('')

            # check if the selected answer is correct
            if user_answer == question_data['Correct Answer']:
                right_answers_total += 1
            else:
                wrong_answers[question_data['Question']] = question_data['Correct Answer']

            # display an empty line between questions
            st.write('')

        # submit button to calculate the score
        finish_quiz_button = st.form_submit_button('Submit answers')

        # display the message after the user submits the quiz
        if finish_quiz_button:
            st.write('You finished the quiz!')
            st.write(f"Number of right answers: {right_answers_total}, from total: {len(question_set)}.")
            st.write('Correct answers are:')
            st.dataframe(wrong_answers)
            print(all_answers)


# MAIN PART OF THE QUIZ APP
# load data, display image and question sets
quiz_data = load_quiz_data()

st.image('Linux_image2.jpg')
st.title('Linux knowledge quiz')
question_set_picked = st.radio(
    'Choose a set of questions',
    [1, 2, 3, 4, 5, 6]
)

# assuming each quiz part has 20 questions
questions_per_set = 20
start_index = (question_set_picked - 1) * questions_per_set
end_index = start_index + questions_per_set

# Display the selected quiz questions
display_quiz(quiz_data[start_index:end_index])

# source: https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/linux/linux-quiz.md
