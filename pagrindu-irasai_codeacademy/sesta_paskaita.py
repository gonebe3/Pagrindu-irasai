# Break
# Continue
# While
# random (random.randint(nuo,iki))



# while condition:
#     statement
 
# if 6> 5:
#     print("ifas veika")
 
# kelintas = 0
 
# while 6 > kelintas: # ciklas veikia, tol kol salyga yra teisinga
#     print("Labas") # 0, 1 ,2 ,3 4, 5
#     kelintas = kelintas + 1
   
# ivesta_teisingai = False
 
# while not ivesta_teisingai: # False invertuoja i True
 
#     ivestis = input("Iveskite zodi ate, jeigu norite baigti: ")
 
#     if ivestis == "ate":
#         print("Ciklas baigtas")
#         ivesta_teisingai = True
#     else:
#         print("Ivedete ne ate meginkite dar karta")
 
# ivesta_neteisingai = True
 
# while ivesta_neteisingai: # False invertuoja i True
 
#     ivestis = input("Iveskite zodi ate, jeigu norite baigti: ")
   
#     if ivestis == "ate":
#         print("Ciklas baigtas")
#         ivesta_neteisingai = False
#     else:
#         print("Ivedete ne ate meginkite dar karta")
 
 
# sarasas = [5,1,7,9,2,3,8]
# print(sarasas[0])
# print(sarasas[1])
# print(sarasas[2])
# print(sarasas[3])
# print(sarasas[4])
# print(sarasas[5])
# kelintas = 0
 
# while kelintas < len(sarasas):
#     print(sarasas[kelintas]) # 5,1,7,9,2,3,8
#     kelintas = kelintas + 1
 
# kelintas = 2
# while True:
#     print(kelintas)
#     kelintas = kelintas * kelintas
 
# while 1>1:
#     pass
# print("PRograma toliau tesiasi")
 
# isiaiskinti ar sarase yra skaicius 7
 
# sarasas = [5,1,30,19,500,4,7,8,2,3,8,9,10,11,12,13,14,15,16,17,18,19,20]
 
# for skaicius in sarasas:
#     print(f"Tikrinu skaiciu {skaicius}")
#     if skaicius == 7:
#         print("skaicius 7 rastas")
#         break # break nutraukia cikla ten kur jis yra parasytas
 
# print("Programa baigta")
   
 
# while True:
#     print("Ciklas veikia")
#     break
#     # if input("Iveskite savo reiksme: ") == "q":
#     #     break
#     # else:
#     #     print("Iveskite q jeigu norite baigti")
#     #     print("Tikiuosi, jums patinka si programa cia dabar daromi veiksmai...")
 
# print("programa baigta")

# # continue
 
# sarasas = [5,1,30,19,500,4,7,8,2,3,8,9,10,11,12,13,14,15,16,17,18,19,20]
 
# for skaicius in sarasas:
#     if skaicius % 2 == 0:
#         print("SKaicius lyginis")
#     else:
#         print("SKaicius nelyginis")
#         continue # continue uzbaigia dabartine iteracija ir pereina prie kitos iteracijos
#     print("Cia dar kazkokie veiksmai")
#     print("kurie atliekami tik su lyginiais skaiciais")


# sarasas = [4,1,3]
 
# kint,kint2,kint3 = sarasas # unpacking
 
 
# kint,kint2 = sarasas # unpacking
 
 
# print(kint)
 
# dictionary = {"Ugne":[9,8,10,9,10], "Mantas":[8,9,10,9,10], "Tomas":[7,8,9,8,9]} # zodynas su sarasais
# print(dictionary.items())
 
# tuplu_sarasas = [ (1,2), (3,4), (5,6), (7,8,9,12,1), (9,10)] # sarasas su tuplemis
 
# dictionary_names_lastname = {
#     "Ugne": "ugnaite",
#     "Mantas": "Mantaitis",
#     "Tomas": "Tomaitis",
#     "Justas": "Justaitis",
   
# } # zodynas su sarasais
 
# print(dictionary_names_lastname.items()) # isveda zodyna
 
# for kvp in dictionary_names_lastname.items(): # keys eina per raktus
#     print(kvp)
#     vardas, pavarde = kvp # unpacking
#     print(f"Vardas: {vardas}, Pavarde: {pavarde}") # isveda visus zodyno raktus
 
 
 
# dictionary_names_lastname = {
#     "Ugne": "ugnaite",
#     "Mantas": "Mantaitis",
#     "Tomas": "Tomaitis",
#     "Justas": "Justaitis",
   
# } # zodynas su sarasais
 
# print(dictionary_names_lastname.items()) # isveda zodyna
 
# for vardas, pavarde in dictionary_names_lastname.items(): # vardas = kvp[0] | pavarde = kvp[1]
 
#     print(f"Vardas: {vardas}, Pavarde: {pavarde}") # isveda visus zodyno raktus



 
 
 

# Sukurkite while ciklą, kuris atspausdintų skaičius nuo 1 iki 10

# kelintas = 1
# skaicius = 1
# rezultatas = 0
# while 11 > kelintas:
#     rezultatas += skaicius
#     print(rezultatas)
#     kelintas = kelintas + 1

# Sukurkite while ciklą kuris atspausdintų žodyje esančias raides po vieną
# kelintas = 0
# zodis = "kebabas"

# while kelintas < len(zodis):
#     print(zodis[kelintas])
#     kelintas = kelintas + 1


# Sukurkite for ciklą, kuris veikia tol kol sąraše randa žodį "labas" ir tada nutraukia savo veikla

# sarasas = ["bmw", "audi", "volkswagen", "labas", "kompiuteris"]


# for i in sarasas:
#     print((f"Tikrinu zodi {i}"))
#     if i == "labas":
#         print("žodis rastas")
#         break


# Atspausdinkite su for ciklu visas žodyno reikšmių poras (panaudokite items)

# zodynas = {"labas":"kojotas", "bebras":"zuikis", "vaflis":"junga"}

# for i in zodynas.items():
#     print(i)


# # Sukurkite tuple su trimis elementais ir išveskite antrą elementą.
 
# tuplas = ("labas", "zuikis", "kiskis")

# print(tuplas[1])


# Sukurkite set ir išveskite jo ilgį 
# setas = {1,1,2,2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7}
# print(len.setas())

# setas = {1,1,2,2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7}
# atrinkti = set(setas)

# print(len(atrinkti))

# vart_ivest = int(input("irasykite kiek kartu atspausdinti: "))

# nulinis = 0

# while vart_ivest > nulinis:
#     print("Sveikas, pasauli!")
#     nulinis += 1

# Parašykite programą, kuri suskaičiuoja skaičių nuo 1 iki n sumą naudodama while ciklą.
# stopas = 1
# skaicius1 = 1
# skaicius2 = int(input("iveskite iki kokios skaicio skaiciuosime: "))
# sarasas = []
# while skaicius2 > stopas:
#     rezultatas = sarasas.append(skaicius2)
#     stopas +=1
# print(sum(sarasas))


# Parašykite programą, kuri priima tris kampų dydžius ir patikrina, ar jie gali sudaryti trikampį (suma lygi 180°).

# kampas_1 = int(input("iveskite 1 kampo laipsnius: ")
# kampas_2 = int(input("iveskite 2 kampo laipsnius: ")
# kampas_3 = int(input("iveskite 3 kampo laipsnius: ")

# kampas_1,kampas_2,kampas_3 = 






