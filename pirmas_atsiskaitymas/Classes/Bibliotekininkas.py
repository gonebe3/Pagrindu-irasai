class Bibliotekininkas():
    def __init__ (self, vardas, pavarde, vartotojo_vardas, slaptazodis):
        self.vardas = vardas
        self.pavarde = pavarde
        self.vartotojo_vardas = vartotojo_vardas
        self.slaptazodis = slaptazodis

    def __str__(self):
        return f"Bibliotekininkas: {self.vardas} {self.pavarde} ({self.vartotojo_vardas})"

    def __repr__(self):
        return (f"Bibliotekininkas(vardas={self.vardas}, pavarde={self.pavarde}, "
                f"vartotojo_vardas={self.vartotojo_vardas})")