# import datetime

import datetime


# # siandien = datetime.datetime.today()
# # siandien_data = datetime.date.today()
# # siandien_laikas = datetime.datetime.today().time()

# # print(siandien)
# # print(siandien_data)
# # print(siandien_laikas)
# # print("" + "-" * 20)

mano_data = datetime.datetime(2023, 10, 1, 12, 0, 0)

print(mano_data.strftime("%B %A"))


# # text = "2023-10-01 12:00:00"

# # data = datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S")



# # print(data.year)




# print("tekstas ", str(type(text)))
# print("data " + str(type(data)))

# # print(data)

# text = input("Iveskite data(yyyy-mm-dd): ")
# # metai = int(input("Iveskite data(yyyy): "))
# # menesis = int(input("Iveskite data(mm): "))
# # diena = int(input("Iveskite data(dd): "))


# # print(metai, menesis, diena)
# data = datetime.datetime.strptime(text, "%Y-%m-%d")

# # print(type(text))
# # print(type(data))

# # print(data)
# # print(data.year)    

# skirtumas = datetime.datetime.now() - data

# print("Skirtumas: ", type(skirtumas))
# print(skirtumas.days)


# _____________________________________________________________
# TRY and Expect
# _____________________________________________________________

# import datetime
 
# while True:
#     try:
#         metai = int(input("Iveskite data(yyyy): "))
#         print(metai)
#         # test = 10 / 0  # sulus nes negalima dalyba is nulio
 
#         # text = "sdfsdf"+ type("text")
#         break
#     except ValueError:
#         print("Iveskite teisinga data")
#     except ZeroDivisionError:
#         print("Negalima dalinti is nulio")
#     except Exception as e:
#         print("Ivyko klaida: ", e)

# try:
#     date = datetime.datetime(metai, 10, 1, 12, 0, 0)
#     print(date.strftime("%B %A"))
# except ValueError:
#     print("Iveskite teisinga data")
 
 
 
# try:
#     test = 10 / 0
# except Exception as e:
#     print(e)
 
#     tracebackas = traceback.extract_tb(e.__traceback__)
#     print(tracebackas)
 
#     for i in tracebackas:
#         print(i.lineno, i.line)
 
# try:
#     skaicius = int(input("Iveskite procentus(0 - 100): "))
#     if skaicius < 0:
#         raise ValueError("Skaicius negali buti neigiamas")
   
#     if skaicius > 100:
#         raise ValueError("Skaicius negali buti daugiau negu 100")
   
#     print("Skaicius: ", skaicius)
   
# except ValueError as e:
#     print("Klaida: ", e)
 
 
 
# while True:
#     try:
#         metai = int(input("Iveskite data(yyyy): "))
#         print(metai)
#         test = 10 / 0
#         break
#     except Exception:
#         print("Iveskite teisinga data")


# Parašyti programą, kuri:
# Leistų vartotojui įvesti sveiką skaičių.
# Atspausdinti True, jei skaičius teigiamas
# Atspausdinti False, jei skaičius neigiamas ar lygus 0
# True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį ar skaicius teigiamas
# Patarimas: naudoti input, boolean, if/else


# Sukurkite sąrašą iš kelių skirtingų tipų elementų string, bool, int, float (galite įterpti ir daugiau tipų), sukurkite ciklą kuris paimtų visus skaičius (int ir float) ir išvestų jų sumą.

# sarasas = [5, 7.5, "laba diena", True, False, 15, 8.5]
# rezultatas = 0
# for i in sarasas:
#     if type(i) == int or type(i) == float:
#         rezultatas += i
# print(rezultatas)

# Parašyti programą, kuri:
# Leistų vartotojui įvesti sveiką skaičių.
# Atspausdinti True, jei skaičius teigiamas
# Atspausdinti False, jei skaičius neigiamas ar lygus 0
# True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį ar skaicius teigiamas
# Patarimas: naudoti input, boolean, if/else

# vart_ivest = int(input("Iveskite sveika skaiciu: "))

# if vart_ivest > 0:
#     vart_ivest = True
#     print(vart_ivest)
# else:
#     vart_ivest = False
#     print(vart_ivest)

# Parašyti programą, kuri:
# • Atspausdintų dabartinę datą ir laiką
# • Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# • Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# • Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)

# import datetime
# from datetime import timedelta

# siandien = datetime.datetime.today()
# print(siandien)

# nauja_data = siandien - timedelta(days=5) 
# print(f"nauja data: {nauja_data}")

# tinkamas_formatas = nauja_data.strftime("%Y-%m-%d, %H:%M:%S")
# print(f"tinkamas formatas: {tinkamas_formatas}")

# Parašyti programą, kuri:
# • Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
# • Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
# • Metų
# • Mėnesių
# • Dienų
# • Valandų
# • Minučių
# • Sekundžių
# • Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
# Patarimas: naudoti datetime, days, total_seconds()
# Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje):
# skaicius = 4.66
# print(round(skaicius))

# import datetime

# vart_ivest = input("Iveskite savo gimimo data ir laika (YYYY-MM-DD, HH:MM:SS): ")
# data_formatuota = datetime.datetime.strptime(vart_ivest, "%Y-%m-%d, %H:%M:%S")
# data_dbr = datetime.datetime.today()

# rezultatas = data_dbr - data_formatuota
# print(f"Nuo jūsų gimimo datos praėjo metu: {round(rezultatas.days/365)}")
# print(f"Nuo jūsų gimimo datos praėjo menesiu: {round(rezultatas.days/30.43)}")
# print(f"Nuo jūsų gimimo datos praėjo dienu: {rezultatas.days}")
# print(f"Nuo jūsų gimimo datos praėjo sekundziu: {round(rezultatas.total_seconds())}")



#  Užduotis nr. 4
#  Pakeisti 1 ir 3 užduotis taip, kad neteisingai įvedus duomenis ar įvykus klaidoms, programos mestų norimas klaidas lietuvių kalba
#  (panaudoti try/except)

# 1 uzduotis turbinimas
# while True:
#     try:
#         vart_ivest = int(input("Iveskite sveika skaiciu: "))
#         if vart_ivest > 0:
#             vart_ivest = True
#             print(vart_ivest)
#         else:
#             vart_ivest = False
#             print(vart_ivest)
#         break
#     except ValueError:
#         print("Neteisingai! Ivedete sveika skaiciu neteisingai")

# 3 uzduotis turbinimas

# while True:
#     try:
#         import datetime

#         vart_ivest = input("Iveskite savo gimimo data ir laika (YYYY-MM-DD, HH:MM:SS): ")
#         data_formatuota = datetime.datetime.strptime(vart_ivest, "%Y-%m-%d, %H:%M:%S")
#         data_dbr = datetime.datetime.today()

#         rezultatas = data_dbr - data_formatuota
#         print(f"Nuo jūsų gimimo datos praėjo metu: {round(rezultatas.days/365)}")
#         print(f"Nuo jūsų gimimo datos praėjo menesiu: {round(rezultatas.days/30.43)}")
#         print(f"Nuo jūsų gimimo datos praėjo dienu: {rezultatas.days}")
#         print(f"Nuo jūsų gimimo datos praėjo sekundziu: {round(rezultatas.total_seconds())}")
#         break
#     except Exception:
#         print("Neteisingai ivesta data! Data reikia nurodyti (YYYY-MM-DD, HH:MM:SS) formatu: ")


# Praplėskite arba vėl sukurkite mini skaičiuotuvo programą, kurioje programą prašytų įvesti skaičius ir ženklus, tol kol naudotojas įves teisingas reikšmes

# while True:
#     uzduotis = input("įveskite kokį matematinį veiksmą reiktų atlikti (+,-,/,*,istrauk sakni): ")
#     try:
#         pirmas_skaicius = int(input("įveskite pirmą skaičių: "))
#         antras_skaicius = int(input("įveskite antrą skaičių arba laipsni: "))

#         if uzduotis == "+" or uzduotis == "-" or uzduotis == "/" or uzduotis == "istrauk sakni":

#                 if uzduotis == "+":
#                     atsakymas = pirmas_skaicius + antras_skaicius
#                     print(atsakymas)
#                     break
#                 elif uzduotis == "-":
#                     atsakymas = pirmas_skaicius - antras_skaicius
#                     print(atsakymas)
#                     break
#                 elif uzduotis == "/":
#                     atsakymas = pirmas_skaicius / antras_skaicius
#                     print(atsakymas)
#                     break
#                 elif uzduotis == "*":
#                     atsakymas = pirmas_skaicius * antras_skaicius
#                     print(atsakymas)
#                     break
#                 elif uzduotis == "istrauk sakni":
#                     atsakymas = pirmas_skaicius**(1/antras_skaicius)
#                     print(atsakymas)
#                     break
#         else:
#             print("neteisingas veiksmas, bandykite dar karta: ")
#     except ValueError:
#         print("Patikrinkite, ar ivedete teisinga veiksma")
#     except ZeroDivisionError:
#         print("Deja, dalinti is 0 nera imanoma, bandykite dar karta")


# Paprašykite naudotojo įvesti ilgesnį tekstą.
 
# Tuomet paprašykite naudotojo įvesti ieškomų raktažodžių sąrašą.
 
# Ciklo pagalba suraskite kiek kiekvienas raktažodis pasitaikė tekste.

# vart_ivest = input("Iveskite ilgesni teksta: ")

# rakt = input("Kokius 3 raktazodzius naudosime, atskiriant kabliuku: ")

# konvert = vart_ivest.split()
# rakt1,rakt2,rakt3 = rakt.split(", ")

# pasitaike1 = 0
# pasitaike2 = 0
# pasitaike3 = 0
# for i in konvert:
#     if i == rakt1:
#         pasitaike1 += 1
#     if i == rakt2:
#         pasitaike2 += 1
#     if i == rakt3:
#         pasitaike3 += 1

# print(f"Zodis {rakt1} pasitaike {pasitaike1} kartu.")
# print(f"Zodis {rakt2} pasitaike {pasitaike2} kartu.")
# print(f"Zodis {rakt3} pasitaike {pasitaike3} kartu.")

# Birthday Countdown Tikslas: suskaičiuoti, kiek liko dienų iki kito gimtadienio.
# Per try/except paprašyk įvesti gimimo mėnesį ir dieną (du sveikus skaičius).
# Su today = datetime.date.today() ir datetime.date(this_year, month, day): • jei šių metų gimtadienis jau praėjo, sukurk datą kitais metais.
# Apskaičiuok skirtumą delta = birthday - today.
# Išvesk: yaml Šiandien: 2025-04-23 Kitas gimtadienis: 2025-10-15 Likusių dienų: 175 Copy Edit


# import datetime
# from datetime import timedelta

# vart_gimt = input("iveskite savo gimtadienio data (mm-dd): ")

# menuo_diena = vart_gimt.split("-")
# menuo = int(menuo_diena[0])
# diena = int(menuo_diena[1])

# siandien = datetime.date.today()

# vart_2025 = datetime.date(2025, menuo, diena)
# vart_2026 = datetime.date(2026, menuo, diena)

# if vart_2025>siandien:
#     atsakymas = vart_2025 - siandien
#     print(f"siandien: {siandien}")
#     print(f"kitas gimtadienis: {vart_2025}")
#     print(f"Jusu gimtadienis bus po {atsakymas.days} dienu")
# else:
#     atsakymas1 = vart_2026 - siandien
#     print(f"siandien: {siandien}")
#     print(f"kitas gimtadienis: {vart_2026}")
#     print(f"Jusu gimtadienis bus po {atsakymas1.days} dienu")