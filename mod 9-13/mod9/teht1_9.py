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


car = Auto("ABC-123", 142)

#car.kiihdytä(30)
#car.kiihdytä(70)
#car.kiihdytä(41)
#print(car.nykyinen_nopeus)
#car.kiihdytä(-200)
#print(car.nykyinen_nopeus)

#car.kiihdytä(60)
#car.kulje(1.5)
#print(car.kuljettu_matka)

autot = {}

for i in range(1,11):
    autot[i] = Auto(f"ABC-{i}",randint(100,200))
run = True
while run:
    for auto_numero, auto in autot.items():
        auto.kiihdytä(randint(-10,15))
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            print(f"Auto {auto_numero} voitti! Huippunopeus oli {auto.huippunomeus} ja kuljettu matka oli {auto.kuljettu_matka}.")
            run = False
            break

for k,v in autot.items():
    print("Autonumero:",k)
    print("Ominaisuudet:")
    print(f"Kilometriä kuljettu: {v.kuljettu_matka}\nHuippunopeus: {v.huippunomeus}km/h\nNykyinen nopeus: {v.nykyinen_nopeus}km/h\n")