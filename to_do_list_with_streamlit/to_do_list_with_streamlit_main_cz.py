import streamlit as st
import to_do_list_functions_cz as funkce
from datetime import datetime


def pridat_ukol_on_change():
    """ Funkce přidá nový úkol do seznamu. """
    pridat = st.session_state['okno_novy_ukol'] + ' ' + str(datetime.now())[:10] + '\n'
    seznam_ukolu.append(pridat)
    funkce.ulozit_seznam_ukolu(seznam_ukolu)
    st.session_state.novy_ukol = st.session_state.okno_novy_ukol
    st.session_state.okno_novy_ukol = ''


seznam_ukolu = funkce.ziskat_seznam_ukolu()
st.set_page_config(layout='wide')


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


# přidání nového úkolu verze B
st.title('Nový úkol +')
st.text_input(label='Zadej nový úkol:', value='', placeholder='Zadej nový úkol... [pro potvrzení stiskněte tlačítko Enter]',
              on_change=pridat_ukol_on_change, key='okno_novy_ukol')


# vyčištění okna pro přidání nového úkolu
if 'novy_ukol' not in st.session_state:
    st.session_state.novy_ukol= ''

st.write(f'Poslední přidaný úkol: {st.session_state.novy_ukol}')


# kontrola: zobrazí všechny prvky streamlit aplikace
# st.session_state
