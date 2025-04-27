import streamlit as st

PATH = r'to_do_list_with_streamlit/to_do_list_data.txt'
PATH_HISTORY = r'to_do_list_with_streamlit/to_do_list_history.txt'


def get_to_do_list(pathx=PATH):
    """ Function loads and returns to-do list. """
    with open(pathx, mode='r', encoding='UTF-8') as filex:
        to_do_listx = filex.readlines()
        # delete empty first row, when there is no to-do
        if to_do_listx:
            if to_do_listx[0] == '\n':
                to_do_listx.remove('\n')
        # delete the second to-do when double input occurs
        if len(to_do_listx) > 1 and to_do_listx[-2] == to_do_listx[-1]:
            del to_do_listx[-1]
    return to_do_listx


def save_to_do_list(to_do_listx, pathx=PATH, save_mode='w'):
    """ This function saves the to-do list (save_mode 'w') or history (save_mode 'a'). """
    with open(pathx, mode=save_mode, encoding='UTF-8') as filex:
        filex.writelines(to_do_listx)


def check_valid_input(new_to_dox):
    """ This function checks if user input is valid. """
    # check whitespace, valid input cannot be only whitespaces
    if new_to_dox.isspace():
        return False
    else:
        return True
