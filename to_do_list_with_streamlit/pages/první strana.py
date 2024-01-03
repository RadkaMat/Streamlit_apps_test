import streamlit as st
import os

st.text(os.system('pwd'))
st.text(os.system('ls'))
st.write('První strana')
