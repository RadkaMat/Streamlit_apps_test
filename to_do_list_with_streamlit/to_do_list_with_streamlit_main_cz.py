import streamlit as st
import to_do_list_functions_cz as funkce
import os

os.system('touch vystup_prikazu.txt')
os.system('pwd > vystup_prikazu.txt')
os.system('ls >> vystup_prikazu.txt')
os.system('ls /mount/src/application_python/to_do_list_with_streamlit >> vystup_prikazu.txt')

with open('vystup_prikazu.txt', mode='r', encoding='UTF-8') as souborx:
        seznam_ukolux = souborx.readlines()
st.write(seznam_ukolux)


seznam_ukolu = funkce.ziskat_seznam_ukolu()
st.set_page_config(layout='wide')

'''
# seznam úkolů k splnění
st.title('Seznam úkolů &#9989;')

formular = st.form('Zašktávací pole', clear_on_submit=True)
with formular:
    for index, ukol in enumerate(seznam_ukolu):
        zaskrtavaci_policko = st.checkbox(ukol, key=ukol)
        if zaskrtavaci_policko:
            seznam_ukolu.pop(index)
            funkce.ulozit_seznam_ukolu(seznam_ukolu)
            st.experimental_rerun()
    potvzeni = formular.form_submit_button('Hotovo')


# tlačítko přo přidání nového úkolu verze B
st.title('Nový úkol +')
st.text_input(label='', placeholder='Zadej nový úkol... [pro potvrzení stiskněte tlačítko Enter]',
              on_change=funkce.pridat_ukol, key='Nový úkol')'''
