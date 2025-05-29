# bool tipo kintamasis
# bool_tipo = 5==5 # = - priskiria | == klausia ar lygu
 
# print(bool_tipo)
 
# bool_tipo = 4>=5 # = - priskiria | == klausia ar lygu
 
# print(bool_tipo)
 
# bool_tipo = (4>=5) or (5 > 7 and 4 > 5) # = and reiskia abi salygos teisingos | or bent viena teisinga
 
# print(bool_tipo)
 
# if - salygos sakinys
 
# skaicius = int(input("Iveskite savo skaiciu: "))
 
# if skaicius > 1:  # po dvitaskio pythone visados eina atitrauktos eilutes
#     print("Labas") # atitrauktos eilutes yra vykdomos tik tada jeigu salyga yra teisinga
#     print("Tavo ivestas skaicius yra daugiau uz 1")
#     print("Labas")
 
# print("Programa baigta")
 
 
# amzius = int(input("Iveskite savo amziu: "))
 
# if amzius >= 18:
#     print("Gali nusipirkti energetini gerima")
 
# if amzius >= 20:
#     print("Gali nusipirkti ir salto gerimo")
 
# if amzius >= 65:
#     print("Tu esi pensininkas")
 
# amzius = int(input("Iveskite savo amziu: "))
# stazas = int(input("Iveskite savo staza (metais): "))
 
# if amzius >= 18:
#     print("Gali nusipirkti energetini gerima")
 
# if amzius >= 20:
#     print("Gali nusipirkti ir salto gerimo")
 
# if amzius >= 65:
#     print("Tu esi pensininkas")
#     if stazas > 10: # jeigu apgaubiantis ifas yra netiesa, vidinis yra net netikrinamas
#         print("jus gaunate pensija")
#     # print("Grizome i pirma ifa")
 
 
# amzius = int(input("Iveskite savo amziu: "))
 
# if amzius >= 65: # tikrinama ar tiesa
#     print("Tu esi pensininkas")
# else: # jeigu netiesa ivyksta else
#     print("Tu nesi pensininkas")
 
 
 
# if "LABAs".isupper():
#     print("visas tavo zodis yra didziosiomis raidemis")
 
# ivestis = input("Iveskite skaiciu: ")
 
# if ivestis.isdigit():
#     print("Aciu ivedete teisingai")
#     suma = 5 + int(ivestis) # tai dabar garantuoju sau, kad nebus klaidos ir visad teisingai paversime i int
# else:
#     print("ivedete arba ne skaiciu arba ne teigiama sveika skaiciu")


# NAMU DARBAI 


#     # Parašyti programą, kuri:
# •Leistų įvesti skaičius a ir b (int arba float)
# •Išvestų į ekraną „a mažesnis už b“, jei taip yra
# •Išvestų į ekraną „a lygu b“, jei taip yra
# •Išvestų į ekraną „a didesnis už b“, jei taip yra
# Patarimas: naudoti if, else sąlygas

#Atlikta UZD

# pirmas_skaicius = int (input("įveskite pirmą skaičių:"))

# antras_skaicius = int (input("įveskite antrą skaičių: "))

# if pirmas_skaicius > antras_skaicius:
#     print("Pirmas skaičius yra didesnis už antrą")
# if pirmas_skaicius < antras_skaicius:
#     print("antras skaičius yra didesnis už pirmą")
# if pirmas_skaicius == antras_skaicius:
#     print("Pateikti skaiciai yra lygus")


# Parašyti programą, kuri:
# •Leistų įvesti pirmą skaičių
# •Leistų įvesti antrą skaičių
# •Paklaustų, kokį matematinį veiksmą reiktų atliktų (Pradžioje +,-,/,* kai pavyks pridėkite ir kėlima laipsniu, kas nori savarankiškai, dar pridėkite ir šaknies traukimą)
# •Atspausdintų rezultatą: pasirinktų skaičių suma, daugybą ar pan.
# Patarimas: naudoti input(), if, print,

# pirmas_skaicius = int (input("įveskite pirmą skaičių:"))

# antras_skaicius = int (input("įveskite antrą skaičių: "))

# uzduotis = (input("įveskite kokį matematinį veiksmą reiktų atlikti (+,-,/,*): "))

# if uzduotis=:
#     atsakymas = (pirmas_skaicius+antras_skaicius)
#     print("Atsakymas lygu: ")

# amzius = int(input("Iveskite savo amziu: "))
 
# if amzius > 65: # sitas patikrinamas visada
#     print("Tu esi pensininkas")
# elif amzius > 20: # sitas tikrinamas tik jeigu pirmas yra netiesa
#     print("Gali nusipirkti ir salto gerimo")
# elif amzius > 18: # sitas tikrinamas tik jeigu pirmas ir antras yra netiesa
#     print("Tu gali nusipirkti energetini gerima")
# else: # jeigu visi trys netiesa
#     print("nezinau ka su tavimi daryti")
 
 
 
# if amzius > 65: # sitas patikrinamas visada
#     print("Tu esi pensininkas")
# if amzius > 20: # sitas tikrinamas tik jeigu pirmas yra netiesa
#     print("Gali nusipirkti ir salto gerimo")
# if amzius > 18: # sitas tikrinamas tik jeigu pirmas ir antras yra netiesa
#     print("Tu gali nusipirkti energetini gerima")
# else: # jeigu visi trys netiesa
#     print("nezinau ka su tavimi daryti")

















