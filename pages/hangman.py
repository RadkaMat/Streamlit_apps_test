import streamlit as st
from random import choice
from random_words import random_words1


def print_user_quess(button):
    print_out['text'] = button
    return button


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
        hangman_picture = st.PhotoImage(file=f"..\\pictures\\hang_{7 - int(number_of_lives['text'])}.png")
        hangman_image['image'] = hangman_picture

        if number_of_lives['text'] < 1:
            end_game_label = st.Label(master=window, text='You lost!', font='Arial 16', bg='#5bdddd', height=1,
                                      width=15)
            end_game_label.place(x=355, y=120)
            lives_emoji.config(text=sacred_word, anchor='center')


window = st.Tk()
window.title('Game Hangman')
window.geometry('608x342')
window.iconphoto(False, st.PhotoImage(file='..\\pictures\\icon.png'))

background_picture = st.PhotoImage(file='..\\pictures\\bg_meadow.png')
background = st.Label(window, image=background_picture)
background.place(x=0, y=0, relwidth=1, relheight=1)

sacred_word = choice(random_words1)
word_puzzle = ['_ '] * len(sacred_word)

button_picture = st.PhotoImage(file='..\\pictures\\button.png')
blue_button = st.Label(master=window, borderwidth=0, image=button_picture, bg='#33C6D8')
blue_button.place(x=195, y=6)

lives_label = st.Label(master=window, text='Lives:', font='Arial 18', bg='#4dcfdc', height=1, width=11)
lives_label.place(x=30, y=75)

number_of_lives = st.Label(master=window, text=7, font='Arial 18', bg='#4dcfdc', height=1, width=2)
number_of_lives.place(x=160, y=75)

lives_emoji = st.Label(master=window, text='\U00002764' * number_of_lives['text'], fg='red', font='Arial 16',
                     bg='#5bdddd', height=1, width=13, anchor='w')
lives_emoji.place(x=30, y=115)

print_out = st.Label(master=window, text='', font='Arial 16', height=1, width=4, bg='#5bdddd')
print_out.place(x=285, y=120)

title = st.Label(master=window, text='Game Hangman', font='Arial 18', bg='#7de6f0')
title.place(x=207, y=10)

label_word_puzzle = st.Label(master=window, text=''.join(list(word_puzzle)), font='Arial 16', bg='#4dcfdc', height=1, width=20)
label_word_puzzle.place(x=295, y=75)

confirm = st.Button(master=window, text='Confirm', font='Arial 16', command=game, bg='#5bdddd', height=1, width=16)
confirm.place(x=350, y=115)

hangman_picture1 = st.PhotoImage(file='..\\pictures\\hang_0.png')
hangman_image = st.Label(master=window, borderwidth=0, image=hangman_picture1)
hangman_image.place(x=50, y=152)

# Alphabet buttons
button_A = st.Button(master=window, text='A', font='Arial 16', bg='#b7ffeb', command=lambda button='A': print_user_quess(button))
button_A.place(x=230, y=180)

button_B = st.Button(master=window, text='B', font='Arial 16', bg='#b7ffeb', command=lambda button='B': print_user_quess(button))
button_B.place(x=270, y=180)

button_C = st.Button(master=window, text='C', font='Arial 16', bg='#b7ffeb', command=lambda button='C': print_user_quess(button))
button_C.place(x=310, y=180)

button_D = st.Button(master=window, text='D', font='Arial 16', bg='#b7ffeb', command=lambda button='D': print_user_quess(button))
button_D.place(x=350, y=180)

button_E = st.Button(master=window, text='E', font='Arial 16', bg='#b7ffeb', command=lambda button='E': print_user_quess(button))
button_E.place(x=390, y=180)

button_F = st.Button(master=window, text='F', font='Arial 16', bg='#b7ffeb', command=lambda button='F': print_user_quess(button))
button_F.place(x=430, y=180)

button_G = st.Button(master=window, text='G', font='Arial 16', bg='#b7ffeb', command=lambda button='G': print_user_quess(button))
button_G.place(x=470, y=180)

button_H = st.Button(master=window, text='H', font='Arial 16', bg='#b7ffeb', command=lambda button='H': print_user_quess(button))
button_H.place(x=510, y=180)

button_I = st.Button(master=window, text='I', font='Arial 16', bg='#b7ffeb', command=lambda button='I': print_user_quess(button))
button_I.place(x=550, y=180)

button_J = st.Button(master=window, text='J', font='Arial 16', bg='#b7ffeb', command=lambda button='J': print_user_quess(button))
button_J.place(x=230, y=230)

button_K = st.Button(master=window, text='K', font='Arial 16', bg='#b7ffeb', command=lambda button='K': print_user_quess(button))
button_K.place(x=270, y=230)

button_L = st.Button(master=window, text='L', font='Arial 16', bg='#b7ffeb', command=lambda button='L': print_user_quess(button))
button_L.place(x=310, y=230)

button_M = st.Button(master=window, text='M', font='Arial 16', bg='#b7ffeb', command=lambda button='M': print_user_quess(button))
button_M.place(x=350, y=230)

button_N = st.Button(master=window, text='N', font='Arial 16', bg='#b7ffeb', command=lambda button='N': print_user_quess(button))
button_N.place(x=390, y=230)

button_O = st.Button(master=window, text='O', font='Arial 16', bg='#b7ffeb', command=lambda button='O': print_user_quess(button))
button_O.place(x=430, y=230)

button_P = st.Button(master=window, text='P', font='Arial 16', bg='#b7ffeb', command=lambda button='P': print_user_quess(button))
button_P.place(x=470, y=230)

button_Q = st.Button(master=window, text='Q', font='Arial 16', bg='#b7ffeb', command=lambda button='Q': print_user_quess(button))
button_Q.place(x=510, y=230)

button_R = st.Button(master=window, text='R', font='Arial 16', bg='#b7ffeb', command=lambda button='R': print_user_quess(button))
button_R.place(x=550, y=230)

button_S = st.Button(master=window, text='S', font='Arial 16', bg='#b7ffeb', command=lambda button='S': print_user_quess(button))
button_S.place(x=240, y=280)

button_T = st.Button(master=window, text='T', font='Arial 16', bg='#b7ffeb', command=lambda button='T': print_user_quess(button))
button_T.place(x=280, y=280)

button_U = st.Button(master=window, text='U', font='Arial 16', bg='#b7ffeb', command=lambda button='U': print_user_quess(button))
button_U.place(x=320, y=280)

button_V = st.Button(master=window, text='V', font='Arial 16', bg='#b7ffeb', command=lambda button='V': print_user_quess(button))
button_V.place(x=360, y=280)

button_W = st.Button(master=window, text='W', font='Arial 16', bg='#b7ffeb', command=lambda button='W': print_user_quess(button))
button_W.place(x=395, y=280)

button_X = st.Button(master=window, text='X', font='Arial 16', bg='#b7ffeb', command=lambda button='X': print_user_quess(button))
button_X.place(x=440, y=280)

button_Y = st.Button(master=window, text='Y', font='Arial 16', bg='#b7ffeb', command=lambda button='Y': print_user_quess(button))
button_Y.place(x=480, y=280)

button_Z = st.Button(master=window, text='Z', font='Arial 16', bg='#b7ffeb', command=lambda button='Z': print_user_quess(button))
button_Z.place(x=520, y=280)

window.mainloop()
