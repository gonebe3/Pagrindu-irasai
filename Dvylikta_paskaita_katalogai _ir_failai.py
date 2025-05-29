# import os
# print(os.getcwd()) #dabartine aktyvi direktorija
 
# os.chdir("G:") #pakeicia dabartine aktyvia direktorija
 
# print(os.listdir()) #sarasas aplanku ar failu aktyvioje direktorijoje
 
#Jei nurodome visa kelia nuo disko pvz: D:\Games\L2 tada globaliai kuria ir yra patogiau jei naudosime kituose kompiuteriuose ar kiti vartotojai
# os.mkdir("mano direktorija - test") #sukuria aktyviame kataloge diretorija su nurodytu pavadinimu
# os.makedirs(r"mano direktorija - test/tavo/geras") #sukuria visa kelia nurodyta, r raidele apsauga nuo klaidos
 
# print(os.stat("Ai studijos").st_size)  # direktorijos statusas funkcijos kaip st.size dydi parodo


# import os
# import datetime
# print(dir(os))
 
# print(os.getcwd()) # current working directory
 
# os.chdir("D:\AIU7") # change directory
 
# print(os.getcwd()) # current working directory
 
# print(os.listdir()) # list files in directory
 
# os.mkdir("aplankas\Mano_direktorija") # create directory
 
# os.makedirs(r"D:\AIU7\Pagrindai\Mano_direktorija\Mano\Tavo\Gera") # create directory
 
# svarbus pastebejimas
# jeigu nurodome visa kelia nuo disko pvz C:, D: tai mums nesvarbu kokiam aplanke esame
# jeigu nurodome kelia tik iki aplanko pvz aplankas\Mano_direktorija tai jis sukurs aplanka tik tame aplanke kuriame esame
# os.chdir("D:\AIU7") # change directory
 
# sukurimas = os.stat("Pagrindai").st_birthtime # get directory status
 
# print(datetime.datetime.fromtimestamp(sukurimas)) # convert to datetime
# dabar = datetime.datetime.now()
# dabar.timestamp() # get current timestamp
 
 # failas = open("failas.txt", "w")
# failas.write("Labas rytas\n")
# input("Paspauskite bet kuri klavišą, kad uždarytumėte failą...") # wait for user input
# failas.close() # close file
# input("Failas uždarytas. Paspauskite bet kuri klavišą, kad tęstumėte...") # wait for user input
# with open("failas.txt", "w") as failas: # w - rasyti (write), r - skaityti (read), a - prideti (append) | failas = open("failas.txt", "w")
#     failas.write("Labas rytas\n")
#     failas.write("Labas vakaras\n")
 
# failas.write("Labas vakaras\n") # klaida, nes failas jau uzdarytas
# galima isivaizduoti, kad failas.close() yra automatinis
 
# with open("failas.txt", "w") as failas: # w - sukuria faila jeigu jo nera, jeigu yra tai jis ji perraso
#     failas.write("Mano uzrasai\n")
#     failas.write("Labas rytas\n")
#     # failas.read() # klaida, nes failas rasymo rezimu
 
# with open("failas.txt", "r") as failas: # r - skaito faila jeigu failo nera tai klaida
    # tekstas = failas.read() # read file
    # print(tekstas) # spausdina failo turini
    # print(failas.readline()) # read line by line
    # read line by line with loop with readline()
    # while True:
    #     line = failas.readline()
    #     if not line:
    #         break
    #     print(line.strip()) # remove new line character
 
    # print(failas.readlines()) # read all lines
    # failas.write("Labas rytas\n") # klaida, nes failas skaitymo rezimu
 
# with open("failas.txt", "a") as failas: # a - prideda prie failo, jeigu failo nera tai jis ji sukuria
   
#     failas.write("Labas vakaras\n")
#     failas.write("Labas naktis\n")


# ------------------------------------------------------------------------------
# Sukurkite naują aplanką pavadinimu duomenys savo darbineje direktorijoje
# jame sukurkite failą pavadinimu vardai
# ir ten irasykite savo grupioku/kolegu vardus
# Tuomet paklauskite naudotojo ar jis nori atspausdinti vardus, jeigu jis nori atspausdinti tuomet atspausdinkite failo turini



import os

# print(os.getcwd())

# os.makedirs(r"C:\Users\domin",exist_ok=True)

# with open(r"C:\Users\domin\vardai.txt", "w") as vardai:
#     vardai.write("Marius\n")
#     vardai.write("Simonas\n")
#     vardai.write("Ugnes\n")    
#     vardai.write("Kestutis\n")  
#     vardai.write("Justas\n")  

# klausimas = input("Ar norite atspausdinti failus?(taip arba ne): ")

# if klausimas == "taip":
#     with open(r"C:\Users\domin\vardai.txt", "r") as vardai:    
#         tekstas = vardai.read()
#         print(tekstas)
# else:
#     print("Nespausiname vardus")

# ------------------------------------------------------------------------------
#  Sukurti ant savo darbalaukio aplanką Pagrindinis jame sukurkite du aplankus "pirmas" ir "antras"

# os.makedirs(r"C:\Users\domin\OneDrive\Рабочий стол\pagrindinis\pirmas")
# os.makedirs(r"C:\Users\domin\OneDrive\Рабочий стол\pagrindinis\antras")

# ------------------------------------------------------------------------------

# Sukurti programą, kuri:
# •Leistų vartotojui įvesti norimą eilučių kiekį
# •Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# •Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
 
# Patarimai:
# •Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)

# Failo_pav = input("Iveskite failo pavadinima: ") + ".txt"


# with open(Failo_pav, "w") as failas:
#     print("Rasykite norimas eilutes (noredami sustabdyti, tiesiog paspauskite ENTER):")

#     while True:
#         eilute = input("Iveskite eilute:")
#         if eilute == "":
#             break
#         failas.write(eilute + "\n") 

#     print(f"Failas {Failo_pav} sukurtas ir uzpildytas sekmingai")

# ------------------------------------------------------------------------------

# Pamėginkite įdėti sąrašą į failą ir tada jį vėl užkrauti, kaip sąrašą
 
# Sukuriam sąrašą
# Įrašom į failą
# Užkraunam failo turinį
# Paverčiam į sąrašą
# Ataspausdinam


# def failo_uzpildymas(sarasas, failo_pavadinimas):
#     with open(failo_pavadinimas, "w") as failas:
#         for skaiciai in sarasas:
#             failas.write(f"{skaiciai}\n")

# def nuskaityti_faila(failo_pavadinimas):
#     atstatytas_sarasas = []
#     with open(failo_pavadinimas, "r") as failas:
#         for skaiciai in failas:
#             atstatytas_sarasas += [int(skaiciai.strip())] 
#         return atstatytas_sarasas

# sarasas = [1, 2, 3, 4]
# failas = "duomenys1.txt"

# failo_uzpildymas(sarasas, failas)       
# naujas_sarasas = nuskaityti_faila(failas)  

# print(f"Atgautas sąrašas iš failo: {naujas_sarasas}")


# ------------------------------------------------------------------------------
# TEORIJA
# with open("failas.txt", "r+") as failas: # r+ - skaito ir raso faila, jeigu failo nera, tai klaida
#     failas.write("Test")
#     failas.seek(0)
#     failas.write("BE")
#     tekstas = failas.read() # read file
#     print(tekstas) # spausdina failo turini
 
# with open("failas.txt", "w+") as failas: # w+ - sukuria faila jeigu jo nera, jeigu yra tai jis ji perraso ir skaito faila
#     failas.write("Labas rytas\n")
#     failas.seek(0)
#     tekstas = failas.read() # read file
#     print(tekstas) # spausdina failo turini
 
 
 
# with open("failas.txt", "w", encoding="utf-8") as failas:
#     failas.write("Kęstutis") # K ę - o tai kaip man irasyti sita savo nesamoninga simboli ?
#     failas.write("ė")
 
# with open("failas.txt", "r", encoding="utf-8") as failas:
#     tekstas = failas.read() # read file
#     print(tekstas) # spausdina failo turini
     


# ------------------------------------------------------------------------------

# Sukurti programą, kuri:
# •Sukurtų failą „Tekstas.txt“ su pilnu tekstu "Zen of Python".
# •Atspausdintų tekstą iš sukurto failo
# •Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
# •Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# •Sukurtame faile eilutę "Beautifulis better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
# •Atspausdintų visą failo tekstą atbulai
# •Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# •Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS

# from datetime import datetime

# def sukurti_faila(failo_pavadinimas):
#     with open(failo_pavadinimas, "w", encoding="utf-8") as failas:
#         failas.write("Beautiful is better than ugly.\n Explicit is better than implicit.\n Simple is better than complex.\n Complex is better than complicated.\n Flat is better than nested.\n Sparse is better than dense.\n Readability counts.\n Special cases aren't special enough to break the rules.\n Although practicality beats purity.\n Errors should never pass silently.\n Unless explicitly silenced.\n In the face of ambiguity, refuse the temptation to guess.\n There should be one-- and preferably only one --obvious way to do it.\n Although that way may not be obvious at first unless you're Dutch.\n Now is better than never.\n Although never is often better than *right* now.\n If the implementation is hard to explain, it's a bad idea.\n If the implementation is easy to explain, it may be a good idea.\n Namespaces are one honking great idea -- let's do more of those!")

# def atspausdinti_failo_teksta(failo_pavadinimas):
#     with open(failo_pavadinimas, "r", encoding="utf-8") as failas:
#         tekstas = failas.read()
#         return tekstas
    
# def prideti_data(failo_pavadinimas):
#     with open(failo_pavadinimas, "a", encoding="utf-8") as failas:
#         dabar = datetime.now()
#         failas.write("\n" + dabar.strftime("%Y-%m-%d %H:%M:%S"))

# def sunumeruoti_eilutes(failo_pavadinimas):
#     with open(failo_pavadinimas, "r", encoding="utf-8") as failas:
#         eilutes = failas.readlines()

#     eiluciu_numeris = 1
#     with open(failo_pavadinimas, "w", encoding="utf-8") as failas:
#         for nr in eilutes:
#             failas.write(f"{eiluciu_numeris}.{nr}")
#             eiluciu_numeris += 1

# def pakeisti_teksta(failo_pavadinimas, senas_tekstas, naujas_tekstas):
#     with open(failo_pavadinimas, "r", encoding="utf-8") as failas:
#         tekstas = failas.read()

#     uzkeistas_tekstas = tekstas.replace(senas_tekstas, naujas_tekstas)

#     with open(failo_pavadinimas, "w", encoding="utf-8") as failas:
#         failas.write(uzkeistas_tekstas)

# def atspausdinti_atbulai(failo_pavadinimas):
#     with open(failo_pavadinimas, "r", encoding="utf-8") as failas:
#         tekstas_atbulai = failas.read()
#         return tekstas_atbulai[::-1]

# def kiek_kokie_simboliai(failo_pavadinimas):
#     with open(failo_pavadinimas, "r", encoding="utf-8") as failas:
#         tekstas = failas.read()    

#     zodziai = tekstas.split()

#     skaiciai = int(0)
#     for simbolis in tekstas:
#         if simbolis.isdigit():
#             skaiciai += 1   

#     did_raides = int(0)
#     maz_raides = int(0)
#     for raides in tekstas:
#         if raides.isupper():
#             did_raides += 1
#         if raides.islower():
#             maz_raides += 1

#     return len(zodziai), skaiciai, did_raides, maz_raides

# def nukopijuoti_didziosiomis(failo_pavadinimas, naujas_failas):
#     with open(failo_pavadinimas, "r", encoding="utf-8") as failas:
#         tekstas = failas.read()

#     with open(naujas_failas, "w", encoding="utf-8") as failas:
#         failas.write(tekstas.upper())


# failas = "Tekstas1.txt"

# naujas_failas = "Tekstas_didziosiomis.txt"

# sukurti_faila(failas)

# pakeisti_teksta(failas,"Beautiful is better than ugly.","Gražu yra geriau nei bjauru.")

# tekstas = atspausdinti_failo_teksta(failas)

# prideti_data(failas)

# sunumeruoti_eilutes(failas)


# atbulas_tekstas = atspausdinti_atbulai(failas)

# zodziai, skaiciai, didziosios, mazosios = kiek_kokie_simboliai(failas)

# nukopijuoti_didziosiomis(failas, naujas_failas)

# print("Failo tekstas:\n", tekstas)
# print("\nAtbulai:\n", atbulas_tekstas)
# print(f"\nzodziu: {zodziai}, Skaiciu: {skaiciai}, Didziuju raidziu: {didziosios}, Mazuju raidziu: {mazosios}")

# ------------------------------------------------------------------------------

# Sukurti programą, kuri:
# •Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
# •Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
# •Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
 
# Patarimai:
# •Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_birthtime


# from datetime import datetime
# def sukurti_kataloga():
#     os.makedirs(r"C:\Users\domin\OneDrive\Рабочий стол\Naujas Katalogas", exist_ok=True)

# def sukurti_faila(failo_pavadinimas):
#     kelias = rf"C:\Users\domin\OneDrive\Рабочий стол\Naujas Katalogas\{failo_pavadinimas}"
#     with open(kelias, "w") as failas:
#         dabar = datetime.now()
#         failas.write(f"Siandienos data:{dabar} " + "\n")

# def prideti_info(failo_pavadinimas):
#     kelias = rf"C:\Users\domin\OneDrive\Рабочий стол\Naujas Katalogas\{failo_pavadinimas}"
#     failo_dyd = os.stat(kelias).st_size
#     sukurimo_data = os.stat(kelias).st_birthtime
#     konver_data = datetime.fromtimestamp(sukurimo_data)
    
#     with open(kelias, "a") as failas:
#         failas.write(f"Sukurimo data: {konver_data}, failo dydis: {failo_dyd} baitu")

# sukurti_kataloga()
# sukurti_faila("tekstas1.txt")
# prideti_info("tekstas1.txt")

# _________________________________________________________________________________________


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


# import os
# import pickle

# def paleisti_meniu():
#     inventory = []

#     while True:
#         print("\n==== Inventoriaus valdymas ====")
#         print("1.Prideti preke")
#         print("2.Atnaujinti preke")
#         print("3.Pasalinti preke")
#         print("4.Rodyti visas prekes")





# inventorija = [
#     {"pavadinimas": "stiline", "kiekis": 15, "kaina": 50, "Unikalus ID": 1},
#     {"pavadinimas": "piestukas", "kiekis": 30, "kaina": 0.5,"Unikalus ID": 2},
#     {"pavadinimas": "trintukas", "kiekis": 20, "kaina": 1,"Unikalus ID": 3}
# ]

# def direktoriju_kurimas():
#     os.makedirs(r"C:\Users\domin\Darbui\direktorija", exist_ok=True)
#     os.makedirs(r"C:\Users\domin\Darbui\direktorija1", exist_ok=True)

# direktoriju_kurimas()

# def inventorija(id, pavadinimas, kiekis, kaina):
#     invent_kelias = r"C:\Users\domin\Darbui\direktorija\inventorija.txt"
#     id_kelias = r"C:\Users\domin\Darbui\direktorija\id.txt.txt"
#     with open (invent_kelias, "w") as failas:


# _________________________________________________________________________________________
# TEORIJA APIE AGURKELI
# _________________________________________________________________________________________

# import pickle
 
# with open("duomenys.pickle", "wb") as failiukas: # wb - binary write
#     pickle.dump("Labas rytas", failiukas) # write to file
 
# with open("duomenys.pickle", "rb") as failiukas: # rb - binary read
#     tekstas = pickle.load(failiukas) # read from file
#     print(tekstas) # spausdina failo turini
# sarasas = [5,4,19,2,6,48,1,0,3,7,8,9,10]
# sarasas.append(5)
# with open("duomenys.txt", "w") as failiukas: # w - write
#     failiukas.write(str(sarasas)) # write to file
 
# with open("duomenys.txt", "r") as failiukas: # r - read
#     tekstas = failiukas.read() # read from file
#     print(tekstas) # spausdina failo turini
 
# sarasas = [5,4,19,2,6,48,1,0,3,7,8,9,10]
# with open("duomenys.pickle", "wb") as failiukas: # wb - binary write
#     pickle.dump(sarasas, failiukas) # write to file
 
# with open("duomenys.pickle", "rb") as failiukas: # rb - binary read
#     nuskaitytas_sarasas = pickle.load(failiukas) # read from file
#     nuskaitytas_sarasas.append(5) # prideti elementa i sarasa
#     print(nuskaitytas_sarasas) # spausdina failo turini
 
# saras_sarase = [[1,2,3],[4,5,6],[7,8,9]]
# zodynai_sarase = [{"vardas":"Jonas","pavarde":"Jonaitis"},{"vardas":"Petras","pavarde":"Petraitis"},{"vardas":"Ona","pavarde":"Onaitė"}]
# print(zodynai_sarase)

# _______________________________________________________________________________________

# Sukurti minibiudžeto programą, kuri:
# •Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
# •Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
# •Atvaizduotų jau įvestas pajamas ir išlaidas
# •Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)

def vart_ivesties_iskvietimas():
    while True:
        try:
            a = input("Iveskite pajamas arba islaidas: ")
            skaicius = float(a)
            return skaicius
        except Exception:
            print("Ivedete ne skaicius, bandykite dar karta")


vart_ivesties_iskvietimas()










