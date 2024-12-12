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


class SähköAuto(Auto):
    def __init__(self, rekisteritunnus: str, huippunomeus: int, akku_kapasiteetti: float):
        super().__init__(rekisteritunnus, huippunomeus)

        self.akku_kapasiteetti = akku_kapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus: str, huippunomeus: int, bensatankin_koko: float):
        super().__init__(rekisteritunnus, huippunomeus)

        self.bensatankin_koko = bensatankin_koko

sahko = SähköAuto("ABC-15", 180, 52.5)

poltto = Polttomoottoriauto("ABC-15", 165, 32.3)

sahko.kiihdytä(150)
poltto.kiihdytä(150)

sahko.kulje(3)
poltto.kulje(3)

print(sahko.kuljettu_matka, poltto.kuljettu_matka)
