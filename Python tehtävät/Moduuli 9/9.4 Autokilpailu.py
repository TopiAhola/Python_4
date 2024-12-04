'''Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti
nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta
auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h
väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.

Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.'''



# Luokkamääritelmä
class Auto:

    määrä = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

        Auto.määrä += 1

    def tiedot(self):

        tieto = [ self.rekisteritunnus,
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

        return

    def kulje(self, aika):

        d_matka = aika * self.nopeus
        self.matka = self.matka + d_matka

        return


# Importit
#PrettyTable lopputaulukon tulostusta varten
import random
from prettytable import PrettyTable


#toistorakenne toimi kun käytti dictionaryä
autot = {}
for n in range(1,11):

    rekisteri_tunnus = f"ABC-{n}"
    autot[n] = Auto(rekisteri_tunnus, random.randint(100, 200))

print("Autojen tiedot: ")
for a in autot:
    print(a, autot[a].tiedot())



matka = [0]
while max(matka) <= 10000:


    for a in autot:
        # nopeuden muutos arvotaan väliltä -10 ja +15 km/h
        d_nopeus = int(random.randint(-10,+15))
        autot[a].kiihdytä(d_nopeus)
        print(f"Auton {a} nopeus on {autot[a].nopeus}km/h")

    #kaikki autot kulkevat tunnin ajan
        autot[a].kulje(1)
        print(f" Auto {a} on kulkenut {autot[a].matka}km.")

    #listataan kuljetut matkat
        matka.append(autot[a].matka)


#lopuksi tulostetaan tiedot

lopputiedot = PrettyTable(["Auto", "Rekisteritunnus", "Huippunopeus (km/h)", "Nopeus (km/h)", "Matka (km)"])
for a in autot:
    a_tiedot = autot[a].tiedot()
    lopputiedot.add_row([a , a_tiedot[0], a_tiedot[1], a_tiedot[2], a_tiedot[3] ])

print(lopputiedot)



