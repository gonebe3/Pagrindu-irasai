# Pagrindinis meniu failas: main.py #python -m pirmas_atsiskaitymas.main
# Importuojame servisus ir klases is tavo projekto struktūros
from pirmas_atsiskaitymas.Servises.Knygu_servisas import *
from pirmas_atsiskaitymas.Servises.Skaitytoju_servisas import *
from pirmas_atsiskaitymas.Servises.Bibliotekininko_servisas import *
from pirmas_atsiskaitymas.Servises.failu_valdymo_servisas import ikelti_duomenis, issaugoti_duomenis
from pirmas_atsiskaitymas.Classes.Knyga import Knyga

# Colorama spalvos: pravers grazesniam meniu atvaizdavimui
try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)
    COLORAMA = True
except ImportError:
    COLORAMA = False

def spalva(tekstas, spalva="yellow"):
    """Gražina spalvotą tekstą jei įmanoma."""
    if not COLORAMA:
        return tekstas
    spalvos = {
        "yellow": Fore.YELLOW,
        "green": Fore.GREEN,
        "red": Fore.RED,
        "blue": Fore.BLUE,
        "cyan": Fore.CYAN,
        "magenta": Fore.MAGENTA,
        "white": Fore.WHITE
    }
    return spalvos.get(spalva, Fore.YELLOW) + tekstas + Style.RESET_ALL

def bruksnys():
    """Meniu atskyrimui, kad viskas butu aiskiu blokais"""
    print(spalva("-"*60, "cyan"))

# Ikeliami duomenys is failu arba gaunami tusci sarasai jei failo nera
knygos = ikelti_duomenis("knygos.pickle")
skaitytojai = ikelti_duomenis("skaitytojai.pickle")
bibliotekininkai = ikelti_duomenis("bibliotekininkai.pickle")

def issaugoti_viska():
    """Issaugo visus objektus i failus."""
    issaugoti_duomenis(knygos, "knygos.pickle")
    issaugoti_duomenis(skaitytojai, "skaitytojai.pickle")
    issaugoti_duomenis(bibliotekininkai, "bibliotekininkai.pickle")

def pagrindinis_meniu():
    """Pagrindinis meniu: galima prisijungti kaip skaitytojas, bibliotekininkas arba uzregistruoti bibliotekininka."""
    while True:
        bruksnys()
        print(spalva("--- BIBLIOTEKOS SISTEMA ---", "magenta"))
        print("1. Prisijungti kaip skaitytojas")
        print("2. Prisijungti kaip bibliotekininkas")
        print("3. Registruoti bibliotekininka")
        print("4. Baigti darba")
        bruksnys()
        pasirinkimas = input(spalva("Pasirinkite veiksma: ", "yellow"))
        if pasirinkimas == "1":
            skaitytojo_meniu()
        elif pasirinkimas == "2":
            bibliotekininko_meniu()
        elif pasirinkimas == "3":
            registruoti_bibliotekininka_view()
        elif pasirinkimas == "4":
            issaugoti_viska()
            print(spalva("\nDuomenys issaugoti. Iki!", "green"))
            bruksnys()
            break
        else:
            print(spalva("Neteisingas pasirinkimas. Bandykite dar karta.", "red"))

def registruoti_skaitytoja_view():
    """Tik bibliotekininkas gali registruoti nauja skaitytoja"""
    bruksnys()
    print(spalva("-- Naujo skaitytojo registracija --", "cyan"))
    while True:
        vardas = input("Iveskite varda ('q' - grizti): ")
        if vardas.lower() == "q":
            return
        pavarde = input("Iveskite pavarde: ")
        kontaktai = input("Kontaktai (el. pastas arba tel. nr.): ")
        if vardas and pavarde and kontaktai:
            naujas = registruoti_skaitytoja(skaitytojai, vardas, pavarde, kontaktai)
            issaugoti_viska()
            print(spalva(f"Skaitytojas uzregistruotas! Korteles numeris: {naujas.korteles_numeris}", "green"))
            bruksnys()
            return
        else:
            print(spalva("Visi laukai privalomi. Bandykite dar karta.", "red"))

def registruoti_bibliotekininka_view():
    """Leidzia uzregistruoti nauja bibliotekininka is pagrindinio meniu"""
    bruksnys()
    print(spalva("-- Naujo bibliotekininko registracija --", "cyan"))
    while True:
        vardas = input("Iveskite varda ('q' - grizti): ")
        if vardas.lower() == "q":
            return
        pavarde = input("Iveskite pavarde: ")
        vartotojo_vardas = input("Sukurkite prisijungimo varda: ")
        slaptazodis = input("Sukurkite slaptazodi: ")
        if vardas and pavarde and vartotojo_vardas and slaptazodis:
            naujas = registruoti_bibliotekininka(bibliotekininkai, vardas, pavarde, vartotojo_vardas, slaptazodis)
            issaugoti_viska()
            print(spalva(f"Bibliotekininkas uzregistruotas! Prisijungimo vardas: {naujas.vartotojo_vardas}", "green"))
            bruksnys()
            return
        else:
            print(spalva("Visi laukai privalomi. Bandykite dar karta.", "red"))

def skaitytojo_meniu():
    """Skaitytojo meniu: prisijungiama pagal korteles numeri"""
    while True:
        bruksnys()
        korteles_nr = input(spalva("Iveskite savo skaitytojo korteles numeri (arba 'q' - grizti): ", "yellow"))
        if korteles_nr.lower() == 'q':
            return
        skaitytojas = ieskoti_skaitytojo_pagal_kortele(skaitytojai, korteles_nr)
        if skaitytojas:
            break
        print(spalva("Skaitytojas nerastas. Patikrinkite numeri arba kreipkites i bibliotekininka.", "red"))
    while True:
        bruksnys()
        print(spalva(f"Skaitytojo meniu ({skaitytojas.vardas} {skaitytojas.pavarde})", "magenta"))
        print("1. Mano paimtos knygos")
        print("2. Paimti nauja knyga")
        print("3. Grazinti knyga")
        print("4. Velyuojancios knygos")
        print("5. Atgal")
        bruksnys()
        pasirinkimas = input(spalva("Pasirinkite veiksma: ", "yellow"))
        if pasirinkimas == "1":
            bruksnys()
            print(spalva("-- Jusu paimtos knygos --", "cyan"))
            for knyga in skaitytojas.visos_imtos_knygos():
                print(knyga)
            bruksnys()
        elif pasirinkimas == "2":
            pavadinimas = input("Iveskite knygos pavadinima (arba jo dali, 'q' - grizti): ")
            if pavadinimas.lower() == "q":
                continue
            galimos = ieskoti_pagal_pavadinima(knygos, pavadinimas)
            if not galimos:
                print(spalva("Knygu nerasta.", "red"))
            else:
                print(spalva("Galimos knygos:", "cyan"))
                for idx, kn in enumerate(galimos):
                    print(f"{idx+1}. {kn}")
                while True:
                    try:
                        nr = input("Pasirinkite kuri knyga paimti (numeris, 'q' - grizti): ")
                        if nr.lower() == "q":
                            break
                        nr = int(nr) - 1
                        if nr < 0 or nr >= len(galimos):
                            raise IndexError
                        pasirinkta = galimos[nr]
                        rez = prideti_knyga_skaitytojui(skaitytojas, pasirinkta)
                        if rez is True:
                            print(spalva("Knyga paimta sekmingai!", "green"))
                            issaugoti_viska()
                        elif rez == "veluoja":
                            print(spalva("Negalima imti knygos, nes turite veluojanciu knygu.", "red"))
                        elif rez == "nera_laisvu":
                            print(spalva("Nera laisvu egzemplioriu.", "red"))
                        break
                    except (ValueError, IndexError):
                        print(spalva("Blogas pasirinkimas. Bandykite dar karta.", "red"))
        elif pasirinkimas == "3":
            negr = [k for k in skaitytojas.visos_imtos_knygos() if not k["Ar_grazinta"]]
            if not negr:
                print(spalva("Neturite negrazintu knygu.", "yellow"))
            else:
                for idx, k in enumerate(negr):
                    print(f"{idx+1}. {k}")
                while True:
                    try:
                        nr = input("Kuria knyga grazinti (numeris, 'q' - grizti): ")
                        if nr.lower() == "q":
                            break
                        nr = int(nr) - 1
                        if nr < 0 or nr >= len(negr):
                            raise IndexError
                        knygos_id = negr[nr]["Knygos_ID"]
                        kn_obj = next((kn for kn in knygos if kn.unikalus_id == knygos_id), None)
                        if kn_obj and grazinti_knyga_skaitytojui(skaitytojas, kn_obj):
                            print(spalva("Knyga grazinta sekmingai!", "green"))
                            issaugoti_viska()
                        else:
                            print(spalva("Grazinimas nepavyko.", "red"))
                        break
                    except (ValueError, IndexError):
                        print(spalva("Blogas pasirinkimas. Bandykite dar karta.", "red"))
        elif pasirinkimas == "4":
            veluojancios = skaitytojas.veluojancios_knygos()
            if not veluojancios:
                print(spalva("Velyuojanciu knygu nera.", "green"))
            else:
                print(spalva("Velyuojancios knygos:", "red"))
                for kn in veluojancios:
                    print(kn)
            bruksnys()
        elif pasirinkimas == "5":
            bruksnys()
            return
        else:
            print(spalva("Neteisingas pasirinkimas.", "red"))

def bibliotekininko_meniu():
    """Bibliotekininko meniu su prisijungimu ir galimomis funkcijomis"""
    while True:
        bruksnys()
        vartotojo_vardas = input(spalva("Iveskite vartotojo varda (arba 'q' - grizti): ", "yellow"))
        if vartotojo_vardas.lower() == "q":
            return
        slaptazodis = input("Iveskite slaptazodi: ")
        bibliotekininkas = autentifikuoti_bibliotekininka(bibliotekininkai, vartotojo_vardas, slaptazodis)
        if bibliotekininkas:
            break
        print(spalva("Neteisingi prisijungimo duomenys. Bandykite dar karta arba iveskite 'q' grizimui.", "red"))
    while True:
        bruksnys()
        print(spalva(f"Bibliotekininko meniu ({bibliotekininkas.vardas} {bibliotekininkas.pavarde})", "magenta"))
        print("1. Prideti nauja knyga")
        print("2. Pasalinti knyga pagal ID")
        print("3. Pasalinti senas knygas pagal metus")
        print("4. Perziureti visas knygas")
        print("5. Perziureti visus skaitytojus")
        print("6. Registruoti nauja skaitytoja")
        print("7. Statistika")
        print("8. Atgal")
        bruksnys()
        pasirinkimas = input(spalva("Pasirinkite veiksma: ", "yellow"))
        if pasirinkimas == "1":
            pavadinimas = input("Pavadinimas: ")
            autorius = input("Autorius: ")
            try:
                metai = int(input("Isleidimo metai: "))
                zanras = input("Zanras: ")
                kiekis = int(input("Knygu kiekis: "))
                prideti_knyga(knygos, pavadinimas, autorius, metai, zanras, kiekis)
                issaugoti_viska()
                print(spalva("Knyga prideta.", "green"))
            except Exception:
                print(spalva("Blogas ivesties formatas.", "red"))
        elif pasirinkimas == "2":
            id = input("Iveskite knygos ID: ")
            if pasalinti_knyga(knygos, id):
                issaugoti_viska()
                print(spalva("Knyga pasalinta.", "green"))
            else:
                print(spalva("Knyga nerasta.", "red"))
        elif pasirinkimas == "3":
            try:
                metai = int(input("Pasalinti visas knygas isleistos pries metus (pvz., 2000): "))
                kiek = pasalinti_senas_knygas(knygos, metai)
                issaugoti_viska()
                print(spalva(f"Pasalinta {kiek} knygu.", "green"))
            except Exception:
                print(spalva("Blogas ivesties formatas.", "red"))
        elif pasirinkimas == "4":
            print(spalva("-- Visos bibliotekos knygos --", "cyan"))
            for kn in knygos:
                print(kn)
                print(spalva("-"*200, "yellow"))
            bruksnys()
        elif pasirinkimas == "5":
            print(spalva("-- Visi skaitytojai --", "cyan"))
            for s in skaitytojai:
                print(s)
                print(spalva("-"*200, "yellow"))
            bruksnys()
        elif pasirinkimas == "6":
            registruoti_skaitytoja_view()
        elif pasirinkimas == "7":
            print(spalva("Populiariausi zanrai:", "yellow"))
            for zanras, kiekis in populiariausi_zanrai(knygos).most_common():
                print(f"{zanras}: {kiekis}")
            vidurkis = round(vidutinis_veluojanciu_kiekis(skaitytojai), 2)
            print(spalva(f"Vidutinis veluojanciu knygu kiekis skaitytojui: {vidurkis}", "yellow"))
            bruksnys()
        elif pasirinkimas == "8":
            bruksnys()
            return
        else:
            print(spalva("Neteisingas pasirinkimas.", "red"))

if __name__ == "__main__":
    pagrindinis_meniu()

