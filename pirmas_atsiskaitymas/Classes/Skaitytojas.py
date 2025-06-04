import uuid
from datetime import datetime, timedelta

class Skaitytojas(): #Saugo skaitytojo duomenis ir informacija apie paimtas knygas. 
    def __init__(self, vardas, pavarde, kontaktai, paimtos_knygos=None,): #naudojame None, kad isvengti mutable defalult argument bug'o 
        self.vardas = vardas
        self.pavarde = pavarde
        self.kontaktai = kontaktai
        self.paimtos_knygos = paimtos_knygos if paimtos_knygos is not None else []
        self.korteles_numeris = str(uuid.uuid4())

    def prideti_paimta_knyga(self, knygos_id, paemimo_data=None, grazinti_iki=None): #Prideda nauja paimta knyga i sarasa (visada kaip nauja irasa)
        try:
            paemimo_data = paemimo_data if paemimo_data is not None else datetime.now()
            grazinti_iki = grazinti_iki if grazinti_iki is not None else paemimo_data + timedelta(days=30)
            knygos_zodynas = {"Knygos_ID" : knygos_id, "Paemimo_data" : paemimo_data, "Grazinti_iki" : grazinti_iki, "Ar_grazinta" : False} # is karto nurodome paemus knyga ar_grazinta kaip False
            self.paimtos_knygos.append(knygos_zodynas)
        except Exception as E:
            print(f"Ivyko nenumatyta klaida: {E}, bandykite dar karta")


    def knygos_grazinimas(self, knygos_id): #Pazymi knyga (pagal ID) kaip grazinta.
        for knyga in self.paimtos_knygos:
            if knyga["Knygos_ID"] == knygos_id:
                if knyga["Ar_grazinta"]: # if its True
                    return False  # jau grazinta
                knyga["Ar_grazinta"] = True # if its False
                return True
        return False # jeigu nerado, grazina False
    
    def veluojancios_knygos(self): #grazina visu veluojanciu knygu sarasa
        return [knyga for knyga in self.paimtos_knygos
            if not knyga["Ar_grazinta"] and knyga["Grazinti_iki"] < datetime.now()] # is karto i sarasa papildo knyga, jeigu Ar_grazinta yra False ir jeigu grazinimo_data yra praeityje

    def visos_imtos_knygos(self): # grazina visu grazintu ir ne knygu sarasa
        return self.paimtos_knygos

    def __str__(self):
        return (f"Skaitytojas: {self.vardas}, {self.pavarde} | Korteles numeris: {self.korteles_numeris} | Paimtu knygu kiekis: {len(self.paimtos_knygos)} | Kontaktai {self.kontaktai}")
    
    def __repr__(self):
        return (f"Skaitytojas(vardas={self.vardas}), pavarde={self.pavarde}"
                f"Kontaktai={self.kontaktai}"
                f"paimtos_knygos={self.paimtos_knygos}"
                f"veluojancios_knygos={self.veluojancios_knygos}"
                f"korteles_numeris={self.korteles_numeris}")












