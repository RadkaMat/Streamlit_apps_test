import streamlit as st
from functions import to_do_list_func as functions


def add_new_to_do_on_change():
    """ Handle the event of adding a new to-do via Streamlit widget. """
    new_to_do = st.session_state['new_to_do_widget']
    if functions.check_valid_input(new_to_do):
        updated_to_do_list = functions.add_new_to_do_logic(to_do_list, new_to_do)
        st.session_state['new_to_do'] = new_to_do
    st.session_state['new_to_do_widget'] = ''


st.page_link('home.py', label='Home', icon='🏠')
st.title('To-Do List 📝')

# Clean New to-do+ widget
if 'new_to_do' not in st.session_state:
    st.session_state.new_to_do = ''
to_do_list = functions.get_to_do_list()
checkbox_state = {to_do: False for to_do in to_do_list}

form = st.form('Checking form', clear_on_submit=True)

# Create a to-do list with a checkbox for every to-do
with form:
    for index, to_do in enumerate(to_do_list):
        checkbox_state[to_do] = st.checkbox(label=to_do, key=index)

    confirm = form.form_submit_button('Done')

    # Remove finished to-does from the to-do list when the form is submitted
    if confirm:
        to_do_list = [to_do for to_do, checked in checkbox_state.items() if not checked]
        functions.save_to_do_list(to_do_list, file_path=functions.FILE_PATHS['data'])

        to_do_list_done = [to_do for to_do, checked in checkbox_state.items() if checked]
        functions.save_to_do_list(to_do_list_done, file_path=functions.FILE_PATHS['history'], save_mode='a')
        st.rerun()

# New to-do+ widget
st.title('New to-do +')
st.text_input(label='Write new to-do:', value='', placeholder='Write new to-do... [for comfirmation press Enter key]',
              on_change=add_new_to_do_on_change, key='new_to_do_widget')

st.write(f'The last added to-do: {st.session_state.new_to_do}')

# Show the history of the finished to-does
if st.button('Show history 🕒'):
    history = functions.show_to_do_history()
    st.table(history)
