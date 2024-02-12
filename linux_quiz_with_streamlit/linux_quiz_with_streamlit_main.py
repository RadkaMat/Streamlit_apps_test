import streamlit as st
import json


# load quiz data
with open(r'linux_quiz_with_streamlit/linux_quiz_data.json', 'r') as file_to_read:
    file_content = file_to_read.read()
quiz_data = json.loads(file_content)


# Function to get color based on difficulty
def get_color(difficulty):
    if difficulty.lower() == "easy":
        return "green"
    elif difficulty.lower() == "medium":
        return "yellow"
    elif difficulty.lower() == "hard":
        return "orange"
    else:
        return "black"  # Default color


def display_quiz():
    score = 0

    # create a form
    with st.form('Linux question'):
        for index, question_data in enumerate(quiz_data):
            # Get color based on difficulty
            # color = get_color(question_data['Difficulty'])

            # Colorful question name using HTML formatting
            # st.write(f"<h5 style='color: {color};'> {question_data['Difficulty']} question</h5> {index + 1}. {question_data['Question']}",
            #         unsafe_allow_html=True)
            st.write(f"{index + 1}. question_data['Question']")
            st.write(question_data['Bash script'])

            # display options using radio buttons
            user_answer = st.radio('Select your answer:',
                                   [question_data['Answer A'],
                                    question_data['Answer B'],
                                    question_data['Answer C'],
                                    question_data['Answer D']])

            # check if the selected answer is correct
            if user_answer == question_data["Correct Answer"]:
                score += 1

            # display an empty line between questions
            st.write('')

        # submit button to calculate the score
        submit_button = st.form_submit_button('Submit answers')

    return score, submit_button


# main(), display the image at the top, the quiz and get the score
st.image(r'linux_quiz_with_streamlit/Linux_image2.jpg')
st.title('Linux knowledge quiz')
score, submit_button = display_quiz()

# display the score only after the user submits the quiz
if submit_button:
    st.write(f"Your scored {score} out of {len(quiz_data)} quistions.")
    min_score_perc = 70
    min_score = len(quiz_data)/100 * min_score_perc
    if score > min_score:
        st.write('🙂 Congratulation! You passed the exam.')
    else:
        st.write('😕 You failed the exam. You should learn more.')
        st.image(r'linux_quiz_with_streamlit/Linux_Commands.png')
      
