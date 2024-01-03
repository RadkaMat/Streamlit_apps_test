import streamlit as st
import os

os.system('touch vystup_prikazu.txt')
os.system('pwd > vystup_prikazu.txt')
os.system('ls >> vystup_prikazu.txt')
st.write('První strana')
