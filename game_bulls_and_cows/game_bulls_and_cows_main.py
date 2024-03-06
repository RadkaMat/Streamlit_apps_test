import streamlist as st
from random import randint


def create_sacret_number():
  ''' Create sacred number like 1342. '''
	while True:
		sacred_word = str(randint(1000, 9999))
		if len(set(sacred_word)) == 4:
			break
	return sacred_word


def check_bulls_and_cows():
	''' Checking number of bulls and cows in the player's tip. '''
	bulls = []
	cows = []
	bulls_emoji = '🐂'
	cows_emoji = '🐄'

	for index, digit in enumerate(tip):
		if digit in sacred_word and sacred_word[index] == tip[index]:
			bulls.append(digit)
		if digit in sacred_word and sacred_word[index] != tip[index]:
			cows.append(digit)

	if len(bulls) == 1:
		bulls_count = 'bull'
	else:
		bulls_count = 'bulls'
	if len(cows) == 1:
		cows_count = 'cow'
	else:
		cows_count = 'cows'

	return f"{len(bulls)} {bulls_count} {bulls_emoji*len(bulls)}, {len(cows)} {cows_count} {cows_emoji*len(cows)}"


def check_players_tip(tip, attampts_count):
	''' Checking if player's tip follows game rules. '''
	if not tip.isnumeric():
		return 'Write only numbers.'
	elif tip[0] == '0':
		return 'Digit 0 must not be on 1. position.'
	elif len(tip) != 4:
		return 'Your number must have 4 digits.'
	elif len(set(tip)) != 4:
		return 'Your number must not contain duplicite digit.'
	else:
		return check_bulls_and_cows()


def game():
  ''' Main function, runs the game. '''
	global sacred_word
	sacred_word = create_sacret_number()
	st.write('-' * 49)
	st.write(text)
	st.write(game_rules)
	attampts_count = 0

    
  # player repeats his attampts since guess the correct number
	while True:
		st.write('-' * 49)
		global tip
		tip = input()
    st.input_box(label='Guess my 4-digit numer:', placeholder='Guess my 4-digit numer: [for comfirmation press Enter key]', on_change=game, key='tip_widget')
		st.write(check_players_tip(tip, attampts_count))
		attampts_count += 1
		if tip == sacred_word:
			st.write(f"Congratulation! You won on {attampts_count}. attempt!")
			break


text = f"{'':🐂^8}  Welcome to number-guessing game!  {'':🐄^8}"
game_rules = '''
Game Rules, I am thinking a number that
1. have 4 different digits
2. doesn't start with digit 0 '''


game()
