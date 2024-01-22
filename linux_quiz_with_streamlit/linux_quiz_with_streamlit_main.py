import streamlit as st
from json import loads
import time


# load quiz data
with open(r'linux_quiz_with_streamlit/linux_quiz_data.json', 'r') as file_to_read:
    file_content = file_to_read.read()
quiz_data = loads(file_content)


# Function to get color based on difficulty
def get_color(difficulty):
    if difficulty.lower() == "easy":
        return "green"
    elif difficulty.lower() == "medium":
        return "yellow"
    elif difficulty.lower() == "hard":
        return "red"
    else:
        return "black"  # Default color


def display_quiz(time_limit=1):
    score = 0

    # Set the start time
    start_time = time.time()

    # create a form
    with st.form('Linux question'):
        for index, question_data in enumerate(quiz_data):
            # Get color based on difficulty
            color = get_color(question_data['Difficulty'])

            # Colorful question name using HTML formatting
            st.write(f"<h5 style='color: {color};'> {question_data['Difficulty']} question</h5> {index + 1}. {question_data['Question']}",
                     unsafe_allow_html=True)
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

    # Check the time elapsed
    elapsed_time = time.time() - start_time
    remaining_time = max(0, time_limit * 60 - elapsed_time)  # Calculate remaining time in seconds

    # Display countdown timer
    st.write(f"Time left: {int(remaining_time)} seconds")

    if elapsed_time > (time_limit * 60):  # Convert time limit to seconds
        st.warning(f"Time limit exceeded! Quiz automatically submitted.")
        submit_button = True  # Automatically submit the quiz



    return score, submit_button


# display the image at the top, the quiz and get the score
st.image(r'linux_quiz_with_streamlit/Linux_image.jpg', width=620)
st.image(r'linux_quiz_with_streamlit/Linux_image2.jpg', width=620)
st.title('Linux knowledge quiz')
score, submitted = display_quiz()

# display the score only after the user submits the quiz
if submitted:
    st.write(f"Your scored {score} out of {len(quiz_data)} quistions.")
    min_score_perc = 70
    min_score = len(quiz_data)/100 * min_score_perc
    if score > min_score:
        st.write('🙂 Congratulation! You passed the exam.')
    else:
        st.write('😕 You failed the exam. You should learn more.')
        st.image(r'linux_quiz_with_streamlit/Linux_Commands.png')
      
