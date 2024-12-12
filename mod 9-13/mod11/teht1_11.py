
class Julkaisu:
    def __init__(self, nimi:str):
        self.nimi =  nimi

class Kirja(Julkaisu):
    def __init__(self, nimi: str, kirjoittaja: str, sivumaara: int):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}\n")

class Lehti(Julkaisu):
    def __init__(self, nimi: str, paatoimittaja: str):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}\n")


test = Lehti("Aku Ankka", "Aki Hyyppä")
test1 = Kirja("Hytti n:o6", "Rosa Liksom", 200)

test.tulosta_tiedot()
test1.tulosta_tiedot()