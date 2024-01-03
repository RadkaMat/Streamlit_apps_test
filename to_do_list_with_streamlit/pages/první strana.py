import streamlit as st
import os

st.text(os.system('touch vystup_prikazu.txt'))
st.text(os.system('pwd > vystup_prikazu.txt'))
st.text(os.system('ls >> vystup_prikazu.txt'))
st.write('První strana')
