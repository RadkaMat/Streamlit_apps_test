CESTA = 'to_do_list_result_cz.txt'


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
