'''
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
Polttomoottoriauton ominaisuutena on bensatankin koko litroina.

Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa
parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä
asettaa oman kapasiteettinsa.

Kirjoita pääohjelma, jossa luot yhden sähköauton
(ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton
(ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.


'''

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

class Sahkoauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, nopeus = 0, matka = 0 ):
        Auto.__init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, bensatankki, nopeus = 0, matka = 0):
        Auto.__init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0)
        self.bensatankki = bensatankki

auto1 = Sahkoauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 165, 32.3)

#Testitulostus
#print(auto1.tiedot())
#print(auto2.tiedot())

#Aseta nopeus
auto1.nopeus = 100
auto2.nopeus = 150

#Kulje 3h
auto1.kulje(3)
auto2.kulje(3)

print(f"Auto {auto1.rekisteritunnus} on kulkenut {auto1.matka} km.")
print(f"Auto {auto2.rekisteritunnus} on kulkenut {auto2.matka} km.")
print(Auto.määrä)
