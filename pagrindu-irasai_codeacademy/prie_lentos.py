# import datetime
# import pickle
# import os
 
# class Studentas():
#     def __init__(self, vardas, pavarde, pazymiai, gimimo_data):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pazymiai = pazymiai
#         self.gimimo_data = gimimo_data
 
#     def __str__(self):
#         return f"{self.vardas} {self.pavarde} {self.pazymiai} {self.gimimo_data}"
    
#     def pazymiu_vidurkis(self):
#         suma = 0
#         for i in self.pazymiai:
#             suma += i
#         vidurkis = suma / len(self.pazymiai)
#         return vidurkis

# def ivesties_nuskaitymas(kelias):
#     try:
#         with open (kelias, "rb") as failas:
#             duomenys = pickle.load(failas)
#             return duomenys
#     except FileNotFoundError:
#         return []
 
# def ivesties_issaugojimas(kelias, data):
#     with open (kelias, "wb") as failas:
#         pickle.dump(data,failas)
#     print("Įvestis išsaugota ")
 
# def naujas_studentas(vardas, pavarde,pazymiai,gimimo_data):
#     stud = Studentas(vardas,pavarde,pazymiai,gimimo_data)
#     return stud
 
 
 
# def ivesti_studentai(studentai):
#     while True:
#         naujas_vardas = input("Įveskite studento vardą: ")
#         nauja_pavarde = input("Įveskite studento pavardę: ")
#         pazymiai = pazymiu_ikrovimas()
#         nauja_gim_data = input("Įveskite studento gimimo datą: ")
#         gimimo_data = datetime.datetime.strptime(nauja_gim_data, "%Y-%m-%d")
 
#         naujas_1 = naujas_studentas(naujas_vardas,nauja_pavarde,pazymiai,gimimo_data)
#         studentai.append(naujas_1)
 
#         klausimas = input("Ar norite įvesti dar vieną studentą (Y/N): ")
#         if klausimas== "Y":
#             continue
#         elif klausimas=="N":
#             break
#         else:
#             print("Bloga įvestis, bandykite dar kartą. ")
#     return studentai

# def pazymiu_ikrovimas():
#     pazymiai = []
#     for _ in range(5): # range(5) --> [0,1,2,3,4]
#         pazymys = int(input("Įveskite pažymį(iš viso 5 pažymius): "))
#         pazymiai.append(pazymys)
#     return pazymiai

# def studentu_atvaizdavimas(studentai):
#     for i in studentai:
#         print(i)
#         print(f"Studento pazymiu vidurkis: {i.pazymiu_vidurkis()}")


    
 
# studentai = []

# def vidurkiu_sukelimas(studentai):
#     vidurkiai = {}
#     for i in studentai:
#         vidurkiai[i.vardas] = i.pazymiu_vidurkis()
#     return vidurkiai


# def dvi_max(vidurkiai):
#     sortiravimas = sorted(vidurkiai.items(), key=lambda item: item[1], reverse=True)[:2]
#     return sortiravimas

# ivesti_studentai(studentai)


# kelias = "duomenys.pickle"
# ivesties_issaugojimas(kelias,studentai)

# studentu_atvaizdavimas(studentai)

# vidurkiai = vidurkiu_sukelimas(studentai)

# print(dvi_max(vidurkiai))

# # sorted(x.items(), key=lambda item: item[1], reverse.top2)



# Parašyk funkciją sveikinu(vardas), kuri atspausdintų „Labas, {vardas}!“.

# def sveikinu(vardas):
#     print(f"Labas, {vardas}!")

# vardas = input("Iveskite savo varda: ")
# sveikinu(vardas)

# _______________________________________________
# Sukurk sąrašą su sveikaisiais skaičiais nuo 1 iki 10 ir atspausdink kiekvieną elementą for ciklu.

# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in sarasas:
#     print(i) 

# _______________________________________________
# Parašyk funkciją daugyba(a, b), kuri gražintų a * b.



# def vart_ivestis():
#     try:
#         a = float(input("Iveskite pirma skaiciu: "))
#         b = float(input("Iveskite antra skaiciu: "))
#         return a, b
#     except ValueError:
#         print("Ivedete ne skaicius.")
#         return None, None

# def daugyba(a, b):
#     rezultatas = 0
#     try:
#         return a * b
#     except Exception as e:
#         print(f"Ivyko nenumatyta klaida {e}, bandykite dar karta")
#         return None

# def paleidimas():
#     while True:
#         a, b = vart_ivestis()
#         if a is None or b is None:
#             print("Pandykite dar karta, ivedete ne skaicius.")
#             continue
        
#         rezultatas = daugyba(a, b)
#         if rezultatas is not None:
#             print(f"Rezultatas: {rezultatas}")
#         else:
#             print("Skaiciavimas nepavyko.")

#         break
    
# paleidimas()

# __________________________________________________________________________
# Sukurk skaičių nuo vartotojo ir patikrink, ar tai lyginis (naudojant %).

# def ar_lyginis(skaicius):
#     try: 
#         if skaicius % 2 == 0:
#             return f"{skaicius} yra lyginis"
#         else:
#             return "skaicius yra nelyginis"
#     except Exception as e:
#        return f"Ivyko nenumatyta klaida {e}, bandykite dar karta"

# try:
#     skaicius = int(input("Iveskite skaiciu: "))
#     print(ar_lyginis(skaicius))
# except ValueError:
#     print("Ivedete neteisingai, bandykite dar karta")

# __________________________________________________________________________
# Parašyk while ciklą, kuris skaičiuoja nuo 5 iki 1 atbuline tvarka.

# def skaiciuoti_atbulai():
#     skaicius = 5
#     while skaicius >= 1:
#         print(skaicius)
#         skaicius -= 1

# skaiciuoti_atbulai()

# __________________________________________________________________________
# Parašyk funkciją sumuoti_skaicius(n), kuri susumuotų skaičius nuo 1 iki n.

# def sumuoti_skaicius(n):
#     rezultatas =0
#     for i in range(1,n+1):
#         rezultatas += i
#     return rezultatas

# n = int(input("Iveskite skaiciu iki kuriuo sumuosime: "))
# print(sumuoti_skaicius(n))

# __________________________________________________________________________
# Iš sąrašo ['a', 'b', 'c', 'd'] sukurk naują eilutę „abcd“ naudojant join().

# def saraso_apjungimas(sarasas):
#     return ''.join(sarasas)

# sarasas = ['a', 'b', 'c', 'd']
# print(saraso_apjungimas(sarasas))


# __________________________________________________________________________
# Sudėk du sąrašus [1,2,3] ir [4,5,6] į vieną.

# def saraso_sujungimas(a, b):
#     return a + b

# pirmas_sarasas = [1,2,3]
# antras_sarasas = [4,5,6]
# print(saraso_sujungimas(pirmas_sarasas, antras_sarasas))

# __________________________________________________________________________
# Paprašyk vartotojo įvesti žodį ir patikrink ar jis yra palindromas.

# def ar_palindromas(zodis):
#     zodis = zodis.lower()
#     atvirsciai = zodis[::-1]
#     if zodis == atvirsciai:
#         print(f"Zodis {zodis} yra palindromas")
#     else:
#         print(f"Zodis {zodis} yra ne palindromas ")

# zodis = input("Iveksite zodi, kuri tikrinsime: ")
# ar_palindromas(zodis)

# __________________________________________________________________________
# Sukurk žodyną su raktu „vardas“ ir savo vardu kaip reikšme, atspausdink reikšmę.

# zodynas = {"vardas":"Dominik"}

# print(zodynas["vardas"])

# __________________________________________________________________________
# Parašyk funkciją maksimalus(a, b, c), kuri gražintų didžiausią iš trijų skaičių.

# def maksimalus(a, b, c):
#     sarasas = [a, b, c]
#     didziausias = sarasas[0]
#     for i in sarasas:
#         if i >= didziausias:
#             didziausias = i
#     return didziausias

# print(maksimalus(2, 8, 10))

# __________________________________________________________________________
# Išvesk sveikinimą su dabartine data (naudok modulį datetime).

# from datetime import datetime
# dabar = datetime.now()
# print(f"Sveiki! siandienos data yra {dabar.date()}")

# __________________________________________________________________________
# Sugeneruok 5 atsitiktinius skaičius nuo 1 iki 100 ir atspausdink juos (naudok random).
# import random
# for _ in range(5):
#     skaicius = random.randint(1, 100)
#     print(skaicius)

# __________________________________________________________________________
# Iš teksto eilutės atskirk žodžius į sąrašą naudojant split().

# def is_teksto_i_sarasas(tekstas):
#     return tekstas.split()

# print(is_teksto_i_sarasas("Labas, as esu Dominik"))

# __________________________________________________________________________

# Parašyk funkciją factorial(n), kuri apskaičiuotų n! (naudodamas for arba while).

# def faktorial(n):
#     rezultatas = 1
#     for i in range(1, n+1):
#         rezultatas *= i
#     return rezultatas

# print(faktorial(5))