from random import randint
class Auto:
    def __init__(self, rekisteritunnus: str, huippunomeus: int):
        self.rekitesteritunnus = rekisteritunnus

        self.huippunomeus = huippunomeus # given in km/h

        self.nykyinen_nopeus = 0

        self.kuljettu_matka = 0

    def kiihdytä(self, nopeus: int):
        if nopeus < 0:
            if self.nykyinen_nopeus + nopeus < 0:
                self.nykyinen_nopeus = 0
            else:
                self.nykyinen_nopeus += nopeus
        elif self.nykyinen_nopeus + nopeus >= self.huippunomeus:
            self.nykyinen_nopeus = self.huippunomeus
        else:
            self.nykyinen_nopeus += nopeus

    def kulje(self, tunteja:float):
        self.kuljettu_matka += (self.nykyinen_nopeus * tunteja)


class Kilpailu:
    def __init__(self, nimi:str, pituus:float, annetut_autot:dict):
        self.kilpailun_nimi = nimi
        self.kilpailun_pituus = pituus
        self.kilpailijat = annetut_autot
        self.aika_maara = 0
    def tunti_kuluu(self):
        if not kilpailu_ohi():
            for car in self.kilpailijat.values():
                car.kiihdytä(randint(-10, 15))
                car.kulje(1)

    def kilpailu_ohi(self):
        for car in self.kilpailijat.values():
            if car.kuljettu_matka >= self.kilpailun_pituus:
                return True


autot = {}
for i in range(1, 11):
    autot[i] = Auto(f"ABC-{i}", randint(100, 200))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)