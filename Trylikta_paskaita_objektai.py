# class Dog(): # Klase - kaip sablonas
#     def __init__(self, spalva): # Konstruktorius (__init__)
#         self.legs = 4 # legs - savybe
#         self.color = spalva
 
#     def bark(self, sound):
#         print(f"{self.color} dog says AU AU {sound}")
 
 
# reksas = Dog("Brown") # is esmes tarsi kviecaiams __init__
 
# print(reksas.legs, reksas.color)
 
# reksas.bark("GRRR")
 
# rikis = Dog("Black") # is esmes tarsi kviecaiams __init__
 
# print(rikis.legs, rikis.color)
# rikis.bark(" umm umm")
 
# suo = Dog() # sukuriamas objektas (inicilizuojamas objektas) kaip konkretus individas
 
# print(suo.legs)


# class Human():
#     def __init__(self, ugis, weight, name, last_name):
#         self.arms = 2
#         self.legs = 2
#         self.head = 1
#         self.height = ugis
#         self.weight = weight
#         self.name = name
#         self.last_name = last_name
 
#     def bmi(self):
#         return self.weight / (self.height / 100) ** 2
   
#     def __str__(self): # kai meginam spausdinti automatiskai yra ieskoma str metodo
#         return f"{self.name} {self.last_name} kurio ugis yra {self.height} ir svoris yra {self.weight}"
 
# zmogus = Human(190,80, "Jonas", "Jonaitis")
# # print(zmogus.bmi())
 
# # zmogus2 = Human(int(input("Iveskite savo ugi (CM)")), int(input("Iveskite savo svori (kg)")))
# # print(f"Jusu KMI yra: {zmogus2.bmi()}")
 
# print(zmogus)
 
# zmogus2 = Human(170,65, "Mantas", "Mantaitis")
# print(zmogus2)
 
# print("Programa baigta")
 
# class Human():
#     def __init__(self, ugis, weight, name, last_name):
#         self.arms = 2
#         self.legs = 2
#         self.head = 1
#         self.height = ugis
#         self.weight = weight
#         self.name = name
#         self.last_name = last_name
 
#     def bmi(self):
#         return self.weight / (self.height / 100) ** 2
   
#     def __str__(self): # kai meginam spausdinti automatiskai yra ieskoma str metodo
#         return f"{self.name} {self.last_name} kurio ugis yra {self.height} ir svoris yra {self.weight}"
 
# zmogus = Human(190,80, "Jonas", "Jonaitis")
# # print(zmogus.bmi())
 
# # zmogus2 = Human(int(input("Iveskite savo ugi (CM)")), int(input("Iveskite savo svori (kg)")))
# # print(f"Jusu KMI yra: {zmogus2.bmi()}")
 
# # print(zmogus)
 
# zmogus2 = Human(170,65, "Mantas", "Mantaitis")
# # print(zmogus2)
 
 
# zmones = [zmogus2]
# zmones.append(zmogus)
 
# for zm in zmones:
#     print(zm)
#     print(zm.bmi())
 
 
# Sukurit prekės objektą, pagal praeitą uždavinį (tokia pat struktūra) ir sukurti 5 prekes su naudotojo įvestimi. ID galite nurodyti bet kokį.

# class Preke():
#     sekantis_id = 1
#     def __init__(self, kaina, kiekis, pavadinimas ):
#         self.id = Preke.sekantis_id
#         Preke.sekantis_id += 1
#         self.kaina = kaina
#         self.kiekis = kiekis
#         self.pavadinimas = pavadinimas
        
# prekiu_kiekis = int(input("Iveskite prekiu kieki: "))
# prekiu_sarasas = []

# for i  in range(prekiu_kiekis):
#     print(f"\nPreke #{i + 1}")
#     vart_pavadinimas = input("Iveskite produkto pavadinima: ")
#     vart_kaina = float(input("Iveskite produkto kaina: "))
#     vart_kiekis = int(input("Iveskite produkto kieki: "))
#     preke = Preke(vart_kaina, vart_kiekis, vart_pavadinimas)
#     prekiu_sarasas.append(preke)

# kolkas_didziausia = 0
# print("\nIvestos prekes: ")
# for preke in prekiu_sarasas:
#     bendra_suma = preke.kaina*preke.kiekis
#     print(f"ID: {preke.id} | Pavadinimas: {preke.pavadinimas} | kaina: {preke.kaina} Eur | kiekis: {preke.kiekis} | Bendra kaina: {bendra_suma} ")
#     if bendra_suma > kolkas_didziausia:
#         brangiausia = preke
#         print(f"Brangiausia preke yra {preke.pavadinimas}, jos bendra kaina yra {bendra_suma} Eur")


# Write a Python program to create a person class. 
# Include attributes like name, country and date of birth. Implement a method to determine the person's age.
 
# import datetime

# class Person():
#     def __init__(self, name, country, birth_date):
#         self.name = name
#         self.country = country
#         self.birth_date = birth_date
    
#     def suzinoti_amziu(self):
#         siandien = datetime.date.today()
#         amzius = siandien.year - self.birth_date.year
#         if (siandien.month, siandien.day) < (self.birth_date.month, self.birth_date.day):
#             amzius -= 1
#         return amzius

# try:
#     print("Iveskite informacija apie save: ")
#     print("-"*50)
#     vardas = input("Vardas: ")
#     print("-"*50)
#     pavarde = input("Pavarde: ")
#     print("-"*50)
#     salis = input("Salis: ")
#     print("-"*50)
#     metai = int(input("Iveskite savo gimimi metus: "))
#     print("-"*50)
#     menuo = int(input("Iveskite savo gimimo menesi: "))
#     print("-"*50)
#     diena = int(input("Iveskite gimimo diena: "))
# except ValueError:
#     print("Ivestas neteisingas formatas, bandykite dar karta")

# gimimo_data = datetime.date(metai, menuo, diena)

# zmogus = Person(vardas, salis, gimimo_data)

# print(f"\n {zmogus.name}, Jus esate is {zmogus.country} ir Jus esate {zmogus.suzinoti_amziu()} metų amžiaus.")


# ___________________________________________________________________________________
# Perdaryti (arba iš naujo sukurti) programą su prekėmis, kad veiktų su objektais.

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

import pickle

# class Preke(): #si klase yra atsakinga tik uz preke, ja sukuria, parodo jos informacija, atnaujina joje informacija
#     def __init__(self, id, pavadinimas, kiekis, kaina):
#         self.pavadinimas = pavadinimas
#         self.id = id
#         self.kiekis = kiekis
#         self.kaina = kaina
    
#     def rodyti_prod_info(self):
#         print("-" * 50)
#         print(f"ID: {self.id} | Pavadinimas: {self.pavadinimas} | Kiekis = {self.kiekis} | Kaina = {self.kaina:.2f} €")
#         print("-" * 50)
    
#     def atnaujinti_kieki(self, naujas_kiekis):
#         try:
#             naujas_kiekis = int(naujas_kiekis)
#             if naujas_kiekis >= 0:
#                 self.kiekis = naujas_kiekis
#             else:
#                 raise ValueError
#         except ValueError:
#             print("Ivedete ne skaiciu, arba neigiama, bandykite dar karta.")
    
#     def atnaujinti_kaina(self, nauja_kaina):
#         try:
#             nauja_kaina = float(nauja_kaina)
#             if nauja_kaina >= 0:
#                 self.kaina = nauja_kaina
#             else:
#                 print("Ivedete ne skaiciu, arba neigiama, bandykite dar karta.")
#         except ValueError:
#             print("Ivedete ne skaiciu, arba neigiama, bandykite dar karta.")
    
#     def atnaujinti_pavadinima(self, naujas_pavadinimas):
#         if naujas_pavadinimas == "":
#             print("Neivedete naujo pavadinimo, bandykite dar karta.")
#         else:
#             self.pavadinimas = naujas_pavadinimas


# class Inventorius(): #si klase atsakinga uz invenoriu ir ji valdo - sukuria sarasa, kur visi Preke klases sukurti objektai yra saugomi, 
#     def __init__(self, prekiu_sarasas=None):
#         if prekiu_sarasas is None:
#             self.prekiu_sarasas = []
#         else:
#             self.prekiu_sarasas = prekiu_sarasas
    

#     def uzkrauti_pickle(self, kelias):
#         try:
#             with open(kelias, "rb") as failas:
#                 nuskaitytas_failas = pickle.load(failas)
#                 self.prekiu_sarasas = nuskaitytas_failas
#                 print("-"*50)
#                 print("Inventorius sekmingai uzkrautas.")
#                 print("-"*50)
#         except FileNotFoundError:
#             print("-"*50)
#             print("Failas nerastas - sukuriamas naujas tuscias sarasas")
#             print("-"*50)
#             self.prekiu_sarasas = []

#     def issaugoti_pickle(self, kelias):
#         try:
#             with open(kelias, "wb") as failas:
#                 pickle.dump(self.prekiu_sarasas, failas)
#                 print(f"Atnaujinti duomenys issaugiti sekmingai i faila {kelias}")
#         except Exception:
#             print("Ivyko nenumatyta klaida, bandykite dar karta.")

#     def generuoti_nauja_id(self):
#         if self.prekiu_sarasas == []:
#             naujas_id = 1
#         else:
#             didziausiais_id = 0
#             for i in self.prekiu_sarasas:
#                 id_reiksme = i.id
#                 if id_reiksme > didziausiais_id:
#                     didziausiais_id = id_reiksme
#             naujas_id = didziausiais_id + 1
#         return naujas_id

#     def prideti_nauja_preke(self):
#         naujas_id = self.generuoti_nauja_id()
#         prekes_pavadinimas = input("Iveskite prekes pavadinima: ")

#         while True:
#             try:
#                 prekes_kiekis = int(input("Iveskite prekes kieki: "))
#                 if prekes_kiekis < 0:
#                     print("Prekes kiekis turi buti teigiamas")
#                     continue
#                 break
#             except ValueError:
#                 print("Prekes kiekis turi buti sveikas skaicius.")

#         while True:
#             try:
#                 prekes_kaina = float(input("Iveskite prekes kaina: "))
#                 if prekes_kaina < 0:
#                     print("Prekes kaina negali buti neigiama, bandykite dar karta")
#                     continue
#                 break
#             except ValueError:
#                 print("Ivedete neteisinga kainos formata, bandykite dar karta")

#         nauja_preke = Preke(naujas_id, prekes_pavadinimas, prekes_kiekis, prekes_kaina)

#         self.prekiu_sarasas.append(nauja_preke)

#         print("-"*50)
#         print(f"Preke {prekes_pavadinimas} prideta i faila, jai priskirtas {naujas_id} ID.")
#         print("-"*50)
    
#     def rodyti_visas_prekes(self):
#         if self.prekiu_sarasas == []:
#             print("Prekiu sarasas yra tuscias.")
#         else:
#             for i in self.prekiu_sarasas:
#                 i.rodyti_prod_info()

#     def pasalinti_preke_pagal_id(self):
#         try:
#             salinamas = int(input("Iveskite produkto ID, kuri norite pasalinti: "))
#         except ValueError:
#             print("Neteisingai ivedete ID koda, bandykite dar karta")
#             return

#         radau = False
#         for i in self.prekiu_sarasas:
#             if i.id == salinamas:
#                 self.prekiu_sarasas.remove(i)
#                 print(f"Preke {i.pavadinimas} su {i.id} ID buvo pasalinta sekmingai")
#                 radau = True
#                 break
#         if not radau:
#             print("Prekes su tokiu ID nera.")

#     def redaguoti_preke_id(self):
#         try:
#             ivestas_id = int(input("Iveskite produkto ID, kuri norite pasalinti: "))
#         except ValueError:
#             print("Neteisingai ivedete ID koda, bandykite dar karta")
#             return
    
#         redaguojama_preke = None
#         for i in self.prekiu_sarasas:
#             if i.id == ivestas_id:
#                 redaguojama_preke = i
#                 break

#         if redaguojama_preke is None:
#             print("Preke su toki ID neegzistuoja.")
#             return

#         veiksmas = input("Pasirinkite, ka redaguosime (pavadinimas / kiekis / kaina):")

#         if veiksmas == "kiekis":
#             try:
#                 naujas_kiekis = int(input("Iveskite nauja kieki: "))
#             except ValueError:
#                 print("'Kiekis' privalo buti sveikas skaicius")
#                 return
            
#             redaguojama_preke.atnaujinti_kieki(naujas_kiekis)
#             print(f"Preke su ID {ivestas_id} kiekis atnaujintas i {naujas_kiekis}")

#         elif veiksmas == "kaina":
#             try:
#                 nauja_kaina = float(input("Iveskite nauja kaina: "))
#             except ValueError:
#                 print("Neteisingai ivesta kaina, bandykite dar karta")
#                 return
#             redaguojama_preke.atnaujinti_kaina(nauja_kaina)
#             print(f"Preke su ID {ivestas_id} kaina atnaujinta i {nauja_kaina:.2f} €")

#         elif veiksmas == "pavadinimas":
#             naujas_pavadinimas = input("Iveskite nauja pavadinima: ")
#             redaguojama_preke.atnaujinti_pavadinima(naujas_pavadinimas)
#             print(f"Preke su ID {ivestas_id} pavadinimas atnaujintas i {naujas_pavadinimas}")
#         else:
#             print("Tokio lauko redaguoti negalima, arba ivedete neteisingai.")


# def valdymo_meniu():
#     kelias = "inventorius.pickle"
#     inventorius = Inventorius()
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
#             inventorius.prideti_nauja_preke()
#         elif pasirinkimas == 2:
#             inventorius.redaguoti_preke_id()
#         elif pasirinkimas == 3:
#             inventorius.pasalinti_preke_pagal_id()
#         elif pasirinkimas == 4:
#             inventorius.rodyti_visas_prekes()
#         elif pasirinkimas == 5:
#             inventorius.issaugoti_pickle(kelias)
#             print("Inventorius irasytas i faila")
#         elif pasirinkimas == 6:
#             inventorius.uzkrauti_pickle(kelias)
#             print("Inventorius uzkrautas is failo")
#         elif pasirinkimas == 7:
#             print("Programa uzsidaro")
#             break
#         else:
#             print("neteisingas pasirinkimas, bandykite dar karta.")            

# valdymo_meniu()

# Kas jau baigė ir neturi ką veikti:
# Parašyti klasę Sakinys, kuri turi savybę tekstas irmetodus,kurie:
# •Gražina tekstą atbulai
# •Gražina tekstą mažosiomis raidėmis
# •Gražina tekstą didžiosiomis raidėmis
# •Gražina žodį pagal nurodytą eilės numerį
# •Gražina, kiek teksteyranurodytų simbolių arba žodžių
# •Gražinatekstą su pakeistu nurodytu žodžiu arba simboliu
# •Atspausdina, kiek sakinyje yra žodžių,skaičių,didžiųjų ir mažųjų raidžių
# Susikurti kelis klasės objektus ir išbandyti visus metodus

class Sakinys():
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def tekstas_atbulai(self):
        return self.tekstas[::-1]
    
    def mazosiomis(self):
        return self.tekstas.lower()
    
    def didziosiomis(self):
        return self.tekstas.upper()
    
    def zodis_pagal_eilesnr(self, numeris):
        zodziai = self.tekstas.split()
        if 1 <= numeris <= len(zodziai):
            return zodziai[numeris - 1]
        else:
            return "Tokio zodzio nera" 

    def kiek_simboliu(self):
        return len(self.tekstas)

    def kiek_zodziu(self):
        zodziai = self.tekstas.split()
        return len(zodziai)

    def uzkeisti_zodi(self, senas_zodis, naujas_zodis):
        return self.tekstas.replace(senas_zodis, naujas_zodis)
    
    def simboliu_analize(self):
        mazosios = 0
        didziosios = 0
        skaiciai = 0
        for i in self.tekstas:
            if i.isdigit():
                skaiciai += 1
            elif i.isupper():
                didziosios += 1
            elif i.islower():
                mazosios += 1
        return print(f"Mazuju raidziu: {mazosios}, didziuju raidziu: {didziosios}, skaiciu: {skaiciai}")
    


s = Sakinys("Labas, ka tu ka vakare? mano numeris 888888855")

print("-"*50)

print(s.tekstas_atbulai())

print("-"*50)

print(s.didziosiomis())

print("-"*50)

print(s.mazosiomis())

print("-"*50)

s.simboliu_analize()

print("-"*50)

print(s.zodis_pagal_eilesnr(2))

print("-"*50)

print(s.kiek_simboliu())

print("-"*50)

print(s.kiek_zodziu())

print("-"*50)

print(s.uzkeisti_zodi("Labas", "kebabas"))