# hra maly osadnici
import catan_dice_game_word_version_functions as fo

# seznam surovin
drevo = '\U0001fab5'
cihly = '\U0001f9f1'
vlna = '\U0001F411'
obili = '\U0001F33E'
kamen = '\U0001faa8'
zlato = '\U0001fa99'

# pokud se špatně zobrazují emoji
# drevo = 'drevo'
# cihly = 'cihly'
# vlna = 'vlna'
# obili = 'obili'
# kamen = 'kamen'
# zlato = 'zlato'

suroviny = ['', drevo, cihly, vlna, obili, kamen, zlato]

# vysvětlivka pro hráče
nakupy = {'Cesta': [drevo + cihly],
          'Vesnice': [drevo + cihly + vlna + obili],
          'Město': [obili + obili + kamen + kamen + kamen],
          'Rytíř': [vlna + obili + kamen]}

print('Náklady:')
for nakup in nakupy:
    print(nakup, ': ', nakupy[nakup])

herni_kolo = 1
inventar_hrac1 = []
inventar_rytiru_hrac1 = []

# smyčka herních kol
while herni_kolo < 15:
    print('-' * 44)
    print('Herní kolo:', herni_kolo)
    print('-' * 44)
    print('Inventář hráče 1:', inventar_hrac1)
    maximalni_pocty = [('Cesta', 10), ('Cesta k městu', 6), ('Rytíř', 6), ('Vesnice', 6), ('Město', 4)]
    for maximum in maximalni_pocty:
        print(maximum[0], inventar_hrac1.count(maximum[0]), '/', maximum[1])

    # 1. hod
    prvni_hod_hrac1 = fo.prvni_hod_kostkami()
    moznosti_nakupu_hrac1 = fo.nakup(prvni_hod_hrac1)

    print('-' * 44)
    print('Hráč 1 hodil kostkami:')
    for index, hod in enumerate(prvni_hod_hrac1):
        print(f"Kostka {index + 1}: {hod}")
    print('-' * 44)
    print('Po 1. hodu si můžeš koupit: (před kontrolou)', moznosti_nakupu_hrac1)
    fo.druhy_rytiru(inventar_rytiru_hrac1, prvni_hod_hrac1)
    print('po použití rytíře:', prvni_hod_hrac1)

    # kontrola maximálního množství a odebraní přebytku z možností nákupu hráče
    fo.kontrola_max_mnozstvi(inventar_hrac1, moznosti_nakupu_hrac1)

    # možnosti hráče s max limity a požavky nákupu
    moznosti_nakupu_pozadavky_hrac1 = fo.kontrola_pozadavku_nakupu(inventar_hrac1, moznosti_nakupu_hrac1)
    # více možnosti nákupu omezit na jednu, pokud jde o cestu, zda hráč ji chce k městu
    vyber_hrace1 = fo.vice_moznosti_nakupu(moznosti_nakupu_pozadavky_hrac1)
    vyber_cest_hrac1 = fo.druhy_cest(vyber_hrace1, inventar_hrac1)

    # přidání do inventáře
    fo.pridani_do_inventare(vyber_cest_hrac1, inventar_hrac1, inventar_rytiru_hrac1)
    print('Do inventáře můžeš získat:', vyber_cest_hrac1)

    # 2. hod
    otazka1 = input('Chceš použít 2. hod kostkami? (odpověz A/N) ')

    if otazka1 == 'N':
        # přidání do inventáře
        fo.pridani_do_inventare(vyber_cest_hrac1, inventar_hrac1, inventar_rytiru_hrac1)
        print('Do inventáře můžeš získat:', vyber_cest_hrac1)

    elif otazka1 == 'A':
        otazka2 = list(input('Kterými kostkami chceš znovu hodit?\n(odpověz číslami kostek 1 až 6 bez mezer př. 123) '))
        druhy_hod_hrac1 = fo.druhy_a_treti_hod_kostkami(prvni_hod_hrac1, otazka2)

        print('-' * 44)
        print('Hráč 1 hodil kostkami:')
        for index, hod in enumerate(druhy_hod_hrac1):
            print(f"Kostka {index + 1}: {hod}")
        print('-' * 44)
        print('Po 1. hodu si můžeš koupit: (před kontrolou)', moznosti_nakupu_hrac1)
        fo.druhy_rytiru(inventar_rytiru_hrac1, druhy_hod_hrac1)
        print('po použití rytíře:', druhy_hod_hrac1)

        # kontrola maximálního množství a odebraní přebytku z možností nákupu hráče
        fo.kontrola_max_mnozstvi(inventar_hrac1, moznosti_nakupu_hrac1)

        # možnosti hráče s max limity a požavky nákupu
        moznosti_nakupu_pozadavky_hrac1 = fo.kontrola_pozadavku_nakupu(inventar_hrac1, moznosti_nakupu_hrac1)
        # více možnosti nákupu omezit na jednu, pokud jde o cestu, zda hráč ji chce k městu
        vyber_hrace1 = fo.vice_moznosti_nakupu(moznosti_nakupu_pozadavky_hrac1)
        vyber_cest_hrac1 = fo.druhy_cest(vyber_hrace1, inventar_hrac1)

        # 3. hod
        otazka3 = input('Chceš použít 3. hod kostkami? (odpověz A/N) ')

        if otazka3 == 'N':
            # přidání do inventáře
            fo.pridani_do_inventare(vyber_cest_hrac1, inventar_hrac1, inventar_rytiru_hrac1)
            print('Do inventáře můžeš získat:', vyber_cest_hrac1)

        elif otazka3 == 'A':
            otazka4 = list(input('Kterými kostkami chceš znovu hodit?\
                                (odpověz číslami kostek 1 až 6 bez mezer př. 123) '))
            treti_hod_hrac1 = fo.druhy_a_treti_hod_kostkami(druhy_hod_hrac1, otazka4)

            print('-' * 44)
            print('Hráč 1 hodil kostkami:')
            for index, hod in enumerate(treti_hod_hrac1):
                print(f"Kostka {index + 1}: {hod}")
            print('-' * 44)
            print('Po 1. hodu si můžeš koupit: (před kontrolou)', moznosti_nakupu_hrac1)
            fo.druhy_rytiru(inventar_rytiru_hrac1, treti_hod_hrac1)
            print('po použití rytíře:', treti_hod_hrac1)

            # kontrola maximálního množství a odebraní přebytku z možností nákupu hráče
            fo.kontrola_max_mnozstvi(inventar_hrac1, moznosti_nakupu_hrac1)

            # možnosti hráče s max limity a požavky nákupu
            moznosti_nakupu_pozadavky_hrac1 = fo.kontrola_pozadavku_nakupu(inventar_hrac1, moznosti_nakupu_hrac1)
            # více možnosti nákupu omezit na jednu, pokud jde o cestu, zda hráč ji chce k městu
            vyber_hrace1 = fo.vice_moznosti_nakupu(moznosti_nakupu_pozadavky_hrac1)
            vyber_cest_hrac1 = fo.druhy_cest(vyber_hrace1, inventar_hrac1)

            # přidání do inventáře
            fo.pridani_do_inventare(vyber_cest_hrac1, inventar_hrac1, inventar_rytiru_hrac1)
            print('Do inventáře můžeš získat:', vyber_cest_hrac1)

        else:
            print('Napiš čísla kostek která chceš znovu hodit 1 až 6 bez mezer př. 123')

    else:
        print('Vyber si "A" pro ano a "N" pro ne.')

    print('Konec kola')
    herni_kolo += 1

print('Konec hry')

# (x, x, x) body za rytire, vesnici a mesto)
bodovani = {0: (0, 0, 0), 1: (1, 3, 7), 2: (2, 4, 12), 3: (3, 5, 20), 4: (4, 7, 30), 5: (5, 9), 6: (6, 11)}

pocet_cest = inventar_hrac1.count('Cesta')
pocet_cest_k_mestu = inventar_hrac1.count('Cesta k městu')
pocet_rytiru = inventar_hrac1.count('Rytíř')
pocet_vesnic = inventar_hrac1.count('Vesnice')
pocet_mest = inventar_hrac1.count('Město')

body_celkem = pocet_cest + pocet_cest_k_mestu +\
              bodovani[pocet_rytiru][0] + bodovani[pocet_vesnic][1] + bodovani[pocet_mest][2]

print(f"Dosáhl jsi celkem: {body_celkem} bodů.")
