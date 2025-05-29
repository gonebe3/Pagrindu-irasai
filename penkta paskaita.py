
# Ciklai
# Reikalingi kartoti daug uzd daug kartu

# sarasas = [4,5,1,7,2,9]
 
# # for # pagrindinis ciklo zodis
 
# for skaicius in sarasas: # for ciklas, kuris iteruoja per sarasa | 1 iteracija -  skaicius = sarasas[0] | 2 iteracija - skaicius = sarasas[1] | 3 iteracija - skaicius = sarasas[2] | 4 iteracija - skaicius = sarasas[3] | 5 iteracija - skaicius = sarasas[4] | 6 iteracija - skaicius = sarasas[5]
#     print(skaicius) # isveda kiekviena skaiciu is saraso
#     print("Skaicius atspausdintas")
 
 
# zodziai = ["pirmas", "antras", "trecias", "ketvirtas", "penktas"] # sarasas su zodziais
 
# for zodis in zodziai:
#     print(zodis)
 
# skaiciai = [7,4,9,2,4,3,1,5,6,8] # sarasas su skaiciais
 
# suma = 0
 
# for skaicius in skaiciai: # for ciklas, kuris iteruoja per sarasa | 1 iteracija -  skaicius = skaiciai[0] | 2 iteracija - skaicius = skaiciai[1] | 3 iteracija - skaicius = skaiciai[2] | 4 iteracija - skaicius = skaiciai[3] | 5 iteracija - skaicius = skaiciai[4] | 6 iteracija - skaicius = skaiciai[5]
#     suma = skaicius + suma
#     print(f"Tarpine suma: {suma}")
 
# print(suma)

# skaiciai = [7,4,9,2,4,3,1,5,6,8] # sarasas su skaiciais
# suma = 0
 
# for skaicius in skaiciai: # for ciklas, kuris iteruoja per sarasa | 1 iteracija -  skaicius = skaiciai[0] | 2 iteracija - skaicius = skaiciai[1] | 3 iteracija - skaicius = skaiciai[2] | 4 iteracija - skaicius = skaiciai[3] | 5 iteracija - skaicius = skaiciai[4] | 6 iteracija - skaicius = skaiciai[5]
#     if skaicius % 2 == 0: # tikriname ar skaicius lyginis
#         suma = suma + skaicius # jei lyginis, sudedame prie sumos
#         print(f"Tarpine suma: {suma}")

# Sukurkite sąrašą iš žodžių ir atspausdinkite kiekvieną žodį atskiroje eilutėje.
 
# sarasas = ["Berzas", "Liepa", "Obelis", "Klevas"]
# for medziai in sarasas:
#     print(medziai)
 
# Sukurkite skaičių sąrašą ir pakelkite visu sąrašo skaičius naudotojo
# pasirnktu laipsniu, sąrašą sukursite patys, laipsnį pasirinks naudotojas.
# Kiekvieno elemento pakelta laipsniu reikšmę atspausdinkite.
 
# sarasas = [2, 3, 5, 6, 8, 10]
# laipsnis = int(input("Parasykite kuriuo laipsniu kelti skaicius is saraso: "))
# for skaiciai in sarasas:
#     print(f"Skaicius pakeltas nurodytu laipsniu: {skaiciai ** laipsnis}")

# sarasas = [4, 'Labas', 8.5, True, 7] # sarasas su ivairiais elementais
 
# for mano_kintamasis in sarasas: # for ciklas, kuris iteruoja per sarasa | 1 iteracija -  mano_kintamasis = sarasas[0] | 2 iteracija - mano_kintamasis = sarasas[1] | 3 iteracija - mano_kintamasis = sarasas[2] | 4 iteracija - mano_kintamasis = sarasas[3] | 5 iteracija - mano_kintamasis = sarasas[4]
#     print(mano_kintamasis) # isveda kiekviena elementa is saraso
 
# sarasas_sarase = [4,5,2,4,8,[9,2,1],7,4,[5,4,2]] # sarasai gali turėti sarasus
 
# # print(sarasas_sarase) # isveda sarasa su sarasu
 
# print(sarasas_sarase[5][0])
 
# print(f"Galutine suma: {suma}") # isvedame galutine suma

# zodynas = {"Ugne":[9,8,10,9,10], "Mantas":[8,9,10,9,10], "Tomas":[7,8,9,8,9]} # zodynas su sarasais
# # print(zodynas) # isveda zodyna
 
 
# suma = 0
 
# for elementas in zodynas["Ugne"]: # for ciklas, kuris iteruoja per sarasa | 1 iteracija -  elementas = zodynas["Ugne"][0] | 2 iteracija - elementas = zodynas["Ugne"][1] | 3 iteracija - elementas = zodynas["Ugne"][2] | 4 iteracija - elementas = zodynas["Ugne"][3] | 5 iteracija - elementas = zodynas["Ugne"][4]
#     suma += elementas # sudedame visus elementus
#     print(suma) # isveda tarpine suma
 
# print(suma/len(zodynas["Ugne"]))


# amziai = {"Ugne": 32, "Mindaugas":30, "Justas":26}
 
# print(amziai)
 
# print(amziai.keys())
 
# for key in amziai.keys():
#     print(key) # isveda visus zodyno raktus
 
# amziai = {"Ugne": 32, "Mindaugas":30, "Justas":26}
 
# # print(amziai)
 
# # print(amziai.keys())
 
# # for key in amziai.keys(): # keys eina per raktus
# #     print(key) # isveda visus zodyno raktus
 
 
# amziai = {"Ugne": 32, "Mindaugas":30, "Justas":26}
 
# print(amziai)
 
# print(amziai.values())
 
# for value in amziai.values(): # values eina per reiksmes
#     print(value) # isveda visus zodyno raktus
 
 
# I UZD

# sarasas = ["Jurgis", "Antanas", "Mantas", "Linas", "Kostas"]

# for zodis in sarasas:
#     print(zodis)

# sarasas = [1,2,4,5,8,4,6,7,7,9,2,24,5,7,8,52,8]
# print(sarasas)
# laipsnis = int(input("Iveskite laipsnį, kuri norite: "))
# for skaicius in sarasas:
#   naujas_sarasas = [skaicius ** laipsnis for skaicius in sarasas]
# print(naujas_sarasas)

# II uzd

# sarasas = ["Jurgis", "Antanas", "Mantas", "Linas", "Kostas"]
# for zod_ilg in sarasas:
#     if len(zod_ilg) > 5:
#         print(zod_ilg)




# RANGE

# range - leidzia nustatyti kiek kartu bus kartojamas ciklas
 
# range is esmes tiesiog sukuria sarasa su skaiciais nuo 0 iki n-1 | range(5) - [0,1,2,3,4] | range(5,10) - [5,6,7,8,9] | range(5,10,2) - [5,7,9] | range(10,5,-1) - [10,9,8,7,6] | range(0,-10,-1) - [0,-1,-2,-3,-4,-5,-6,-7,-8,-9]
 
# for i in range(5): # range(5) - [0,1,2,3,4] | 5 kartus
#     print(i) # isveda 0,1,2,3,4

# for i in range(3,8): # range turi panasia sintakse kaip ir slicing range(start,stop,step) | jeigu tik vienas skaicius - tai bus stop | jeigu du - tai bus start ir stop | jeigu trys - tai bus start, stop ir step
#     print(i)
 
# for i in range(3,8,2): # range turi panasia sintakse kaip ir slicing range(start,stop,step) | jeigu tik vienas skaicius - tai bus stop | jeigu du - tai bus start ir stop | jeigu trys - tai bus start, stop ir step
#     print(i)


# Sukurti programą, kuri:
# •Leistų vartotojui įvesti metus
# •Atspausdintų „Keliamieji metai“, jei taip yra
# •Atspausdintų „Nekeliamieji metai“, jei taip yra
# •Perdaryti užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų.
# Šią programą jau darėte praeitą paskaitą, reikia pasiimti prieš tai darytą programą ir pritaikyti ketvirtą punktą.
# Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų




# I UZD

# for i in range(1900,2100):
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0: #jei dalinasi is 4 ir nesidalina is 100
#         print(f"{i} - keliamieji metai")
#     else:
#         print(f"{i} - nekelemieji metai")



# II UZD

# suma = 0

# for i in range(10,101):
#  if i % 2 != 0:
#     suma = suma + i

# print(suma)

# III UZD

# Leiskite naudotojui įvesti, kiek jis nori įvesti skaičių (pvz 7), tuomet leiskite jam įvesti tiek skaičių  kiek jis prašė ir suskaičiuokite jų vidurkį.

# vidurkis = 0

# vart_ivest1 = float(input("iveskite kiek norite skaičių: "))

# for i in range(vart_ivest1):
#     vart_ivest2 = float(input ("iveskite skaiciu: "))
#     vidurkis = vidurkis + vart_ivest2

# vidurkis = vidurkis / vart_ivest1

# print(f"skaiciu vidurkis: {vidurkis} ")


# Raidžių išskaidymas
# Paprašykite naudotojo įvesti trumpą žodį arba frazę.
# Panaudokite for ciklą, kad išvestumėte kiekvieną įvesto teksto simbolį (raidę, tarpą) naujoje eilutėje.


# vart_ivestis = input("iveskite fraze ar zodi: ")

# for raide in vart_ivestis:
#     print(raide)


# Skaičių pakėlimas laipsniu
# Paprašykite naudotojo įvesti du skaičius: pagrindą (base) ir laipsnį (power) (pvz., 2 ir 3).
# Sukurkite ciklą, kuris dauginimo būdu apskaičiuotų base^power (nereikėtų naudoti integruotos ** operacijos).
# Išveskite gautą rezultatą.
# Pavyzdys: Jei naudotojas įveda 2 ir 3, rezultatas: 2^3 = 8.

# rezultatas = 1
# base = int(input("Iveskite skaiciu, kuri norite kelti laipsniu: "))
# power = int(input("Iveskite laipsni, kuriuo norite kelti skaiciu: "))

# for i in range(power):
#     rezultatas = rezultatas * base

# print(rezultatas)


# Simbolių paieška
# Paprašykite naudotojo įvesti sakinį.
# Tuomet leiskite įvesti raidę (ar kitą simbolį), kurio bus ieškoma sakinyje.
# Naudodami for ciklą suskaičiuokite, kiek kartų ši raidė pasikartoja sakinyje, ir išveskite rezultatą.

# rezultatas = 0
# vart_ivest = input("iveskite sakini: ")
# vart_ivest1 = input("nurodykite koki simbolio ieskoti: ")

# for raide in vart_ivest:
#     if vart_ivest1 == raide:
#         rezultatas = rezultatas + 1
# print(f"simoliu kiekis sakinyje = {rezultatas}")



# Žodžių išskaidymas ir spausdinimas
# Paprašykite naudotojo įvesti sakinio ilgį (kiek žodžių planuoja įvesti).
# Tegul naudotojas įveda kiekvieną žodį atskirai. Visus žodžius išsaugokite sąraše.
# Naudodami for ciklą išveskite žodžius atvirkštine tvarka (nuo paskutinio iki pirmo).

# kiek_zod = int(input("iveskite kiek zodziu norite ivesti: "))
# sarasas = []
# for i in range(kiek_zod):
#     vart_ivest = str(input("iveskite zodzius: "))
#     sarasas.append(vart_ivest)
# print(sarasas[::-1])

# Žodžio apsukimas
# Paprašykite naudotojo įvesti žodį ar trumpą frazę.
# Sukurkite programą, kuri, naudodama for ciklą, atspausdintų šį žodį (pvz., "Kava" → "avaK"). Nenaudokite [::-1] ar reverse
# Išveskite gautą apsuktą tekstą.

# apsuktas = ""
# vart_ivest = input("iveskite norima zodi ar sakini: ")

# for i in vart_ivest:
#     apsuktas =  i + apsuktas

# print(apsuktas)

# Didžiausios reikšmės radimas be max
# Susikurkite sąrašą, pvz. [3, 7, 1, 12, 9].
# Naudodami for ciklą raskite didžiausią elementą sąraše (nenaudokite max() funkcijos).
# Išveskite rastą reikšmę.



# sarasas = [3, 7, 1, 12, 9]
# didziausias = sarasas[0]
# for i in sarasas:
#     if i > didziausias:
#         didziausias = i
# print(didziausias)
   
# Sukurkite ciklą kuris atspausdintų visus skaičius nuo 10 iki 1
# for i in range(10,1,-1):
#     print(i)

# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki -100
# for i in range(0,-100,-1):
#     print(i)

# Sukurkite ciklą kuris atspausdintų skaičius nuo naudotojo įvesto skaičiaus iki naudotojo įvesto skaičiaus

# ivestis1 = int(input("iveksite nuo kokio skaiciaus spausdinsime: "))
# ivestis2 = int(input("iveksite iki kokio skaiciaus spausdinsime: ")) + 1

# for i in range(ivestis1,ivestis2):
#     print(i)


# Sukurkite žodyną kuriame saugosite Žmonių pavardes, naudotojui įvedus vardą pasisveikinkite su juo jo vardu ir Pavarde

# sarasas = {"Antanas":"Packauskas",
#            "Gediminas":"Jonunas",
#            "Gierius":"Cimbalas"}


# vardas = input("iveskite varda: ")
# print(sarasas[vardas])

# zodynas = {"cepelinai":"spirgos",
#            "koldunai":"grietine",
#            "makaronai":"suris"}

# print(zodynas.keys())

# Lyginių skaičių atspausdinimas
# Sukurkite ciklą, kuris spausdina visus lyginius skaičius nuo 2 iki 20.

# for i in range(2,21):
#     if i % 2 == 0:
#         print(i)

# Mėgstamų gyvūnų sąrašas
# Sukurkite sąrašą su penkiais mėgstamiausiais gyvūnų pavadinimais. Naudokite ciklą, kad kiekvieno gyvūno pavadinimą išvestumėte kartu su prierašu, pvz., " - yra nuostabus."


# sarasa = ["suo", "kate", "chameleonas", "zirafas", "hipopotamas"]

# for i in sarasa:
#     print(f" {i} - yra nuostabus.")

# Spalvų sąrašo transformacija
# Sukurkite sąrašą su keliomis spalvų reikšmėmis (pvz., „raudona“, „žalia“, „mėlyna“). 
# Naudokite ciklą, kad kiekvieną spalvą konvertuotumėte į mažąsias raides ir išveskite naują sąrašą.

# sarasas = ["geltona","raudona","zalia","melyna","oranzine"]














