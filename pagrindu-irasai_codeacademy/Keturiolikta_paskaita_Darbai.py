# _________________________________________________
#  Parašyti klasę Sakinys, kuri turi savybę tekstas irmetodus,kurie:
# •Gražina tekstą atbulai
# •Gražina tekstą mažosiomis raidėmis
# •Gražina tekstą didžiosiomis raidėmis
# •Gražina žodį pagal nurodytą eilės numerį
# •Gražina, kiek teksteyranurodytų simbolių arba žodžių
# •Gražinatekstą su pakeistu nurodytu žodžiu arba simboliu
# •Atspausdina, kiek sakinyje yra žodžių,skaičių,didžiųjų ir mažųjų raidžių
# Susikurti kelis klasės objektus ir išbandyti visus metodus


# class Sakinys():
#     def __init__(self, tekstas="Labas kebabas, ka tu vakare?"): # dabar pakeista: default tekstas iterptas
#         self.tekstas = tekstas

#     def tekstas_atbulai(self):
#         return self.tekstas[::-1]
    
#     def mazosiomis(self):
#         return self.tekstas.lower()
    
#     def didziosiomis(self):
#         return self.tekstas.upper()
    
#     def zodis_pagal_eilesnr(self, numeris):
#         zodziai = self.tekstas.split()
#         if 1 <= numeris <= len(zodziai):
#             return f"{numeris} zodis yra '{zodziai[numeris - 1]}'"
#         else:
#             return "Tokio zodzio nera" 

#     def kiek_simboliu(self):
#         return f" Tekste yra {len(self.tekstas)} simboliu."

#     def kiek_zodziu(self):
#         zodziai = self.tekstas.split()
#         return f"tekste yra {len(zodziai)} zodziai"

#     def uzkeisti_zodi(self, senas_zodis, naujas_zodis):
#         return self.tekstas.replace(senas_zodis, naujas_zodis)
    
#     def simboliu_analize(self):
#         mazosios = 0
#         didziosios = 0
#         skaiciai = 0
#         for i in self.tekstas:
#             if i.isdigit():
#                 skaiciai += 1
#             elif i.isupper():
#                 didziosios += 1
#             elif i.islower():
#                 mazosios += 1
#         return {"Mazuju raidziu": mazosios, "didziuju raidziu": didziosios, "skaiciu": skaiciai}
    
#     def __str__(self): #prideta keiciant programa, kad negrazintu adreso, o teksta. 
#         return self.tekstas
    


# s = Sakinys("Labas, ka tu ka vakare? mano numeris 888888855")

# print("-"*50)

# print(s.tekstas_atbulai())

# print("-"*50)

# print(s.didziosiomis())

# print("-"*50)

# print(s.mazosiomis())

# print("-"*50)

# print(s.simboliu_analize())

# print("-"*50)

# print(s.zodis_pagal_eilesnr(2))

# print("-"*50)

# print(s.kiek_simboliu())

# print("-"*50)

# print(s.kiek_zodziu())

# print("-"*50)

# print(s.uzkeisti_zodi("Labas", "kebabas"))


# print("-"*50)

# s = Sakinys() # pratestavimui pakeitimu
# print(s)  

# _________________________________________________
# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) irmetodus,kurie:
# •Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
# •Gražina,ar nurodytos sukakties metai buvo keliamieji
# •Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
# •Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą
# •2 užduotį taip, kad jei kuriant objektą, nepaduodamas jokia data,veiksmai turi būti atliekami su programuotojo gimtadieniu
# •2 užduotį taip, kad spausdinant datos objektą, spausdintų ne objekto adresą, o įvestą datą

# from datetime import timedelta
# from datetime import datetime

# class Sukaktis():
#     def __init__(self, metai=1999, menuo=7, diena=14, valanda=0, minutes=0, sekundes=0):
#         self.data = datetime(metai,menuo,diena,valanda,minutes,sekundes)

#     def __str__(self):
#         return str(self.data)
    
#     def kiek_praejo(self):
#         data_dbr = datetime.now()
#         sukaktis = self.data
#         rezultatas = data_dbr - sukaktis
#         kiek_dienu = rezultatas.days
#         kiek_sekundziu = rezultatas.total_seconds()
#         kiek_metu = self.kiek_metu()
#         savaites = kiek_dienu / 7
#         valandos = kiek_sekundziu / 3600
#         minutes = kiek_sekundziu / 60
#         menesiai = self.kiek_menesiu()
#         return (
#         f"{"-"*50}\n"
#         f"Nuo sukakties praejo:\n"
#         f"Metu: {kiek_metu}\n"
#         f"Menesiu: {menesiai}\n"
#         f"Savaiciu: {round(savaites)}\n"
#         f"Dienu: {kiek_dienu}\n"
#         f"Valandu: {round(valandos)}\n"
#         f"Minuciu: {round(minutes)}\n"
#         f"Sekundziu: {round(kiek_sekundziu)}\n"
#         f"{"-"*50}\n"
#     )

#     def kiek_metu(self):
#         dabar = datetime.now()
#         skirtumas = dabar.year - self.data.year
#         if dabar.month < self.data.month or (dabar.month == self.data.month and dabar.day < self.data.day):
#             skirtumas -=1
#         return skirtumas
    
#     def kiek_menesiu(self):
#         dabar = datetime.now()
#         menesiai = (dabar.year - self.data.year) * 12 + (dabar.month - self.data.month)
#         if dabar.day < self.data.day:
#             menesiai -= 1
#         return menesiai
    
#     def ar_keliamieji(self):
#         data = self.data
#         if (data.year % 4 == 0 and data.year % 100 != 0) or (data.year % 400 == 0):
#             return (
#                 f"{"-"*50}\n"
#                 f"{data.year} metai yra keliamieji\n"
#                 f"{"-"*50}"
#                 )
#         else:
#             return f"{data.year} metai yra NE keliamieji"
        
#     def prideti_dienas(self):
#         while True:
#             try:
#                 dienu_kiekis = int(input("Iveskite dienu kieki, kuri norite prideti: "))
#                 break
#             except ValueError:
#                 print("dienu kiekis privalo buti sveikas skaicius, bandykite dar karta.")
#                 continue
#         skirtumas_dienu = timedelta(days=dienu_kiekis)
#         nauja_data = self.data + skirtumas_dienu
#         return (
#             f"{"-"*50}\n"
#             f"Nauja data, pridejus {dienu_kiekis} dienu: {str(nauja_data)}\n"
#             f"{"-"*50}\n"
#             )
    
#     def atimti_dienas(self):
#         while True:
#             try:
#                 dienu_kiekis = int(input("Iveskite dienu kieki, kuri norite atimti: "))
#                 break
#             except ValueError:
#                 print("dienu kiekis privalo buti sveikas skaicius, bandykite dar karta.")
#                 continue
#         skirtumas_dienu = timedelta(days=dienu_kiekis)
#         nauja_data = self.data - skirtumas_dienu
#         return (
#             f"{"-"*50}\n"
#             f"Nauja data, atemus {dienu_kiekis} dienu: {str(nauja_data)}\n"
#             f"{"-"*50}\n"
#             )
    
# s = Sukaktis()

# print(s)

# print(s.kiek_praejo())

# print(s.ar_keliamieji())

# print(s.prideti_dienas())

# print(s.atimti_dienas())


# _________________________________________________
# Padaryti mini biudžeto programą, kuri:
# •Leistų vartotojui įvesti pajamas
# •Leistų vartotojui įvesti išlaidas
# •Leistų vartotojui parodyti pajamų/išlaidų balansą
# •Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
# •Leistų vartotojui išeiti iš programos
 
# Rekomendacija, kaip galima būtų padaryti:
# •Programa turi turėti klasę Irasas, kuri turėtų argumentus tipas (Pajamos arba Išlaidos) ir suma. Galima prirašyti str metodą, kuris gražintų, kaip bus atvaizduojamas spausdinamas objektas.
# •Programa turi turėti klasę Biudzetas, kurioje būtų:
# •Metodas init, kuriame sukurtas tuščias sąrašas zurnalas, į kurį bus dedami sukurti pajamų ir išlaidų objektai
# •Metodasprideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
# •Metodasprideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
# •Metodasgauti_balansą(self), kuris gražintų žurnale laikomų pajamų ir išlaidų balansą.
# •Metodasparodyti_ataskaita(self), kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).


# # _________________________________________________

class Irasas():
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return str(f"{self.tipas}:{self.suma} Eur")

class Biudzetas():
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        irasas = Irasas("Pajamos", suma)
        self.zurnalas.append(irasas)

    def prideti_islaidu_irasa(self, suma):
        irasas = Irasas("Islaidos", suma)
        self.zurnalas.append(irasas)

    def parodyti_ataskaita(self):
        for i in self.zurnalas:
            print(i)

    def gauti_balansa(self):
        pajamos = 0
        islaidos = 0
        for i in self.zurnalas:
            if i.tipas == "Pajamos":
                pajamos += i.suma
            else:
                islaidos += i.suma
        balansas = pajamos - islaidos
        return (
            f"{"-"*50}\n"
            f"Dabartinis balansas: {balansas}\n"
            f"{"-"*50}\n"
            )
    
def paleisti_meniu(biudzetas):
    while True:
        print(""" --- MENIU --- \n
1. Pajamos \n
------------\n
2. Islaidos \n
------------\n
3. Balansas \n
------------\n
4. Ataskaita \n
------------\n
5. Iseiti \n
------------\n
                """)
        try:
            pasirinkimas = int(input("Iveskite funkcijos numeri: "))
        except ValueError:
            print("Privalote ivesti sveika skaiciu, bandykite dar karta.")
            continue
        
        if pasirinkimas == 1:
            try:
                pajamu_suma = float(input("Iveskite pajamu suma: "))
            except ValueError:
                print("Ivedete pajamu suma neteisingai, bandykite dar karta.")
                continue
            biudzetas.prideti_pajamu_irasa(pajamu_suma)
            print(
                f"{"-"*50}\n"
                f"Pajamos {pajamu_suma} Eur pridetos i biudzeta.\n"
                f"{"-"*50}\n"
                    )
            
        elif pasirinkimas == 2:
            try:
                islaidu_suma = float(input("Iveskite islaidu suma: "))
            except ValueError:
                print("Ivedete islaidu suma neteisingai, bandykite dar karta.")
                continue
            biudzetas.prideti_islaidu_irasa(islaidu_suma)
            print(
                f"{"-"*50}\n"
                f"Islaidos {islaidu_suma} Eur pridetos i biudzeta.\n"
                f"{"-"*50}\n"
                    ) 
        
        elif pasirinkimas == 3:
            print(biudzetas.gauti_balansa())

        elif pasirinkimas == 4:
            biudzetas.parodyti_ataskaita()
        
        elif pasirinkimas == 5:
            break
            
b = Biudzetas()

paleisti_meniu(b)
                
# _____________________________________________________________________

# Vidutinės
# Sukurk klasę Apskritimas, kurios konstruktoriuje būtų spindulys r. Parašyk metodus plotas() ir perimetras().
# Patarimas: naudok math.pi ir metodų aprašymą klasėje.
# Parašyk klasę Studentas, turinčią atributus vardas, pazymiai (sąrašas). Parašyk metodą vidurkis(), grąžinantį pažymių vidurkį.
# Patarimas: naudok sumavimo ir ilgio funkcijas (sum(), len()).
# Sukurk sąrašą objektų Studentas su bent 3 studentais ir atspausdink kiekvieno vardą bei vidurkį.
# Patarimas: naudok for studentas in sarasas:.
# Parašyk funkciją, kuri surikiuotų sąrašą sveikųjų skaičių didėjimo tvarka be sort() (naudok paprastą rūšiavimo algoritmą).
# Patarimas: pabandyk “bubble sort” metodą.
# Sukurk žodyną su keliais klasės objektais kaip reikšmėmis, kur raktai – studentų ID, ir rask studentą pagal ID.
# Patarimas: naudok dict metodo get().
# Parašyk generatoriaus funkciją fibonacci(n), kuri generuotų pirmus n Fibonačio skaičius.
# Patarimas: pažvelk į yield.
# Sukurk dekoratorių timer, kuris apskaičiuotų ir atspausdintų funkcijos vykdymo trukmę.
# Patarimas: naudok time.time().
# Parašyk programą, kuri iš failo duomenys.txt nuskaito skaičius, sudeda juos ir išveda rezultatą.
# Patarimas: naudok with open(...) as f:.
# Sukurk klasę Knyga su atributais pavadinimas, autorius, metai. Parašyk __str__, kad gražintų aprašą.
# Patarimas: panaudok f-string konstrukciją def __str__(self):.
# Parašyk funkciją, kuri gautų žodžių sąrašą ir gražintų naują sąrašą, kuriame – tik unikalūs žodžiai.
# Patarimas: panaudok set() viduje funkcijos.

# Sukurk klasę Apskritimas, kurios konstruktoriuje būtų spindulys r. Parašyk metodus plotas() ir perimetras().
# Patarimas: naudok math.pi ir metodų aprašymą klasėje.

import math

class Apskritimas():
    def __init__(self, spindulys_r):
        self.spindulys_r = spindulys_r

    def ploto_skaiciavimas(self):
        plotas = (self.spindulys_r * self.spindulys_r) * math.pi
        return f"Apskritimo plotas: {plotas}"
    
    def perimetro_skaiciavimas(self):
        perimetras = (self.spindulys_r + self.spindulys_r) * math.pi
        return f"Apskritimo perimetras: {perimetras}"
    

a = Apskritimas(50)

print(a.ploto_skaiciavimas())

print(a.perimetro_skaiciavimas())
