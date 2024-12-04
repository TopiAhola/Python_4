'''
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun
nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle
annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä
kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla,
onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä
kertaalleen sen jälkeen, kun kilpailu on päättynyt.
'''

# Importit
#PrettyTable lopputaulukon tulostusta varten
import random
from prettytable import PrettyTable

# Auto luokka
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

# Kilpailu luokka

class Kilpailu:
    def __init__(self, nimi, pituus, autolista) :
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = autolista

    def tunti_kuluu(self):

        for a in autot:
            # nopeuden muutos arvotaan väliltä -10 ja +15 km/h
            d_nopeus = int(random.randint(-10, +15))
            a.kiihdytä(d_nopeus)
            print(f"Auton {a.rekisteritunnus} nopeus on {a.nopeus}km/h")

            # kaikki autot kulkevat tunnin ajan
            a.kulje(1)
            print(f" Auto {a.rekisteritunnus} on kulkenut {a.matka}km.")

    def tulosta_tilanne(self):
        tilanne = PrettyTable(["Auto", "Rekisteritunnus", "Huippunopeus (km/h)", "Nopeus (km/h)", "Matka (km)"])
        n = 1
        for a in autot:

            a_tiedot = a.tiedot()
            tilanne.add_row([n, a_tiedot[0], a_tiedot[1], a_tiedot[2], a_tiedot[3]])
            n += 1

        print(tilanne)

    def kilpalu_ohi(self):
        ohi = False
        for a in self.autolista:
            if a.matka >= self.pituus:
                ohi = True

        return ohi



# Luodaan 10 autoa:

autot = []
for n in range(1,11):

    rekisteri_tunnus = f"ABC-{n}"
    autot.append( Auto(rekisteri_tunnus, random.randint(100, 200)) )

print("Autojen tiedot: ")
for a in autot:
    print(a.tiedot())

#Luodaan kilpailu

kilpailu1 = Kilpailu("Suuri romuralli", 8000, autot )


aika = 0
while True:

    kilpailu1.tunti_kuluu()

    if aika % 10 == 0:
        print(f"Kilpailu kestänyt {aika} tuntia: ")
        kilpailu1.tulosta_tilanne()

    aika += 1

    if kilpailu1.kilpalu_ohi() == True:

        print(f"Kilpailu {kilpailu1.nimi} ohi.")
        print(f"Kilpailu kesti {aika} tuntia.")
        kilpailu1.tulosta_tilanne()
        break
