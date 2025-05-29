# # tuscas_zodynas = {} # tuscias zodynas
# # zodynas = {"Lietuva":"Vilnius", # Lietuva - raktas(key), Vilnius - reikšmė(value)
# #             "Latvija":"Riga",
# #             "Estija":"Talinas",
# #             "Lenkija":"Varšuva",
# #             "Vokietija":"Berlynas",
# #             "Prancūzija":"Paryžius"}
# # print(zodynas)
# # # zodyne skirtingai nei sarase viskas vyksta aplink raktus nera indeksu
 
# # print(zodynas["Estija"])
# # print(zodynas["Lietuva"])
 
# # zodynas["Ispanija"] = "Madridas" # Pridedamas naujas raktas ir reikšmė
# # print(zodynas) # Išvedamas zodynas su nauju raktu ir reikšme
 
# # zodynas["Lietuva"] = "Kaunas" # Atnaujinama reikšmė pagal raktą
# # print(zodynas) # Išvedamas zodynas su atnaujinta reikšme
# # # jeigu raktas jau yra zodyne tai jis atnaujina reiksme, jeigu nera tai prideda nauja raktas-reiksme
 
# # zodynas["Lietuva"] = zodynas["Lietuva"].upper() # Atnaujinama reikšmė pagal raktą
# # print(zodynas)
 
# # zodynas.pop("Estija") # Ištrinamas raktas ir reikšmė pagal raktą
# # print(zodynas) # Išvedamas zodynas be ištrinto rakto ir reikšmės
 
# # # del zodynas["Latvija"] # Ištrinamas raktas ir reikšmė pagal raktą, rečiausiai naudojamas
# # # print(zodynas) # Išvedamas zodynas be ištrinto rakto ir reikšmės

# # I uzduotis
# # zodynas = {"cepelinai":"spirgos",
# #            "koldunai":"grietine",
# #            "makaronai":"suris"}

# # print(zodynas["cepelinai"])

# # zodynas["pica"] = "padazas"

# # zodynas.pop("cepelinai")

# # zodynas["koldunai"] = "pipirai"

# # print(zodynas)

# # zodynas = {"cepelinai":"spirgos",
# #            "koldunai":"grietine",
# #            "makaronai":"suris"}

# # funkcija = input("iveskite ka norite padaryti: istrinti, prideti, pakeisti: ")

# # if funkcija == "pakeisti":
# #     vart_ivestis = input("iveskite koki irasa norite redaguoti: ")
# #     vart_ivestis2 = input("i ka norite pakeisti: ")
# #     zodynas[vart_ivestis] = vart_ivestis2
# #     print(zodynas)
# # if funkcija == "istrinti":
# #     vart_ivestis = input("iveskite koki irasa norite redaguoti: ")
# #     zodynas.pop(vart_ivestis)
# #     print(zodynas)
# # if funkcija == "prideti":
# #     vart_ivestis3 = input("ka norite prideti: ")
# #     vart_ivestis4 = input("ka tai reiskia: ")
# #     zodynas[vart_ivestis3] = vart_ivestis4
# #     print(zodynas)

# # I papild uzd

# # zodynas = {"cepelinai":"spirgos",
# #            "koldunai":"grietine",
# #            "makaronai":"suris"}

# # raktai = zodynas.keys()
# # print(raktai)


# # II papild uzd

# # zodynas = {"cepelinai":"spirgos",
# #            "koldunai":"grietine",
# #            "makaronai":"suris"}

# # zodynas2 = {"subaru":"impreza",
# #            "audi":"a4",
# #            "bmw":"3 series"}

# # zodynas.update(zodynas2)

# # print(zodynas)

# # zodynas = {"cepelinai":"spirgos",
# #            "koldunai":"grietine",
# #            "makaronai":"suris"}

# # zodynas2 = {"cepelinai":"spirgos",
# #            "koldunai":"grietine",
# #            "makaronai":"suris"}


# # zodynas.clear()

# # print(zodynas)

# # setas = {1,1,2,2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7} # setas - unikalus elementai, nera pasikartojimu
# # print(setas)
 
# # # turite sarasa su pasikartojanciais elementais, atrinkite tik unikalius elementus
 
# # sarasas = [1,1,1,2,2,2,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8] # sarasas su pasikartojanciais elementais
# # print(sarasas) # Išvedamas sąrašas su pasikartojančiais elementais
# # # int(input("Tekstas"))
# # atrinkti = set(sarasas)
# # print(atrinkti)
 
# tuplas = (1,2,3,4,5) # tuplas - nekeičiama sekos struktūra, panaši į sąrašą, bet negalima keisti elementų
 
# print(tuplas) # Išvedamas tuplas, tuplas naudojamas nes, `jeigu reikia, kad elementai butu nekeičiami`
# tuplas[0] = 10 # Išmetama klaida, nes tuplas yra nekeičiama sekos struktūra
 
# # set - {}, tuple -(), list - [], dict - {key:value}

# # sarasas = [1,2,3,4,5] # sarasas - keičiama sekos struktūra, galima keisti elementus
 
# # if 2 in sarasas: # tikrina ar elementas yra sarase
# #     print("Yra") # Išvedamas tekstas "Yra"
 
# # zodynas = {"Lietuva":"Vilnius", # Lietuva - raktas(key), Vilnius - reikšmė(value)
# #             "Latvija":"Riga",
# #             "Estija":"Talinas",
# #             "Lenkija":"Varšuva",
# #             "Vokietija":"Berlynas",
# #             "Prancūzija":"Paryžius"}
 
# # if "Lietuva" in zodynas: # tikrina ar raktas yra zodyne
# #     print("Yra") # Išvedamas tekstas "Yra"
 
# # is
# # sarasas = [1,2,3,4,5]
# # sarasas2 = [1,2,3,4,5]
 
# # if sarasas is sarasas:
# #     print("Yra") # Išvedamas tekstas "Yra"
 
# # if not 3> 5: # not paneigia (arba invertuoja) sąlygą
# #     print("3 didesnis uz 5")
 
# # dirbu dirbu...
 
# # if 2> 3:
# #     pass # nieko nedaro, bet leidžia tęsti kodą
 
# # print("Baigta") # Išvedamas tekstas "Baigta"
# kintamasis = "labas" # kintamasis su tekstu
# if type(kintamasis) == str: # tikrina ar tipas yra int
#     print(type(kintamasis)) # Išvedamas tekstas "Yra"



# import time # tai ikelia kazkieno kito koda
 
# start_time = time.perf_counter() # pradeda matuoti laiką
 
# # cia rasomas kodas, kurio vykdymo laikas bus matuojamas
 
# # ilgai trunkanti opercija
 
 
# end_time = time.perf_counter() # baigia matuoti laiką
 
# print(f"Vykdymo laikas: {end_time - start_time} sek") # Išvedamas vykdymo laikas
 

# Parašyti programą, kuri su eilute "Zen of Python, by Tim Peters„ (tai yra pirma eilutė) darytų šiuos veiksmus:
# •Atspausdintų paskutinį antro žodžio simbolį (situos darykite su split)
# •Atspausdintų pirmą trečio žodžio simbolį
# •Atspausdintų tik pirmą žodį (pameginkite ir su slicing pvz. tekstas[0:5]) ir su split
# •Atspausdintų tik paskutinį žodį
# •Atspausdintų visą frazę atbulai
# •Atskirtų žodžius ir juos atspausdintų
# •Žodį "Python" pakeistų į "Programming" ir atspausdintų naują sakinį
# Patarimas: naudoti string karpymo įrankius, funkcijas split(), replace()




# sakinys = "Zen of Python, by Tim Peters"

# rezultatas = sakinys.split()
# antras_zodis = rezultatas[1]
# print(antras_zodis[1])

# trecias_zodis = rezultatas[2]
# print(trecias_zodis[0])

# print(sakinys[0:3])

# split = rezultatas[0]
# print(split)

# print(sakinys[-6:-1])

# print(sakinys[::-1])

# sakinys = "Zen of Python, by Tim Peters"
# print(sakinys.split())

# sakinys1 = "Zen of Python, by Tim Peters"

# sakinys1.replace("Python", "Programming")
# print(sakinys1)

# III UZD
# •Sukurkite sąrašą su pasikartojančiomis reikšmėmis, viena komanda pašalinkite visas šias pasikartojančias reikšmes (print galima naudoti, neribotą kiekį kartų)
# •Sukurkite du identiškus objektus (tuple ir sąrašas), pamatuokite ar atspausdindami visus tuple elementus sutaupote laiko palyginus su spausdinant visus sąrašo elementus.


# sarasas = [1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,4,]

# rezultatas = set(sarasas)

# print(rezultatas)

# import time
# start_time = time.perf_counter()

# sarasas = ["labas", 1, 7, 7.5, "kaip", ] * 500

# print(sarasas)

# end_time = time.perf_counter()

# print(f"Vykdymo laikas: {end_time - start_time} sek")
# 0.0023099000100046396 sek

# import time
# start_time = time.perf_counter()

# tuple = ("labas", 1, 7, 7.5, "kaip", ) * 500
# print(tuple)

# end_time = time.perf_counter()
# print(f"Vykdymo laikas: {end_time - start_time} sek")
# 0.00224910001270473 sek


# Užduotis 1: Sakinių Kūrėjas su Akcentais
# Tikslas:
# Paprašyk vartotojo įvesti:
# Daiktavardį,
# Veiksmažodį,
# Būdvardį.
# Sudaryk žaismingą sakinį, kuriame:
# Būdvardis pateikiamas DIDŽIOSIOMIS RAIDĖMIS,
# Daiktavardis pakartojamas du kartus,
# Veiksmažodis pateikiamas mažosiomis raidėmis.


# daiktavardis = input("Parasykite daiktavardi: ")
# veiksmazodis = input("Parasykite veiksmazodi: ")
# budvardis = input("Parasykite budvardi: ")

# maz_raid = veiksmazodis.lower()

# did_raid = budvardis.upper()

# print(did_raid)
# print(daiktavardis + " " + daiktavardis)
# print(maz_raid)



# II uzd 

# temp = float(input("iveskie temp celsijumi: "))

# rezultatas = (temp * 9/5 + 32 )

# konvertuotas = str(rezultatas) + "F"

# atsakymas = str(temp) + "C" +" " + "atitinka" + " " + konvertuotas

# print(atsakymas)


# balai = int(input("Iveskite savo bala: "))

# if balai > 100:
#     print("balas negali buti daugiau uz 100")
# if balai < 0:
#     print("balai negali buti maziau uz 0")

# if 90 >= balai <100:
#     print("Tavo pazymis: A - Puikiai ")
# elif 80 >= balai <90:
#     print("Tavo pazymis: B - Gerai ")
# elif 70 >= balai <80:
#     print("Tavo pazymis: C - Patenkinamai ")
# elif 60 >= balai <70:
#     print("Tavo pazymis: D - Reikia tobulėti ")
# elif 59 >= balai:
#     print("Tavo pazymis: D - Reikia tobulėti ")





























