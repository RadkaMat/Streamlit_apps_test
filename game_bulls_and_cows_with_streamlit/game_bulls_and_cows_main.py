import streamlit as st
import random


# Function to initialize or reset the game
def generate_secred_number():
    """ Random number between 1023 and 9876 """
    while True:
        secred_number = str(random.randint(1023, 9876))
        if len(set(secred_number)) == 4:
            break
    return secred_number


def reset_game():
    """ Initialize game variables """
    st.session_state['number'] = int(generate_secred_number())
    st.session_state['attempts'] = 0  # Reset attempts
    st.session_state['cow_score'] = ''


# Check if 'number' and 'attempts' are already in session_state (i.e., the game is ongoing)
if 'number' not in st.session_state or 'attempts' not in st.session_state:
    reset_game()  # Initialize game variables

# Title for the app
st.title('🐂 Guess the Number! 🐄')

# User input for guesses
players_guess = st.text_input('Enter your guess 4-digit number:', key='guess')

# Button to make a guess
if st.button('Guess'):
    # decrease difficulty
    # if players_guess < int(st.session_state.number):
    #    st.warning('Too low! Try again.')
    # elif players_guess > int(st.session_state.number):
    #    st.error('Too high! Try again.')
    st.session_state.attempts += 1  # Increment attempts
    if not players_guess.isnumeric():
        st.markdown(':red[Write only numbers.]')
    elif players_guess[0] == '0':
        st.markdown(':red[Digit 0 must not be on 1. position.]')
    elif len(players_guess) != 4:
        st.markdown(':red[Your number must have exactly 4 digits.]')
    elif len(set(players_guess)) != 4:
        st.markdown(':red[Your number must not contain duplicite digit.]')
    else:
        bulls = []
        cows = []
        bulls_emoji = '🐂'
        cows_emoji = '🐄'
        secred_number = str(st.session_state['number'])
        for index, digit in enumerate(players_guess):
            if digit in secred_number and secred_number[index] == players_guess[index]:
                 bulls.append(digit)
            if digit in secred_number and secred_number[index] != players_guess[index]:
                cows.append(digit)

        if len(bulls) == 1:
            bulls_count = 'bull'
        else:
            bulls_count = 'bulls'
        if len(cows) == 1:
            cows_count = 'cow'
        else:
            cows_count = 'cows'

        st.session_state['cow_score'] = f"{len(bulls)} {bulls_count} {bulls_emoji * len(bulls)}, {len(cows)} {cows_count} {cows_emoji * len(cows)}"
        # Victory
        if len(bulls) == 4:
            st.success(f'Congratulations! You found the number {st.session_state.number} in {st.session_state.attempts} attempts.')
            if st.button('Play Again'):
                reset_game()

# Show the current number of attempts
st.write(f'Attempts: {st.session_state.attempts}')
st.write(f'Cow score: {st.session_state.cow_score}')

# Optionally, add a button to reset the game at any time
if st.button('Reset Game'):
    reset_game()
