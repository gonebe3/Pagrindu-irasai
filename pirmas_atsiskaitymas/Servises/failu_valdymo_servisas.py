import pickle
import os

def issaugoti_duomenis(objektas, failo_vardas): # iraso i Pickle objekta(kintamaji) i faila(kintamaji)
    try:
        with open(failo_vardas, 'wb') as f:
            pickle.dump(objektas, f)
        return True
    except Exception as e:
        print(f"Klaida įrašant duomenis į {failo_vardas}: {e}")
        return False

def ikelti_duomenis(failo_vardas): # Ikelia objektus is failo, jei failo nera, grazina tuscia sarasa
    try:
        with open(failo_vardas, 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError):
        return []
    except Exception as e:
        print(f"Klaida įkeliant duomenis iš {failo_vardas}: {e}")
        return []

def trinti_duomenu_faila(failo_vardas): #pasalina visa faila 
    try:
        os.remove(failo_vardas)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"Klaida trinant failą {failo_vardas}: {e}")
        return False