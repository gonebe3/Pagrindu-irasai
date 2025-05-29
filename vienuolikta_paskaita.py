# def skaiciavimo_funkcija(skaicius,daugiklis=1,pridetis=0,nebutinas=4):
#     return (skaicius * daugiklis) + pridetis
 
 
# print(skaiciavimo_funkcija(7))
 
# def neribota_suma(*skaiciai): # is esmes zvaigzdute tiesiog sukuria tupla, kurioje yra visi argumentai | skaiciai = [9,4,5,8,7,89,5,4,5,1,4,8,6]
#     """
#     Funkcija, kuri priima neribotą skaičių argumentų ir grąžina jų sumą.
 
#     :param skaiciai: Neribotas skaičių kiekis.
#     :return: Skaičių suma.
#     """
#     suma = 0
#     for skaicius in skaiciai:
#         suma += skaicius
#     return suma
 
# print(neribota_suma(9,4,5,8,7,89,5,4,5,1,4,8,6))
 
# def neribota_suma(skaiciai): # is esmes zvaigzdute tiesiog sukuria tupla, kurioje yra visi argumentai | skaiciai = [9,4,5,8,7,89,5,4,5,1,4,8,6]
#     """
#     Funkcija, kuri priima neribotą skaičių argumentų ir grąžina jų sumą.
 
#     :param skaiciai: Neribotas skaičių kiekis.
#     :return: Skaičių suma.
#     """
#     suma = 0
#     for skaicius in skaiciai:
#         suma += skaicius
#     return suma
 
# print(neribota_suma([9,4,5,8,7,89,5,4,5,1,4,8,6]))
 
# def spausdinti_neribota_teksta(**tekstas): # **tekstas = {'vardas': 'Jonas', 'pavarde': 'Jonaitis'}
#     """
#     Funkcija, kuri spausdina neribotą skaičių argumentų.
 
#     :param tekstas: Neribotas skaičių argumentų kiekis.
#     """
#     for raktas, reiksme in tekstas.items():
#         print(f'{raktas}: {reiksme}')
 
 
# spausdinti_neribota_teksta(vardas='Jonas', pavarde='Jonaitis', amzius=30, miestas='Vilnius')
 
# def spausdinti_neribota_teksta(tekstas): # **tekstas = {'vardas': 'Jonas', 'pavarde': 'Jonaitis'}
#     """
#     Funkcija, kuri spausdina neribotą skaičių argumentų.
 
#     :param tekstas: Neribotas skaičių argumentų kiekis.
#     """
#     for raktas, reiksme in tekstas.items():
#         print(f'{raktas}: {reiksme}')
 
 
# spausdinti_neribota_teksta({'vardas': 'Jonas', 'pavarde': 'Jonaitis', 'amzius': 30, 'miestas': 'Vilnius'})
 
# def neribota_suma(*skaiciai,daugiklis): # is esmes zvaigzdute tiesiog sukuria tupla, kurioje yra visi argumentai | skaiciai = [9,4,5,8,7,89,5,4,5,1,4,8,6]
#     """
#     Funkcija, kuri priima neribotą skaičių argumentų ir grąžina jų sumą.
 
#     :param skaiciai: Neribotas skaičių kiekis.
#     :return: Skaičių suma.
#     """
#     suma = 0
#     for skaicius in skaiciai:
#         suma += skaicius * daugiklis
#     return suma
 
# print(neribota_suma(9,4,5,8,7,89,5,4,5,1,4,8,6,daugiklis=2))


# def sumuoti(skaiciu_sarasas):
#     """
#     Funkcija, kuri apskaičiuoja sumą.
 
#     :param skaiciai: Neribotas skaičių kiekis.
#     :return: Suma.
#     """
#     suma = 0
#     for skaicius in skaiciu_sarasas:
#         suma += skaicius
#     return suma
 
# def vidurkis(*skaiciai):
#     """
#     Funkcija, kuri apskaičiuoja vidurkį.
 
#     :param skaiciai: Neribotas skaičių kiekis.
#     :return: Vidurkis.
#     """
#     grazinta_suma = sumuoti(skaiciai)
#     kiekis = len(skaiciai)
#     return grazinta_suma / kiekis if kiekis > 0 else 0
 
# print(sumuoti([1, 2, 3, 4, 5])) # 15
# print(vidurkis(1, 2, 3, 4, 5)) # 3.0


# def kubu(skaicius):
#     return skaicius ** 3
 
 
# funkcijos_kint = lambda skaicius: print(skaicius ** 3 * 5 + 2)
 
 
# funkcijos_kint(5)
# funkcijos_kint(5)
 
# import time
 
# sarasas = range(1,20000)
 
# start = time.perf_counter()
 
# naujas_sarasas = []
 
# for i in sarasas:
#     naujas_sarasas.append(i ** 2)
 
# # print(naujas_sarasas)
 
# end = time.perf_counter()
# print(f'for ciklas uztruko {(end - start)*1000} ms.')
 
# start = time.perf_counter()
# naujas_map_sarasas = list(map(lambda x: x ** 2, sarasas)) # tas pats kas for ciklas, tik trumpesnis plius lambada funkcija,
# # print(naujas_map_sarasas)
   
# end = time.perf_counter()
# print(f'map uztruko {(end - start)*1000} ms.')



# ____________________________________________________________
# 1.Gražinti trijų paduotų skaičių sumą.

# def suma(a,b,c):
#     return a+b+c

# print(suma(1,2,3))

# ____________________________________________________________
# 2.Gražintų paduoto sąrašo iš skaičių, sumą.

# def saraso_suma(*a):
#     rezultatas = 0
#     for i in a:
#         rezultatas += i
#     return rezultatas

# print(saraso_suma(1,2,3,4,5))

# ____________________________________________________________
# 3.Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).

# def didziausias_skaicus(*a):
#     didziausias = a[0]
#     for i in a:
#         if i > didziausias:
#             didziausias = i
#     return didziausias

# print(didziausias_skaicus(1,2,5,8,7,125))

# ____________________________________________________________

# 4.Gražintų paduotą stringą atbulai.

# def tekstas_atbulai(tekstas):
#     return tekstas[::-1]

# print(tekstas_atbulai("labas"))


# ____________________________________________________________

# 5.Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.

# def ivesites_analizatorius(tekstas):
#     zodziu_kiekis = len(tekstas.split())
#     didziosios_raides = 0
#     mazosios_raides = 0
#     skaiciu_kiekis = 0

#     for i in tekstas:
#         if i.isupper():
#             didziosios_raides += 1
#         elif i.islower():
#             mazosios_raides += 1
#         elif i.isdigit():
#             skaiciu_kiekis += 1 

#     print(f"zodziu: {zodziu_kiekis}")
#     print(f"didziuju raidziu: {didziosios_raides}")
#     print(f"mazuju raidziu {mazosios_raides}")
#     print(f"skaiciu: {skaiciu_kiekis}")

# ivesites_analizatorius("labas kebabas 3 Sabonis")

# ____________________________________________________________

# 6.Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.

# def unikalus_elementai(sarasas):
#     return list(set(sarasas))

# print(unikalus_elementai([1, 2, 2, 3, 3, 3, 3, 4, 4, 5])) 


# ____________________________________________________________

# 7.Gražintų, ar paduotas skaičius yra pirminis.

# Pirminis skaičius – bet kuris natūralusis skaičius, didesnis nei 1, kuris dalinasi tik iš savęs ir vieneto. 
# Vienetas nelaikomas nei pirminiu skaičiumi, nei sudėtiniu, kartais dar vadinamas neutraliuoju dauginamuoju, kadangi yra kiekvieno skaičiaus skaidinyje

# def ar_pirminis_skaicius(skaicius):
#     if skaicius < 2:
#         return "Skaicius nera pirminis"
#     for i in range(2, int(skaicius ** 0.5) + 1):
#         if skaicius % i == 0:
#             return "skaicius nera pirminis"
#     return "skaicius yra pirminis"

# print(ar_pirminis_skaicius(7))
# ____________________________________________________________

# 8.Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

# def atvirkstinis_surasymas(stringas):
#     zodziai = stringas.split(" ")
#     iskrikiavimas = ""
    
#     for zodis in zodziai[::-1]:
#         iskrikiavimas += zodis + " "
    
#     return iskrikiavimas

# Lengvesnis budas
def atvirkstinis_surasymas(stringas):
    zodziai = stringas.split(" ")
    
    return ".".join(zodziai[::-1])

print(atvirkstinis_surasymas("labas kebabas"))


# ____________________________________________________________

# 9.Gražina, ar paduoti metai yra keliamieji, ar ne.

# def ar_keliamieji(metai):
#     if metai % 4 == 0 and metai % 100 != 0 or metai % 400 == 0: 
#         return print("Keliamieji")
#     else:
#         return print("nekeliamieji")

# ar_keliamieji(1600)


# ____________________________________________________________

# 10.Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.


# from datetime import datetime

# def nuo_sukakties(data):
#     siandien_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     siandien = datetime.strptime(siandien_str, "%Y-%m-%d %H:%M:%S")
#     laikas_nuo_sukakties = siandien - data
#     return laikas_nuo_sukakties


# import datetime

# siandien = datetime.today()

# print(siandien)
#  mano_data.strftime("%B %A")

# # text = "2023-10-01 12:00:00"

# # data = datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S")


# ____________________________________________________________
# 1.Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.





# ____________________________________________________________
# 2.Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau sukurtą funkciją) pagal įvestą lytį, gimimo datą ir eilės numerį).


39907140171

# 1 SK = 3 - šimtmetį ir asmens | 1 - 1800 gimes vyras, 2 moteris | 3-1900 vyras, 4-moteris | 5-2000 vyras, 6-moteris 
# 2-7 SK = metu, men, ir dienu paskutiniai skaiciai
# 8-10 SK = Eiles nr
# 11 = Kontrolinis (S = A*1 + B*2 + C*3 + D*4 + E*5 + F*6 + G*7 + H*8 + I*9 + J*1)/11 % == 10 then its it. 
# If not, then again /11 % == 10, 
# if not then again, but (A*3 + B*4 + C*5 + D*6 + E*7 + F*8 + G*9 + H*1 + I*2 + J*3) /11 % == 10
# if not then its 0.

# from datetime import datetime

# def kontrolinis_sk(pirmi_10):
#     sk = [int(s) for s in pirmi_10]

#     daugyba_is1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

#     galimas1 = sum(sk[i] * daugyba_is1[i] for i in range(10)) % 11
#     if galimas1 != 10:
#         return galimas1
       
#     daugyba_is2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

#     galimas2 = sum(sk[i] * daugyba_is2[i] for i in range(10)) % 11
#     if galimas2 != 10:
#         return galimas2


# def ak_kurimas(lytis,gimimo_data,eiles_nr=0):
#     sk_1 = 0
#     konvert_data = data_objektas = datetime.strptime(gimimo_data, "%Y-%m-%d")
#     if konvert_data < datetime(1900, 1, 1):
#         if lytis == "vyras":
#             sk_1 = 1
#         elif lytis == "moteris":
#             sk_1 = 2
#     elif datetime(1900, 1, 1) < konvert_data < datetime(2000, 1, 1):
#         if lytis == "vyras":
#             sk_1 = 3
#         elif lytis == "moteris":
#             sk_1 = 4
#     elif konvert_data > datetime(2000, 1, 1):
#         if lytis == "vyras":
#             sk_1 = 5
#         elif lytis == "moteris":
#             sk_1 = 5
#     sk_2 = f"{konvert_data.year % 100:02}"
#     sk_3 = f"{konvert_data.month:02}"
#     sk_4 = f"{konvert_data.day:02}"
#     sk_5 = f"{eiles_nr:03}"

#     pirmi_10 = f"{sk_1}{sk_2}{sk_3}{sk_4}{sk_5}"
#     sk_6 = kontrolinis_sk(pirmi_10)

#     galutinis_ak = pirmi_10 + str(sk_6)
#     return galutinis_ak

# lyt = input("Iveskite savo lyti (vyras ar moteris): ")
# vart_met = input("Iveskite savo gimimo data pvz.: 1999-07-14 : ")

# print(ak_kurimas(lyt,vart_met))
      
# ____________________________________________________________


# def grazinti_asmens_kodo_kontrolinį(asmens_kodas):
#     kodas = str(asmens_kodas)
#     A = int(kodas[0])
#     B = int(kodas[1])
#     C = int(kodas[2])
#     D = int(kodas[3])
#     E = int(kodas[4])
#     F = int(kodas[5])
#     G = int(kodas[6])
#     H = int(kodas[7])
#     I = int(kodas[8])
#     J = int(kodas[9])
#     S = A * 1 + B * 2 + C * 3 + D * 4 + E * 5 + F * 6 + G * 7 + H * 8 + I * 9 + J * 1
#     if S % 11 != 10:
#         return S % 11
#     else:
#         S = A * 3 + B * 4 + C * 5 + D * 6 + E * 7 + F * 8 + G * 9 + H * 1 + I * 2 + J * 3
#         if S % 11 != 10:
#             return S % 11
#         else:
#             return 0
 
 
# def asmens_kodo_validacija(asmens_kodas):
#     paskutinis_sk = int(str(asmens_kodas)[-1])
#     return paskutinis_sk == grazinti_asmens_kodo_kontrolinį(asmens_kodas)
 
 
# def asmens_kodo_generavimas(lytis, gimimo_data, eiles_numeris):
#     pirmas_skaicius = ""
 
 
#     data_split = gimimo_data.split("-") # ["2000", "12", "12"]
#     metai = int(data_split[0][:2]) # 20
 
#     if lytis == "vyras":
#         pirmas_skaicius = str((int(metai) - 18) * 2 + 1)
#     else:
#         pirmas_skaicius = str((int(metai) - 18) * 2 + 2)
 
#     metai = data_split[0][2:] # 00
#     menuo = data_split[1] # 12
#     diena = data_split[2] # 12
 
#     be_paskutinio = pirmas_skaicius + metai + menuo + diena + eiles_numeris # 5001212512
 
#     return int(be_paskutinio + str(grazinti_asmens_kodo_kontrolinį(be_paskutinio)))
 
 
# print(asmens_kodo_validacija(45102129987))
# print(asmens_kodo_validacija(61907108400))
 
# print(asmens_kodo_generavimas("vyras", "2000-12-12", "512"))



# ______________________________________________________________________________________________________________
# 1.Sukurti funkciją, kuri grąžintų True reikšmę, jei įvesto skaičiaus pirma skaitmenų pusė yra lygi antrąjai, priešingu atveju grąžintų False. # 1569 | 1+5 = 6 ir 6+9 = 15

# def lyginimas(skaiciai):
#     skaiciai_konvert = str(skaiciai)
#     skaiciu_kiekis = len(skaiciai_konvert)
#     sk1 = []
#     sk2 = []

#     if skaiciu_kiekis % 2 == 0:
#         puse = skaiciu_kiekis // 2
#         pirma_dalis = sk1[:puse]
#         antra_dalis = sk2[puse:]
#         pirma_sum = sum(int(sk1))
#         antra_sum = sum(int(sk2))
#         if pirma_sum == antra_sum:
#             return True
#         else:
#             return False
#     else:
#         raise ValueError("Neimanoma palyginti, kadangi nurodete nelygini skaiciu")
#         return ValueError
    
# lyginimas(545687)


# ______________________________________________________________________________________________________________

# 2.Parašyti funkciją, kuri grąžintų, kiekvieno elemento gretimą skaičių. Pvz:
#       Input: 56789
#       Output: 5 – 46, 6 – 57, 7 – 68, 8 - 79, 9 - 8






































