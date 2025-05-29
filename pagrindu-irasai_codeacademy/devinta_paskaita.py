# ______________________________________
#Funkicjos
# ______________________________________

# def test():
#     print("bandau pakelti kvadratu")
#     print(1)
#     print(2)
#     print(3)
 
 
# print("pradzia")
 
# test()
# test()
 
# for i in range(1000):
#     test()
 
# print("pabaiga")
 
 
# def pakelk_kvadratu(skaicius):
#     result = skaicius ** 2
#     print(result)
#     print("end of function")
 
 
 
 
# pakelk_kvadratu(5.5)
 
 
 
# for i in range(100):
#     pakelk_kvadratu(i)
 
 
# def vardas_graziai(vardas):
#     print('*'*30)
#     print(vardas)
#     print('*'*30)
 
 
 
 
# list_of_names = ["Paulius","Rokas", "Tomas", "Jonas", "Diana"]
 
# for name in list_of_names:
#     vardas_graziai(name)
 
 
# def pakelk_kvadratu_su_return(skaicius):
#     result = skaicius ** 2
#     return result
 


# ats = pakelk_kvadratu_su_return(5)
 
# print(f"Kvadratu: {ats}")
# _______________________________________________________________________________________________
# Sukurkite 4 matematines funkcijas kurios gražina atsakymus (sudetis, atimtis, daugyba, dalyba)

# def pridejimas(a, b):
#     rezultatas = a + b
#     return rezultatas

# print(pridejimas(2, 3))


# def minus(a, b):
#     rezultatas = a - b
#     return rezultatas

# print(minus(3, 2))

# def dalyba(a, b):
#     if b == 0:
#         print("dalyba negalima is 0")
#         return
#     rezultatas = a/b
#     return rezultatas

# print(dalyba(4, 2))

# def daugyba(a, b):
#     rezultatas = a*b
#     return rezultatas

# print(daugyba(4, 2))

# ______________________________________________

# Sukurkite Funkcija kuri grąžina didesnį iš dviejų paduotų skaičių.


# def did_graz(a, b):
#     if a > b:
#         atsakymas = f"{a} yra didesnis"
#     elif a < b:
#         atsakymas = f"{b} yra didesnis"
#     else:
#         atsakymas = f"{a} yra lygus {b}"
#     return atsakymas

# print(f"atsakymas: {did_graz(1, 1)}")

# __________________________________________________

# Funkcija kuri apskaičiuoja stačiakampio plotą.
# def plotas(plotis, ilgis):
#     rez = plotis*ilgis
#     return rez
# print(plotas(5, 7))

# __________________________________________________
# Funkcija kuri apskaičiuoja trijų skaičių vidurkį.

# def skaiciu_vid(sk1, sk2, sk3):
#     rezultatas = (sk1+sk2+sk3)/3
#     return rezultatas
# print(skaiciu_vid(2, 5, 8))

# __________________________________________________
# Patikrinti ar skaičius lyginis
# def ar_lyg(sk):
#     if sk % 2 == 0:
#         rez = "Lyginis"
#     else:
#         rez = "Nelyginis"
#     return rez
# print(ar_lyg(2))

# __________________________________________________
# Funkcija kuri suskaičiuoja, kiek kartų nurodyta raidė pasikartoja tekste.


# def simb_tekst(tekstas, raide):
#     kiekis = 0
#     for i in tekstas:
#         if i == raide:
#             kiekis += 1
#     return kiekis

# tekstas = "labas ka tu ka vakare"
# raide = "a"
# rezultatas = simb_tekst(tekstas, raide)
# print(rezultatas)


# def vardu_sujungimas(vardas1, vardas2, sujungimo_simbolis=" "): #default kintamieji(nebutinieji argument) turi būti gale
#     result = vardas1 + sujungimo_simbolis + vardas2
#     return result
 
 
# ats = vardu_sujungimas("Rokas", "Paulius", "---")
# print(ats)
 
# ats = vardu_sujungimas("Rokas", "Paulius")
# print(ats)
 
 
# def vardu_sujungimas(vardas1, vardas2, sujungimo_simbolis=" ", galutinis_simbolis = "."): #default kintamieji(nebutinieji argument) turi būti gale
#     result = vardas1 + sujungimo_simbolis + vardas2 + galutinis_simbolis
#     return result
 
 
# ats = vardu_sujungimas("Rokas", "Paulius")
# print(ats)
 
# ats = vardu_sujungimas("Rokas", "Paulius", "---")
# print(ats)
 
# ats = vardu_sujungimas("Rokas", "Paulius", "---", "*")
# print(ats)
 
# ats = vardu_sujungimas("Rokas", "Paulius", galutinis_simbolis="+/+")
# print(ats)
 
# ats = vardu_sujungimas("Rokas", "Paulius", galutinis_simbolis="+/+", sujungimo_simbolis="///")
# print(ats)


# __________________________________________________
# NAMU DARBAI
# __________________________________________________

# Sukurkite funkciją, kuri sveikina vartotoją. Funkcija turi priimti vartotojo vardą kaip privalomą parametrą ir pasveikinimo tekstą kaip neprivalomą parametrą. 
# Jeigu pasveikinimo tekstas nenurodytas, naudokite numatytąjį tekstą "Labas".
 
# def sveikinimas(vart_v, pasveik="labas"):
#     return f"{pasveik}, {vart_v}!"
# vart_ivest = str(input("iveskite savo varda: "))
# print(sveikinimas(vart_ivest))

# __________________________________________________

# Sukurkite funkciją, kuri apskaičiuoja prekės kainą su PVM. 
# Funkcija turi priimti prekės kainą kaip privalomą parametrą ir PVM tarifą kaip neprivalomą parametrą. Jeigu PVM tarifas nenurodytas, naudokite 21%.

# def pvmas(prek_k, tarifas="21"):
#     rezultatas = prek_k + (prek_k/100*int(tarifas))
#     return rezultatas

# vart_ivest = float(input("iveskite prekes kaina: "))
# vart_ivest2 = input("iveskite pvm tarifa (nenurodzius skaiciuos 21%): ")

# if vart_ivest2 == "":
#     print(f"prekes kaina su pvm: {pvmas(vart_ivest)} ")
# else:
#     print(f"prekes kaina su pvm: {pvmas(vart_ivest, vart_ivest2)} ")


# __________________________________________________
# Sukurkite funkciją, kuri pakelia skaičių nurodytu laipsniu. Funkcija turi priimti skaičių kaip privalomą parametrą ir laipsnį kaip neprivalomą parametrą. Jeigu laipsnis nenurodytas, kelkite kvadratu.


# def kelimas_laipsniu(skaicius, laipsnis=2):
#     rezultatas = skaicius ** laipsnis
#     return rezultatas

# vart_ivest = float(input("iveskite skaiciu, kuri kelsime laipsniu: "))
# vart_ivest2 = input("iveskite laipsni (nenurodzius kels kvadratu): ")

# if vart_ivest2 == "":
#     print(f"{vart_ivest} keliant kvadratu bus: {kelimas_laipsniu(vart_ivest)} ")
# else:
#     vart_ivest2 = float(vart_ivest2)
#     print(f"{vart_ivest} pakelus {vart_ivest2} laipsniu bus: {kelimas_laipsniu(vart_ivest, vart_ivest2)} ")

# __________________________________________________
# Sukurkite funkciją, kuri suformuoja vartotojo pilną vardą. 
# Funkcija turi priimti vardą ir pavardę kaip privalomus parametrus ir kreipinį (p., dr., prof.) kaip neprivalomą parametrą.

# def pilnas_vardas(vardas, pavarde, laipsnis=""):
#     if laipsnis != "":
#         return f"{laipsnis}, {vardas}, {pavarde}"
#     else:
#         return f"{vardas}, {pavarde}"
    
# vart_v = input("iveskite savo varda: ")
# vart_p = input("iveskite savo pavarde: ")
# vart_l = input("iveskite savo laipsni(nebutina): ")

# print(pilnas_vardas(vart_v, vart_p, vart_l))

# __________________________________________________
# Sukurkite funkciją, kuri apskaičiuoja atlyginimą atskaičius mokesčius. 
# Funkcija turi priimti atlyginimą "ant popieriaus" kaip privalomą parametrą ir mokesčių tarifą kaip neprivalomą parametrą. 
# Jeigu mokesčių tarifas nenurodytas, naudokite 20%.

# def atlyg_rank(atlyg, tarifas="20"):
#     rezultatas = atlyg - (atlyg/100*int(tarifas))
#     return rezultatas

# vart_ivest = float(input("iveskite atlyginima ant popieriaus: "))
# vart_ivest2 = input("iveskite mokesciu tarifa (nenurodzius skaiciuos 20%): ")

# if vart_ivest2 == "":
#     print(f"prekes kaina su pvm: {atlyg_rank(vart_ivest)} ")
# else:
#     print(f"prekes kaina su pvm: {atlyg_rank(vart_ivest, vart_ivest2)} ")

# __________________________________________________
# Sukurkite funkciją, kuri generuoja sąrašą skaičių nuo pradžios iki pabaigos. 
# Funkcija turi priimti pabaigos skaičių kaip privalomą parametrą ir pradžios skaičių bei žingsnį kaip neprivalomus parametrus. 
# Jeigu pradžios skaičius nenurodytas, pradėkite nuo 0. Jeigu žingsnis nenurodytas, naudokite 1.

# def skaiciu_sar_gen(pabaiga, pradzia=0, zingsnis=1):
#     sarasas = []
#     while pradzia <= pabaiga:
#         sarasas.append(pradzia)
#         pradzia += 1
#     sarasas = sarasas[::zingsnis]
#     return(sarasas)

# vart_pradzia = int(input("iveskite skaiciu nuo ko pradesime: "))

# vart_pabaiga = int(input("iveskite skaiciu kur pabaigsime: "))

# vart_zingsnis = input("iveskite kaip sarasa formuosime (paeiliui, kas antra, atvirksciai)")
# if vart_zingsnis == "paeiliui":
#     vart_zingsnis_konvert = int(1)
# elif vart_zingsnis == "kas antra": 
#     vart_zingsnis_konvert = int(2)
# elif vart_zingsnis == "atvirksciai": 
#     vart_zingsnis_konvert = int(-1)

# print(skaiciu_sar_gen(vart_pabaiga,vart_pradzia,vart_zingsnis_konvert))

# __________________________________________________
# Sukurkite funkciją, kuri apkerpa tekstą iki nurodyto ilgio. 
# Funkcija turi priimti tekstą kaip privalomą parametrą ir maksimalų ilgį bei pabaigos simbolius kaip neprivalomus parametrus. 
# Jeigu maksimalus ilgis nenurodytas, naudokite 10. Jeigu pabaigos simboliai nenurodyti, naudokite "
 
# UZDUPTIS ATLIKTA SU KLAIDA

# def teksto_apkirpimas(tekstas, maksimalus=10, apkirpimas='"'):
#     if len(tekstas) <= maksimalus:
#         return tekstas
#     else:
#         return tekstas[:maksimalus+1] + apkirpimas
    
# vart_tekstas = input("Iveskite norima teksta: ")
# vart_max = input("Iveskite kiek simboliu reikia (nebutinas, numatytas = 10): ")

# vart_atskirimas = input("Iveskite kokiu simboliu atskirti(nebutina): ")

# if vart_max and vart_atskirimas == "":
#     print(teksto_apkirpimas(vart_tekstas, int(vart_max)))
# elif vart_max == "":
#     print(teksto_apkirpimas(vart_tekstas, 10, vart_atskirimas))
# elif vart_atskirimas =="":
#     print(teksto_apkirpimas(vart_tekstas, int(vart_max),))
# else:
#     print(teksto_apkirpimas(vart_tekstas))


# __________________________________________________
# Sukurkite funkciją, kuri priima skaičių sąrašą ir grąžina jų kvadratų sąrašą.

# def saraso_kelimas(vart_sarasas):
#     sarasas = []
#     for skaicius in vart_sarasas:
#         sarasas.append(skaicius ** 2)
#     return sarasas

# ivestis = input("iveskite skaicius, atskirtus kableliais (be tarpu): ")
# skaiciai = ivestis.split(",")
# skaiciai_skaiciais = []

# for x in skaiciai:
#     skaicius = int(x)
#     skaiciai_skaiciais.append(skaicius)

# print(saraso_kelimas(skaiciai_skaiciais))
    
# __________________________________________________
# Parašykite funkciją, kuri priima vartotojo vardą ir spausdina sveikinimo žinutę, pvz., "Labas, Jonas!".

# def pasveikimas(vardas):
#     rezultatas = f"Labas, {vardas}!"
#     return rezultatas

# vart_v = input("iveskite savo varda: ")
# print(pasveikimas(vart_v))

# __________________________________________________
# Sukurkite funkcija, kuri turi ciklą for, kuris atspausdina skaičius nuo 1 iki 10.

# def spausdinti_skaicius():
#     for skaicius in range(1, 11):
#         print(skaicius)

# spausdinti_skaicius()

# __________________________________________________
# Parašyk funkciją, kuri tikrina, ar duotas skaičius yra teigiamas, neigiamas, ar lygus nuliui.

def patikrinimas(sk):
    if sk < 0:
        sk = "neigiamas"
    elif sk == 0:
        sk = "lygus nuliui"
    else:
        sk = "teigiamas"
    return sk

vart_sk = int(input("iveskite norima skaiciu: "))
print(patikrinimas(vart_sk))

# __________________________________________________
# Parašyk funkciją, kuri gauna sąrašą ir grąžina sąrašo elementų kiekį.
# __________________________________________________

