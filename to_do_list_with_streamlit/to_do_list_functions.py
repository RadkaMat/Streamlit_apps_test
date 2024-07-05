import streamlit as st

PATH = r'to_do_list_with_streamlit/to_do_list_result.txt'
PATH_HISTORY = r'to_do_list_with_streamlit/to_do_list_history.txt'


def get_to_do_list(pathx=PATH):
    """
        Function loads the to-do list.
        Returns to-do list.
    """
    with open(pathx, mode='r', encoding='UTF-8') as filex:
        to_do_listx = filex.readlines()
        if to_do_listx:
            if to_do_listx[0] == '\n':
                to_do_listx.remove('\n')
    return to_do_listx


def save_to_do_list(to_do_listx, pathx=PATH, save_mode='w'):
    """ This function saves the to-do list (save_mode 'w') or history (save_mode 'a'). """
    with open(pathx, mode=save_mode, encoding='UTF-8') as filex:
        filex.writelines(to_do_listx)
