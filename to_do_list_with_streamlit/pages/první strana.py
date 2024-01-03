import streamlit as st
import os

os.system('touch vystup_prikazu.txt')
os.system('pwd > vystup_prikazu.txt')
os.system('ls >> vystup_prikazu.txt')

with open(cestax, mode='r', encoding='UTF-8') as souborx:
        seznam_ukolux = souborx.readlines()
st.write(seznam_ukolux)

st.write('První strana')
