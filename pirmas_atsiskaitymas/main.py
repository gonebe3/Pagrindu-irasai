# Pagrindinis meniu failas: main.py 
# Naudotojo prisijungimas: c70f6cd0-28c5-4114-9739-946251a71ca1


from Servises.db_servisas import *
from Classes.Knyga import Knyga
from Classes.Skaitytojas import Skaitytojas
from Classes.Bibliotekininkas import Bibliotekininkas

# Colorama - grazesniam meniu
try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)
    COLORAMA = True
except ImportError:
    COLORAMA = False

def spalva(tekstas, spalva="yellow"):
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
    print(spalva("-"*60, "cyan"))

def pagrindinis_meniu():
    inicijuoti_db()
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
            print(spalva("\nIki!", "green"))
            break
        else:
            print(spalva("Neteisingas pasirinkimas.", "red"))

def registruoti_bibliotekininka_view():
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
            try:
                b = Bibliotekininkas(vardas, pavarde, vartotojo_vardas, slaptazodis)
                prideti_bibliotekininka(b)
                print(spalva(f"Bibliotekininkas uzregistruotas! Prisijungimo vardas: {vartotojo_vardas}", "green"))
                bruksnys()
                return
            except Exception as e:
                print(spalva(f"Klaida: {e}", "red"))
        else:
            print(spalva("Visi laukai privalomi. Bandykite dar karta.", "red"))

def registruoti_skaitytoja_view():
    bruksnys()
    print(spalva("-- Naujo skaitytojo registracija --", "cyan"))
    while True:
        vardas = input("Iveskite varda ('q' - grizti): ")
        if vardas.lower() == "q":
            return
        pavarde = input("Iveskite pavarde: ")
        kontaktai = input("Kontaktai (el. pastas arba tel. nr.): ")
        if vardas and pavarde and kontaktai:
            try:
                s = Skaitytojas(vardas, pavarde, kontaktai)
                prideti_skaitytoja(s)
                print(spalva(f"Skaitytojas uzregistruotas! Korteles numeris: {s.korteles_numeris}", "green"))
                bruksnys()
                return
            except Exception as e:
                print(spalva(f"Klaida: {e}", "red"))
        else:
            print(spalva("Visi laukai privalomi. Bandykite dar karta.", "red"))

def skaitytojo_meniu():
    while True:
        bruksnys()
        korteles_nr = input(spalva("Iveskite savo skaitytojo korteles numeri (arba 'q' - grizti): ", "yellow"))
        if korteles_nr.lower() == 'q':
            return
        skaitytojas = gauti_skaitytoja_pagal_kortele(korteles_nr)
        if skaitytojas:
            break
        print(spalva("Skaitytojas nerastas. Patikrinkite numeri arba kreipkites i bibliotekininka.", "red"))
    while True:
        bruksnys()
        print(spalva(f"Skaitytojo meniu ({skaitytojas.vardas} {skaitytojas.pavarde})", "magenta"))
        print("1. Mano paimtos knygos")
        print("2. Paimti nauja knyga")
        print("3. Grazinti knyga")
        print("4. Veluojancios knygos")
        print("5. Visos bibliotekos knygos")
        print("6. Atgal")
        bruksnys()
        pasirinkimas = input(spalva("Pasirinkite veiksma: ", "yellow"))
        if pasirinkimas == "1":
            bruksnys()
            print(spalva("-- Jusu paimtos knygos --", "cyan"))
            pask = gauti_skaitytojo_pasiskolinimus(skaitytojas.korteles_numeris)
            if not pask:
                print(spalva("Neturite paimtu knygu.", "yellow"))
            else:
                for i, k in enumerate(pask, 1):
                    knyga = gauti_knyga_pagal_id(k[2])
                    print(f"{i}. Pavadinimas: {knyga.pavadinimas if knyga else 'Nerasta'}")
                    print(f"   Paemimo data: {k[3][:10]}")
                    print(f"   Grazinti iki: {k[4][:10]}")
                    print(f"   Ar grazinta : {'Taip' if k[5] else 'Ne'}")
                    print(spalva("-"*50, "cyan"))
        elif pasirinkimas == "2":
            pavadinimas = input("Iveskite knygos pavadinima (arba jo dali, 'q' - grizti): ")
            if pavadinimas.lower() == "q":
                continue
            galimos = ieskoti_knygu_pagal_pavadinima(pavadinimas)
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
                        if skaitytojas_turi_veluojanciu(skaitytojas.korteles_numeris):
                            print(spalva("Negalima imti knygos, nes turite veluojanciu knygu.", "red"))
                            break
                        if not ar_yra_laisvu_knygu(pasirinkta.unikalus_id):
                            print(spalva("Nera laisvu egzemplioriu.", "red"))
                            break
                        import uuid
                        from datetime import datetime, timedelta
                        paemimo_data = datetime.now()
                        grazinti_iki = paemimo_data + timedelta(days=30)
                        prideti_pasiskolinima(
                            skaitytojas.korteles_numeris, pasirinkta.unikalus_id, paemimo_data, grazinti_iki
                        )
                        print(spalva("Knyga paimta sekmingai!", "green"))
                        break
                    except (ValueError, IndexError):
                        print(spalva("Blogas pasirinkimas. Bandykite dar karta.", "red"))
        elif pasirinkimas == "3":
            pask = skaitytojo_negrązintos_knygos(skaitytojas.korteles_numeris)
            if not pask:
                print(spalva("Neturite negrazintu knygu.", "yellow"))
            else:
                for idx, k in enumerate(pask, 1):
                    knyga = gauti_knyga_pagal_id(k[2])
                    print(f"{idx}. Pavadinimas: {knyga.pavadinimas if knyga else 'Nerasta'}")
                    print(f"   Knygos ID     : {k[2]}")
                    print(f"   Paemimo data  : {k[3][:10]}")
                    print(f"   Grazinti iki  : {k[4][:10]}")
                    print(spalva("-"*50, "cyan"))
                while True:
                    try:
                        nr = input("Kuria knyga grazinti (numeris, 'q' - grizti): ")
                        if nr.lower() == "q":
                            break
                        nr = int(nr) - 1
                        if nr < 0 or nr >= len(pask):
                            raise IndexError
                        knygos_id = pask[nr][2]
                        if grazinti_knyga(skaitytojas.korteles_numeris, knygos_id):
                            print(spalva("Knyga grazinta sekmingai!", "green"))
                        else:
                            print(spalva("Grazinimas nepavyko.", "red"))
                        break
                    except (ValueError, IndexError):
                        print(spalva("Blogas pasirinkimas. Bandykite dar karta.", "red"))
        elif pasirinkimas == "4":
            pask = skaitytojo_negrązintos_knygos(skaitytojas.korteles_numeris)
            from datetime import datetime
            veluojancios = [k for k in pask if not k[5] and k[4] < datetime.now().isoformat()]
            if not veluojancios:
                print(spalva("Veluojanciu knygu nera.", "green"))
            else:
                print(spalva("Veluojancios knygos:", "red"))
                for idx, k in enumerate(veluojancios, 1):
                    knyga = gauti_knyga_pagal_id(k[2])
                    print(f"{idx}. Pavadinimas    : {knyga.pavadinimas if knyga else 'Nerasta'}")
                    print(f"   Grazinti iki  : {k[4][:10]}")
                    print(spalva("-"*50, "cyan"))
        elif pasirinkimas == "5":
            bruksnys()
            print(spalva("-- Visos bibliotekos knygos --", "cyan"))
            knygos = gauti_visas_knygas_db()
            if not knygos:
                print(spalva("Bibliotekoje nera nei vienos knygos.", "yellow"))
            else:
                for i, kn in enumerate(knygos, 1):
                    print(f"{i}. {kn}")
                    print(spalva("-"*50, "cyan"))
        elif pasirinkimas == "6":
            bruksnys()
            return
        else:
            print(spalva("Neteisingas pasirinkimas.", "red"))

def bibliotekininko_meniu():
    while True:
        bruksnys()
        vartotojo_vardas = input(spalva("Iveskite vartotojo varda (arba 'q' - grizti): ", "yellow"))
        if vartotojo_vardas.lower() == "q":
            return
        slaptazodis = input("Iveskite slaptazodi: ")
        bibliotekininkas = gauti_bibliotekininka_pagal_vartotojo_varda(vartotojo_vardas)
        if bibliotekininkas and bibliotekininkas.slaptazodis == slaptazodis:
            break
        print(spalva("Neteisingi prisijungimo duomenys.", "red"))
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
        print("8. Perziureti visas veluojancias knygas")
        print("9. Populiariausi zanrai pagal paemimus")
        print("10. Atgal")
        bruksnys()
        pasirinkimas = input(spalva("Pasirinkite veiksma: ", "yellow"))
        if pasirinkimas == "1":
            pavadinimas = input("Pavadinimas: ")
            autorius = input("Autorius: ")
            try:
                metai = int(input("Isleidimo metai: "))
                zanras = input("Zanras: ")
                kiekis = int(input("Knygu kiekis: "))
                k = Knyga(pavadinimas, autorius, metai, zanras, kiekis, 0)
                prideti_knyga(k)
                print(spalva("Knyga prideta.", "green"))
            except Exception:
                print(spalva("Blogas ivesties formatas.", "red"))
        elif pasirinkimas == "2":
            id = input("Iveskite knygos ID: ")
            pasalinti_knyga(id)
            print(spalva("Knyga pasalinta (jei buvo rasta).", "green"))
        elif pasirinkimas == "3":
            try:
                metai = int(input("Pasalinti visas knygas isleistos pries metus (pvz., 2000): "))
                kiek = pasalinti_senas_knygas(metai)
                print(spalva(f"Pasalinta {kiek} knygu.", "green"))
            except Exception:
                print(spalva("Blogas ivesties formatas.", "red"))
        elif pasirinkimas == "4":
            print(spalva("-- Visos bibliotekos knygos --", "cyan"))
            bruksnys()
            knygos = gauti_visas_knygas_db()
            for kn in knygos:
                print(kn)
                print(spalva("-"*50, "yellow"))
            bruksnys()
        elif pasirinkimas == "5":
            print(spalva("-- Visi skaitytojai --", "cyan"))
            bruksnys()
            skaitytojai = gauti_visus_skaitytojus_db()
            for s in skaitytojai:
                print(s)
                print(spalva("-"*50, "yellow"))
            bruksnys()
        elif pasirinkimas == "6":
            registruoti_skaitytoja_view()
        elif pasirinkimas == "7":
            print(spalva("Populiariausi zanrai:", "yellow"))
            for zanras, kiekis in populiariausi_zanrai():
                print(f"{zanras}: {kiekis}")
            vidurkis = round(vidutinis_veluojanciu_kiekis(), 2)
            print(spalva(f"Vidutinis veluojanciu knygu kiekis skaitytojui: {vidurkis}", "yellow"))
            bruksnys()
        elif pasirinkimas == "8":
            bruksnys()
            print(spalva("-- Visos veluojancios knygos --", "red"))
            veluojancios = gauti_veluojancias_knygas()
            if not veluojancios:
                print(spalva("Veluojanciu knygu nera.", "green"))
            else:
                for info in veluojancios:
                    print(f"Skaitytojas: {info['skaitytojas']}")
                    print(f"Pavadinimas: {info['pavadinimas']}")
                    print(f"Grazinti iki: {info['grazinti_iki'][:10]}")
                    print(spalva("-"*50, "cyan"))
            bruksnys()
        elif pasirinkimas == "9":
            print("Populiariausi zanrai pagal paemimus:")
            for zanras, kiekis in populiariausi_zanrai_pagal_paemimus():
                print(f"{zanras}: {kiekis}")
            bruksnys()
        elif pasirinkimas == "10":
            bruksnys()
            return
        else:
            print(spalva("Neteisingas pasirinkimas.", "red"))

if __name__ == "__main__":
    pagrindinis_meniu()

