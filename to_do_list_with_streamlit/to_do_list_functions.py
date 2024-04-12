import streamlit as st

PATH = r'Streamlit_apps/to_do_list_with_streamlit/to_do_list_result.txt'


def get_to_do_list(pathx=PATH):
    """
        Function loads the to-do list from streamlit linux cloud server.
        Returns to-do list.
    """
    with open(pathx, mode='r', encoding='UTF-8') as filex:
        to_do_listx = filex.readlines()
        if to_do_listx:
            if to_do_listx[0] == '\n':
                to_do_listx.remove('\n')
    return to_do_listx


def save_to_do_list(to_do_listx, pathx=PATH):
    """ Function saves the to-do list to streamlit linux cloud server. """
    with open(pathx, mode='w', encoding='UTF-8') as filex:
        filex.writelines(to_do_listx)
