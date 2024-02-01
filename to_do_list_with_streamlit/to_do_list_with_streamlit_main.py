import streamlit as st
import to_do_list_functions as function
from datetime import datetime


def add_new_to_do_on_change():
    """ Function adds new to-do to to-do list. """
    add_new_to_do = st.session_state['new_to_do_widget'] + ' ' + str(datetime.now())[:10] + '\n'
    to_do_list.append(add_new_to_do)
    function.save_to_do_list(to_do_list)
    st.session_state.new_to_do = st.session_state.new_to_do_widget
    st.session_state.new_to_do_widget = ''


to_do_list = function.get_to_do_list()
st.set_page_config(layout='wide')


# To-do list with unfinished tasks
st.title('To-do list &#9989;')

form = st.form('Checking form', clear_on_submit=True)
with form:
    for index, to_do in enumerate(to_do_list):
        checking_box = st.checkbox(to_do, key=to_do)
        if checking_box:
            to_do_list.pop(index)
            functions.save_to_do_list(to_do_list)
            st.experimental_rerun()
    confirm = form.form_submit_button('Done')


# add new to-do
st.title('New to-do +')
st.text_input(label='Write new to-do:', value='', placeholder='Write new to-do... [for comfirmation press Enter key]',
              on_change=add_new_to_do_on_change, key='new_to_do_widget')


# clean new to-do widget
if 'new_to_do' not in st.session_state:
    st.session_state.new_to_do= ''

st.write(f'The last added to-do: {st.session_state.new_to_do}')


# check tha state of all variables
# st.session_state
