from Classes.Bibliotekininkas import Bibliotekininkas

def registruoti_bibliotekininka(bibliotekininku_sarasas, vardas, pavarde, vartotojo_vardas, slaptazodis):
    naujas = Bibliotekininkas(vardas, pavarde, vartotojo_vardas, slaptazodis)
    bibliotekininku_sarasas.append(naujas)
    return naujas

def ieskoti_pagal_vartotojo_varda(bibliotekininku_sarasas, vartotojo_vardas): # grazina bibliotekininka pagal vartotojo varda, arba None jeigu nerastas
    for i in bibliotekininku_sarasas:
        if i.vartotojo_vardas == vartotojo_vardas:
            return i
    return None

def autentifikuoti_bibliotekininka(bibliotekininku_sarasas, vartotojo_vardas, slaptazodis): # tikrina ar atitinka pirisijungimai, jeigu ok, tuomet grazina visa objekta, jei ne None
    for b in bibliotekininku_sarasas:
        if b.vartotojo_vardas == vartotojo_vardas and b.slaptazodis == slaptazodis:
            return b
    return None

def gauti_visus_bibliotekininkus(bibliotekininku_sarasas):
    return bibliotekininku_sarasas

