'''
Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun
taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.

Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja
Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

'''

class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

        Julkaisu.__init__(self, nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi} \nKirjoittaja: {self.kirjoittaja} \nSivumaara: {self.sivumaara}")

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja

        Julkaisu.__init__(self, nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi} \nPäätoimittaja: {self.paatoimittaja} ")



#Pääohjelma

aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hyttino6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hyttino6.tulosta_tiedot()

#Tämä toimii kanssa:
Lehti.tulosta_tiedot(aku_ankka)

