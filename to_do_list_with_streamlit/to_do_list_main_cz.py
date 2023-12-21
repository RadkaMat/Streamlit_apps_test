import streamlit as st
import to_do_list_functions_cz as funkce

seznam_ukolu = funkce.ziskat_seznam_ukolu()

st.set_page_config(layout='wide')


def pridat_ukol():
    pridat = st.session_state['Nový úkol'] + '\n'
    seznam_ukolu.append(pridat)
    funkce.ulozit_seznam_ukolu(seznam_ukolu)


st.title('Moje aplikace')
st.subheader('Můj seznam úkolů')
st.write('Úkoly:')

for index, ukol in enumerate(seznam_ukolu):
    zaskrtavaci_policko = st.checkbox(ukol, key=ukol)
    if zaskrtavaci_policko:
        seznam_ukolu.pop(index)
        funkce.ulozit_seznam_ukolu(seznam_ukolu)
        del st.session_state[ukol]
        st.experimental_rerun()

st.text_input(label='', placeholder='Zadej nový úkol...',
              on_change=pridat_ukol, key='Nový úkol')
