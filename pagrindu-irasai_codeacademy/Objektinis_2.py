# class Vehicle():
#     def __init__(self, speed, material):
#         self.speed = speed
#         self.material = material
#     def __str__(self):
#         return f"Made from {self.material} and speed of {self.speed}"
 
 
# class LandVehicle(Vehicle):
#     def __init__(self, speed, material, wheels):
#         super().__init__(speed, material) # Vehicle.__init__
#         self.wheels = wheels
 
#     def __str__(self):
#         return super().__str__() + f" and with {self.wheels} wheels"
   
#     def vaziuoti(self):
#         print(f"As vaziuoju {self.wheels} ratais")
 
# class WaterVehicle(Vehicle):
#     pass
 
 
 
# class AirVehicle(Vehicle):
#     pass
 
# tr_pr = Vehicle(30,"Aluminium")
# saus_tr_pr = LandVehicle(180,"Aluminium",4)
# vand_tr_pr = WaterVehicle(30,"Aluminium")
 
# print(tr_pr)
# print(saus_tr_pr)
# print(vand_tr_pr)
 
 
# # tr_pr.vaziuoti()
# saus_tr_pr.vaziuoti()
# # vand_tr_pr.vaziuoti()
 
 
# class Gyvunas():
#     def __init__(self, age, color, vardas):
#         self.age = age
#         self.colour = color
#         self.name = vardas
 
#     def kalbeti(self):
#         print("As kalbu kaip moku")
 
#     def __str__(self): # Kai mes darom pvz print(gyvuno_objektas), jis skirtas duoti detalia informacija apie viena objekta
#         return f"Labas as {self.name} man {self.age} ir mano spalva yra {self.colour}"
   
#     def __repr__(self): # kai mes darome print(guvunu_sarasas), jis skirtas trumpai reprezentuoti gyvuna sarase
#         return self.name
 
 
# class Dog(Gyvunas):
#     def __init__(self, age, color, vardas):
#         super().__init__(age, color, vardas)
 
#     def kalbeti(self):
#         print("As esu suo ir loju AU AU")
 
# class Cat(Gyvunas):
#     def __init__(self, age, color, vardas):
#         super().__init__(age, color, vardas)
 
# suo = Dog(7,"Ruda","Reksas")
# suo2 = Dog(1,"Balta","Mikis")
 
# kate = Cat(2,"Orandzine","Maja")
# kate2 = Cat(3,"Juoda","Mice")
 
# gyvunai = [suo,suo2,kate,kate2]
 
# print(gyvunai)
 
# for gyvunas in gyvunai:
#     print(gyvunas)
#     gyvunas.kalbeti()




# ____________________________________________________
# Noriu, kad sukurtumėte tokias klases. Asmuo, kaip tėvas. 
# Darbuotojas ir Klientas, kaip vaikai. 
# Darbuotojas turi galimybę parduoti produktą (imitacinis metodas parduoti) klientas turi turėti perku. 
# Abu jie turi turėti bendras sąvybes Vardas ir Pavardė, bei gimimo data. Ir turi bendrai turėti metodą paskaičiuojanti jų amžių. 


# from datetime import datetime

# class Asmuo():
#     def __init__(self, vardas, pavarde, gimimo_data):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.gimimo_data = gimimo_data

#     def apskaiciuoti_amziu(self):
#         gim_data = datetime.strptime(self.gimimo_data, '%Y-%m-%d')
#         siandien = datetime.today()
#         amzius = siandien.year - gim_data.year
#         if (siandien.month, siandien.day) < (gim_data.month, gim_data.day):
#             amzius -= 1
#         return amzius
    
# class Darbuotojas(Asmuo):
#     def __init__(self, vardas, pavarde, gimimo_data, alga):
#         super().__init__(vardas, pavarde, gimimo_data)
#         self.alga = alga

#     def parduoti(self):
#         print(f" {self.vardas} {self.pavarde} pardave preke.")

# class Klientas(Asmuo):
#     def __init__(self, vardas, pavarde, gimimo_data, uzsakymu_kiekis):
#         super().__init__(vardas, pavarde, gimimo_data)
#         self.uzsakymu_kiekis = uzsakymu_kiekis

#     def pirkti(self):
#         print(f"{self.vardas} {self.pavarde} nupirko preke.")

# d = Darbuotojas("Jonas", "Jonaitis", "1990-05-20", 1500)
# k = Klientas("Ona", "Petrauskiene", "1985-03-15", 5)

# d.parduoti()
# print(f"{d.vardas} yra {d.apskaiciuoti_amziu()} metu ir jo alga yra {d.alga} EUR.")

# k.pirkti()
# print(f"{k.vardas} yra {k.apskaiciuoti_amziu()} metu ir turi {k.uzsakymu_kiekis} uzsakymus.")

# ____________________________________________________

# Sukurti programą, kuri:
# •Turėtų klasę Automobilis
# •Automobilis turėtų savybes: metai, modelis, kuro_tipas
# •Automobilis turėtųmetodus: vaziuoti, stoveti, pildyti_degalu,kurie atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“
# •Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą
# •Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)
# •Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad jis atspausdintų „Baterija įkrauta“
# •Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“
# •Sukurti norimą Automobilio objektą
# •Sukurti norimą Elektromobilio objektą
# •Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti,pildyti_degalu
# •Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti,stoveti,pildyti_degalu,vaziuoti_autonomiskai

# from datetime import datetime

# class Automobilis():
#     def __init__(self, metai, modelis, kuro_tipas):
#         self.metai = metai
#         self.modelis = modelis
#         self.kuro_tipas = kuro_tipas
#         print(f"Sukurtas automobilis: {self.modelis}, {self.metai}, {self.kuro_tipas}")
    
#     def __str__(self):
#         return f"{self.modelis} ({self.metai}) - kuro tipas: {self.kuro_tipas}"

#     def vaziuoti(self):
#         print(f"Automobilis {self.modelis} vaziuoja")
    
#     def stoveti(self):
#         print(f"Automobilis {self.modelis} priparkuotas")

#     def pildyti_degalus(self):
#         print(f"Automobiliui {self.modelis} degalai ipilti")

# class Elektromobilis(Automobilis):
#     def __init__(self, metai, modelis, kuro_tipas):
#         super().__init__(metai, modelis, kuro_tipas)

#     def pildyti_degalus(self):
#         print(f"Automobilio {self.modelis} baterija ikrauta")

#     def vaziuoti_autonomiskai(self):
#         print(f"Automobilis {self.modelis} vaziuoja autonomiskai")

# e = Elektromobilis(2025, "Tesla Model X", "elektra")
# e.vaziuoti()
# e.stoveti()
# e.pildyti_degalus()
# e.vaziuoti_autonomiskai()
# print(e)

# a = Automobilis(2025, "BMW 550", "Benzinas")

# a.vaziuoti()
# a.stoveti()
# a.pildyti_degalus()
# print(a)

# ____________________________________________________
# Sukurti programą, kuri:
# •Turėtų klasę Darbuotojas
# •Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
# •Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
# •Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
# •Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant darbuotojui 5 dienas per savaitę
# •Sukurti norimą Darbuotojo objektą
# •Sukurti norimą NormalusDarbuotojas objektą
# •Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima

# from datetime import datetime

# from datetime import timedelta

# class Darbuotojas():
#     def __init__(self, vardas, pavarde, valandos_ikainis, dirba_nuo):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.valandos_ikainis = valandos_ikainis
#         self.dirba_nuo = dirba_nuo

#     def __str__(self):
#         return f"{self.vardas} {self.pavarde}, dirba nuo {self.dirba_nuo}, {self.valandos_ikainis} €/val."
    
#     def _dirbtu_dienu_skaicius(self):
#         pirma_diena = datetime.strptime(self.dirba_nuo, '%Y-%m-%d')
#         siandien = datetime.today()
#         kiek_dienu = siandien - pirma_diena
#         return kiek_dienu.days
    
#     def paskaiciuoti_atlyginima(self):
#         dirbtos_dienos = self._dirbtu_dienu_skaicius()
#         atlyginimas = dirbtos_dienos * 8 * self.valandos_ikainis
#         return round(atlyginimas, 2)
    
# class Normalus(Darbuotojas):
#     def __init__(self, vardas, pavarde, valandos_ikainis, dirba_nuo):
#         super().__init__(vardas, pavarde, valandos_ikainis, dirba_nuo)

#     def _dirbtu_dienu_skaicius(self):
#         pirma_diena = datetime.strptime(self.dirba_nuo, '%Y-%m-%d')
#         siandien = datetime.today()
#         darbo_dienos = 0

#         while pirma_diena.date() <= siandien.date():
#             if pirma_diena.weekday() < 5:
#                 darbo_dienos += 1
#             pirma_diena += timedelta(days=1)

#         return darbo_dienos

# d1 = Darbuotojas("Jonas", "Jonunas", 10, "2024-01-01")
# d2 = Normalus("Petras","Petrauskas", 10, "2024-01-01")

# print(d1.paskaiciuoti_atlyginima())
# print(d2.paskaiciuoti_atlyginima())


# # ____________________________________________________
# Patobulinti 5 pamokos biudžeto programą:
# •Sukurti tėvinę klasę Irasas, kurioje būtų savybės suma , iš kurios klasės PajamuIrasas ir IslaiduIrasas paveldėtų visas savybes.
# •Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija, kurias vartotojas galėtų įrašyti.
# •Į klasę IslaiduIrasas papildomai pridėti savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias vartotojas galėtų įrašyti.
# •Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa ir gauti_ataskaita kad pasiėmus įrašą iš žurnalo, atpažintų, 
# ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą) ir atitinkamai atliktų veiksmus.
# •Padaryti, kad vartotojui (per konsolę) būtų leidžiama įrašyti pajamų ir išlaidų įrašus, peržiūrėti balansą ir ataskaitą.

# class Irasas():
#     def __init__(self, suma):
#         self.suma = suma

#     def __str__(self):
#         return str(f"Suma: {self.suma} Eur")

# class Pajamu(Irasas):
#     def __init__(self, suma, siuntejas, papildoma_informacija):
#         super().__init__(suma)
#         self.tipas = "Pajamos"
#         self.siuntejas = siuntejas
#         self.papildoma_informacija = papildoma_informacija
    
#     def __str__(self):
#         return str(f" Pajamu suma: {self.suma}, siuntejas: {self.siuntejas}, papildoma informacija: {self.papildoma_informacija}")

# class Islaidu(Irasas):
#     def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
#         super().__init__(suma)
#         self.tipas = "Islaidos"
#         self.atsiskaitymo_budas = atsiskaitymo_budas
#         self.isigyta_preke_paslauga = isigyta_preke_paslauga
    
#     def __str__(self):
#         return str(f"Islaidu suma: {self.suma}, atsiskaitymo budas: {self.atsiskaitymo_budas}, isigyta preke: {self.isigyta_preke_paslauga}")

# class Biudzetas():
#     def __init__(self):
#         self.zurnalas = []

#     def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_info):
#         irasas = Pajamu(suma, siuntejas, papildoma_info)
#         self.zurnalas.append(irasas)

#     def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
#         irasas = Islaidu(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
#         self.zurnalas.append(irasas)

#     def parodyti_ataskaita(self):
#         for i in self.zurnalas:
#             print(i)

#     def gauti_balansa(self):
#         pajamos = 0
#         islaidos = 0
#         for i in self.zurnalas:
#             if i.tipas == "Pajamos":
#                 pajamos += i.suma
#             else:
#                 islaidos += i.suma
#         balansas = pajamos - islaidos
#         return (
#             f"{"-"*50}\n"
#             f"Dabartinis balansas: {balansas}\n"
#             f"{"-"*50}\n"
#             )
    
#     def parodyti_ataskaita(self):
#         for i in self.zurnalas:
#             print("-"*20)
#             print(i)
    
# def paleisti_meniu(biudzetas):
#     while True:
#         print(""" --- MENIU --- \n
# 1. Pajamos \n
# ------------\n
# 2. Islaidos \n
# ------------\n
# 3. Balansas \n
# ------------\n
# 4. Ataskaita \n
# ------------\n
# 5. Iseiti \n
# ------------\n
#                 """)
#         try:
#             pasirinkimas = int(input("Iveskite funkcijos numeri: "))
#         except ValueError:
#             print("Privalote ivesti sveika skaiciu, bandykite dar karta.")
#             continue
        
#         if pasirinkimas == 1:
#             try:
#                 pajamu_suma = float(input("Iveskite pajamu suma: "))
#                 print("-"*20)
#                 siuntejas = input("Iveskite siunteja: ")
#                 print("-"*20)
#                 info = input("Iveskite papildoma info: ")
#                 biudzetas.prideti_pajamu_irasa(pajamu_suma, siuntejas, info)
#                 print(
#                 f"{"-"*50}\n"
#                 f"Pajamos {pajamu_suma} Eur pridetos i biudzeta.\n"
#                 f"{"-"*50}\n"
#                     )
#             except ValueError:
#                 print("Ivedete pajamu suma neteisingai, bandykite dar karta.")
#                 continue

            
#         elif pasirinkimas == 2:
#             try:
#                 islaidu_suma = float(input("Iveskite islaidu suma: "))
#                 budas = input("Iveskite atsiskaitymo buda (pvz.: grynais, kortele): ")
#                 preke = input("Iveskite kliento isigyta preke/paslauga: ")
#                 biudzetas.prideti_islaidu_irasa(islaidu_suma, budas, preke)
#                 print(
#                     f"{"-"*50}\n"
#                     f"Islaidos {islaidu_suma} Eur pridetos i biudzeta.\n"
#                     f"{"-"*50}\n"
#                         ) 
#             except ValueError:
#                 print("Ivedete islaidu suma neteisingai, bandykite dar karta.")
#                 continue

        
#         elif pasirinkimas == 3:
#             print(biudzetas.gauti_balansa())

#         elif pasirinkimas == 4:
#             biudzetas.parodyti_ataskaita()
        
#         elif pasirinkimas == 5:
#             break
            
# b = Biudzetas()

# paleisti_meniu(b)