from pirmas_atsiskaitymas.Classes.Skaitytojas import Skaitytojas
from pirmas_atsiskaitymas.Classes.Knyga import Knyga

def registruoti_skaitytoja(skaitytoju_sarasas, vardas, pavarde, kontaktai): #sukuria nauja objekta Skaitytojas, prideda ji i skaitytoju sarasa(kaip objekta) ir grazina
    naujas_skaitytojas = Skaitytojas(
        vardas=vardas,
        pavarde=pavarde,
        kontaktai=kontaktai
    )
    skaitytoju_sarasas.append(naujas_skaitytojas)
    return naujas_skaitytojas

def ieskoti_skaitytojo_pagal_kortele(skaitytoju_sarasas, korteles_numeris): #Ieskomas skaitytojas pagal korteles nr
    for skaitytojas in skaitytoju_sarasas:
        if skaitytojas.korteles_numeris == korteles_numeris:
            return skaitytojas
    return None

def prideti_knyga_skaitytojui(skaitytojas, knyga):
    if skaitytojas is None or knyga is None: # Tikrina ar skaitytojas ir knyga egzistuoja 
        return False
    if skaitytojas.veluojancios_knygos(): #Tikrina ar skaitytojas turi veluojanciu knygu
        return "veluoja"
    if not knyga.ar_yra_laisvu(): #Tikrina ar yra laisvu knygu
        return "nera_laisvu"
    skaitytojas.prideti_paimta_knyga(knyga.unikalus_id) # pridedame knyga skaitytojui
    knyga.paimtas_kiekis += 1 # Atnaujiname paimtos knygos kieki
    return True

def grazinti_knyga_skaitytojui(skaitytojas, knyga):
    if skaitytojas is None or knyga is None:
        return False
    pavyko = skaitytojas.knygos_grazinimas(knyga.unikalus_id)
    if pavyko:        # Atnaujina knygos paimtu kieki
        knyga.paimtas_kiekis -= 1
        return True
    return False

def ar_gali_paimti_knyga(skaitytojas):
    return not skaitytojas.veluojancios_knygos() #Kadangi metodas grazina tuscia sarasa, jeigu nera veluojancios knygos o tuscias sarasas yra False, tai not False = True, o not True = False

def veluojancios_knygos_skaitytojo(skaitytojas):
    return skaitytojas.veluojancios_knygos()

def gauti_visus_skaitytojus(skaitytoju_sarasas):
    return skaitytoju_sarasas

def vidutinis_veluojanciu_kiekis(skaitytoju_sarasas): 
    veluojancios = [len(s.veluojancios_knygos()) for s in skaitytoju_sarasas] #suskaiciuojame kiek veluojanciu knygu yra pas kiekviena vartotojui, ir sudedame i sarasa
    if not veluojancios:
        return 0
    return sum(veluojancios) / len(veluojancios) 