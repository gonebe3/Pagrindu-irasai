import uuid

class Knyga(): #Klases paskirtis = laikyti viso info apie viena atskira knyga ir automatiskas id priskirimas su uuid
    def __init__(self, pavadinimas, autorius, metai, zanras, turimas_kiekis, paimtas_kiekis):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.metai = metai
        self.zanras = zanras
        self.turimas_kiekis = turimas_kiekis
        self.paimtas_kiekis = paimtas_kiekis
        self.unikalus_id = str(uuid.uuid4())

    def likutis(self):
        return self.turimas_kiekis - self.paimtas_kiekis

    def __str__(self):
        return f"| Pavadinimas: {self.pavadinimas} | Autorius: {self.autorius} | Zanras: {self.zanras} | Isleidimo metai: {self.metai} | Knygu kiekis: {self.turimas_kiekis} | Paimtu knygu kiekis: {self.paimtas_kiekis} | Unikalus knygos ID: {self.unikalus_id} | Dabartinis likutis: {self.likutis()} | "

    def __repr__(self):
        return f"Knyga('{self.pavadinimas}', '{self.autorius}', '{self.zanras}', {self.metai}, {self.turimas_kiekis}, {self.paimtas_kiekis}, {self.unikalus_id}, Likutis: {self.likutis()})"
    
    def ar_yra_laisvu(self):
        return self.likutis() > 0