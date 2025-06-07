import streamlit as st
from random import choice

# Constants
PAGE_BG_STYLE = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("some url");
    background-size: cover;
    }
</style>
"""


def print_user_quess(button):
    st.title(button)


def game():
    guess = print_out['text']

    if guess.lower() in sacred_word\
    or guess.upper() in sacred_word:
        for index, letter in enumerate(sacred_word):

            if guess.lower() == letter:
                word_puzzle[index] = guess.lower() + ' '
                label_word_puzzle['text'] = ''.join(list(word_puzzle))

            if guess.upper() == letter:
                word_puzzle[index] = guess.upper() + ' '
                label_word_puzzle['text'] = ''.join(list(word_puzzle))

            if '_ ' not in word_puzzle:
                end_game_label = st.Label(master=window, text='You won!', font='Arial 16', bg='#5bdddd', height=1,
                                       width=15)
                end_game_label.place(x=355, y=120)

    else:
        number_of_lives['text'] -= 1
        lives_emoji['text'] = '\U00002764' * number_of_lives['text']
        global hangman_picture
        hangman_picture = st.PhotoImage(file=f"images\\hang_{7 - int(number_of_lives['text'])}.png")
        hangman_image['image'] = hangman_picture

        if number_of_lives['text'] < 1:
            end_game_label = st.Label(master=window, text='You lost!', font='Arial 16', bg='#5bdddd', height=1,
                                      width=15)
            end_game_label.place(x=355, y=120)
            lives_emoji.config(text=sacred_word, anchor='center')


# load data and set variable
with open('data/english_words.txt') as file:
    all_words = file.readlines()
sacred_word = choice(all_words)
word_puzzle = ['_ '] * len(sacred_word)
number_of_lives = 7
if 'users_tip' not in st.session_state:
    st.session_state['users_tip'] = ''

# GUI
st.title('Game Hangman')
st.button(label='Lives: ' + '\U00002764' * number_of_lives)
st.button(label=st.session_state['users_tip'])
st.button(label=str(word_puzzle))
st.button(label='Confirm')
st.image('images\\hang_0.png')

# Alphabet buttons
alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
for index, alpha in enumerate(alphabet):
    if st.button(label=alpha, key=index):
        st.session_state['users_tip'] = alpha
        # st.rerun() run only locally


st.session_state
