# amzius = 20
# # skirtas tam, kai reikia palyginti daug salygu ar ji yra lygi kazkam
# match amzius:
#     case 0: # if amzius == 0:
#         print("Tu katik gimei")
#     case 1 : # elif amzius == 1:
#         print("Tu esi kudikis")
#     case 10 : # elif amzius == 10:
#         print("Tu esi vaikas")
#     case 20 : # elif amzius == 20:
#         print("Tu esi jaunas suaugęs žmogus")
#     case _: # else:
#         print("Tu esi suaugęs žmogus")

# MASYVAIo 
# Saraso CRUD
# sarasas = [4,1,7,5,8]
# sarasas.append(7) # Pridedamas elementas 7 prie sąrašo pabaigos
# print(sarasas) # Išvedamas sąrašas su nauju elementu
# sarasas.remove(7) # Ištrinama pirmoji 7 reikšmė iš sąrašo
# print(sarasas) # Išvedamas sąrašas be 7 reikšmės
# sarasas.pop(0) # Ištrinama pirmoji reikšmė iš sąrašo (indeksas 0)
# print(sarasas) # Išvedamas sąrašas be pirmos reikšmės
# sarasas[3] = 10 # Atnaujinama ketvirto elemento reikšmė į 10
# print(sarasas) # Išvedamas sąrašas su atnaujinta reikšmė

# sarasas = [] # Sukuriamas tuščias sąrašas
 
# sarasas = [4,1,7,5,8] # Sukuriamas sąrašas su penkiais elementais | list tipo
 
# print(sarasas) # Išvedamas sąrašas
 
# sarasas.append(7) # Pridedamas elementas 7 prie sąrašo pabaigos
# print(sarasas) # Išvedamas sąrašas su nauju elementu
 
# print(sarasas[3]) # Išvedamas ketvirtas elementas sąraše (indeksas 3)
# # programavime skaičiuojama nuo 0, todėl pirmas elementas yra indeksu 0, antras 1 ir t.t.
 
# # print(sarasas[5]) # index out of range - klaida, nes sąraše nėra šešto elemento (indeksas 5)
 
# # CRUD operacijos:
# # Create - sukurti
# # Read - nuskaityti
# # Update - atnaujinti
# # Delete - ištrinti
 
# sarasas.remove(7) # Ištrinama pirmoji 7 reikšmė iš sąrašo
# print(sarasas) # Išvedamas sąrašas be 7 reikšmės
# sarasas.pop(0) # Ištrinama pirmoji reikšmė iš sąrašo (indeksas 0)
 
# # print(sarasas) # Išvedamas sąrašas be pirmos reikšmės
 
# sarasas = [4,1,7,5,8]
# sarasas[3] = 10 # Atnaujinama ketvirto elemento reikšmė į 10
# print(sarasas) # Išvedamas sąrašas su atnaujinta reikšme
 
# Saraso CRUD
# sarasas = [4,1,7,5,8]
# sarasas.append(7) # Pridedamas elementas 7 prie sąrašo pabaigos
# print(sarasas) # Išvedamas sąrašas su nauju elementu
# sarasas.remove(7) # Ištrinama pirmoji 7 reikšmė iš sąrašo
# print(sarasas) # Išvedamas sąrašas be 7 reikšmės
# sarasas.pop(0) # Ištrinama pirmoji reikšmė iš sąrašo (indeksas 0)
# print(sarasas) # Išvedamas sąrašas be pirmos reikšmės
# sarasas[3] = 10 # Atnaujinama ketvirto elemento reikšmė į 10
# print(sarasas) # Išvedamas sąrašas su atnaujinta reikšmė



# 1 uzduotis

# print(sarasas[1])
# sarasas = [4,1,7,5,8]
# sarasas.append(7)
# sarasas.remove(8)
# sarasas[2] = 15
# print(sarasas)

# 2 uzduotis

# pirmas_skaicius = int(input("įveskite pirmą skaičių: "))
# antras_skaicius = int(input("įveskite antrą skaičių: "))
# trecia_skaicius = int(input("įveskite trečią skaičių: "))

# sarasas = [pirmas_skaicius, antras_skaicius, trecia_skaicius]

# print(sarasas)

# sakinys = "Sveiki studentai, tikiuosi, kad jums sekasi gerai"
 
# print(sakinys[10]) # Išvedamas pirmas simbolis sakinyje
 
# Pagrindinis skirtumas tarp string ir saraso yra, tas, kad string yra immutable, o sarasas yra mutable
# sakinys[5] = "a" # TypeError: 'str' object does not support item assignment
 
# slicing
# print(sakinys[0:5]) # Išvedamas pirmas 5 simboliai sakinyje | pirmas elementas ieina o antras nera imtinai
# print(sakinys[-3]) # minus reiskia nuo antro galo
# print(sakinys[5:]) # Išvedamas simboliai nuo 5 iki galo
# print(sakinys[:5]) # Išvedamas simboliai nuo pradzios iki 5
# print(sakinys[-10:-3]) # geriau privengti, nes sudetinga skaityti
# print(sakinys[::-1]) # sarasas[start:stop:step]
# print(sakinys[::2])
# print(sakinys[5:20:2]) # Išvedamas simboliai nuo 5 iki 20 kas antras


# https://www.w3schools.com/python/python_ref_list.asp



# # uzduotis 1
# Paklausk vartotojo amžiaus ir parodyk, kiek jam bus metų po 10 metų.

# amzius = int(input("įveskite savo amžių: "))
# print("Jūsų amžius po 10 metu bus: ", amzius+10)

# # Uzduotis 2

# Paklausk vartotojo, koks jo amžius, ir jei jam daugiau nei 18 metų, išspausdink „Tu esi pilnametis“, jei mažiau – „Tu esi nepilnametis

# amzius = int(input("įveskite savo amžių: "))

# if amzius>=18:
#     print("Tu esi pilnametis")
# else:
#     print("Tu esi nepilnametis")


# # Uzduotis 3
# Paklausk vartotojo įvesti slaptažodį. Jei jis yra „python“, išspausdink „Prisijungta“, kitu atveju – „Klaidingas slaptažodis“

# vartotojo_ivestis = input("įveskite slaptazodi: ")

# if vartotojo_ivestis == "python":
#     print("Prisijungta")
# else:
#     print("Klaidingas slaptažodis")

# # Uzduotis 4
# Sukurk sąrašą su 5 vaisiais ir išspausdink trečią sąrašo elementą

# sarasas = ["bananas", "apelsinas", "mango", "ananasas", "kivi"]
# print(sarasas[2])


# # Uzduotis 5
# Sukurkite konkretaus ilgio sarasas pavyzdziui 5 elementu ir isveskite jo suma
# taip pat isveskite koks yra saraso ilgis

# sarasas = [15, 20, 25, 5 ,8]
# suma = sum(sarasas)
# print("saraso suma:", suma)

# ilgis = len(sarasas)
# print("saraso ilgis: ", ilgis)

# # Uzduotis 6
# Sukurk sąrašą iš 6 spalvų ir išspausdink pirmas tris spalvas naudodamas slicing
# Iš to paties sąrašo išspausdink paskutines dvi spalvas

# sarasas = ["geltona", "zalia", "raudona", "melyna", "oranzine", "violetine"]
# print("pirmos 3 spalvos: ", sarasas[0:3])
# print("paskutines 2 spalvos: ", sarasas[len(sarasas)-2:len(sarasas)])

# uzduotis 7
# Sukurk skaičių sąrašą [10, 20, 30, 40, 50, 60] ir išspausdink tik [20, 30, 40]

# sarasas = [10, 20, 30, 40, 50, 60]
# print(sarasas[1:4])

# reikiami_skaiciai = []
# if 20 in sarasas:
#     reikiami_skaiciai.append(20)
# if 30 in sarasas:
#     reikiami_skaiciai.append(30)
# if 40 in sarasas:
#     reikiami_skaiciai.append(40)
#     print(f"{reikiami_skaiciai[0]}, {reikiami_skaiciai[1]}, {reikiami_skaiciai[2]}")
# else:
#     print("neradome reikiamu skaiciu")


# uzduotis 8
# Sukurkite sakinį ir atspausdinkite jį atvirkščiai

# sakinys= "as esu Dominik"
# print(sakinys[::-1])
# print(sakinys[::2])

# # 25.04.13 papild. namu darbai
# sarasas = ["makaronai", "kebabas", "kepsnys"]
# print(sarasas[1])

# sarasas.append("vaisių salotos")

# del sarasas[0]

# sarasas[2] = "pica"

# print(sarasas)

# #clear
# gyvunai = ["šuo", "katė", "triušis"]

# #insert
# miestai = ["Kaunas", "Klaipėda", "Šiauliai"]

# miestai.insert(0, "Vilnius")

# print(miestai)  # ['Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai']

# Uzduotis keliamieji metai

# vartotojo_ivestis = int(input("Iveskite norimus metus, kad suzinoti ar jie keliamieji: "))

# if vartotojo_ivestis < 0:
#     print("Klaida: metai negali buti neigiami.")
# elif (vartotojo_ivestis % 400 == 0) or (vartotojo_ivestis % 4 == 0):
#     print("sie metai yra keliamieji")
# else:
#     print("sie metai yra nekeliamieji")

# metai = int(input("iveskite metus: "))
 
# if metai % 4 == 0 and metai % 100 != 0 or metai % 400 == 0: #jei dalinasi is 4 ir nesidalina is 100
#     print("keliamieji metai")
# else:
#     print("nekelemieji metai")































