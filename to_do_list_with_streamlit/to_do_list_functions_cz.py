import streamlit as st
from datetime import datetime

CESTA = r'to_do_list_with_streamlit/to_do_list_result_cz.txt'


def ziskat_seznam_ukolu(cestax=CESTA):
    """
        Funkce načte obsah souboru na parametru funkce cesta.
        Navrací obsah souboru.
    """
    with open(cestax, mode='r', encoding='UTF-8') as souborx:
        seznam_ukolux = souborx.readlines()
    return seznam_ukolux


def ulozit_seznam_ukolu(seznam_ukolux, cestax=CESTA):
    """ Funkce uloží proměnnou do souboru 'seznam_ukolu.txt'. """
    with open(cestax, mode='w', encoding='UTF-8') as souborx:
        souborx.writelines(seznam_ukolux)


def pridat_ukol(seznam_ukolux):
    """ Funkce přidá nový úkol do seznamu. """
    pridat = st.session_state['Novy_ukol'] + ' ' + str(datetime.now())[:10] + '\n'
    seznam_ukolux.append(pridat)
    ulozit_seznam_ukolu(seznam_ukolux)
    
