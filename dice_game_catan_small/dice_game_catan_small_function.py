from random import randint

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

suroviny = [drevo, cihly, vlna, obili, kamen, zlato]


def prvni_hod_kostkami():
    hod_kostkamix = [suroviny[randint(0, 5)] for _ in range(6)]
    return hod_kostkamix


def druhy_a_treti_hod_kostkami(hod_kostkami, indexy_hodu_kostek):
    for index in indexy_hodu_kostek:
        hod_kostkami[int(index) - 1] = suroviny[randint(0, 5)]
    return hod_kostkami


def nakup(hod_kostkami):
    # 5 kostek, nákup Města = [obili, obili, kamen, kamen, kamen, zlato]
    if hod_kostkami.count(obili) >= 2 and hod_kostkami.count(kamen) >= 3:
        if vlna in hod_kostkami:
            return [['Město'], ['Rytíř']]
        else:
            return [['Město']]

    # 6 kostek, nákup Města za 2 zlata = [obili, obili, kamen, kamen, zlato, zlato]
    elif hod_kostkami.count(zlato) // 2 == 1 and (
            (hod_kostkami.count(obili) == 1 and hod_kostkami.count(kamen) == 3) or (
            hod_kostkami.count(obili) == 2 and hod_kostkami.count(kamen) == 2)):
        return [['Město'], ['Rytíř']]

    # 5 kostek, nákup Rytíře s Cestou = [obili, kamen, vlna, drevo, cihly, zlato]
    elif vlna in hod_kostkami and obili in hod_kostkami and kamen in hod_kostkami and drevo in hod_kostkami and \
            cihly in hod_kostkami:
        return [['Rytíř', 'Cesta'], ['Vesnice']]

    # 6 kostek, nákup Cesty a Rytíře za 2 zlata = [drevo, cihly, vlna, obili, zlato, zlato]
    elif drevo in hod_kostkami and cihly in hod_kostkami and hod_kostkami.count(zlato) // 2 == 1 and (
            (vlna in hod_kostkami and obili in hod_kostkami) or (obili in hod_kostkami and kamen in hod_kostkami) or
            (vlna in hod_kostkami and kamen in hod_kostkami)):
        return [['Rytíř', 'Cesta'], ['Vesnice']]

    # 6 kostek, nákup Rytíře a Cestu za 2 zlata = [vlna, obili, kamen, zlato, zlato, cihly]
    elif vlna in hod_kostkami and obili in hod_kostkami and kamen in hod_kostkami and hod_kostkami.count(
            zlato) // 2 == 1 and (drevo in hod_kostkami or cihly in hod_kostkami):
        return [['Rytíř', 'Cesta'], ['Vesnice']]

    # 6 kostek, nákup Vesnice s Cestou = [drevo, cihly, vlna, obili, cihly, drevo]
    elif drevo in hod_kostkami and cihly in hod_kostkami and vlna in hod_kostkami and obili in hod_kostkami:
        if hod_kostkami.count(drevo) == 2 and hod_kostkami.count(cihly) == 2:
            return [['Cesta', 'Cesta'], ['Vesnice', 'Cesta']]
        else:
            return [['Cesta'], ['Vesnice']]

    # 5 kostek, nákup Vesnice za 2 zlata = [drevo, cihly, vlna, zlato, zlato, vlna]
    elif hod_kostkami.count(zlato) // 2 == 1 and (
            (drevo in hod_kostkami and cihly in hod_kostkami and vlna in hod_kostkami) or (
            cihly in hod_kostkami and vlna in hod_kostkami and obili in hod_kostkami) or (
                    drevo in hod_kostkami and cihly in hod_kostkami and obili in hod_kostkami) or (
                    drevo in hod_kostkami and vlna in hod_kostkami and obili in hod_kostkami)):
        return [['Cesta'], ['Vesnice']]

    # 6 kostek, nákup Vesnice za 4 zlata = [zlato, zlato, zlato, zlato, drevo, cihly]
    elif hod_kostkami.count(zlato) // 2 == 2:
        if (drevo in hod_kostkami and vlna in hod_kostkami) or (drevo in hod_kostkami and obili in hod_kostkami) or \
           (cihly in hod_kostkami and vlna in hod_kostkami) or (cihly in hod_kostkami and obili in hod_kostkami) or \
           (vlna in hod_kostkami and obili in hod_kostkami):
            return [['Cesta'], ['Vesnice'], ['Rytíř']]
        elif drevo in hod_kostkami and cihly in hod_kostkami:
            return [['Cesta'], ['Vesnice']]
        elif hod_kostkami.count(drevo) == 2 or hod_kostkami.count(cihly) == 2:
            return [['Cesta', 'Cesta']]
        elif vlna in hod_kostkami or obili in hod_kostkami or kamen in hod_kostkami:
            return [['Cesta'], ['Rytíř']]

    # 3 kostky, nákup Rytíře = [vlna, obili, kamen, vlna, obili, kamen]
    elif vlna in hod_kostkami and obili in hod_kostkami and kamen in hod_kostkami:
        if hod_kostkami.count(vlna) == 2 and hod_kostkami.count(obili) == 2 and hod_kostkami.count(kamen) == 2:
            return[['Rytíř', 'Rytíř']]
        else:
            return [['Rytíř']]

    # 6 kostek, nákup 3 Cest, 2 Cest a Cesty = [drevo, drevo, drevo, cihly, cihly, cihly]
    elif drevo in hod_kostkami and cihly in hod_kostkami:
        if hod_kostkami.count(drevo) == 3 and hod_kostkami.count(cihly) == 3:
            return [['Cesta', 'Cesta', 'Cesta']]
        elif hod_kostkami.count(drevo) >= 2 and hod_kostkami.count(cihly) >= 2:
            return [['Cesta', 'Cesta']]
        else:
            return [['Cesta']]

    # 6 kostek, nákup Rytíře a Cesty za 2 zlata = [zlato, zlato, obili, cihly, vlna, obili]
    elif hod_kostkami.count(zlato) // 2 == 1:
        if (vlna in hod_kostkami and obili in hod_kostkami) or (obili in hod_kostkami and kamen in hod_kostkami) or (
                kamen in hod_kostkami and vlna in hod_kostkami) and (drevo in hod_kostkami or cihly in hod_kostkami):
            return [['Cesta'], ['Rytíř']]
        elif drevo in hod_kostkami or cihly in hod_kostkami:
            return [['Cesta']]

    # 6 kostek, nákup rytíře nebo 3 cest za 6 zlata = [zlato, zlato, zlato, zlato, zlato, zlato]
    elif hod_kostkami.count(zlato) == 6:
        return [['Cesta', 'Cesta'], ['Rytíř']]
    else:
        return [['nic']]


def kontrola_max_mnozstvi(inventar_hrac0, moznosti_nakupu_hrac0):
    maximalni_pocty = [('Cesta', 10), ('Cesta k městu', 6), ('Rytíř', 6), ('Vesnice', 6), ('Město', 4)]
    for maximum in maximalni_pocty:
        # když hráč už dosáhl u určité položka max. množství, položka bude odebrána
        if (maximum[1] - inventar_hrac0.count(maximum[0])) == 0:
            print(f"Dosáhl jsi maximálního množství pro nákup: {maximum[0]}. Další už si nemůžeš koupit.")
            if inventar_hrac0.count('Cesta') == 10 and inventar_hrac0.count('Cesta k městu') < 6:
                print('Máš maximální počet Cest. Můžeš si koupit jen Cestu k městu')
                for index, moznost in enumerate(moznosti_nakupu_hrac0):
                    pocet_cest = moznosti_nakupu_hrac0[index].count('Cesta')
                    do_max = 6 - inventar_hrac0.count('Cesta k městu')
                    nasobitel = pocet_cest if do_max > pocet_cest else do_max
                    if 'Cesta' in moznost:
                        moznosti_nakupu_hrac0[index] = ['Cesta k městu'] * nasobitel

            elif len(moznosti_nakupu_hrac0) and len(moznosti_nakupu_hrac0[0]) == 1:
                moznosti_nakupu_hrac0[0] = ['nic']
            else:
                for index in range(len(moznosti_nakupu_hrac0)):
                    if maximum[0] in moznosti_nakupu_hrac0[index]:
                        moznosti_nakupu_hrac0[index].remove(maximum[0])
                        moznosti_nakupu_hrac0[index].remove(maximum[0])
            print('Hotovo, je dosaženo maximum.')

        # když hráč dosáhne max. množství po nákupu 1x položky, zbytek bude odebrán
        elif (maximum[1] - inventar_hrac0.count(maximum[0])) == 1 and moznosti_nakupu_hrac0[0].count(maximum[0]) >= 2:
            if moznosti_nakupu_hrac0[0].count(maximum[0]) == 2:
                print(f"Dosáhl jsi maximálního množství pro nákup: {maximum[0]}. Můžeš si to koupit jen jednou.")
                moznosti_nakupu_hrac0[0].remove(maximum[0])
                print('Chybí už jen jeden.')

            elif moznosti_nakupu_hrac0[0].count(maximum[0]) == 3:
                print(f"Dosáhl jsi maximálního množství pro nákup: {maximum[0]}. Můžeš si to koupit jen dvakát.")
                moznosti_nakupu_hrac0[0].remove(maximum[0])
                moznosti_nakupu_hrac0[0].remove(maximum[0])
                print('Chybí už jen dva.')
            break

        # když hráč dosáhne max. množství po nákupu 2x položky, zbytek bude odebrán
        elif (maximum[1] - inventar_hrac0.count(maximum[0])) == 2 and moznosti_nakupu_hrac0[0].count(maximum[0]) == 3:
            print(f"Dosáhl jsi maximálního množství pro nákup: {maximum[0]}. Můžeš si to koupit jen dvakrát.")
            moznosti_nakupu_hrac0[0].remove(maximum[0])
            break
    return moznosti_nakupu_hrac0


def kontrola_pozadavku_nakupu(inventar_hrac0, moznosti_nakupu_hrac0):
    # x. vesnice: (počet cest za vesnici)
    nakup_vesnic = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
    # x. město: (počet cest, počet cest k městu, body za město)
    nakup_mest = {0: (1, 1), 1: (3, 2), 2: (6, 4), 3: (6, 6)}
    pocet_cest = inventar_hrac0.count('Cesta')
    pocet_cest_k_mestu = inventar_hrac0.count('Cesta k městu')

    if ['Město'] in moznosti_nakupu_hrac0:
        pocet_mest = inventar_hrac0.count('Město')
        # pokud hráč nemá dost cest na nákup dané vesnice
        if pocet_cest < nakup_mest[pocet_mest][0] or pocet_cest_k_mestu < nakup_mest[pocet_mest][1]:
            if len(moznosti_nakupu_hrac0) == 1:
                index_mesta = moznosti_nakupu_hrac0.index(['Město'])
                moznosti_nakupu_hrac0[index_mesta] = ['nic']
                print('Nemáš dost cest nebo cest k městu na nákup města.')
            else:
                moznosti_nakupu_hrac0.remove(['Město'])
                print('Nemáš dost cest nebo cest k městu na nákup města.')

    for moznost in moznosti_nakupu_hrac0:
        # pokud hráč nemá dost cest na nákup dané vesnice
        if 'Vesnice' in moznost:
            pocet_vesnic = inventar_hrac0.count('Vesnice')
            if pocet_cest < nakup_vesnic[pocet_vesnic]:
                moznost.remove('Vesnice')
                print('Nemáš dost cest na nákup vesnice.')

    return moznosti_nakupu_hrac0


def vice_moznosti_nakupu(moznosti_nakupu_hrac0):
    if len(tuple(moznosti_nakupu_hrac0)) > 1:
        if not all(moznosti_nakupu_hrac0):
            vyber_hrace0 = ['nic']
        else:
            print('Máš na výběr:')

            for index, moznost in enumerate(moznosti_nakupu_hrac0):
                print(f"{index + 1}. možnost je: {moznost}")

            moznost = int(input('Napiš číslo té možnosti, kterou chceš použít: '))
            vyber_hrace0 = moznosti_nakupu_hrac0[moznost - 1]
    else:
        vyber_hrace0 = moznosti_nakupu_hrac0[0]

    return vyber_hrace0


def druhy_cest(vyber_hrace0, inventar_hrac0):
    nakup_cest_k_mestu = {0: 1, 1: 3, 2: 6, 3: 6, 4: 6, 5: 6}
    if inventar_hrac0.count('Cesta') >= nakup_cest_k_mestu[inventar_hrac0.count('Cesta k městu')]:
        if vyber_hrace0.count('Cesta') > 1:
            pocet_cest = vyber_hrace0.count('Cesta')
            volba1 = input('Chceš postavit cesty k městu? (odpověz A/N) ')
            if volba1 == 'A':
                volba2 = int(input(f"Kolik chceš postavit cest k městu? max. {pocet_cest} "))
                for index in range(volba2):
                    vyber_hrace0[index] = 'Cesta k městu'

        elif vyber_hrace0.count('Cesta') == 1:
            volba3 = input('Chceš postavit cestu k městu? (odpověz A/N) ')
            if volba3 == 'A':
                for index, moznost in enumerate(vyber_hrace0):
                    if 'Cesta' in moznost:
                        vyber_hrace0[index] = 'Cesta k městu'
    else:
        print('Nemáš dost cest na nákup Cest k městu.')

    return vyber_hrace0


def pridani_do_inventare(vyber_moznosti_cest_hrac0, inventar_hrac0, inventar_rytiru_hrac1):
    pocet_rytirux = inventar_hrac0.count('Rytíř')
    if vyber_moznosti_cest_hrac0 != ['nic']:
        inventar_hrac0 += vyber_moznosti_cest_hrac0
        if 'Rytíř' in vyber_moznosti_cest_hrac0:
            inventar_rytiru_hrac1.append(pocet_rytirux)
        return inventar_hrac0


def druhy_rytiru(inventar_rytiru_hrac0, prvni_hod_hrac0):
    rytiri = {0: 'kamen', 1: 'obili', 2: 'vlna', 3: 'drevo', 4: 'cihly', 5: ('zlato', 'zlato')}
    if inventar_rytiru_hrac0:
        print('K dipozici máš rytíře, které/ho můžeš použít místo hozené kostky vždy 1:1.')
        for cislo_rytire in inventar_rytiru_hrac0:
            print(f"Číslo rytíře: {cislo_rytire} se surovinou: {rytiri[cislo_rytire]}")
        volba_rytire = input('Chceš použít rytíře? (odpověz A/N) ')
        if volba_rytire == 'A':
            volba_rytire2 = int(input('Napiš číslo rytíře/ů. (odpověz číslem rytíře 0 až 5) '))
            volba_kostky = int(input('Za jakou kostku chceš vyměnit rytíře? (odpověz číslem rytíře 1 až 6) '))
            inventar_rytiru_hrac0.remove(inventar_rytiru_hrac0[volba_rytire2])
            prvni_hod_hrac0[int(volba_kostky) - 1] = rytiri[volba_rytire2]
    return prvni_hod_hrac0
  
