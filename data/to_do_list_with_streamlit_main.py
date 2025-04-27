import streamlit as st
from st_files_connection import FilesConnection
from functions import to_do_list_functions as function
from datetime import datetime
from pandas import DataFrame, RangeIndex


def add_new_to_do_on_change():
    """ Function adds new to-do to to-do list. """
    # check if input is valid: is not only whitespaces
    add_new_to_do = st.session_state['new_to_do_widget'] + ' ' + str(datetime.now().strftime('%Y-%m-%d %H:%M')) + '\n'
    if function.check_valid_input(st.session_state['new_to_do_widget']):
        to_do_list.append(add_new_to_do)
        function.save_to_do_list(to_do_list)
    st.session_state.new_to_do = st.session_state.new_to_do_widget
    st.session_state.new_to_do_widget = ''


# Load To-do list and add False value for unfinished to-does.
to_do_list = function.get_to_do_list()
checkbox_state = {to_do: False for to_do in to_do_list}

# Page settings and background image
# st.set_page_config(layout='wide')
page_bg_image = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1722082839802-18b18cb23a62");
background-size: cover;

[data-testid="stMainBlockContainer"] {
background-color: #262626;
}
</style>
"""

# To-do list with unfinished tasks.
st.markdown(page_bg_image, unsafe_allow_html=True)
st.title('To-do list &#9989;')

form = st.form('Checking form', clear_on_submit=True)
with form:
    for index, to_do in enumerate(to_do_list):
        # Use the checkbox to display the to-does
        checkbox_state[to_do] = st.checkbox(label=to_do, key=index)

    confirm = form.form_submit_button('Done')

    # Remove checked to-does from the to-do list when the form is submitted
    if confirm:
        # Create a new To-do list of to-does excluding the checked ones
        to_do_list = [to_do for to_do, checked in checkbox_state.items() if not checked]
        function.save_to_do_list(to_do_list)

        # Create a new list of finished tasks for history logs
        to_do_list_done = [to_do for to_do, checked in checkbox_state.items() if checked]
        function.save_to_do_list(to_do_list_done, pathx=function.PATH_HISTORY, save_mode='a')
        st.rerun()

# Add new to-do.
st.title('New to-do +')
st.text_input(label='Write new to-do:', value='', placeholder='Write new to-do... [for comfirmation press Enter key]',
              on_change=add_new_to_do_on_change, key='new_to_do_widget')


# Clean new to-do widget.
if 'new_to_do' not in st.session_state:
    st.session_state.new_to_do = ''

# Button to add new to-do
if st.button('Add to-do +'):
    add_new_to_do_on_change
    st.rerun()

# Message to write the last added to-do
st.write(f'The last added to-do: {st.session_state.new_to_do}')

if st.button('Show history'):
    to_do_list_history = function.get_to_do_list(pathx=function.PATH_HISTORY)
    data_frame_history = DataFrame({'Name of To-do': to_do_list_history},
                                   index=RangeIndex(start=1, stop=len(to_do_list_history)+1))
    st.table(data_frame_history)

# Delete history of the finished to-does
if st.button('Delete history', type='primary'):
    clear_history = []
    function.save_to_do_list(clear_history, pathx=function.PATH_HISTORY)
    st.success('The history of your finished to-does was deleted.', icon="✅")

# check tha state of all variables
# st.session_state
