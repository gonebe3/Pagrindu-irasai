from pirmas_atsiskaitymas.Classes.Knyga import Knyga

# Prideti knyga i biblioteka  
def prideti_knyga(knygu_sarasas, pavadinimas, autorius, metai, zanras, turimas_kiekis): #Sukuria nauja Knyga objekta ir prideda i knygu sarasa(paduodamas, kaip argumentas) ir grazina

    nauja_knyga = Knyga(
        pavadinimas=pavadinimas,
        autorius=autorius,
        metai=metai,
        zanras=zanras,
        turimas_kiekis=turimas_kiekis,
        paimtas_kiekis=0
    )
    knygu_sarasas.append(nauja_knyga)
    return nauja_knyga

# Pasalinti knyga pagal ID
def pasalinti_knyga(knygu_sarasas, knygos_id): # Pasalina knyga pagal ID, jeigu pasalina grazina True, kitaip False
    for knyga in knygu_sarasas:
        if knyga.unikalus_id == knygos_id:
            knygu_sarasas.remove(knyga)
            return True
    return False

#pasalinti pasenusias knygas

def pasalinti_senas_knygas(knygu_sarasas, metai):
    """
    [:] duoda galimybe naudoti ta pati sarasa duomenu sukelimui(issaugo ram'uose)
    Veliau naudojame list comprehension naujo saraso sukurimui, pagal nurodytu metu atitikmeni
    graziname istrintu knygu kieki
    """
    knygu_kiekis_iki_salinimo = len(knygu_sarasas)
    knygu_sarasas[:] = [k for k in knygu_sarasas if k.metai >= metai] 
    return knygu_kiekis_iki_salinimo - len(knygu_sarasas)

def ieskoti_pagal_pavadinima(knygu_sarasas, pavadinimas): # grazina visus atitikmenis pagal pavadinima(arba jo dali), jeigu neranda, tuomet grazina tuscia sarasa
    return [k for k in knygu_sarasas if pavadinimas.lower() in k.pavadinimas.lower()]

def ieskoti_pagal_autoriu(knygu_sarasas, autorius):
    return [k for k in knygu_sarasas if autorius.lower() in k.autorius.lower()]

def ieskoti_pagal_zanra(knygu_sarasas, zanras):
    return [k for k in knygu_sarasas if zanras.lower() in k.zanras.lower()]

def gauti_visas_knygas(knygu_sarasas):
    return knygu_sarasas

from collections import Counter
from datetime import datetime

def populiariausi_zanrai(knygu_sarasas): #grazina zanru skaiciavima, kiekvieno zanro kieki atskirai (Suskaiciuoja su Counter)
    visi_zanrai = [k.zanras for k in knygu_sarasas]
    return Counter(visi_zanrai)

def populiariausi_zanrai_pagal_paeimus(skaitytojai, knygos):
    # Skaiciuoja populiariausius zanrus pagal visu skaitytoju paimtu knygu sarasus
    zanrai = []
    for skaitytojas in skaitytojai:
        for kn in skaitytojas.paimtos_knygos:
            for k in knygos:
                if k.unikalus_id == kn["Knygos_ID"]:
                    zanrai.append(k.zanras)
                    break
    return Counter(zanrai)

def gauti_visas_veluojancias_knygas(skaitytojai, knygos): #paduosime visu skaitytoju sarasa ir visu knygu sarasa
    # Surenka visas veluojancias knygas is visu skaitytoju
    veluojancios = []
    for skaitytojas in skaitytojai:
        for kn in skaitytojas.veluojancios_knygos():
            pavadinimas = "Nerasta"
            for k in knygos:  
                if k.unikalus_id == kn["Knygos_ID"]: # palyginame ar veluojancios knygos sutampa pagal Id su visomis bibliotekos knygomis
                    pavadinimas = k.pavadinimas
                    break
            veluoja_dienu = (datetime.now() - kn["Grazinti_iki"]).days
            veluojancios.append({
                "skaitytojas": f"{skaitytojas.vardas} {skaitytojas.pavarde}",
                "pavadinimas": pavadinimas,
                "grazinti_iki": kn["Grazinti_iki"].strftime('%Y-%m-%d'),
                "veluoja_dienu": veluoja_dienu
            })
    return veluojancios


def knygu_balansas(knygu_sarasas):
    balansas = []
    for k in knygu_sarasas:
        balansas.append({
            "Pavadinimas": k.pavadinimas,
            "Autorius": k.autorius,
            "Turimas_kiekis": k.turimas_kiekis,
            "Paimtas_kiekis": k.paimtas_kiekis,
            "ID": k.unikalus_id
        })
    return balansas


