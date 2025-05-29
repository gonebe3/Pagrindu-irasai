# _______________________________________________________________________________________

# Sukurti minibiudžeto programą, kuri:
# •Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
# •Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
# •Atvaizduotų jau įvestas pajamas ir išlaidas
# •Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)

# import pickle

# def vart_ivesties_iskvietimas():
#     while True:
#         try:
#             a = input("Iveskite pajamas arba islaidas: ")
#             skaicius = float(a)
#             return skaicius
#         except Exception:
#             print("Ivedete ne skaicius, bandykite dar karta")


# def ivesties_saugojimas(skaicius):
#     try:
#         with open ("biudzeto_saugykla.pickle", "rb") as failas:
#             duomenys = pickle.load(failas)
#     except FileNotFoundError:
#         duomenys = []

#     duomenys.append(skaicius)

#     with open("biudzeto_saugykla.pickle", "wb") as failas:
#         pickle.dump(duomenys, failas)

# def atvaizduoti_visus():
#     try:
#         with open("biudzeto_saugykla.pickle", "rb") as failas:
#             visi_irasai = pickle.load(failas)
#             for kintamasis,i in enumerate(visi_irasai):
#                 if i < 0:
#                     print(f"{kintamasis+1}. Išlaidos: {i}")
#                 else:
#                     print(f"{kintamasis+1}. Pajamos: {i}")

#     except FileNotFoundError:
#         print("Faile dar nera duomenu, turite is pradziu ivesti duomenys")

  

# def balansas():
#     try:
#         with open ("biudzeto_saugykla.pickle", "rb") as failas:
#             duomenys = pickle.load(failas)
#         dabartinis_balansas = sum(duomenys)
#         print(f"Bendras balansas: {dabartinis_balansas}")
#     except FileNotFoundError:
#         print("Faile dar nera duomenu, turite is pradziu ivesti duomenys")

    


# def biudzeto_meniu():

#     while True:
#         funkcija = input("""1 -Ivesti pajamas ar islaidas  
# 2 -Rodyti visus irasus  
# 3 -Rodyti balansa  
# 4 -Iseiti
# Iveskite funkcijos numerį, kuria norite atlikti: """)
#         try:
#             if funkcija == "1":
#                 skaicius = vart_ivesties_iskvietimas()
#                 ivesties_saugojimas(skaicius)
#             if funkcija == "2":
#                 atvaizduoti_visus()
#             if funkcija == "3":
#                 balansas()
#             if funkcija == "4":
#                 break
#         except Exception:
#             print("Ivyko nenumatyta klaida, bandykite dar karta")
            

# biudzeto_meniu()


# _________________________________________________________________________________________


# inventory: sąrašas žodynų, kur kiekvienas žodynas turi laukus:
# id (unikalus sveikasis skaičius)
# pavadinimas (eilutė)
# kiekis (sveikasis skaičius)
# kaina (slankusis skaičius)
# Pagrindinis meniu (while True)
# Pridėti prekę
# Atnaujinti prekę
# Pašalinti prekę
# Rodyti visas prekes
# Įrašyti į „pickle“ failą
# Užkrauti iš „pickle“ failo
# Išeiti
# Funkcijos
# load_pickle(filepath) → list[dict]
# save_pickle(data, filepath) → None
# add_product(data) → None
# update_product(data, product_id) → None
# remove_product(data, product_id) → None
# display_inventory(data) → None



# import pickle

# def inventoriaus_nuskaitymas(kelias):
#     try:
#         with open(kelias, "rb") as failas:
#             duomenys = pickle.load(failas)
#         return duomenys
#     except FileNotFoundError:
#         return []

# def inventoriaus_saugojimas(informacija, kelias):
#     with open (kelias, "wb") as failas:
#         pickle.dump(informacija, failas)

# def inventoriaus_pridejimas(sarasas):
#     if sarasas == []:
#         naujas_id = 1
#     else:
#         didziausiais_id = 0
#         for i in sarasas:
#             id_reiksme = i["id"]
#             if id_reiksme > didziausiais_id:
#                 didziausiais_id = i["id"]
#         naujas_id = didziausiais_id + 1

#     pavadinimas = input("Iveskite produkto pavadinimą: ")

#     while True:
#         try:
#             kiekis = int(input("Iveskite produkto kieki: "))
#             break
#         except ValueError:
#             print("Neteisingas formatas, skaicius turi buti sveikas, bandykite dar karta.")

#     while True:
#         try:
#             kaina = float(input("Iveskite prekes kaina: "))
#             break
#         except ValueError:
#             print("Ivedete neteisinga kainos formata, bandykite dar karta.")
        
#     nauja_preke = {"id": naujas_id, "pavadinimas": pavadinimas, "kiekis": kiekis, "kaina": kaina}
#     sarasas.append(nauja_preke)

#     print(f"Preke {pavadinimas} prideta i inventorija su ID numeriu: {naujas_id}")

# def inventoriaus_atvaizdavimas(sarasas):
#     if sarasas == []:
#         print("Inventorius kol kas tuscias")
#     else:
#         for i in sarasas:
#             id = i["id"]
#             pavadinimas = i["pavadinimas"]
#             kiekis = i["kiekis"]
#             kaina = i["kaina"]
#             print("-" * 50)
#             print(f"ID: {id} | Pavadinimas: {pavadinimas} | Kiekis = {kiekis} | Kaina = {kaina:.2f} €")
#             print("-" * 50)

# def pasalinti_preke(sarasas):
#     try:
#         ivestas_id = int(input("Iveskite prekes ID, kuria norite pasalinti: "))
#     except ValueError:
#         print("Neteisingas, formatas, ID turi buti sveikas skaicius")
#         return
#     radau = False
#     for i in sarasas:
#         if i["id"] == ivestas_id:
#             sarasas.remove(i)
#             print(f"Preke {i['id']} buvo pasalinta sekmingai")
#             radau = True
#             break
#     if not radau:
#         print("Prekes su tokiu ID nera.")

# def prekes_redagavimas(sarasas):
#     try:
#         ivestas_id = int(input("Iveskite prekes ID, kuria norite redaguoti: "))
#     except ValueError:
#         print("Neteisingas, formatas, ID turi buti sveikas skaicius")
#         return
    
#     radau = False
#     for i in sarasas:
#         if i["id"] == ivestas_id:
#             redaguojama_preke = i
#             radau = True
#             break
#     if not radau:
#         print("Prekes su tokiu ID nera.")

#     veiksmas = input("Pasirinkite, ka redaguosime (pavadinimas / kiekis / kaina):")

#     if veiksmas == "kiekis":
#         try:
#             naujas_kiekis = int(input("Iveskite nauja kieki: "))
#         except ValueError:
#             print("'Kiekis' privalo buti sveikas skaicius")
#             return
#         redaguojama_preke["kiekis"] = naujas_kiekis
#         print(f"Preke su ID {ivestas_id} kiekis atnaujintas i {naujas_kiekis}")
#     elif veiksmas == "kaina":
#         try:
#             nauja_kaina = float(input("Iveskite nauja kaina: "))
#         except ValueError:
#             print("Neteisingai ivesta kaina, bandykite dar karta")
#             return
#         redaguojama_preke["kaina"] = nauja_kaina
#         print(f"Preke su ID {ivestas_id} kaina atnaujinta i {nauja_kaina}")
#     elif veiksmas == "pavadinimas":
#         naujas_pavadinimas = input("Iveskite nauja pavadinima: ")
#         redaguojama_preke["pavadinimas"] = naujas_pavadinimas
#         print(f"Preke su ID {ivestas_id} pavadinimas atnaujintas i {naujas_pavadinimas}")
#     else:
#         print("Tokio lauko redaguoti negalima, arba ivedete neteisingai.")

# def valdymo_meniu():
#     kelias = "inventorius.pickle"
#     sarasas = inventoriaus_nuskaitymas(kelias)

#     while True:
#         print(""" 
# --- INVENTORIAUS VALDYMAS ---
# ______________________________________
# 1 - Prideti produkta prie inventoriaus
# ______________________________________
# 2 - Redaguoti produkta
# ______________________________________
# 3 - Pasalinti preke pagal ID
# ______________________________________
# 4 - Rodyti visas prekes
# ______________________________________
# 5 - Irasyti i ,,Pickle" faila
# ______________________________________
# 6 - Uzkrauti is pickle failo
# ______________________________________
# 7 - Iseiti""")
        
#         print("-"*50)
        
#         try:
#             pasirinkimas = int(input("Pasirinkite veiksma (1-7): "))
#         except ValueError:
#             print("Ivedete neteisingai, bandykite dar karta")
#             continue

#         if pasirinkimas == 1:
#             inventoriaus_pridejimas(sarasas)
#         elif pasirinkimas == 2:
#             prekes_redagavimas(sarasas)
#         elif pasirinkimas == 3:
#             pasalinti_preke(sarasas)
#         elif pasirinkimas == 4:
#             inventoriaus_atvaizdavimas(sarasas)
#         elif pasirinkimas == 5:
#             inventoriaus_saugojimas(sarasas, kelias)
#             print("Inventorius irasytas i faila")
#         elif pasirinkimas == 6:
#             sarasas = inventoriaus_nuskaitymas(kelias)
#             print("Inventorius uzkrautas is failo")
#         elif pasirinkimas == 7:
#             print("Programa uzsidaro")
#             break
#         else:
#             print("neteisingas pasirinkimas, bandykite dar karta.")

# valdymo_meniu()


















