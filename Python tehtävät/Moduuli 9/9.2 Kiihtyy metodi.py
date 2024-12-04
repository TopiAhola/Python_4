'''Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan
nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin
on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa
huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden
muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.'''

class Auto:

    määrä = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

        Auto.määrä += 1

    def tiedot(self):

        tieto = [self.rekisteritunnus,
                  self.huippunopeus,
                  self.nopeus,
                  self.matka]

        return tieto

    def kiihdytä(self, dV):

        self.nopeus = self.nopeus + dV
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        print(f"Vauhti kiihtyy {dV}km/h")

        return




auto1 = Auto("ABC-123", 142)
#print(auto1.tiedot())


auto1.kiihdytä(30)
print(f"Nopeus on {auto1.nopeus}km/h")

auto1.kiihdytä(70)
print(f"Nopeus on {auto1.nopeus}km/h")

auto1.kiihdytä(50)
print(f"Nopeus on {auto1.nopeus}km/h")

auto1.kiihdytä(-200)
print(f"Nopeus on {auto1.nopeus}km/h")



