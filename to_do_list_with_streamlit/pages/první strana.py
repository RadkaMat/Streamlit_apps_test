import streamlit as st
import os

st.text(os.system('pwd'), os.system('ls'))
st.write('První strana')
