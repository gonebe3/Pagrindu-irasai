# suma = 0
# for sk in sarasas:
#     suma = suma + sk
 
# min(sarasas) - duoda maziausia skaiciu is saraso
# max(sarasas) - duoda didziausia skaiciu is saraso
# sum(sarasas) - susumuoja saraso skaicius ir atiduoda viena rezultata
# mean(sarasas) sudeda visus skaicius ir padalina is kiekio (vidurkis)
# median(sarasas) -
# from statistics import median
# sarasas = [6,1,10,8,9,2] # -> [1,2,6,8,9,10]
# print(median(sarasas))
 
 
# list comprehension - greitas saraso sudarymas
 
# sarasas = [7,5,4,2, 5 ,4, 8, 3, 11, 27, 30]
 
# # kvadratai = []
 
# # for sk in sarasas:
# #     kvadratai.append(sk**2)
 
# # print(kvadratai)
 
# kvadratai = [x**2 for x in sarasas]
# print(kvadratai)
 
# kvadratai = [x**2 for x in sarasas if x % 2 == 0]
 
# # for sk in sarasas:
#     #  if sk % 2 == 0
# #     kvadratai.append(sk**2)
 
# print(kvadratai)

# __________________
# Sukurkite sarasa is ivairaus tipo elementu privalo buti bent pora bool, bent pora int float, stringu...
 
# Pasinaudodami list comprehension ir is instance suskaičiuokite atskirai intu ir boolu kieki (int ir bool kiekis kartu)
 
# Ir apskaičiuokite stringu kieki
 
# Apskaičiuokite sąraše esančių skaičių (int, float, bool) sumą (Ne kiekį)

# sarasas = ["labas", True, 5, 12, "Ka", 7.4, 8.5, 8, "tu", False]

# print("-"*30)
# bool_kiekis = sum(type(c) is bool for c in sarasas)
# int_kiekis = sum(type(c) is int for c in sarasas) 
# print(f"Bool kiekis (type): {bool_kiekis}")
# print(f"Int kiekis (type): {int_kiekis}")
# print("-"*30)

# bool_kiekis_ins = sum(isinstance(i, bool) for i in sarasas)
# int_kiekis_ins = sum(isinstance(i, int) for i in sarasas) - bool_kiekis_ins
# print(f"Bool kiekis (isinstance): {bool_kiekis_ins}")
# print(f"Int kiekis (isinstance): {int_kiekis_ins}")
# print("-"*30)

# string_kiekis = sum(isinstance(i, str) for i in sarasas)
# print(f"String kiekis: {string_kiekis}")
# print("-"*30)

# skaiciu_suma = sum(i for i in sarasas if isinstance(i, (int, float)))
# print(f"Skaiciu suma (int, float, bool): {skaiciu_suma}")

# __________________
# Sukurti programą, kuri:
# •Sukurtų sąrašą iš skaičių nuo 0 iki 50
# •Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
# •Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
# •Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
# •Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
# •Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
 
# Patarimai:
# •Naudotimap, filter arba comprehension, sum, min, max, mean, median, %
# •from statistics import mean, median

# sarasas = list(range(51))

# padauginimas_x10 = [x * 10 for x in sarasas]

# print("-"*20)
# print(f"Padauginimas is 10: {padauginimas_x10}")
# print("-"*20)
# ar_dalinasi_is7 = [x for x in sarasas if x % 7 == 0]

# print(f"Skaiciai, kurie dalinasi is 7: {ar_dalinasi_is7}")
# print("-"*20)
# kvadratu = [x**2 for x in sarasas]

# print(f"Skaiciai kvadratu: {kvadratu}")
# print("-"*20)

# from statistics import mean, median

# suma = sum(kvadratu)
# print(f"suma kvadratu: {suma}")
# print("-"*20)
# maziausia = min(kvadratu)
# print(f"Maziausias: {maziausia}")
# print("-"*20)
# didziausia = max(kvadratu)
# print(f"Didziausias: {didziausia}")
# print("-"*20)
# vidurkis = mean(kvadratu)
# print(f"Vidurkis: {vidurkis}")
# print("-"*20)
# mediana = median(kvadratu)
# print(f"Mediana: {mediana}")
# print("-"*20)
# sortiruoti_kvadratai = sorted(kvadratu, reverse=True)
# print(f"Sortiruoti atbulai kvadratai: {sortiruoti_kvadratai}")
# print("-"*20)

# __________________
# Duotas sąrašas: sarasas= [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# Sukurti programą, kuri:
# •Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
# •Sudėtųiratspausdintų visus sąrašo žodžius
# •Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su Truereikšme
 
# Patarimai:
# •Naudotifilterarba comprehension,sum, " ".join()

# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras", False]

# skaiciu_suma = sum(x for x in sarasas if type(x) in (int, float))
# print("-"*50)
# print(f"skaiciu suma: {skaiciu_suma}")

# tekstai = " ".join(x for x in sarasas if isinstance(x, str))
# print("-"*50)

# print(f"Sujungti tekstai: {tekstai}")

# true_kiekis = sum(1 for x in sarasas if isinstance(x, bool) and x is True)
# true_kiekis = sum(x for x in sarasas if isinstance(x, bool))
# print("-"*50)
# print(f"True kiekis: {true_kiekis}")
# print("-"*50)

# ____________________________________
# Sukurti programą, kuri:
# •Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# •Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
# •Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# •Įdėti sukurtus Zmogus objektus į naują sąrašą
# •Surūšiuotųiratspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
 
# Patarimai:
# •Naudotisorted, attrgetter, reverse, funkciją repr
# •from operator import attrgetter

class Zmogus():
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius
    
    def __repr__(self):
        return f"{self.vardas}({self.amzius} m.)"
    
zm1 = Zmogus("Antanas",30)
zm2 = Zmogus("Neringa", 19)
zm3 = Zmogus("Zigfridas", 98)

zmones = [zm1, zm2, zm3]

from operator import attrgetter

pagal_varda = sorted(zmones, key=attrgetter("vardas"))
print("-"*50)
print(pagal_varda)

pagal_amzius = sorted(zmones, key=attrgetter("amzius"))
print("-"*50)
print(pagal_amzius)

atbulai_pagal_amziu = sorted(zmones, key=attrgetter("amzius"), reverse=True)
print("-"*50)
print(atbulai_pagal_amziu)
print("-"*50)

print("labas")